#!/usr/bin/env python3
"""
render_svg.py - renders strategy / process / GTM / AI diagrams to SVG (and PNG) from a JSON spec.

Usage:
  python render_svg.py <type> spec.json -o out.svg [--png] [--scale 2]
  python render_svg.py --types                      # list diagram types
  python render_svg.py --example <type>             # print an example spec for a type
  python render_svg.py --example <type> > spec.json # start from the example and edit it

Every spec shares the same envelope:
{
  "title": "Takeaway title that states the point (not the topic)",
  "subtitle": "optional one-line framing",
  "source": "optional footnote / source",
  "width": 1600, "height": 900,                     # 16:9 default; use 1080x1080 for social, 1600x1200 for docs
  "palette": {                                       # OPTIONAL - user-supplied brand colors. Defaults are neutral.
    "bg": "#FFFFFF", "ink": "#111827", "muted": "#6B7280", "line": "#D1D5DB", "context": "#E5E7EB",
    "accent": "#2563EB",      # the story color (current / highlighted)
    "accent2": "#059669",     # recommended / future / positive
    "risk": "#EA580C",        # risk / negative / attention
    "font": "Inter, Helvetica, Arial, sans-serif"
  },
  "highlight": [0],                                  # indexes of the elements to emphasize; everything else is muted
  "data": { ... type-specific, see --example <type> ... }
}
Design rules baked in: one accent, muted context, direct labels, takeaway title, no 3D, no rainbow.
No network calls.
"""
import argparse, json, math, sys, os, html

# ------------------------------------------------------------------ helpers
DEFAULT_PALETTE = {
    "bg": "#FFFFFF", "ink": "#111827", "muted": "#6B7280", "line": "#D1D5DB", "context": "#E5E7EB",
    "accent": "#2563EB", "accent2": "#059669", "risk": "#EA580C",
    "font": "Inter, Helvetica, Arial, sans-serif",
}

def esc(s): return html.escape(str(s), quote=True)

def wrap(text, max_chars):
    words, lines, cur = str(text).split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > max_chars and cur:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur: lines.append(cur)
    return lines or [""]

def hex_to_rgb(h):
    h = h.lstrip("#"); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def tint(color, amount):
    """Blend color toward white by amount (0..1)."""
    r, g, b = hex_to_rgb(color)
    r, g, b = (int(c + (255 - c) * amount) for c in (r, g, b))
    return f"#{r:02X}{g:02X}{b:02X}"

def contrast_text(color, ink="#111827", light="#FFFFFF"):
    r, g, b = hex_to_rgb(color)
    lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return light if lum < 150 else ink

class Canvas:
    def __init__(self, spec, kind):
        self.W = spec.get("width", 1600); self.H = spec.get("height", 900)
        self.P = dict(DEFAULT_PALETTE); self.P.update(spec.get("palette") or {})
        self.font = self.P["font"]; self.parts = []
        self.hl = set(spec.get("highlight") or [])
        self.spec = spec; self.kind = kind
        self.margin = 80
        self.parts.append(f'<rect width="{self.W}" height="{self.H}" fill="{self.P["bg"]}"/>')
        self.top = self.header()
        self.bottom = self.H - (70 if spec.get("source") else 40)
        self.footer()

    # --- chrome
    def header(self):
        y = 70; t = self.spec.get("title"); s = self.spec.get("subtitle")
        if t:
            size = 40 if len(t) < 70 else 32
            lines = wrap(t, int((self.W - 2 * self.margin) / (size * 0.6)))
            for i, line in enumerate(lines):
                self.text(self.margin, y + i * size * 1.15, line, size, weight=700)
            y += size * 1.15 * len(lines)
        if s:
            self.text(self.margin, y + 8, s, 20, color=self.P["muted"]); y += 34
        return y + 30 if (t or s) else 60

    def footer(self):
        src = self.spec.get("source")
        if src:
            self.text(self.margin, self.H - 28, "Source: " + src, 14, color=self.P["muted"])

    # --- primitives
    def text(self, x, y, s, size=18, color=None, weight=400, anchor="start", italic=False, opacity=1.0):
        color = color or self.P["ink"]
        st = f'font-family="{self.font}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}"'
        if italic: st += ' font-style="italic"'
        if opacity < 1: st += f' opacity="{opacity}"'
        self.parts.append(f'<text x="{x:.1f}" y="{y:.1f}" {st}>{esc(s)}</text>')

    def text_block(self, x, y, s, size, max_chars, color=None, weight=400, anchor="start", lh=1.25, valign="top"):
        lines = wrap(s, max_chars)
        total = (len(lines) - 1) * size * lh
        y0 = y - total / 2 if valign == "middle" else y
        for i, l in enumerate(lines):
            self.text(x, y0 + i * size * lh, l, size, color, weight, anchor)
        return len(lines)

    def rect(self, x, y, w, h, fill, stroke="none", rx=10, sw=1.5, opacity=1.0, dash=None):
        extra = f' stroke-dasharray="{dash}"' if dash else ""
        self.parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"{extra}/>')

    def circle(self, cx, cy, r, fill, stroke="none", sw=1.5, opacity=1.0):
        self.parts.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"/>')

    def line(self, x1, y1, x2, y2, color=None, sw=2, dash=None, arrow=False):
        color = color or self.P["line"]
        extra = f' stroke-dasharray="{dash}"' if dash else ""
        if arrow: extra += f' marker-end="url(#arrow-{self._marker(color)})"'
        self.parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{sw}"{extra}/>')

    def path(self, d, fill="none", stroke=None, sw=2, arrow=False, opacity=1.0, dash=None):
        stroke = stroke or self.P["line"]
        extra = f' marker-end="url(#arrow-{self._marker(stroke)})"' if arrow else ""
        if dash: extra += f' stroke-dasharray="{dash}"'
        self.parts.append(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"{extra}/>')

    def polygon(self, pts, fill, stroke="none", sw=1.5, opacity=1.0):
        p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        self.parts.append(f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"/>')

    _markers = {}
    def _marker(self, color):
        key = color.lstrip("#")
        if key not in self._markers:
            self._markers[key] = f'<marker id="arrow-{key}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{color}"/></marker>'
        return key

    def color_for(self, i, base=None):
        """Highlight logic: if highlight list given, non-highlighted items are muted."""
        base = base or self.P["accent"]
        if self.hl and i not in self.hl:
            return self.P["context"]
        return base

    def mark_color(self, i, base=None):
        """Like color_for, but for small marks (dots) that would vanish in the context gray."""
        base = base or self.P["accent"]
        if self.hl and i not in self.hl:
            return self.P["muted"]
        return base

    def ink_for(self, i):
        return self.P["ink"] if (not self.hl or i in self.hl) else self.P["muted"]

    def box(self, x, y, w, h, label, fill, size=20, weight=600, sub=None, rx=12, stroke="none", txt=None):
        self.rect(x, y, w, h, fill, stroke=stroke, rx=rx)
        txt = txt or contrast_text(fill, self.P["ink"])
        mc = max(6, int((w - 16) / (size * 0.62)))
        if sub:
            self.text_block(x + w / 2, y + h / 2 - size * 0.5, label, size, mc, txt, weight, "middle", valign="middle")
            self.text_block(x + w / 2, y + h / 2 + size * 0.9, sub, size * 0.7, int((w - 16) / (size * 0.7 * 0.6)), txt, 400, "middle")
        else:
            self.text_block(x + w / 2, y + h / 2 + size * 0.35, label, size, mc, txt, weight, "middle", valign="middle")

    def svg(self):
        defs = "<defs>" + "".join(self._markers.values()) + "</defs>"
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.W}" height="{self.H}" viewBox="0 0 {self.W} {self.H}">'
                + defs + "".join(self.parts) + "</svg>")

# ------------------------------------------------------------------ registry
TYPES = {}
EXAMPLES = {}
def diagram(name, example):
    def deco(fn):
        TYPES[name] = fn; EXAMPLES[name] = example; return fn
    return deco

def area(c):
    return c.margin, c.top, c.W - 2 * c.margin, c.bottom - c.top

# ------------------------------------------------------------------ data-ish charts
@diagram("waterfall", {"title": "Expansion, not new logos, drove the $6M ARR gain", "source": "Finance, FY26",
    "data": {"start": {"label": "ARR Jan", "value": 12}, "steps": [{"label": "New logos", "value": 2.5}, {"label": "Expansion", "value": 4.8},
             {"label": "Churn", "value": -2.1}, {"label": "Downgrades", "value": -0.9}, {"label": "Price", "value": 1.7}],
             "end_label": "ARR Dec", "unit": "$M", "decimals": 1}, "highlight": [1]})
def r_waterfall(c, d):
    x0, y0, w, h = area(c)
    steps = d["steps"]; unit = d.get("unit", ""); dec = d.get("decimals", 0)
    vals = [d["start"]["value"]]
    run = d["start"]["value"]
    for s in steps: run += s["value"]; vals.append(run)
    end = run
    top = max(max(vals), d["start"]["value"], end) * 1.15; bot = min(0, min(vals))
    n = len(steps) + 2; gap = w / n; bw = gap * 0.62
    def Y(v): return y0 + h - 60 - (v - bot) / (top - bot) * (h - 100)
    def fmtv(v, sign=False):
        sg = ("+" if v > 0 else "-") if sign else ("-" if v < 0 else "")
        num = f"{abs(v):,.{dec}f}"
        return f"{sg}{unit[0]}{num}{unit[1:]}" if unit[:1] and unit[0] in "$€£" else f"{sg}{num}{unit}"
    fmt = lambda v: fmtv(v, sign=True)
    # start
    x = x0 + gap * 0.5 - bw / 2
    c.rect(x, Y(d["start"]["value"]), bw, Y(0) - Y(d["start"]["value"]), c.P["muted"], rx=4)
    c.text(x + bw / 2, Y(d["start"]["value"]) - 12, fmtv(d["start"]["value"]), 20, weight=700, anchor="middle")
    c.text(x + bw / 2, y0 + h - 30, d["start"]["label"], 17, color=c.P["muted"], anchor="middle")
    run = d["start"]["value"]
    for i, s in enumerate(steps):
        x = x0 + gap * (i + 1.5) - bw / 2
        a, b = run, run + s["value"]
        col = c.color_for(i, c.P["accent2"] if s["value"] >= 0 else c.P["risk"])
        c.rect(x, min(Y(a), Y(b)), bw, abs(Y(a) - Y(b)), col, rx=4)
        c.line(x - gap * 0.38, Y(a), x, Y(a), c.P["line"], 1.5, dash="4,4")
        c.text(x + bw / 2, min(Y(a), Y(b)) - 12, fmt(s["value"]), 20, weight=700, anchor="middle", color=c.ink_for(i))
        c.text_block(x + bw / 2, y0 + h - 30, s["label"], 17, int(bw / 9), c.P["muted"], anchor="middle")
        run = b
    x = x0 + gap * (n - 0.5) - bw / 2
    c.rect(x, Y(end), bw, Y(0) - Y(end), c.P["ink"], rx=4)
    c.text(x + bw / 2, Y(end) - 12, fmtv(end), 20, weight=700, anchor="middle")
    c.text(x + bw / 2, y0 + h - 30, d.get("end_label", "End"), 17, color=c.P["muted"], anchor="middle")
    c.line(x0, Y(0), x0 + w, Y(0), c.P["line"], 1.5)

@diagram("slope", {"title": "Perception shifted from 'tool' to 'system' after repositioning", "data": {
    "left_label": "Before", "right_label": "After", "unit": "%",
    "items": [{"label": "Seen as a platform", "a": 22, "b": 61}, {"label": "Seen as a point tool", "a": 68, "b": 30}, {"label": "Unaware", "b": 9, "a": 10}]}, "highlight": [0]})
def r_slope(c, d):
    x0, y0, w, h = area(c)
    items = d["items"]; unit = d.get("unit", "")
    vals = [i["a"] for i in items] + [i["b"] for i in items]
    lo, hi = min(vals), max(vals); rng = (hi - lo) or 1
    L, R = x0 + w * 0.3, x0 + w * 0.7
    def Y(v): return y0 + h - 40 - (v - lo) / rng * (h - 100)
    c.text(L, y0 + 10, d.get("left_label", "Before"), 20, weight=700, anchor="middle", color=c.P["muted"])
    c.text(R, y0 + 10, d.get("right_label", "After"), 20, weight=700, anchor="middle", color=c.P["muted"])
    for i, it in enumerate(items):
        col = c.color_for(i); ink = c.ink_for(i)
        sw = 5 if (not c.hl or i in c.hl) else 3
        c.line(L, Y(it["a"]), R, Y(it["b"]), col, sw)
        c.circle(L, Y(it["a"]), 8, col); c.circle(R, Y(it["b"]), 8, col)
        c.text(L - 16, Y(it["a"]) + 6, f"{it['label']}  {it['a']}{unit}", 18, ink, anchor="end", weight=600 if i in c.hl else 400)
        c.text(R + 16, Y(it["b"]) + 6, f"{it['b']}{unit}  {it['label']}", 18, ink, weight=600 if i in c.hl else 400)

@diagram("dumbbell", {"title": "AI-assisted reps close the gap fastest in research and drafting", "data": {
    "a_label": "Before AI", "b_label": "With AI", "unit": " hrs/wk",
    "items": [{"label": "Account research", "a": 9, "b": 3}, {"label": "Email drafting", "a": 7, "b": 2.5}, {"label": "Call prep", "a": 4, "b": 2}, {"label": "CRM updates", "a": 5, "b": 4}]}, "highlight": [0, 1]})
def r_dumbbell(c, d):
    x0, y0, w, h = area(c)
    items = d["items"]; unit = d.get("unit", "")
    vals = [i["a"] for i in items] + [i["b"] for i in items]; hi = max(vals) * 1.1
    labw = w * 0.28; X = lambda v: x0 + labw + v / hi * (w - labw - 40)
    rowh = min(90, (h - 60) / len(items))
    c.text(x0 + labw, y0 + 8, "", 1)
    for i, it in enumerate(items):
        y = y0 + 50 + i * rowh; col = c.color_for(i); ink = c.ink_for(i)
        c.text(x0 + labw - 20, y + 7, it["label"], 20, ink, anchor="end", weight=600 if i in c.hl else 400)
        c.line(X(it["a"]), y, X(it["b"]), y, col, 6)
        c.circle(X(it["a"]), y, 11, c.P["bg"], stroke=col, sw=4); c.circle(X(it["b"]), y, 11, col)
        c.text(X(it["a"]), y - 20, f"{it['a']}{unit}", 15, c.P["muted"], anchor="middle")
        c.text(X(it["b"]), y - 20, f"{it['b']}{unit}", 15, ink, anchor="middle", weight=700)
    ly = y0 + 50 + len(items) * rowh + 10
    c.circle(x0 + labw, ly, 9, c.P["bg"], stroke=c.P["accent"], sw=4); c.text(x0 + labw + 18, ly + 6, d.get("a_label", "Before"), 16, c.P["muted"])
    c.circle(x0 + labw + 160, ly, 9, c.P["accent"]); c.text(x0 + labw + 178, ly + 6, d.get("b_label", "After"), 16, c.P["muted"])

@diagram("bullet", {"title": "Enterprise is the only segment below 3x coverage", "data": {"unit": "x", "target_label": "Target",
    "items": [{"label": "Enterprise", "value": 2.1, "target": 3, "max": 5}, {"label": "Mid-market", "value": 3.4, "target": 3, "max": 5}, {"label": "SMB", "value": 4.2, "target": 3, "max": 5}]}, "highlight": [0]})
def r_bullet(c, d):
    x0, y0, w, h = area(c)
    items = d["items"]; unit = d.get("unit", "")
    labw = w * 0.22; rowh = min(120, (h - 40) / len(items))
    for i, it in enumerate(items):
        y = y0 + 30 + i * rowh; mx = it.get("max", max(it["value"], it["target"]) * 1.3)
        X = lambda v: x0 + labw + v / mx * (w - labw)
        ink = c.ink_for(i); col = c.color_for(i, c.P["risk"] if it["value"] < it["target"] else c.P["accent"])
        c.text(x0 + labw - 20, y + 30, it["label"], 20, ink, anchor="end", weight=600 if i in c.hl else 400)
        c.rect(X(0), y, X(mx) - X(0), 46, c.P["context"], rx=6)
        c.rect(X(0), y + 12, X(it["value"]) - X(0), 22, col, rx=4)
        c.line(X(it["target"]), y - 6, X(it["target"]), y + 52, c.P["ink"], 4)
        c.text(X(it["value"]) + 10, y + 30, f"{it['value']}{unit}", 18, ink, weight=700)
        if i == 0: c.text(X(it["target"]), y - 14, f"{d.get('target_label','Target')} {it['target']}{unit}", 15, c.P["muted"], anchor="middle")

@diagram("hero_stat", {"title": "", "data": {"value": "73%", "label": "of GTM leaders say their AI pilots never reached production", "implication": "The constraint is not model quality. It is workflow design.", "source": "GTM AI Report, 2026"}})
def r_hero_stat(c, d):
    x0, y0, w, h = area(c)
    cy = y0 + h * 0.42
    c.text(x0, cy, d["value"], 180, c.P["accent"], weight=800)
    c.text_block(x0, cy + 60, d["label"], 30, int(w / 17), c.P["ink"], 500)
    if d.get("implication"):
        c.line(x0, cy + 150, x0 + 80, cy + 150, c.P["accent"], 4)
        c.text_block(x0, cy + 190, d["implication"], 26, int(w / 15), c.P["ink"], 700)
    if d.get("source"): c.text(x0, c.H - 28, "Source: " + d["source"], 14, c.P["muted"])

@diagram("compare_bars", {"title": "The bottleneck isn't the models. It's workflow redesign.", "width": 1080, "height": 1080, "source": "Survey of 412 B2B marketing leaders", "data": {
    "unit": "%", "max": 100, "items": [{"label": "Ran at least one AI pilot", "value": 73}, {"label": "Got a pilot into production", "value": 19}],
    "gap_label": "54 pts never shipped", "implication": "Three in four can make a model work. One in five can change the work around it."}, "highlight": [1]})
def r_compare_bars(c, d):
    """2-5 proportional horizontal bars for 'X but only Y' claims. Social-friendly: big labels, one highlight."""
    x0, y0, w, h = area(c)
    items = d["items"]; n = len(items); unit = d.get("unit", ""); mx = d.get("max") or max(i["value"] for i in items) * 1.1
    big = c.W <= 1200
    rowh = min(300 if big else 160, (h - 320) / n); bh = min(rowh * 0.42, 110); y = y0 + 40
    for i, it in enumerate(items):
        fill = c.color_for(i, c.P["accent"]); ink = c.ink_for(i)
        c.text(x0, y + 4, it["label"], 30 if big else 22, ink, 700 if (i in c.hl or not c.hl) else 500)
        by = y + 22
        c.rect(x0, by, w, bh, c.P["context"], rx=bh / 2)
        bw = max(w * it["value"] / mx, bh)
        c.rect(x0, by, bw, bh, fill if fill != c.P["context"] else c.P["muted"], rx=bh / 2)
        vtxt = f"{it['value']}{unit}"; vs = 44 if big else 30
        if bw > w * 0.35: c.text(x0 + bw - 20, by + bh / 2 + vs * 0.36, vtxt, vs, "#FFFFFF", 800, anchor="end")
        else: c.text(x0 + bw + 18, by + bh / 2 + vs * 0.36, vtxt, vs, ink, 800)
        y += rowh
    if d.get("gap_label") and n >= 2:
        a, b = items[0]["value"], items[-1]["value"]; xa, xb = x0 + w * min(a, b) / mx, x0 + w * max(a, b) / mx
        gy = y0 + 20 + (n - 1) * rowh + 22 + bh + 22
        c.line(xa, gy, xb, gy, c.P["risk"], 3); c.line(xa, gy - 8, xa, gy + 8, c.P["risk"], 3); c.line(xb, gy - 8, xb, gy + 8, c.P["risk"], 3)
        c.text((xa + xb) / 2, gy + 34, d["gap_label"], 24 if big else 18, c.P["risk"], 700, anchor="middle")
        y = gy + 60
    if d.get("implication"):
        c.text_block(x0, y + 50, d["implication"], 30 if big else 22, int(w / ((30 if big else 22) * 0.58)), c.P["ink"], 700)

# ------------------------------------------------------------------ matrices and grids
@diagram("two_by_two", {"title": "Start with the three high-impact, low-effort plays", "data": {
    "x_axis": "Effort to implement →", "y_axis": "Business impact →",
    "quadrants": ["Quick wins", "Strategic bets", "Fill-ins", "Avoid"],
    "items": [{"label": "AI call summaries", "x": 0.2, "y": 0.8}, {"label": "Intent-triggered outreach", "x": 0.35, "y": 0.9}, {"label": "Auto-QBR decks", "x": 0.25, "y": 0.65},
              {"label": "Agentic SDR", "x": 0.85, "y": 0.85}, {"label": "Predictive churn", "x": 0.7, "y": 0.75}, {"label": "Chatbot refresh", "x": 0.3, "y": 0.2}, {"label": "Full CRM migration", "x": 0.9, "y": 0.3}]},
    "highlight": [0, 1, 2]})
def r_two_by_two(c, d):
    x0, y0, w, h = area(c)
    gx, gy = x0 + 60, y0 + 10; gw, gh = w - 80, h - 70
    q = d.get("quadrants") or ["", "", "", ""]
    fills = [tint(c.P["accent"], 0.9), c.P["context"], c.P["context"], c.P["context"]] if d.get("shade_first", True) else [c.P["context"]] * 4
    # TL, TR, BL, BR
    c.rect(gx, gy, gw / 2, gh / 2, fills[0], rx=0); c.rect(gx + gw / 2, gy, gw / 2, gh / 2, tint(c.P["context"], 0.5), rx=0)
    c.rect(gx, gy + gh / 2, gw / 2, gh / 2, tint(c.P["context"], 0.5), rx=0); c.rect(gx + gw / 2, gy + gh / 2, gw / 2, gh / 2, tint(c.P["context"], 0.3), rx=0)
    c.line(gx + gw / 2, gy, gx + gw / 2, gy + gh, c.P["line"], 2); c.line(gx, gy + gh / 2, gx + gw, gy + gh / 2, c.P["line"], 2)
    for (qx, qy, lab) in [(gx + 14, gy + 30, q[0]), (gx + gw - 14, gy + 30, q[1]), (gx + 14, gy + gh - 14, q[2]), (gx + gw - 14, gy + gh - 14, q[3])]:
        c.text(qx, qy, lab, 18, c.P["muted"], 700, anchor="start" if qx < gx + gw / 2 else "end")
    c.text(gx + gw / 2, gy + gh + 40, d.get("x_axis", ""), 18, c.P["muted"], anchor="middle")
    c.parts.append(f'<text transform="translate({gx - 25},{gy + gh / 2}) rotate(-90)" font-family="{c.font}" font-size="18" fill="{c.P["muted"]}" text-anchor="middle">{esc(d.get("y_axis", ""))}</text>')
    for i, it in enumerate(d["items"]):
        px, py = gx + it["x"] * gw, gy + (1 - it["y"]) * gh
        r = 10 + 14 * it.get("size", 0.3)
        col = c.mark_color(i); ink = c.ink_for(i)
        c.circle(px, py, r, col, stroke=c.P["bg"], sw=2, opacity=1.0 if (not c.hl or i in c.hl) else 0.55)
        c.text(px + r + 8, py + 6, it["label"], 17, ink, weight=700 if (i in c.hl) else 400)

@diagram("grid", {"title": "Capability map: demand and analytics are the weakest links", "data": {
    "columns": 3, "cells": [{"label": "Strategy", "sub": "Strong", "status": "good"}, {"label": "Content", "sub": "Strong", "status": "good"}, {"label": "Demand", "sub": "Gap", "status": "risk"},
    {"label": "Sales enablement", "sub": "Adequate"}, {"label": "Analytics", "sub": "Gap", "status": "risk"}, {"label": "RevOps", "sub": "Building", "status": "accent"}]}})
def r_grid(c, d):
    x0, y0, w, h = area(c)
    cells = d["cells"]; cols = d.get("columns", 3); rows = math.ceil(len(cells) / cols)
    gap = 18; cw = (w - gap * (cols - 1)) / cols; ch = min(200, (h - gap * (rows - 1)) / rows)
    for i, cell in enumerate(cells):
        r, k = divmod(i, cols); x = x0 + k * (cw + gap); y = y0 + r * (ch + gap)
        st = cell.get("status")
        fill = {"good": tint(c.P["accent2"], 0.8), "risk": tint(c.P["risk"], 0.8), "accent": tint(c.P["accent"], 0.8)}.get(st, c.P["context"])
        if c.hl and i not in c.hl: fill = c.P["context"]
        c.box(x, y, cw, ch, cell["label"], fill, size=22, sub=cell.get("sub"), txt=c.P["ink"])

@diagram("table", {"title": "Vendor B wins on the criteria that matter most", "data": {
    "columns": ["Criteria", "Vendor A", "Vendor B", "Vendor C"], "weights": ["", "", "", ""],
    "rows": [["Security", "●●", "●●●", "●"], ["Capability", "●●●", "●●●", "●●"], ["Cost", "●", "●●", "●●●"], ["Speed to deploy", "●●", "●●●", "●●"]],
    "highlight_col": 2, "recommendation": "Recommend Vendor B: strongest on security + speed, acceptable cost."}})
def r_table(c, d):
    x0, y0, w, h = area(c)
    cols = d["columns"]; rows = d["rows"]; hc = d.get("highlight_col")
    cw = [w * 0.28] + [(w * 0.72) / (len(cols) - 1)] * (len(cols) - 1)
    rh = min(70, (h - 120) / (len(rows) + 1))
    x = x0
    for j, col in enumerate(cols):
        fill = c.P["ink"] if j != hc else c.P["accent"]
        c.rect(x, y0, cw[j], rh, fill, rx=0)
        c.text(x + (14 if j == 0 else cw[j] / 2), y0 + rh / 2 + 7, col, 19, contrast_text(fill), 700, anchor="start" if j == 0 else "middle")
        x += cw[j]
    for i, row in enumerate(rows):
        y = y0 + rh * (i + 1); x = x0
        for j, cell in enumerate(row):
            fill = tint(c.P["context"], 0.5 if i % 2 else 0.0)
            if j == hc: fill = tint(c.P["accent"], 0.85)
            c.rect(x, y, cw[j], rh, fill, rx=0, stroke=c.P["bg"], sw=2)
            c.text(x + (14 if j == 0 else cw[j] / 2), y + rh / 2 + 7, cell, 18, c.P["ink"], 600 if j == 0 or j == hc else 400, anchor="start" if j == 0 else "middle")
            x += cw[j]
    if d.get("recommendation"):
        y = y0 + rh * (len(rows) + 1) + 30
        c.rect(x0, y, w, 64, tint(c.P["accent2"], 0.85), rx=10)
        c.text_block(x0 + 20, y + 40, d["recommendation"], 20, int(w / 11), c.P["ink"], 700)

@diagram("dashboard", {"title": "Q3 revenue control tower", "data": {
    "tiles": [{"label": "Pipeline coverage", "value": "2.8x", "delta": "-0.4x vs plan", "status": "risk"}, {"label": "Win rate", "value": "24%", "delta": "+3 pts", "status": "good"},
              {"label": "Avg cycle", "value": "61 d", "delta": "-9 d", "status": "good"}, {"label": "Activated accts", "value": "412", "delta": "+18%", "status": "good"}],
    "blockers": ["Enterprise coverage below 3x", "SDR ramp behind by 3 weeks"], "next_actions": ["Launch intent-triggered outbound", "Re-forecast enterprise Q4"]}})
def r_dashboard(c, d):
    x0, y0, w, h = area(c)
    tiles = d["tiles"]; n = len(tiles); gap = 18; tw = (w - gap * (n - 1)) / n; th = 150
    for i, t in enumerate(tiles):
        x = x0 + i * (tw + gap); st = t.get("status")
        col = {"good": c.P["accent2"], "risk": c.P["risk"]}.get(st, c.P["accent"])
        c.rect(x, y0, tw, th, tint(c.P["context"], 0.5), rx=12)
        c.rect(x, y0, 8, th, col, rx=4)
        c.text(x + 26, y0 + 34, t["label"], 16, c.P["muted"], 600)
        c.text(x + 26, y0 + 96, t["value"], 54, c.P["ink"], 800)
        if t.get("delta"): c.text(x + 26, y0 + 128, t["delta"], 16, col, 600)
    y = y0 + th + 40; colw = (w - gap) / 2
    for k, (head, items, col) in enumerate([("Blockers", d.get("blockers", []), c.P["risk"]), ("Next actions", d.get("next_actions", []), c.P["accent"])]):
        x = x0 + k * (colw + gap)
        c.text(x, y, head, 20, col, 700)
        for j, it in enumerate(items):
            c.circle(x + 8, y + 36 + j * 34, 5, col); c.text(x + 24, y + 42 + j * 34, it, 18, c.P["ink"])

@diagram("card", {"title": "Ideal customer profile", "data": {"cards": [
    {"title": "Firmographics", "lines": ["B2B SaaS, $20-200M ARR", "50-500 person GTM org", "NA / UK"]},
    {"title": "Triggers", "lines": ["New CRO or CMO", "AI mandate from board", "Pipeline miss 2+ quarters"]},
    {"title": "Pains", "lines": ["Fragmented tools", "Reps drowning in admin", "No signal-to-action loop"]},
    {"title": "Buying committee", "lines": ["CRO (economic)", "RevOps lead (champion)", "IT/security (blocker)"]}]}})
def r_card(c, d):
    x0, y0, w, h = area(c)
    cards = d["cards"]; n = len(cards); cols = min(n, 4); rows = math.ceil(n / cols); gap = 20
    cw = (w - gap * (cols - 1)) / cols; ch = min(360, (h - gap * (rows - 1)) / rows)
    for i, cd in enumerate(cards):
        r, k = divmod(i, cols); x = x0 + k * (cw + gap); y = y0 + r * (ch + gap)
        c.rect(x, y, cw, ch, tint(c.P["context"], 0.5), rx=14)
        c.rect(x, y, cw, 54, c.color_for(i), rx=14); c.rect(x, y + 30, cw, 24, c.color_for(i), rx=0)
        c.text(x + 20, y + 35, cd["title"], 20, contrast_text(c.color_for(i)), 700)
        ly = y + 92
        for line in cd.get("lines", []):
            if cd.get("quote"):
                n_l = c.text_block(x + 20, ly, line, 17, int(cw / 9.5), c.P["ink"], italic=False); ly += 26 * n_l + 8
            else:
                c.circle(x + 26, ly - 6, 4, c.P["muted"]); n_l = c.text_block(x + 40, ly, line, 17, int(cw / 10)); ly += 26 * n_l

# ------------------------------------------------------------------ flows and sequences
@diagram("chevron", {"title": "From signal to revenue in five moves", "data": {
    "steps": [{"label": "Detect", "sub": "Intent + product signals"}, {"label": "Enrich", "sub": "Account + contact context"}, {"label": "Decide", "sub": "Play selection"},
              {"label": "Act", "sub": "Personalized outreach"}, {"label": "Learn", "sub": "Outcome feedback"}]}, "highlight": [2]})
def r_chevron(c, d):
    x0, y0, w, h = area(c)
    steps = d["steps"]; n = len(steps); notch = 34; gap = 8
    sw = (w - gap * (n - 1) + notch * (n - 1)) / n; sh = 120; y = y0 + 40
    for i, s in enumerate(steps):
        x = x0 + i * (sw - notch + gap)
        pts = [(x, y), (x + sw - notch, y), (x + sw, y + sh / 2), (x + sw - notch, y + sh), (x, y + sh)] + ([(x + notch, y + sh / 2)] if i > 0 else [])
        fill = c.color_for(i); c.polygon(pts, fill)
        txt = contrast_text(fill, c.P["ink"])
        c.text(x + sw / 2 + (notch / 2 if i > 0 else 0) - notch / 2, y + sh / 2 + 9, s["label"], 24, txt, 700, anchor="middle")
        if s.get("sub"): c.text_block(x + sw / 2 - notch / 2 + (notch / 2 if i > 0 else 0), y + sh + 36, s["sub"], 17, int(sw / 10), c.ink_for(i), anchor="middle")
    if d.get("loop_back"):
        c.path(f"M{x0 + w - 40},{y + sh + 90} C{x0 + w},{y + sh + 170} {x0},{y + sh + 170} {x0 + 40},{y + sh + 90}", stroke=c.P["muted"], sw=2, arrow=True, dash="6,6")
        c.text(x0 + w / 2, y + sh + 165, d["loop_back"], 16, c.P["muted"], anchor="middle")

@diagram("funnel", {"title": "We lose most deals between opportunity and proposal", "data": {
    "stages": [{"label": "Visitors", "value": 48000}, {"label": "Leads", "value": 3900}, {"label": "Opportunities", "value": 610}, {"label": "Proposals", "value": 190}, {"label": "Customers", "value": 84}],
    "show_conversion": True}, "highlight": [3]})
def r_funnel(c, d):
    x0, y0, w, h = area(c)
    st = d["stages"]; n = len(st); rh = min(110, (h - 20) / n); maxv = st[0]["value"]
    fw = w * 0.55; cx = x0 + fw / 2
    for i, s in enumerate(st):
        frac = max(s["value"] / maxv, 0.18) if d.get("proportional", False) else 1 - i * (0.6 / max(n - 1, 1))
        bw = fw * frac; y = y0 + i * rh
        fill = c.color_for(i, tint(c.P["accent"], i * 0.12))
        c.rect(cx - bw / 2, y, bw, rh - 10, fill, rx=8)
        txt = contrast_text(fill, c.P["ink"])
        c.text(cx, y + rh / 2 - 4, f"{s['label']}", 20, txt, 700, anchor="middle")
        c.text(cx, y + rh / 2 + 20, f"{s['value']:,}", 17, txt, 400, anchor="middle")
        if d.get("show_conversion", True) and i > 0:
            conv = s["value"] / st[i - 1]["value"] * 100; leak = 100 - conv
            ink = c.ink_for(i)
            c.text(x0 + fw + 60, y + rh / 2 + 2, f"{conv:.0f}% convert", 20, ink, 700 if i in c.hl else 500)
            c.text(x0 + fw + 60, y + rh / 2 + 26, f"{leak:.0f}% leak", 16, c.P["risk"] if i in c.hl else c.P["muted"])
    if d.get("note"):
        c.text_block(x0 + fw + 60, y0 + n * rh + 10, d["note"], 17, int((w - fw - 60) / 9), c.P["muted"])

@diagram("swimlane", {"title": "AI drafts, humans decide, systems execute", "data": {
    "lanes": ["AI agent", "Human (AE)", "System (CRM)"],
    "steps": [{"lane": 0, "label": "Detect intent signal"}, {"lane": 0, "label": "Draft outreach + rationale"}, {"lane": 1, "label": "Review + approve"}, {"lane": 2, "label": "Send + log"}, {"lane": 0, "label": "Score outcome"}, {"lane": 1, "label": "Coach the model"}]},
    "highlight": [2, 5]})
def r_swimlane(c, d):
    """Optional: data.loop_back = "label" draws a dashed return arrow from the last step to the first;
    data.gate = {"after": step_index, "label": "..."} draws a dashed vertical gate line after that step."""
    x0, y0, w, h = area(c)
    lanes = d["lanes"]; steps = d["steps"]; n = len(steps)
    labw = 170; lh = min(150, (h - 10) / len(lanes)); colw = (w - labw) / n
    for j, lane in enumerate(lanes):
        y = y0 + j * lh
        c.rect(x0, y, w, lh - 6, tint(c.P["context"], 0.6 if j % 2 else 0.3), rx=8)
        c.text_block(x0 + 16, y + lh / 2 + 2, lane, 18, 16, c.P["ink"], 700, valign="middle")
    centers = []
    for i, s in enumerate(steps):
        x = x0 + labw + i * colw + 12; y = y0 + s["lane"] * lh + 22; bw = colw - 24; bh = lh - 50
        fill = c.color_for(i, c.P["accent"] if s["lane"] != 1 else c.P["accent2"])
        c.box(x, y, bw, bh, s["label"], fill, size=17, rx=10)
        centers.append((x + bw / 2, y + bh / 2, x, x + bw, y, y + bh))
    for i in range(1, n):
        a, b = centers[i - 1], centers[i]
        mx = (a[3] + b[2]) / 2
        if abs(a[1] - b[1]) < 1: c.line(a[3], a[1], b[2], b[1], c.P["muted"], 2, arrow=True)
        else: c.path(f"M{a[3]},{a[1]} L{mx},{a[1]} L{mx},{b[1]} L{b[2]},{b[1]}", stroke=c.P["muted"], sw=2, arrow=True)
    if d.get("loop_back") and n > 1:
        a, b = centers[-1], centers[0]; ty = y0 - 22
        c.path(f"M{a[0]},{a[4]} L{a[0]},{ty} L{b[0]},{ty} L{b[0]},{b[4] - 2}", stroke=c.P["risk"], sw=2.5, arrow=True, dash="7,6")
        c.text((a[0] + b[0]) / 2, ty - 8, d["loop_back"], 15, c.P["risk"], 700, anchor="middle")
    g = d.get("gate")
    if g:
        gx = x0 + labw + (g["after"] + 1) * colw
        c.line(gx, y0 - 4, gx, y0 + len(lanes) * lh - 6, c.P["risk"], 3, dash="8,6")
        c.rect(gx - 100, y0 + len(lanes) * lh + 4, 200, 30, c.P["risk"], rx=15); c.text(gx, y0 + len(lanes) * lh + 24, g["label"], 14, "#FFFFFF", 700, anchor="middle")

@diagram("stack", {"title": "AI outcomes rest on six layers, and most teams only fund two", "data": {
    "layers": [{"label": "Outcomes", "sub": "Pipeline, retention, expansion"}, {"label": "Workflows", "sub": "Signal-to-action plays"}, {"label": "Agents & tools", "sub": "Research, drafting, routing"},
               {"label": "Models", "sub": "Foundation + fine-tuned"}, {"label": "Data", "sub": "CRM, product, intent, content"}, {"label": "Governance & people", "sub": "Decision rights, skills, evals"}]},
    "highlight": [1, 4]})
def r_stack(c, d):
    x0, y0, w, h = area(c)
    layers = d["layers"]; n = len(layers); lh = min(110, (h - 10) / n); lw = w * 0.7; x = x0 + (w - lw) / 2
    for i, l in enumerate(layers):
        y = y0 + i * lh
        fill = c.color_for(i, tint(c.P["accent"], 0.15 + 0.12 * i))
        c.box(x, y, lw, lh - 10, l["label"], fill, size=22, sub=l.get("sub"), rx=10)

@diagram("columns", {"title": "Now / next / later", "data": {"columns": [
    {"title": "Now", "items": ["Intent-triggered outbound", "AI call notes in CRM", "Weekly signal review"]},
    {"title": "Next", "items": ["Agentic SDR pilot", "Account health model"]},
    {"title": "Later", "items": ["Autonomous renewals", "Self-optimizing plays"]}]}, "highlight": [0]})
def r_columns(c, d):
    x0, y0, w, h = area(c)
    cols = d["columns"]; n = len(cols); gap = 22; cw = (w - gap * (n - 1)) / n
    for i, col in enumerate(cols):
        x = x0 + i * (cw + gap); fill = c.color_for(i)
        c.rect(x, y0, cw, h, tint(c.P["context"], 0.5), rx=14)
        c.rect(x, y0, cw, 58, fill, rx=14); c.rect(x, y0 + 30, cw, 28, fill, rx=0)
        c.text(x + cw / 2, y0 + 38, col["title"], 22, contrast_text(fill), 700, anchor="middle")
        if col.get("sub"): c.text(x + cw / 2, y0 + 84, col["sub"], 15, c.P["muted"], anchor="middle")
        ly = y0 + (110 if col.get("sub") else 96)
        for it in col.get("items", []):
            c.rect(x + 14, ly - 22, cw - 28, 48, c.P["bg"], rx=8, stroke=c.P["line"])
            nl = c.text_block(x + 28, ly + 8, it, 17, int((cw - 40) / 9.5), c.ink_for(i)); ly += 62 + (nl - 1) * 20

@diagram("timeline", {"title": "Value arrives in three waves", "data": {"milestones": [
    {"label": "Day 30", "title": "Signals live", "sub": "Intent + product usage in CRM"}, {"label": "Day 90", "title": "Plays running", "sub": "3 automated plays, human approval"},
    {"label": "Day 180", "title": "Compounding", "sub": "Learning loop tuned; 2x reply rate"}]}, "highlight": [2]})
def r_timeline(c, d):
    x0, y0, w, h = area(c)
    ms = d["milestones"]; n = len(ms); y = y0 + h * 0.4
    c.line(x0, y, x0 + w, y, c.P["line"], 4, arrow=True)
    for i, m in enumerate(ms):
        x = x0 + (i + 0.5) * w / n; col = c.color_for(i)
        c.circle(x, y, 18, col, stroke=c.P["bg"], sw=4)
        c.text(x, y - 36, m["label"], 18, c.P["muted"], 700, anchor="middle")
        c.text(x, y + 60, m["title"], 22, c.ink_for(i), 700, anchor="middle")
        if m.get("sub"): c.text_block(x, y + 92, m["sub"], 17, int(w / n / 10), c.P["muted"], anchor="middle")

@diagram("gantt", {"title": "Enablement gates the launch, not product", "data": {"periods": ["Sep", "Oct", "Nov", "Dec"], "rows": [
    {"label": "Product readiness", "start": 0, "end": 1.5}, {"label": "Customer proof", "start": 0.5, "end": 2.5}, {"label": "Sales enablement", "start": 2, "end": 3.8, "critical": True}, {"label": "Launch", "start": 3.6, "end": 4, "milestone": True}]}})
def r_gantt(c, d):
    x0, y0, w, h = area(c)
    per = d["periods"]; rows = d["rows"]; labw = w * 0.24; gw = w - labw; pw = gw / len(per); rh = min(80, (h - 60) / len(rows))
    for j, p in enumerate(per):
        c.text(x0 + labw + (j + 0.5) * pw, y0 + 20, p, 17, c.P["muted"], 600, anchor="middle")
        c.line(x0 + labw + j * pw, y0 + 34, x0 + labw + j * pw, y0 + 40 + len(rows) * rh, c.P["context"], 1.5)
    for i, r in enumerate(rows):
        y = y0 + 50 + i * rh; ink = c.ink_for(i)
        c.text(x0 + labw - 20, y + 30, r["label"], 19, ink, 700 if r.get("critical") else 400, anchor="end")
        fill = c.P["risk"] if r.get("critical") else c.color_for(i)
        if r.get("milestone"):
            mx = x0 + labw + r["start"] * pw; c.polygon([(mx, y + 8), (mx + 22, y + 30), (mx, y + 52), (mx - 22, y + 30)], c.P["ink"])
        else:
            c.rect(x0 + labw + r["start"] * pw, y + 10, (r["end"] - r["start"]) * pw, 40, fill, rx=8)

@diagram("journey_curve", {"title": "Onboarding friction peaks at data connection, not at signup", "data": {
    "stages": ["Signup", "Connect data", "First insight", "Invite team", "Renew"], "sentiment": [0.7, 0.15, 0.85, 0.6, 0.9],
    "notes": {"1": "62% stall here; 3 integrations required"}}, "highlight": [1]})
def r_journey_curve(c, d):
    x0, y0, w, h = area(c)
    st = d["stages"]; sv = d["sentiment"]; n = len(st)
    gy, gh = y0 + 20, h - 120
    pts = [(x0 + (i + 0.5) * w / n, gy + (1 - v) * gh) for i, v in enumerate(sv)]
    c.line(x0, gy + gh / 2, x0 + w, gy + gh / 2, c.P["context"], 2, dash="6,6")
    dpath = f"M{pts[0][0]},{pts[0][1]} " + " ".join(f"C{(a[0]+b[0])/2},{a[1]} {(a[0]+b[0])/2},{b[1]} {b[0]},{b[1]}" for a, b in zip(pts, pts[1:]))
    c.path(dpath, stroke=c.P["accent"], sw=5)
    for i, (x, y) in enumerate(pts):
        col = c.P["risk"] if i in c.hl else c.P["accent"]
        c.circle(x, y, 12, col, stroke=c.P["bg"], sw=3)
        c.text(x, gy + gh + 40, st[i], 18, c.ink_for(i), 700 if i in c.hl else 500, anchor="middle")
        note = (d.get("notes") or {}).get(str(i))
        if note: c.text_block(x, y + 40 if sv[i] < 0.5 else y - 30, note, 16, 26, c.P["risk"], 600, anchor="middle")
    c.text(x0 - 12, gy + 10, "High", 14, c.P["muted"], anchor="end"); c.text(x0 - 12, gy + gh, "Low", 14, c.P["muted"], anchor="end")

# ------------------------------------------------------------------ loops, hierarchies, metaphors
@diagram("flywheel", {"title": "Every issue makes the next one easier to sell", "data": {
    "nodes": ["Sharp POV content", "Audience growth", "Trust & authority", "Inbound pipeline", "Customer proof"], "center": "Compounding"}, "highlight": [2]})
def r_flywheel(c, d):
    x0, y0, w, h = area(c)
    nodes = d["nodes"]; n = len(nodes); cx, cy = x0 + w / 2, y0 + h / 2; R = min(w, h) / 2 - 90
    c.circle(cx, cy, R, "none", stroke=c.P["line"], sw=3)
    for i in range(n):
        a1 = -math.pi / 2 + 2 * math.pi * i / n; a2 = -math.pi / 2 + 2 * math.pi * (i + 0.72) / n
        d_ = f"M{cx + R*math.cos(a1+0.28*2*math.pi/n):.1f},{cy + R*math.sin(a1+0.28*2*math.pi/n):.1f} A{R},{R} 0 0 1 {cx + R*math.cos(a2):.1f},{cy + R*math.sin(a2):.1f}"
        c.path(d_, stroke=c.P["muted"], sw=4, arrow=True)
    for i, lab in enumerate(nodes):
        a = -math.pi / 2 + 2 * math.pi * i / n; px, py = cx + R * math.cos(a), cy + R * math.sin(a)
        col = c.color_for(i); bw, bh = 220, 74
        c.box(px - bw / 2, py - bh / 2, bw, bh, lab, col, size=19, rx=37)
    if d.get("center"):
        c.circle(cx, cy, 70, tint(c.P["accent"], 0.85)); c.text_block(cx, cy + 7, d["center"], 20, 12, c.P["ink"], 700, "middle", valign="middle")

@diagram("orbit", {"title": "The buying committee has one champion and two blockers", "data": {
    "center": "Deal", "satellites": [{"label": "CRO", "sub": "Economic buyer"}, {"label": "RevOps lead", "sub": "Champion", "status": "good"}, {"label": "IT/Security", "sub": "Blocker", "status": "risk"},
    {"label": "Procurement", "sub": "Blocker", "status": "risk"}, {"label": "AEs", "sub": "Users"}, {"label": "CFO", "sub": "Approver"}]}})
def r_orbit(c, d):
    x0, y0, w, h = area(c)
    sats = d["satellites"]; n = len(sats); cx, cy = x0 + w / 2, y0 + h / 2; R = min(w, h) / 2 - 80
    c.circle(cx, cy, R, "none", stroke=c.P["context"], sw=2, opacity=1)
    for i, s in enumerate(sats):
        a = -math.pi / 2 + 2 * math.pi * i / n; px, py = cx + R * math.cos(a), cy + R * math.sin(a)
        c.line(cx, cy, px, py, c.P["context"], 2)
    c.circle(cx, cy, 78, c.P["ink"]); c.text_block(cx, cy + 7, d["center"], 22, 10, "#FFFFFF", 700, "middle", valign="middle")
    for i, s in enumerate(sats):
        a = -math.pi / 2 + 2 * math.pi * i / n; px, py = cx + R * math.cos(a), cy + R * math.sin(a)
        col = {"good": c.P["accent2"], "risk": c.P["risk"]}.get(s.get("status"), c.P["accent"])
        col = c.color_for(i, col)
        c.circle(px, py, 60, col, stroke=c.P["bg"], sw=4)
        c.text_block(px, py + 5, s["label"], 15, 12, contrast_text(col), 700, "middle", valign="middle")
        if s.get("sub"): c.text(px, py + 84, s["sub"], 15, c.ink_for(i), 500, anchor="middle")

@diagram("network", {"title": "The orchestrator is the single point of failure", "data": {
    "nodes": [{"id": "crm", "label": "CRM"}, {"id": "wh", "label": "Warehouse"}, {"id": "orch", "label": "Orchestrator", "status": "risk"}, {"id": "llm", "label": "LLM"}, {"id": "human", "label": "Reviewer"}, {"id": "out", "label": "Outreach"}],
    "edges": [["crm", "orch"], ["wh", "orch"], ["orch", "llm"], ["llm", "orch"], ["orch", "human"], ["human", "out"]],
    "layout": "circle"}})
def r_network(c, d):
    x0, y0, w, h = area(c)
    nodes = d["nodes"]; n = len(nodes); pos = {}
    if d.get("layout", "circle") == "circle":
        cx, cy = x0 + w / 2, y0 + h / 2; R = min(w, h) / 2 - 70
        for i, nd in enumerate(nodes):
            a = -math.pi / 2 + 2 * math.pi * i / n; pos[nd["id"]] = (cx + R * math.cos(a), cy + R * math.sin(a))
    else:
        for nd in nodes: pos[nd["id"]] = (x0 + nd["x"] * w, y0 + nd["y"] * h)
    for e in d["edges"]:
        a, b = pos[e[0]], pos[e[1]]; dx, dy = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dy) or 1
        ax, ay = a[0] + dx / L * 62, a[1] + dy / L * 62; bx, by = b[0] - dx / L * 66, b[1] - dy / L * 66
        c.line(ax, ay, bx, by, c.P["muted"], 2.5, arrow=True)
        if len(e) > 2: c.text((ax + bx) / 2, (ay + by) / 2 - 8, e[2], 14, c.P["muted"], anchor="middle")
    for i, nd in enumerate(nodes):
        px, py = pos[nd["id"]]
        col = {"good": c.P["accent2"], "risk": c.P["risk"]}.get(nd.get("status"), c.P["accent"]); col = c.color_for(i, col)
        c.circle(px, py, 62, col, stroke=c.P["bg"], sw=4)
        c.text_block(px, py + 5, nd["label"], 15, 13, contrast_text(col), 700, "middle", valign="middle")

@diagram("tree", {"title": "Hitting $30M needs win rate, not more pipeline", "data": {"root": {"label": "ARR target", "value": "$30M"},
    "children": [{"label": "Pipeline", "value": "$120M", "children": [{"label": "Inbound", "value": "$70M"}, {"label": "Outbound", "value": "$50M"}]},
                 {"label": "Win rate", "value": "25%", "status": "risk", "children": [{"label": "Enterprise", "value": "18%", "status": "risk"}, {"label": "Mid-market", "value": "31%"}]},
                 {"label": "ACV", "value": "$48K", "children": [{"label": "Land", "value": "$32K"}, {"label": "Expand", "value": "+$16K"}]}]}})
def r_tree(c, d):
    x0, y0, w, h = area(c)
    root = dict(d["root"]); kids = d.get("children", []); root["children"] = kids
    levels = [[root], kids, [g for k in kids for g in k.get("children", [])]]
    levels = [l for l in levels if l]
    lh = h / len(levels); bw, bh = min(240, w / max(len(levels[-1]), 1) - 16), 80
    pos = {}
    def draw(node, x, y, i):
        col = {"good": c.P["accent2"], "risk": c.P["risk"]}.get(node.get("status"), c.P["accent"])
        if node is root: col = c.P["ink"]
        c.box(x - bw / 2, y - bh / 2, bw, bh, node["label"], col, size=19, sub=node.get("value"), rx=12)
    for li, lvl in enumerate(levels):
        for i, node in enumerate(lvl):
            # place children under parents: distribute evenly across the width for simplicity
            x = x0 + (i + 0.5) * w / len(lvl); y = y0 + li * lh + bh / 2 + 10
            pos[id(node)] = (x, y)
    for li, lvl in enumerate(levels[:-1]):
        for node in lvl:
            for ch in node.get("children", []):
                if id(ch) in pos:
                    (px, py), (cx_, cy_) = pos[id(node)], pos[id(ch)]
                    c.path(f"M{px},{py + bh/2} C{px},{(py+cy_)/2} {cx_},{(py+cy_)/2} {cx_},{cy_ - bh/2}", stroke=c.P["line"], sw=2.5)
    for li, lvl in enumerate(levels):
        for i, node in enumerate(lvl):
            x, y = pos[id(node)]; draw(node, x, y, i)
    if d.get("formula"): c.text(x0 + w / 2, y0 + h + 10, d["formula"], 17, c.P["muted"], anchor="middle")

@diagram("pyramid", {"title": "Campaigns only work when the layers beneath them are set", "data": {
    "levels": [{"label": "Campaigns", "sub": "Tactics"}, {"label": "Proof", "sub": "Evidence"}, {"label": "Narrative", "sub": "Point of view"}, {"label": "Category", "sub": "The frame"}],
    "inverted": False}, "highlight": [3]})
def r_pyramid(c, d):
    x0, y0, w, h = area(c)
    lv = d["levels"]; n = len(lv); inv = d.get("inverted", False)
    cx = x0 + w * 0.42; maxw = w * 0.7; lh = (h - 20) / n
    for i, l in enumerate(lv):
        k = (n - i) if inv else (i + 1)
        tw, bw_ = maxw * (k - 1) / n, maxw * k / n
        if inv: tw, bw_ = bw_, tw
        y = y0 + i * lh
        pts = [(cx - tw / 2, y), (cx + tw / 2, y), (cx + bw_ / 2, y + lh - 6), (cx - bw_ / 2, y + lh - 6)]
        fill = c.color_for(i, tint(c.P["accent"], 0.1 + 0.15 * i)); c.polygon(pts, fill)
        c.text(cx, y + lh / 2 + 6, l["label"], 22, contrast_text(fill, c.P["ink"]), 700, anchor="middle")
        if l.get("sub"): c.text(cx + maxw / 2 + 40, y + lh / 2 + 6, l["sub"], 18, c.ink_for(i), 500)

@diagram("concentric", {"title": "The reachable market is $180M, not $4B", "data": {
    "rings": [{"label": "TAM", "sub": "$4B", "r": 1.0}, {"label": "SAM", "sub": "$900M", "r": 0.62}, {"label": "SOM", "sub": "$180M", "r": 0.3}]}, "highlight": [2]})
def r_concentric(c, d):
    x0, y0, w, h = area(c)
    rings = d["rings"]; cx, cy = x0 + w * 0.38, y0 + h / 2; R = min(w * 0.38, h / 2) - 10
    for i, rg in enumerate(rings):
        r = R * rg["r"]; fill = c.color_for(i, tint(c.P["accent"], 0.85 - 0.3 * i / max(len(rings) - 1, 1)))
        c.circle(cx, cy + (R - r), r, fill, stroke=c.P["bg"], sw=3)
    for i, rg in enumerate(rings):
        r = R * rg["r"]; ty = cy + (R - r) - r + 34 if i < len(rings) - 1 else cy + (R - r)
        lx = x0 + w * 0.78
        c.text(lx, ty, rg["label"], 22, c.ink_for(i), 700); c.text(lx + 90, ty, rg.get("sub", ""), 22, c.ink_for(i), 400)
        c.line(cx, ty - 6, lx - 16, ty - 6, c.P["line"], 1.5, dash="4,4")

@diagram("venn", {"title": "The wedge is where AI capability meets urgent buyer pain", "data": {
    "sets": ["What AI can do well", "What buyers urgently need", "What we can deliver now"], "center": "The wedge"}})
def r_venn(c, d):
    x0, y0, w, h = area(c)
    sets = d["sets"]; n = len(sets); cx, cy = x0 + w / 2, y0 + h / 2 + 20; R = min(w, h) * 0.30
    off = R * 0.55
    centers = [(cx, cy - off)] + [(cx + off * (1 if i == 1 else -1) * 0.95, cy + off * 0.6) for i in (1, 2)] if n == 3 else [(cx - off, cy), (cx + off, cy)]
    for i, (px, py) in enumerate(centers[:n]):
        c.circle(px, py, R, tint(c.P["accent"], 0.55 + 0.15 * i), opacity=0.6, stroke=c.P["bg"], sw=3)
    for i, (px, py) in enumerate(centers[:n]):
        a = math.atan2(py - cy, px - cx); lx, ly = px + math.cos(a) * R * 0.55, py + math.sin(a) * R * 0.55
        c.text_block(lx, ly, sets[i], 18, 18, c.P["ink"], 700, "middle", valign="middle")
    if d.get("center"):
        c.circle(cx, cy + (0 if n == 3 else 0), 60, c.P["ink"]); c.text_block(cx, cy + 6, d["center"], 17, 10, "#FFFFFF", 700, "middle", valign="middle")

@diagram("iceberg", {"title": "The pipeline miss is a symptom; positioning is the cause", "data": {
    "above": ["Missed pipeline target", "Low reply rates"], "below": ["Undifferentiated message", "No ICP discipline", "Handoffs leak 30% of leads", "No signal-to-action loop"]}})
def r_iceberg(c, d):
    x0, y0, w, h = area(c)
    wl = y0 + h * 0.32; cx = x0 + w * 0.32
    c.rect(x0, wl, w, h - (wl - y0), tint(c.P["accent"], 0.85), rx=0)
    c.polygon([(cx - 120, wl), (cx + 120, wl), (cx + 40, y0 + 20), (cx - 60, y0 + 50)], tint(c.P["accent"], 0.5))
    c.polygon([(cx - 120, wl), (cx + 120, wl), (cx + 200, wl + (h - (wl - y0)) * 0.5), (cx + 20, y0 + h - 10), (cx - 190, wl + (h - (wl - y0)) * 0.6)], c.P["accent"])
    c.text(x0 + w * 0.6, y0 + 30, "What everyone sees", 18, c.P["muted"], 700)
    for i, t in enumerate(d["above"]):
        c.text(x0 + w * 0.6, y0 + 66 + i * 32, "• " + t, 19, c.P["ink"])
    c.text(x0 + w * 0.6, wl + 40, "What actually drives it", 18, c.P["accent"], 700)
    for i, t in enumerate(d["below"]):
        c.text(x0 + w * 0.6, wl + 76 + i * 32, "• " + t, 19, c.P["ink"], 600)

@diagram("staircase", {"title": "Most teams are stuck on step two", "data": {
    "steps": [{"label": "Experimenting", "sub": "Individual prompts"}, {"label": "Enabling", "sub": "Tools + training"}, {"label": "Scaling", "sub": "Workflows + governance"}, {"label": "AI-native", "sub": "Redesigned operating model"}],
    "marker": {"step": 1, "label": "Most teams today"}}, "highlight": [3]})
def r_staircase(c, d):
    x0, y0, w, h = area(c)
    st = d["steps"]; n = len(st); sw = w / n; rise = (h - 80) / n; base = y0 + h - 20
    for i, s in enumerate(st):
        x = x0 + i * sw; top = base - rise * (i + 1)
        fill = c.color_for(i, tint(c.P["accent"], 0.6 - 0.2 * i / max(n - 1, 1)))
        c.rect(x, top, sw - 6, base - top, fill, rx=6)
        c.text(x + 18, top + 36, s["label"], 22, contrast_text(fill, c.P["ink"]), 700)
        if s.get("sub"): c.text_block(x + 18, top + 64, s["sub"], 16, int((sw - 36) / 9), contrast_text(fill, c.P["ink"]))
    m = d.get("marker")
    if m:
        x = x0 + m["step"] * sw + sw / 2; top = base - rise * (m["step"] + 1)
        c.circle(x, top - 40, 14, c.P["risk"]); c.line(x, top - 26, x, top - 4, c.P["risk"], 3, arrow=True)
        c.text(x, top - 66, m["label"], 17, c.P["risk"], 700, anchor="middle")

@diagram("ladder", {"title": "Delegate authority one rung at a time", "data": {
    "rungs": [{"label": "Execute within guardrails", "sub": "No approval, monitored"}, {"label": "Execute with approval", "sub": "Human sign-off"}, {"label": "Recommend", "sub": "Ranked options"}, {"label": "Suggest", "sub": "Drafts only"}],
    "marker": {"rung": 2, "label": "Today"}}, "highlight": [1]})
def r_ladder(c, d):
    x0, y0, w, h = area(c)
    rungs = d["rungs"]; n = len(rungs); lx = x0 + w * 0.12; lw = w * 0.5; rh = (h - 20) / n
    c.rect(lx - 14, y0, 14, h - 20, c.P["muted"], rx=4); c.rect(lx + lw, y0, 14, h - 20, c.P["muted"], rx=4)
    for i, r in enumerate(rungs):
        y = y0 + i * rh + rh / 2; fill = c.color_for(i)
        c.rect(lx, y - 34, lw, 68, fill, rx=8)
        c.text(lx + 22, y - 2, r["label"], 21, contrast_text(fill, c.P["ink"]), 700)
        if r.get("sub"): c.text(lx + 22, y + 24, r["sub"], 15, contrast_text(fill, c.P["ink"]))
        c.text(lx + lw + 40, y + 6, f"{n - i}", 22, c.P["muted"], 700)
    m = d.get("marker")
    if m:
        y = y0 + m["rung"] * rh + rh / 2
        c.text(lx + lw + 80, y + 6, "◀ " + m["label"], 19, c.P["risk"], 700)

@diagram("bridge", {"title": "Three planks get us from tool sprawl to a revenue system", "data": {
    "from": {"label": "Today", "sub": "14 tools, manual handoffs, lagging reports"}, "to": {"label": "Future", "sub": "Signal-driven plays, one operating rhythm"},
    "planks": ["Unify data + signals", "Codify plays with human approval", "Run a weekly learning loop"]}})
def r_bridge(c, d):
    x0, y0, w, h = area(c)
    pw = w * 0.22; by = y0 + h * 0.45
    for k, side in enumerate(["from", "to"]):
        x = x0 if k == 0 else x0 + w - pw; fill = c.P["muted"] if k == 0 else c.P["accent2"]
        c.rect(x, by - 60, pw, 220, fill, rx=14)
        c.text(x + pw / 2, by - 20, d[side]["label"], 24, contrast_text(fill), 700, anchor="middle")
        c.text_block(x + pw / 2, by + 16, d[side].get("sub", ""), 16, int(pw / 9), contrast_text(fill), 400, "middle")
    planks = d["planks"]; n = len(planks); px = x0 + pw + 20; pwid = (w - 2 * pw - 40) / n
    c.rect(px, by + 40, w - 2 * pw - 40, 18, c.P["ink"], rx=4)
    for i, p in enumerate(planks):
        x = px + i * pwid + 10; fill = c.color_for(i)
        c.rect(x, by - 50, pwid - 20, 80, fill, rx=10)
        c.text_block(x + (pwid - 20) / 2, by - 4, p, 17, int((pwid - 40) / 9.5), contrast_text(fill, c.P["ink"]), 700, "middle", valign="middle")
        c.line(x + (pwid - 20) / 2, by + 30, x + (pwid - 20) / 2, by + 40, c.P["ink"], 4)
    c.text(x0 + w / 2, by + 100, d.get("caption", ""), 17, c.P["muted"], anchor="middle")

@diagram("before_after", {"title": "From a funnel of activities to a system that learns", "data": {
    "left": {"title": "Old model", "items": ["Volume KPIs (MQLs, sends)", "Handoffs by email", "Quarterly retros", "Tool-by-tool automation"]},
    "right": {"title": "New model", "items": ["Business KPIs (pipeline, win rate)", "Signal-driven orchestration", "Weekly learning loop", "One operating rhythm"]}}})
def r_before_after(c, d):
    x0, y0, w, h = area(c)
    gap = 60; cw = (w - gap) / 2
    for k, side in enumerate(["left", "right"]):
        s = d[side]; x = x0 + k * (cw + gap); fill = c.P["muted"] if k == 0 else c.P["accent2"]
        c.rect(x, y0, cw, h, tint(fill, 0.88), rx=16)
        c.rect(x, y0, cw, 60, fill, rx=16); c.rect(x, y0 + 32, cw, 28, fill, rx=0)
        c.text(x + cw / 2, y0 + 40, s["title"], 24, contrast_text(fill), 700, anchor="middle")
        for i, it in enumerate(s["items"]):
            yy = y0 + 110 + i * 56
            c.text(x + 28, yy, ("✕ " if k == 0 else "✓ "), 20, fill, 700); c.text_block(x + 58, yy, it, 19, int((cw - 80) / 10), c.P["ink"], 600 if k else 400)
    ax = x0 + cw + gap / 2; c.polygon([(ax - 18, y0 + h / 2 - 26), (ax + 12, y0 + h / 2), (ax - 18, y0 + h / 2 + 26)], c.P["ink"])

@diagram("spectrum", {"title": "Move plays right only as confidence and consequence allow", "data": {
    "left": "Assistive", "right": "Autonomous", "points": [{"label": "Drafts & summaries", "x": 0.12}, {"label": "Recommended next steps", "x": 0.38}, {"label": "Auto-send with approval", "x": 0.62}, {"label": "Self-optimizing plays", "x": 0.9}],
    "thresholds": [{"x": 0.5, "label": "Human approval required →"}]}, "highlight": [1]})
def r_spectrum(c, d):
    x0, y0, w, h = area(c)
    y = y0 + h * 0.45
    c.parts.append(f'<defs><linearGradient id="spec" x1="0" x2="1"><stop offset="0" stop-color="{tint(c.P["accent"], 0.8)}"/><stop offset="1" stop-color="{c.P["accent"]}"/></linearGradient></defs>')
    c.rect(x0, y - 16, w, 32, "url(#spec)", rx=16)
    c.text(x0, y - 40, d.get("left", ""), 20, c.P["muted"], 700); c.text(x0 + w, y - 40, d.get("right", ""), 20, c.P["muted"], 700, anchor="end")
    for i, p in enumerate(d["points"]):
        px = x0 + p["x"] * w; col = c.mark_color(i, c.P["ink"])
        c.circle(px, y, 14, col, stroke=c.P["bg"], sw=3)
        c.text_block(px, y + 50 + (i % 2) * 40, p["label"], 17, 22, c.ink_for(i), 700 if i in c.hl else 500, "middle")
    for t in d.get("thresholds", []):
        tx = x0 + t["x"] * w; c.line(tx, y - 70, tx, y + 130, c.P["risk"], 2.5, dash="6,6")
        c.text(tx + 10, y - 80, t["label"], 16, c.P["risk"], 700)

@diagram("triangle", {"title": "You can optimize two; the third is the tradeoff", "data": {"corners": ["Speed", "Quality", "Cost"], "center": "AI content ops", "emphasis": [0, 1]}})
def r_triangle(c, d):
    x0, y0, w, h = area(c)
    cx, cy = x0 + w / 2, y0 + h / 2 + 30; R = min(w, h) * 0.38
    pts = [(cx + R * math.cos(-math.pi / 2 + 2 * math.pi * i / 3), cy + R * math.sin(-math.pi / 2 + 2 * math.pi * i / 3)) for i in range(3)]
    c.polygon(pts, tint(c.P["accent"], 0.9), stroke=c.P["accent"], sw=3)
    em = set(d.get("emphasis", []))
    for i, (px, py) in enumerate(pts):
        col = c.P["accent"] if i in em else c.P["context"]
        c.circle(px, py, 58, col, stroke=c.P["bg"], sw=4)
        c.text_block(px, py + 7, d["corners"][i], 19, 11, contrast_text(col, c.P["ink"]), 700, "middle", valign="middle")
    if d.get("center"): c.text_block(cx, cy + 20, d["center"], 20, 16, c.P["ink"], 700, "middle", valign="middle")

@diagram("cascade", {"title": "Our strategic choices, top to bottom", "data": {"steps": [
    {"label": "Winning aspiration", "sub": "Own 'AI-native GTM' for mid-market SaaS"}, {"label": "Where to play", "sub": "RevOps-led orgs, $20-200M ARR"},
    {"label": "How to win", "sub": "Signal-to-action plays with proof"}, {"label": "Capabilities", "sub": "Data, plays, enablement, evals"}, {"label": "Systems", "sub": "Weekly loop, decision rights, dashboards"}]}})
def r_cascade(c, d):
    x0, y0, w, h = area(c)
    st = d["steps"]; n = len(st); bh = min(110, (h - 10) / n); bw = w * 0.55
    for i, s in enumerate(st):
        x = x0 + i * (w - bw) / max(n - 1, 1); y = y0 + i * bh; fill = c.color_for(i, tint(c.P["accent"], 0.12 * i))
        c.box(x, y, bw, bh - 12, s["label"], fill, size=21, sub=s.get("sub"), rx=10)
        if i < n - 1: c.line(x + bw * 0.5, y + bh - 12, x + bw * 0.5 + (w - bw) / max(n - 1, 1), y + bh, c.P["muted"], 2, arrow=True)

@diagram("wedge", {"title": "Win the narrow use case first, then own the category", "data": {
    "stages": [{"label": "Wedge", "sub": "Intent-triggered outbound"}, {"label": "Expand", "sub": "Full-funnel plays"}, {"label": "Platform", "sub": "Revenue operating system"}, {"label": "Category", "sub": "AI-native GTM"}]}, "highlight": [0]})
def r_wedge(c, d):
    x0, y0, w, h = area(c)
    st = d["stages"]; n = len(st); cy = y0 + h / 2
    cy = y0 + (h - 90) / 2
    c.polygon([(x0, cy - 20), (x0 + w, y0), (x0 + w, y0 + h - 90), (x0, cy + 20)], tint(c.P["accent"], 0.85))
    for i, s in enumerate(st):
        x = x0 + (i + 0.5) * w / n; half = 20 + (h / 2 - 20) * (i + 0.5) / n
        col = c.color_for(i)
        c.circle(x, cy, 26 + 8 * i, col, stroke=c.P["bg"], sw=3)
        ly = y0 + h - 60
        c.text(x, ly, s["label"], 22, c.ink_for(i), 700, anchor="middle")
        if s.get("sub"): c.text_block(x, ly + 28, s["sub"], 16, int(w / n / 10), c.P["muted"], anchor="middle")

@diagram("message_house", {"title": "Message house", "data": {"roof": "AI-native GTM turns signals into revenue - without adding headcount",
    "pillars": [{"title": "See every signal", "proof": ["Intent + product + CRM in one view", "Live in 30 days"]}, {"title": "Act in hours, not weeks", "proof": ["Pre-built plays", "Human approval built in"]}, {"title": "Learn every week", "proof": ["Outcome feedback loop", "2x reply rate in 90 days"]}],
    "foundation": "Proof: 40 customers, 3 case studies, independent benchmark"}})
def r_message_house(c, d):
    x0, y0, w, h = area(c)
    roofh = 120; c.polygon([(x0, y0 + roofh), (x0 + w / 2, y0), (x0 + w, y0 + roofh)], c.P["ink"])
    c.text_block(x0 + w / 2, y0 + roofh - 30, d["roof"], 20, int(w / 14), "#FFFFFF", 700, "middle", valign="middle")
    pil = d["pillars"]; n = len(pil); gap = 24; pw = (w - gap * (n - 1)) / n; ph = h - roofh - 110; py = y0 + roofh + 14
    for i, p in enumerate(pil):
        x = x0 + i * (pw + gap); fill = c.color_for(i)
        c.rect(x, py, pw, ph, tint(c.P["context"], 0.5), rx=10)
        c.rect(x, py, pw, 56, fill, rx=10); c.rect(x, py + 30, pw, 26, fill, rx=0)
        c.text_block(x + pw / 2, py + 35, p["title"], 19, int(pw / 11), contrast_text(fill), 700, "middle", valign="middle")
        ly = py + 92
        for pr in p.get("proof", []):
            c.circle(x + 22, ly - 6, 4, c.P["muted"]); nl = c.text_block(x + 36, ly, pr, 16, int((pw - 50) / 9)); ly += 24 * nl + 6
    fy = y0 + h - 80; c.rect(x0, fy, w, 70, c.P["muted"], rx=10)
    c.text_block(x0 + w / 2, fy + 42, d.get("foundation", ""), 18, int(w / 11), "#FFFFFF", 600, "middle", valign="middle")

@diagram("funnel_flywheel", {"title": "The funnel feeds the flywheel", "data": {
    "funnel": ["Attract", "Qualify", "Close"], "wheel": ["Onboard", "Adopt", "Expand", "Advocate"]}})
def r_funnel_flywheel(c, d):
    x0, y0, w, h = area(c)
    fw = w * 0.36; cx = x0 + fw / 2; n = len(d["funnel"]); rh = h / n * 0.9
    for i, s in enumerate(d["funnel"]):
        frac = 1 - i * 0.28; bw = fw * frac; y = y0 + i * rh
        c.rect(cx - bw / 2, y, bw, rh - 12, tint(c.P["accent"], 0.6 - 0.2 * i), rx=8)
        c.text(cx, y + rh / 2, s, 20, c.P["ink"], 700, anchor="middle")
    wx, wy = x0 + w * 0.7, y0 + h / 2; R = min(w * 0.25, h / 2 - 50)
    fy = y0 + (n - 1) * rh + (rh - 12) / 2
    c.path(f"M{cx + fw * 0.22},{fy} C{cx + fw * 0.6},{fy} {wx - R - 120},{wy} {wx - R - 86},{wy}", stroke=c.P["muted"], sw=3, arrow=True)
    c.circle(wx, wy, R, "none", stroke=c.P["line"], sw=3)
    m = len(d["wheel"])
    for i in range(m):
        a1 = -math.pi / 2 + 2 * math.pi * (i + 0.3) / m; a2 = -math.pi / 2 + 2 * math.pi * (i + 0.7) / m
        c.path(f"M{wx + R*math.cos(a1):.1f},{wy + R*math.sin(a1):.1f} A{R},{R} 0 0 1 {wx + R*math.cos(a2):.1f},{wy + R*math.sin(a2):.1f}", stroke=c.P["muted"], sw=4, arrow=True)
    for i, lab in enumerate(d["wheel"]):
        a = -math.pi / 2 + 2 * math.pi * i / m; px, py = wx + R * math.cos(a), wy + R * math.sin(a)
        c.box(px - 80, py - 30, 160, 60, lab, c.P["accent2"], size=18, rx=30)

@diagram("scatter_labels", {"title": "Custom AI components are where differentiation lives", "data": {
    "x_axis": "Genesis → Custom → Product → Commodity", "y_axis": "Value to buyer →",
    "items": [{"label": "Foundation models", "x": 0.85, "y": 0.3}, {"label": "CRM", "x": 0.9, "y": 0.5}, {"label": "Signal decisioning", "x": 0.3, "y": 0.85}, {"label": "Play library", "x": 0.45, "y": 0.7}, {"label": "Eval harness", "x": 0.2, "y": 0.55}]}, "highlight": [2, 3]})
def r_scatter_labels(c, d):
    d2 = dict(d); d2["quadrants"] = d.get("quadrants", ["", "", "", ""]); d2["shade_first"] = False
    r_two_by_two(c, d2)

# ------------------------------------------------------------------ signature visuals (neutral templates)
@diagram("signature_revenue_os", {"title": "The AI-native revenue operating model", "subtitle": "Signals in, learning out - humans decide, agents do the work", "data": {
    "signals": ["Intent", "Product usage", "CRM & pipeline", "Content engagement", "Market & news"],
    "intelligence": {"label": "Intelligence layer", "sub": "Enrich · score · decide"},
    "agents": ["Research agent", "Outreach agent", "Content agent", "Analyst agent"],
    "humans": ["Approve", "Relate", "Decide", "Coach"],
    "actions": ["Personalized outreach", "Account plays", "Enablement", "Forecast"],
    "governance": "Governance: decision rights · guardrails · evals · audit",
    "loop": "Outcomes feed back into scoring and plays every week"}})
def r_signature_revenue_os(c, d):
    x0, y0, w, h = area(c)
    colw = w * 0.2; gap = (w - colw * 4) / 3
    def column(k, title, items, fill):
        x = x0 + k * (colw + gap)
        c.text(x + colw / 2, y0 + 16, title, 18, c.P["muted"], 700, anchor="middle")
        ih = min(64, (h - 180) / max(len(items), 1)); y = y0 + 40
        for it in items:
            c.box(x, y, colw, ih - 10, it, fill, size=17, rx=10); y += ih
        return x
    column(0, "SIGNALS", d["signals"], tint(c.P["accent"], 0.75))
    x1 = x0 + 1 * (colw + gap); ih = h - 180
    c.box(x1, y0 + 40, colw, ih * 0.62, d["intelligence"]["label"], c.P["accent"], size=21, sub=d["intelligence"].get("sub"), rx=14)
    hy = y0 + 40 + ih * 0.62 + 12
    c.rect(x1, hy, colw, ih * 0.38 - 12, tint(c.P["accent2"], 0.8), rx=14)
    c.text(x1 + colw / 2, hy + 28, "HUMANS", 15, c.P["ink"], 700, anchor="middle")
    c.text_block(x1 + colw / 2, hy + 56, " · ".join(d["humans"]), 15, int(colw / 8.5), c.P["ink"], 500, "middle")
    column(2, "AGENTS", d["agents"], c.P["accent2"])
    column(3, "ACTIONS", d["actions"], c.P["ink"])
    ay = y0 + 40 + (h - 180) / 2
    for k in range(3):
        xa = x0 + k * (colw + gap) + colw + 6; c.line(xa, ay, xa + gap - 12, ay, c.P["muted"], 3, arrow=True)
    gy = y0 + h - 120; c.rect(x0, gy, w, 44, tint(c.P["risk"], 0.85), rx=10)
    c.text(x0 + w / 2, gy + 29, d["governance"], 17, c.P["ink"], 700, anchor="middle")
    c.path(f"M{x0 + w - 30},{gy + 52} C{x0 + w + 40},{gy + 96} {x0 - 40},{gy + 96} {x0 + 30},{gy + 52}", stroke=c.P["muted"], sw=2.5, arrow=True, dash="6,6")
    c.text(x0 + w / 2, gy + 110, d["loop"], 16, c.P["muted"], 600, anchor="middle")

@diagram("signature_signal_to_action", {"title": "Signal-to-action architecture", "subtitle": "From buyer signal to personalized action in hours, with a human at the gate", "data": {
    "stages": [{"label": "Signal", "sub": "Intent, usage, hiring, news", "items": ["3rd-party intent", "Product events", "Web + content", "CRM changes"]},
               {"label": "Enrich", "sub": "Context + fit", "items": ["Firmographics", "Contacts", "History", "ICP score"]},
               {"label": "Decide", "sub": "Which play, for whom", "items": ["Play rules", "Confidence score", "Priority queue"]},
               {"label": "Act", "sub": "Personalized, approved", "items": ["Outreach", "Ads", "Exec content", "Event invite"]},
               {"label": "Learn", "sub": "Outcomes back to scoring", "items": ["Replies", "Meetings", "Pipeline", "Wins"]}],
    "gate": {"after": 2, "label": "Human approval gate"}, "loop": "Feedback tunes scoring and plays"}})
def r_signature_signal_to_action(c, d):
    x0, y0, w, h = area(c)
    st = d["stages"]; n = len(st); gap = 26; sw = (w - gap * (n - 1)) / n; headh = 92
    for i, s in enumerate(st):
        x = x0 + i * (sw + gap); fill = c.P["accent"] if i < n - 1 else c.P["accent2"]
        c.box(x, y0, sw, headh, s["label"], fill, size=24, sub=s.get("sub"), rx=12)
        c.rect(x, y0 + headh + 10, sw, h - headh - 110, tint(c.P["context"], 0.5), rx=12)
        ly = y0 + headh + 46
        for it in s.get("items", []):
            c.circle(x + 20, ly - 6, 4, c.P["muted"]); c.text(x + 34, ly, it, 16, c.P["ink"]); ly += 30
        if i < n - 1: c.line(x + sw + 2, y0 + headh / 2, x + sw + gap - 4, y0 + headh / 2, c.P["muted"], 3, arrow=True)
    g = d.get("gate")
    if g:
        gx = x0 + (g["after"] + 1) * (sw + gap) - gap / 2
        c.line(gx, y0 + 20, gx, y0 + h - 100, c.P["risk"], 3, dash="8,6")
        c.rect(gx - 90, y0 - 30, 180, 30, c.P["risk"], rx=15); c.text(gx, y0 - 10, g["label"], 14, "#FFFFFF", 700, anchor="middle")
    c.path(f"M{x0 + w - 40},{y0 + h - 90} C{x0 + w},{y0 + h - 40} {x0},{y0 + h - 40} {x0 + 40},{y0 + h - 90}", stroke=c.P["muted"], sw=2.5, arrow=True, dash="6,6")
    c.text(x0 + w / 2, y0 + h - 24, d.get("loop", ""), 16, c.P["muted"], 600, anchor="middle")

@diagram("signature_audience_flywheel", {"title": "Audience → authority → pipeline", "subtitle": "Media is the demand engine: every turn of the wheel lowers the cost of the next customer", "data": {
    "nodes": [{"label": "Sharp POV content", "sub": "Newsletter, posts, reports"}, {"label": "Audience", "sub": "Subscribers, followers, community"}, {"label": "Authority", "sub": "Trust, category ownership"},
              {"label": "Conversations", "sub": "Inbound, referrals, invites"}, {"label": "Pipeline & customers", "sub": "Advisory, product, sponsors"}, {"label": "Proof & insight", "sub": "Cases, data, stories"}],
    "center": "Compounding trust", "accelerators": ["Consistency", "Distinct POV", "Distribution partners"]}})
def r_signature_audience_flywheel(c, d):
    x0, y0, w, h = area(c)
    nodes = d["nodes"]; n = len(nodes); cx, cy = x0 + w * 0.42, y0 + h / 2; R = min(w * 0.4, h / 2) - 70
    c.circle(cx, cy, R, "none", stroke=c.P["line"], sw=3)
    for i in range(n):
        a1 = -math.pi / 2 + 2 * math.pi * (i + 0.3) / n; a2 = -math.pi / 2 + 2 * math.pi * (i + 0.72) / n
        c.path(f"M{cx + R*math.cos(a1):.1f},{cy + R*math.sin(a1):.1f} A{R},{R} 0 0 1 {cx + R*math.cos(a2):.1f},{cy + R*math.sin(a2):.1f}", stroke=c.P["muted"], sw=4, arrow=True)
    for i, nd in enumerate(nodes):
        a = -math.pi / 2 + 2 * math.pi * i / n; px, py = cx + R * math.cos(a), cy + R * math.sin(a)
        fill = c.P["accent"] if i != 4 else c.P["accent2"]
        c.box(px - 115, py - 40, 230, 80, nd["label"], fill, size=18, sub=nd.get("sub"), rx=16)
    c.circle(cx, cy, 80, tint(c.P["accent"], 0.85)); c.text_block(cx, cy + 6, d.get("center", ""), 20, 12, c.P["ink"], 700, "middle", valign="middle")
    ax = x0 + w * 0.84; c.text(ax, y0 + 20, "Accelerators", 18, c.P["muted"], 700, anchor="middle")
    for j, acc in enumerate(d.get("accelerators", [])):
        c.box(ax - 110, y0 + 44 + j * 64, 220, 50, acc, tint(c.P["accent2"], 0.8), size=17, rx=25, txt=c.P["ink"])

@diagram("signature_category_map", {"title": "Category-creation narrative map", "subtitle": "Name the shift, and the category names itself", "data": {
    "old_world": {"title": "Old world", "items": ["Volume-based funnels", "Tool-by-tool automation", "Quarterly learning"]},
    "shift": {"title": "The shift", "items": ["Buyers signal intent everywhere", "Agents can act on signals", "Attention is the scarce input"]},
    "new_world": {"title": "New world", "items": ["Signal-driven plays", "Human-approved agents", "Weekly learning loop"]},
    "category": "AI-native GTM", "enemy": "The enemy: activity without learning", "stakes": "Winners compound; laggards pay more for every dollar of pipeline"}})
def r_signature_category_map(c, d):
    x0, y0, w, h = area(c)
    gap = 30; cw = (w - 2 * gap) / 3; ch = h - 150
    for k, key in enumerate(["old_world", "shift", "new_world"]):
        s = d[key]; x = x0 + k * (cw + gap); fill = [c.P["muted"], c.P["risk"], c.P["accent2"]][k]
        c.rect(x, y0, cw, ch, tint(fill, 0.88), rx=14)
        c.rect(x, y0, cw, 58, fill, rx=14); c.rect(x, y0 + 30, cw, 28, fill, rx=0)
        c.text(x + cw / 2, y0 + 38, s["title"], 22, contrast_text(fill), 700, anchor="middle")
        for i, it in enumerate(s["items"]):
            c.text_block(x + 24, y0 + 100 + i * 54, ("• ") + it, 18, int((cw - 40) / 10), c.P["ink"], 600 if k == 2 else 400)
        if k < 2: c.polygon([(x + cw + 6, y0 + ch / 2 - 18), (x + cw + gap - 6, y0 + ch / 2), (x + cw + 6, y0 + ch / 2 + 18)], c.P["ink"])
    cy_ = y0 + ch + 20
    c.rect(x0, cy_, w * 0.48, 62, c.P["ink"], rx=12); c.text(x0 + 20, cy_ + 40, "Category: " + d["category"], 22, "#FFFFFF", 800)
    c.text_block(x0 + w * 0.52, cy_ + 24, d.get("enemy", ""), 17, int(w * 0.48 / 9.5), c.P["risk"], 700)
    c.text_block(x0 + w * 0.52, cy_ + 50, d.get("stakes", ""), 16, int(w * 0.48 / 9), c.P["muted"], 500)

@diagram("signature_maturity_ladder", {"title": "AI maturity ladder", "subtitle": "What changes at each rung - and what most teams skip", "data": {
    "rungs": [{"label": "Experimenting", "people": "Individuals", "process": "Ad hoc prompts", "data": "Copy-paste", "governance": "None"},
              {"label": "Enabling", "people": "Trained teams", "process": "Templates + playbooks", "data": "Connected tools", "governance": "Usage policy"},
              {"label": "Scaling", "people": "AI operators", "process": "Automated workflows", "data": "Unified signals", "governance": "Decision rights + evals"},
              {"label": "AI-native", "people": "Redesigned roles", "process": "Agentic plays with learning loop", "data": "Proprietary data moat", "governance": "Continuous audit"}],
    "dimensions": ["People", "Process", "Data", "Governance"], "marker": {"rung": 1, "label": "Most teams today"}}, "highlight": [3]})
def r_signature_maturity_ladder(c, d):
    x0, y0, w, h = area(c)
    rungs = d["rungs"]; dims = d["dimensions"]; n = len(rungs); labw = w * 0.2; cw = (w - labw) / n; rh = (h - 60) / (len(dims) + 1)
    keys = [k.lower() for k in dims]
    for i, r in enumerate(rungs):
        x = x0 + labw + i * cw; fill = c.color_for(i, tint(c.P["accent"], 0.55 - 0.18 * i / max(n - 1, 1)))
        stepy = y0 + (n - 1 - i) * 14
        c.box(x + 6, stepy, cw - 12, rh - 10 - (n - 1 - i) * 14, r["label"], fill, size=21, rx=10)
    for j, dim in enumerate(dims):
        y = y0 + rh * (j + 1)
        c.rect(x0, y, w, rh - 8, tint(c.P["context"], 0.6 if j % 2 else 0.3), rx=8)
        c.text(x0 + 16, y + rh / 2 + 2, dim, 18, c.P["ink"], 700)
        for i, r in enumerate(rungs):
            x = x0 + labw + i * cw
            c.text_block(x + 16, y + rh / 2 - 4, r.get(keys[j], ""), 15, int((cw - 30) / 8.5), c.ink_for(i), 600 if i in c.hl else 400, valign="middle")
    m = d.get("marker")
    if m:
        x = x0 + labw + (m["rung"] + 0.5) * cw
        c.rect(x - 90, y0 + h - 44, 180, 34, c.P["risk"], rx=17); c.text(x, y0 + h - 21, m["label"], 15, "#FFFFFF", 700, anchor="middle")

# ------------------------------------------------------------------ main
def render(kind, spec):
    if kind not in TYPES: sys.exit(f"Unknown type '{kind}'. Run --types.")
    c = Canvas(spec, kind); TYPES[kind](c, spec.get("data", {}))
    return c.svg()

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("type", nargs="?"); ap.add_argument("spec", nargs="?")
    ap.add_argument("-o", "--out", default=None); ap.add_argument("--png", action="store_true"); ap.add_argument("--scale", type=float, default=2.0)
    ap.add_argument("--types", action="store_true"); ap.add_argument("--example")
    a = ap.parse_args()
    if a.types:
        for t in TYPES: print(t)
        return
    if a.example:
        ex = dict(EXAMPLES[a.example]); ex.setdefault("width", 1600); ex.setdefault("height", 900)
        print(json.dumps(ex, indent=2, ensure_ascii=False)); return
    if not a.type or not a.spec: ap.print_help(); return
    spec = json.load(open(a.spec)); svg = render(a.type, spec)
    out = a.out or os.path.splitext(a.spec)[0] + ".svg"
    open(out, "w").write(svg); print("wrote", out)
    if a.png:
        try:
            import cairosvg
            png = os.path.splitext(out)[0] + ".png"
            cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=png, scale=a.scale); print("wrote", png)
        except ImportError:
            print("PNG export needs cairosvg: pip install cairosvg --break-system-packages")

if __name__ == "__main__":
    main()
