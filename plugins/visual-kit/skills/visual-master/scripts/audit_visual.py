#!/usr/bin/env python3
"""
audit_visual.py - deterministic QA for visual specs and deck storyboards.

Usage:
  python audit_visual.py spec.json                 # audit one render_svg spec
  python audit_visual.py --storyboard deck.json    # audit a deck storyboard (see format below)

Storyboard format (what you produce in STEP 2 of the skill):
{
  "deck_title": "...",
  "slides": [
    {"n": 1, "takeaway": "The next GTM advantage is faster learning, not more automation", "visual": "thesis_slide", "mode": "assertion"},
    {"n": 2, "takeaway": "Pipeline grew 40% while conversion fell 9 pts", "visual": "dumbbell", "mode": "evidence", "source": "CRM, FY26"},
    ...
  ]
}
mode ∈ assertion | evidence | explanation | implication   (the four beats the skill alternates between)

Checks (each prints PASS / WARN / FAIL with the reason):
  T1  title states a takeaway, not a topic          T2  title length fits a slide
  D1  data visuals cite a source                     D2  element count within cognitive-load limits
  D3  highlight list is small (one story per visual) P1  storyboard alternates beats (no 4+ in a row of the same mode)
  P2  storyboard has a decision / next-step slide    P3  no visual type used 4+ times in a row
  P4  every slide has a takeaway title
Exit code 1 if any FAIL.
"""
import json, re, sys, argparse

TOPIC_WORDS = re.compile(r"^(overview|update|analysis|summary|status|review|results|metrics|kpis|pipeline|market|agenda|background|context|appendix|q[1-4]|fy\d+)\b", re.I)
TOPIC_ENDINGS = re.compile(r"\b(overview|update|analysis|summary|status|review|deep[- ]dive|recap|landscape)$", re.I)
VERBISH = re.compile(r"\b(is|are|was|were|will|won't|can|cannot|can't|should|must|needs?|drives?|drove|grew|fell|lose|lost|wins?|beats?|not|only|because|than|but|while|before|after|from|to|until|unless|if|when|→|->|:|—|-)\b|\d|%|\$", re.I)

LIMITS = {  # max primary elements before the visual stops reading at a glance
    "waterfall": ("steps", 8), "chevron": ("steps", 6), "funnel": ("stages", 7), "flywheel": ("nodes", 6), "stack": ("layers", 7),
    "columns": ("columns", 4), "two_by_two": ("items", 10), "slope": ("items", 8), "dumbbell": ("items", 8), "bullet": ("items", 6),
    "swimlane": ("steps", 8), "orbit": ("satellites", 8), "network": ("nodes", 8), "grid": ("cells", 9), "table": ("rows", 7),
    "timeline": ("milestones", 6), "gantt": ("rows", 8), "pyramid": ("levels", 6), "concentric": ("rings", 4), "staircase": ("steps", 5),
    "ladder": ("rungs", 6), "cascade": ("steps", 6), "spectrum": ("points", 6), "card": ("cards", 4), "dashboard": ("tiles", 6),
}
DATA_TYPES = {"waterfall", "slope", "dumbbell", "bullet", "funnel", "hero_stat", "two_by_two", "journey_curve", "scatter_labels", "dashboard"}

def check_title(t):
    out = []
    if not t: return [("T1", "FAIL", "no title - every visual needs a takeaway title")]
    if TOPIC_WORDS.match(t.strip()) and not VERBISH.search(t):
        out.append(("T1", "FAIL", f"title reads as a topic label, not a claim: '{t}'. Rewrite as the sentence the audience should repeat."))
    elif TOPIC_ENDINGS.search(t.strip()) or (len(t.split()) <= 3 and not VERBISH.search(t)):
        out.append(("T1", "WARN", f"title may be a topic, not a takeaway: '{t}'"))
    else:
        out.append(("T1", "PASS", "title states a claim"))
    if len(t) > 95: out.append(("T2", "WARN", f"title is {len(t)} chars; over ~90 it wraps to 3 lines on a slide"))
    else: out.append(("T2", "PASS", "title length ok"))
    return out

def audit_spec(spec, kind=None):
    res = check_title(spec.get("title", ""))
    kind = kind or spec.get("type")
    d = spec.get("data", {})
    if kind in DATA_TYPES and not (spec.get("source") or d.get("source")):
        res.append(("D1", "WARN", "data visual has no source line; executives discount unsourced numbers"))
    else:
        res.append(("D1", "PASS", "source present or not needed"))
    if kind in LIMITS:
        key, mx = LIMITS[kind]; n = len(d.get(key, []) or [])
        res.append(("D2", "PASS" if n <= mx else "WARN", f"{n} {key} (limit ~{mx} for a {kind}); split or move detail to appendix" if n > mx else f"{n} {key} within limit"))
    hl = spec.get("highlight") or []
    if len(hl) > 3: res.append(("D3", "WARN", f"{len(hl)} highlighted elements - if everything is highlighted, nothing is"))
    else: res.append(("D3", "PASS", "highlight is focused"))
    return res

def audit_storyboard(sb):
    res = []
    slides = sb.get("slides", [])
    for s in slides:
        for code, st, msg in check_title(s.get("takeaway", "")):
            if st != "PASS": res.append((f"P4/s{s.get('n','?')}", st, msg))
    modes = [s.get("mode", "?") for s in slides]
    run = 1
    for i in range(1, len(modes)):
        run = run + 1 if modes[i] == modes[i - 1] else 1
        if run == 4: res.append(("P1", "WARN", f"slides {i-2}-{i+1} are all '{modes[i]}' - alternate assertion / evidence / explanation / implication"))
    vis = [s.get("visual", "?") for s in slides]
    run = 1
    for i in range(1, len(vis)):
        run = run + 1 if vis[i] == vis[i - 1] else 1
        if run == 4: res.append(("P3", "WARN", f"'{vis[i]}' used 4 slides in a row - vary the visual form"))
    last = " ".join((s.get("takeaway", "") + " " + s.get("visual", "")).lower() for s in slides[-3:])
    if not re.search(r"decision|decide|next step|recommend|ask|approve|choose", last):
        res.append(("P2", "WARN", "no decision / next-step slide in the last three - executive decks should end with the ask"))
    if not res: res.append(("P*", "PASS", f"{len(slides)} slides: beats alternate, takeaway titles present, ends with a decision"))
    return res

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", nargs="?"); ap.add_argument("--storyboard"); ap.add_argument("--type", help="diagram type of the spec (if not in the file)")
    a = ap.parse_args()
    if a.storyboard:
        res = audit_storyboard(json.load(open(a.storyboard)))
    elif a.path:
        res = audit_spec(json.load(open(a.path)), a.type)
    else:
        ap.print_help(); return
    fails = 0
    for code, st, msg in res:
        print(f"[{st:4}] {code:8} {msg}"); fails += st == "FAIL"
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
