#!/usr/bin/env python3
"""
chart.py - matplotlib charts that obey the visual-master design rules (one accent, muted context,
direct labels, takeaway title, no chart junk). Same spec envelope as render_svg.py.

Usage:
  python chart.py <kind> spec.json -o out.png [--svg]
  python chart.py --kinds
  python chart.py --example <kind> > spec.json

Kinds: bar, hbar, grouped_bar, stacked_bar, line, area, scatter, dot, histogram, pareto, tornado, scenario
Spec: {"title", "subtitle", "source", "width", "height" (px), "palette" {...same roles as render_svg...},
       "highlight": [indexes of series/categories to emphasize], "data": {...per kind, see --example}}
No network calls.
"""
import argparse, json, sys, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

PAL = {"bg": "#FFFFFF", "ink": "#111827", "muted": "#6B7280", "line": "#D1D5DB", "context": "#C7CBD1",
       "accent": "#2563EB", "accent2": "#059669", "risk": "#EA580C", "font": "DejaVu Sans"}

EX = {
 "bar": {"title": "Mid-market drives two-thirds of new pipeline", "source": "CRM, Q3", "highlight": [1],
         "data": {"categories": ["Enterprise", "Mid-market", "SMB"], "values": [3.1, 8.4, 1.2], "unit": "$M"}},
 "hbar": {"title": "Price is not the top objection - integration risk is", "highlight": [0],
          "data": {"categories": ["Integration risk", "No budget owner", "Price", "Security review", "Timing"], "values": [42, 31, 27, 19, 11], "unit": "%"}},
 "grouped_bar": {"title": "CAC fell on paid while outbound got more expensive", "highlight": [0],
                 "data": {"categories": ["Q1", "Q2", "Q3", "Q4"], "series": [{"name": "Paid", "values": [420, 380, 330, 300]}, {"name": "Outbound", "values": [510, 540, 600, 650]}, {"name": "Partner", "values": [280, 290, 285, 300]}], "unit": "$"}},
 "stacked_bar": {"title": "Inbound share of pipeline doubled in a year", "highlight": [0],
                 "data": {"categories": ["Q1", "Q2", "Q3", "Q4"], "series": [{"name": "Inbound", "values": [2, 3, 4.5, 6]}, {"name": "Outbound", "values": [4, 4, 3.8, 3.5]}, {"name": "Partner", "values": [1, 1.2, 1.5, 1.6]}], "unit": "$M", "percent": False}},
 "line": {"title": "Reply rates broke the trend after the signal-based plays launched", "source": "Outreach + CRM", "highlight": [0],
          "data": {"x": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"], "series": [{"name": "Reply rate", "values": [4.1, 4.0, 3.8, 3.9, 5.2, 6.8, 7.9, 8.4]}, {"name": "Industry median", "values": [4.5, 4.4, 4.4, 4.3, 4.3, 4.2, 4.2, 4.1]}], "unit": "%", "annotate": {"x": 4, "label": "Plays launched"}}},
 "area": {"title": "Total demand volume grew 3x, mostly from owned channels", "highlight": [0],
          "data": {"x": ["Q1", "Q2", "Q3", "Q4"], "series": [{"name": "Owned", "values": [10, 16, 25, 34]}, {"name": "Paid", "values": [8, 9, 10, 11]}, {"name": "Partner", "values": [3, 4, 6, 7]}], "unit": "K"}},
 "scatter": {"title": "Spend and pipeline are barely correlated above $50K per channel", "highlight": [3],
             "data": {"x_label": "Monthly spend ($K)", "y_label": "Pipeline ($M)", "points": [{"label": "Paid search", "x": 80, "y": 2.1}, {"label": "Events", "x": 120, "y": 2.4}, {"label": "Content", "x": 30, "y": 3.2}, {"label": "Community", "x": 15, "y": 2.9}, {"label": "Display", "x": 60, "y": 0.8}]}},
 "dot": {"title": "Only two campaigns beat the 3% conversion bar", "highlight": [0, 1],
         "data": {"categories": ["AI ROI webinar", "Benchmark report", "Product tour", "Newsletter promo", "Retargeting"], "values": [4.8, 3.6, 2.4, 1.9, 1.1], "target": 3, "unit": "%"}},
 "histogram": {"title": "Most deals are under $40K; the plan assumes $60K", "highlight": [],
               "data": {"values": [12, 18, 22, 25, 28, 31, 33, 35, 38, 40, 42, 45, 48, 55, 61, 70, 85, 120, 140, 210], "bins": 8, "unit": "$K", "marker": {"x": 60, "label": "Plan ACV"}}},
 "pareto": {"title": "Three objections cause 80% of lost deals", "highlight": [0, 1, 2],
            "data": {"categories": ["Integration risk", "No budget owner", "Price", "Security", "Timing", "Other"], "values": [38, 27, 16, 9, 6, 4]}},
 "tornado": {"title": "Win rate moves the plan more than any other assumption", "highlight": [0],
             "data": {"base": 30, "unit": "$M", "items": [{"label": "Win rate ±5 pts", "low": 24, "high": 36}, {"label": "ACV ±15%", "low": 26, "high": 34}, {"label": "Pipeline ±20%", "low": 27, "high": 33}, {"label": "Cycle ±10 d", "low": 29, "high": 31}]}},
 "scenario": {"title": "Even the downside case clears $24M if conversion holds", "highlight": [1],
              "data": {"x": ["Q1", "Q2", "Q3", "Q4"], "scenarios": [{"name": "Upside", "values": [6, 13, 21, 32]}, {"name": "Base", "values": [6, 12, 19, 28]}, {"name": "Downside", "values": [6, 11, 17, 24]}], "unit": "$M"}},
}

def tx(s):
    return str(s).replace("$", r"\$")

def setup(spec, left=0.08):
    P = dict(PAL); P.update(spec.get("palette") or {})
    W, H = spec.get("width", 1600), spec.get("height", 900)
    plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": [P.get("font", "DejaVu Sans"), "DejaVu Sans"], "axes.edgecolor": P["line"], "axes.labelcolor": P["muted"], "xtick.color": P["muted"], "ytick.color": P["muted"], "text.color": P["ink"]})
    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100, facecolor=P["bg"])
    ax = fig.add_axes([left, 0.14, 0.94 - left, 0.62]); ax.set_facecolor(P["bg"])
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.tick_params(length=0, labelsize=13)
    if spec.get("title"): fig.text(0.05, 0.93, tx(spec["title"]), fontsize=24, fontweight="bold", color=P["ink"], va="top", wrap=True)
    if spec.get("subtitle"): fig.text(0.05, 0.86, tx(spec["subtitle"]), fontsize=14, color=P["muted"], va="top")
    if spec.get("source"): fig.text(0.05, 0.03, tx("Source: " + spec["source"]), fontsize=10, color=P["muted"])
    return fig, ax, P

def col(P, i, hl, base=None, positive=True):
    base = base or P["accent"]
    if hl and i not in hl: return P["context"]
    return base

def fmt(v, unit):
    s = f"{v:,.1f}" if isinstance(v, float) and v % 1 else f"{v:,.0f}"
    unit = unit or ""
    return tx(f"{unit[0]}{s}{unit[1:]}" if unit[:1] and unit[0] in "$€£" else f"{s}{unit}")

def bar(spec, horizontal=False):
    fig, ax, P = setup(spec, left=0.2 if horizontal else 0.08); d = spec["data"]; hl = set(spec.get("highlight") or []); u = d.get("unit", "")
    cats, vals = d["categories"], d["values"]; cols = [col(P, i, hl) for i in range(len(vals))]
    if horizontal:
        y = np.arange(len(cats))[::-1]; ax.barh(y, vals, color=cols, height=0.62); ax.set_yticks(y); ax.set_yticklabels(cats, fontsize=14)
        for yi, v in zip(y, vals): ax.text(v + max(vals) * 0.01, yi, fmt(v, u), va="center", fontsize=13, fontweight="bold")
        ax.set_xticks([]); ax.spines["bottom"].set_visible(False)
    else:
        x = np.arange(len(cats)); ax.bar(x, vals, color=cols, width=0.62); ax.set_xticks(x); ax.set_xticklabels(cats, fontsize=14)
        for xi, v in zip(x, vals): ax.text(xi, v + max(vals) * 0.01, fmt(v, u), ha="center", fontsize=13, fontweight="bold")
        ax.set_yticks([]); ax.spines["left"].set_visible(False)
    return fig

def grouped_bar(spec, stacked=False):
    fig, ax, P = setup(spec); d = spec["data"]; hl = set(spec.get("highlight") or []); u = d.get("unit", "")
    cats, series = d["categories"], d["series"]; n = len(series); x = np.arange(len(cats)); w = 0.7 / (1 if stacked else n)
    shades = [P["accent"], P["accent2"], P["muted"], P["risk"]]
    bottom = np.zeros(len(cats))
    for i, s in enumerate(series):
        vals = np.array(s["values"], dtype=float)
        if d.get("percent") and stacked:
            tot = np.sum([np.array(t["values"], dtype=float) for t in series], axis=0); vals = vals / tot * 100
        c = col(P, i, hl, shades[i % len(shades)])
        if stacked:
            ax.bar(x, vals, bottom=bottom, color=c, width=0.62, label=s["name"])
            for xi, v, b in zip(x, vals, bottom):
                if i in hl or not hl: ax.text(xi, b + v / 2, fmt(v, "%" if d.get("percent") else u), ha="center", va="center", fontsize=12, color="white" if c != P["context"] else P["ink"], fontweight="bold")
            bottom += vals
        else:
            ax.bar(x + (i - (n - 1) / 2) * w, vals, width=w * 0.92, color=c, label=s["name"])
            if i in hl or not hl:
                for xi, v in zip(x + (i - (n - 1) / 2) * w, vals): ax.text(xi, v + max(vals) * 0.01, fmt(v, u), ha="center", fontsize=11, fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(cats, fontsize=14); ax.set_yticks([]); ax.spines["left"].set_visible(False)
    ax.legend(frameon=False, fontsize=12, loc="upper left", bbox_to_anchor=(0, 1.08), ncol=n)
    return fig

def line(spec, area=False):
    fig, ax, P = setup(spec); d = spec["data"]; hl = set(spec.get("highlight") or []); u = d.get("unit", "")
    x = np.arange(len(d["x"])); shades = [P["accent"], P["accent2"], P["muted"], P["risk"]]
    if area:
        ax.stackplot(x, *[s["values"] for s in d["series"]], colors=[col(P, i, hl, shades[i % 4]) for i in range(len(d["series"]))], alpha=0.9)
        top = np.sum([s["values"] for s in d["series"]], axis=0)
        for i, s in enumerate(d["series"]):
            ax.text(x[-1] + 0.1, np.sum([t["values"][-1] for t in d["series"][:i + 1]]) - s["values"][-1] / 2, s["name"], fontsize=13, va="center", color=P["ink"] if (i in hl or not hl) else P["muted"])
    else:
        for i, s in enumerate(d["series"]):
            c = col(P, i, hl, shades[i % 4]); lw = 4 if (i in hl or not hl) else 2.5
            ax.plot(x, s["values"], color=c, lw=lw, solid_capstyle="round")
            ax.text(x[-1] + 0.12, s["values"][-1], f"{s['name']}  {fmt(s['values'][-1], u)}", fontsize=13, va="center", fontweight="bold" if (i in hl or not hl) else "normal", color=P["ink"] if (i in hl or not hl) else P["muted"])
            if i in hl or not hl: ax.scatter([x[-1]], [s["values"][-1]], color=c, s=60, zorder=5)
    ax.set_xticks(x); ax.set_xticklabels(d["x"], fontsize=13); ax.set_xlim(-0.2, len(x) - 1 + (2.2 if not area else 1.5))
    ax.yaxis.grid(True, color=P["line"], lw=0.8); ax.set_axisbelow(True); ax.spines["left"].set_visible(False)
    an = d.get("annotate")
    if an:
        ax.axvline(an["x"], color=P["risk"], lw=1.5, ls="--"); ax.text(an["x"] + 0.08, ax.get_ylim()[1] * 0.97, an["label"], color=P["risk"], fontsize=12, va="top", fontweight="bold")
    return fig

def scatter(spec):
    fig, ax, P = setup(spec); d = spec["data"]; hl = set(spec.get("highlight") or [])
    for i, p in enumerate(d["points"]):
        c = col(P, i, hl); ax.scatter(p["x"], p["y"], s=220 * p.get("size", 1), color=c, edgecolor=P["bg"], lw=1.5, zorder=5)
        ax.text(p["x"], p["y"] + (ax.get_ylim()[1] - ax.get_ylim()[0]) * 0.03, p["label"], fontsize=12, ha="center", color=P["ink"] if (i in hl or not hl) else P["muted"], fontweight="bold" if i in hl else "normal")
    ax.set_xlabel(tx(d.get("x_label", "")), fontsize=13); ax.set_ylabel(tx(d.get("y_label", "")), fontsize=13); ax.grid(True, color=P["line"], lw=0.6); ax.set_axisbelow(True)
    return fig

def dot(spec):
    fig, ax, P = setup(spec, left=0.2); d = spec["data"]; hl = set(spec.get("highlight") or []); u = d.get("unit", "")
    cats, vals = d["categories"], d["values"]; y = np.arange(len(cats))[::-1]
    for yi, v, i in zip(y, vals, range(len(vals))):
        c = col(P, i, hl); ax.hlines(yi, 0, v, color=P["line"], lw=2); ax.scatter(v, yi, s=260, color=c, zorder=5)
        ax.text(v + max(vals) * 0.03, yi, fmt(v, u), va="center", fontsize=13, fontweight="bold", color=P["ink"] if (i in hl or not hl) else P["muted"])
    if d.get("target") is not None: ax.axvline(d["target"], color=P["ink"], lw=2, ls="--"); ax.text(d["target"], len(cats) - 0.4, f"target {fmt(d['target'], u)}", fontsize=12, ha="center", color=P["ink"])
    ax.set_yticks(y); ax.set_yticklabels(cats, fontsize=14); ax.set_xticks([]); ax.spines["bottom"].set_visible(False); ax.set_xlim(0, max(vals) * 1.25)
    return fig

def histogram(spec):
    fig, ax, P = setup(spec); d = spec["data"]; u = d.get("unit", "")
    ax.hist(d["values"], bins=d.get("bins", 10), color=P["accent"], edgecolor=P["bg"])
    m = d.get("marker")
    if m: ax.axvline(m["x"], color=P["risk"], lw=2.5, ls="--"); ax.text(m["x"], ax.get_ylim()[1] * 0.95, " " + m["label"], color=P["risk"], fontsize=13, fontweight="bold")
    ax.set_xlabel(tx(u), fontsize=12); ax.set_yticks([]); ax.spines["left"].set_visible(False)
    return fig

def pareto(spec):
    fig, ax, P = setup(spec); d = spec["data"]; hl = set(spec.get("highlight") or [])
    cats, vals = d["categories"], d["values"]; x = np.arange(len(cats)); cum = np.cumsum(vals) / sum(vals) * 100
    ax.bar(x, vals, color=[col(P, i, hl) for i in range(len(vals))], width=0.62)
    for xi, v in zip(x, vals): ax.text(xi, v + max(vals) * 0.01, f"{v}", ha="center", fontsize=12, fontweight="bold")
    ax2 = ax.twinx(); ax2.plot(x, cum, color=P["ink"], lw=2.5, marker="o"); ax2.set_ylim(0, 105); ax2.axhline(80, color=P["risk"], lw=1.5, ls="--")
    ax2.text(len(cats) - 0.6, 82, "80%", color=P["risk"], fontsize=12); ax2.set_yticks([]); [ax2.spines[s].set_visible(False) for s in ("top", "right", "left")]
    ax.set_xticks(x); ax.set_xticklabels(cats, fontsize=12, rotation=0); ax.set_yticks([]); ax.spines["left"].set_visible(False)
    return fig

def tornado(spec):
    fig, ax, P = setup(spec, left=0.2); d = spec["data"]; hl = set(spec.get("highlight") or []); u = d.get("unit", ""); base = d["base"]
    items = sorted(d["items"], key=lambda it: -(it["high"] - it["low"])); y = np.arange(len(items))[::-1]
    for yi, it, i in zip(y, items, range(len(items))):
        c = col(P, i, hl)
        ax.barh(yi, it["low"] - base, left=base, color=c if c == P["context"] else P["risk"], height=0.6)
        ax.barh(yi, it["high"] - base, left=base, color=c if c == P["context"] else P["accent2"], height=0.6)
        ax.text(it["low"] - 0.2, yi, fmt(it["low"], u), ha="right", va="center", fontsize=12); ax.text(it["high"] + 0.2, yi, fmt(it["high"], u), ha="left", va="center", fontsize=12)
    ax.axvline(base, color=P["ink"], lw=2); ax.text(base, len(items) - 0.3, f"base {fmt(base, u)}", ha="center", fontsize=12, fontweight="bold")
    ax.set_yticks(y); ax.set_yticklabels([it["label"] for it in items], fontsize=13); ax.set_xticks([]); ax.spines["bottom"].set_visible(False)
    return fig

def scenario(spec):
    fig, ax, P = setup(spec); d = spec["data"]; hl = set(spec.get("highlight") or []); u = d.get("unit", ""); x = np.arange(len(d["x"]))
    sc = d["scenarios"]; hi, lo = np.array(sc[0]["values"]), np.array(sc[-1]["values"])
    ax.fill_between(x, lo, hi, color=P["accent"], alpha=0.12)
    for i, s in enumerate(sc):
        c = col(P, i, hl, P["accent"] if i == 1 else P["muted"]); lw = 4 if (i in hl or not hl) else 2
        ax.plot(x, s["values"], color=c, lw=lw, ls="-" if i == 1 else "--"); ax.text(x[-1] + 0.1, s["values"][-1], f"{s['name']}  {fmt(s['values'][-1], u)}", fontsize=13, va="center", fontweight="bold" if i in hl else "normal")
    ax.set_xticks(x); ax.set_xticklabels(d["x"], fontsize=13); ax.set_xlim(-0.2, len(x) + 1); ax.yaxis.grid(True, color=P["line"], lw=0.8); ax.set_axisbelow(True); ax.spines["left"].set_visible(False)
    return fig

KINDS = {"bar": bar, "hbar": lambda s: bar(s, True), "grouped_bar": grouped_bar, "stacked_bar": lambda s: grouped_bar(s, True), "line": line,
         "area": lambda s: line(s, True), "scatter": scatter, "dot": dot, "histogram": histogram, "pareto": pareto, "tornado": tornado, "scenario": scenario}

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kind", nargs="?"); ap.add_argument("spec", nargs="?"); ap.add_argument("-o", "--out"); ap.add_argument("--svg", action="store_true")
    ap.add_argument("--kinds", action="store_true"); ap.add_argument("--example")
    a = ap.parse_args()
    if a.kinds: print("\n".join(KINDS)); return
    if a.example: print(json.dumps(EX[a.example], indent=2)); return
    if not a.kind or not a.spec: ap.print_help(); return
    spec = json.load(open(a.spec)); fig = KINDS[a.kind](spec)
    out = a.out or os.path.splitext(a.spec)[0] + (".svg" if a.svg else ".png")
    fig.savefig(out, dpi=200 if out.endswith(".png") else None, facecolor=fig.get_facecolor()); print("wrote", out)

if __name__ == "__main__":
    main()
