#!/usr/bin/env python3
"""
select_visual.py - deterministic visual recommender for the visual-master skill.

Usage:
  python select_visual.py "Enterprise pipeline grew 40% but conversion fell"   # free-text claim
  python select_visual.py --claim-type bridge                                    # by claim type
  python select_visual.py --family ai --claim-type loop                          # narrow by family
  python select_visual.py --show waterfall                                       # details for one visual
  python select_visual.py --list-claims | --list-families | --list [family]

Output: ranked candidates (JSON with --json) with best_for, example, and the render route.
No network calls. Reads catalog.json beside this script.
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CATALOG = json.load(open(os.path.join(HERE, "catalog.json")))["visuals"]

# Claim-type inference: phrases a user/author would write -> claim type. Order matters only for ties.
CLAIM_CUES = {
    "trend":          ["over time","trend","growth","grew","declin","month","quarter","week","yoy","trajectory","since","history","curve"],
    "comparison":     ["compare","versus","vs","than","higher","lower","by segment","by channel","by region","by product","across","which","but only","only ","% of","percent of","share of teams","found that"],
    "ranking":        ["top ","rank","most","least","biggest","largest","leaderboard","80/20","pareto","drivers of"],
    "composition":    ["mix","share of","breakdown","made up","composition","portion","split of","% of"],
    "bridge":         ["bridge","from x to y","walk","what drove","variance","missed","beat plan","reconcile","started at","ended at","explain the change","went from"],
    "before_after":   ["before","after","pre-","post-","then and now","was ","is now","lift","improv","transformation","old ","new "],
    "target":         ["target","goal","quota","attainment","coverage","plan","% of","on track","readiness"],
    "distribution":   ["distribution","spread","median","outlier","range of","deal size","cycle length","histogram","how long"],
    "relationship":   ["correlat","relationship","drives","impact of","as x increases","outlier","scatter","depends on"],
    "flow":           ["funnel","conversion","leak","drop-off","stage","flow","source to","where do","routing","journey through","pipeline stages"],
    "intensity":      ["heatmap","grid of","matrix of","where is demand","by segment and","week by","intensity","whitespace"],
    "uncertainty":    ["scenario","forecast","range","confidence","upside","downside","base case","probab"],
    "sensitivity":    ["sensitivity","assumption","what matters most","swing","levers"],
    "hierarchy":      ["decompos","tree","drivers","roll up","made of","levels","tiers","layers of","breaks down into","hierarchy","kpi tree","roi"],
    "loop":           ["flywheel","loop","reinforc","compound","cycle","virtuous","feedback","momentum","self-reinforcing","learning"],
    "overlap":        ["overlap","intersection","sweet spot","meet","venn","where x meets"],
    "hidden_cause":   ["root cause","hidden","beneath","below the surface","symptom","iceberg","underlying","really because"],
    "maturity":       ["maturity","stages","level","ladder","progress","from ad hoc","ai-native","crawl walk run","evolve"],
    "transition":     ["from","to ","legacy","future state","current state","gap","chasm","how we get there","migrat","shift to"],
    "evolution":      ["then now next","evolution","how we got here","history of","era"],
    "portfolio":      ["portfolio","bets","horizon","investments","adjacenc"],
    "decision":       ["decide","decision","recommend","option","choose","build buy","vendor","select","which one","scored","criteria","should we"],
    "tradeoff":       ["tradeoff","trade-off","tension","pick two","speed quality cost","balance"],
    "classification": ["categor","classify","four box","quadrant","types of","kinds of","sort"],
    "prioritization": ["priorit","impact effort","2x2","two by two","first","focus","which to do","use cases","value feasibility"],
    "sequence":       ["step","process","then","workflow","sequence","phase","pipeline","how it works","->","→","stages of"],
    "ownership":      ["who owns","owner","handoff","raci","responsib","accountab","swimlane","team","human in the loop","approve","cross-functional"],
    "timing":         ["roadmap","timeline","when","q1","q2","q3","q4","month","milestone","gantt","now next later","30 60 90","cadence","phased","waves"],
    "architecture":   ["architecture","stack","layers","system of","components","platform","how it fits","tools and data","integration","operating model"],
    "system":         ["ecosystem","stakeholder","system map","interdepend","connected","network","context"],
    "market":         ["market","tam","sam","som","landscape","competitor","industry","forces","category","vendors","opportunity size"],
    "positioning":    ["position","differentiat","perceptual","wedge","beachhead","category","frame","narrative"],
    "competitive":    ["competitor","battlecard","objection","alternative","against","win against","do nothing","status quo"],
    "customer":       ["customer","buyer","persona","icp","journey","jobs to be done","pains","gains","committee","segment"],
    "message":        ["message","messaging","positioning statement","pillars","promise","proof points","narrative"],
    "argument":       ["thesis","argument","story","narrative","problem solution","tension insight","why it works","pitch"],
    "proof":          ["proof","evidence","case study","testimonial","quote","credib","results","receipts"],
    "contrast":       ["myth","reality","old rules","new rules","not x but y","versus","distinction","misconception"],
    "continuum":      ["spectrum","continuum","range from","archetype","degree of","from tactical to strategic","augment"],
    "urgency":        ["why now","urgency","forces","what changed","converging","pressure"],
    "governance":     ["governance","guardrail","policy","control","security","trust boundary","compliance","decision rights","risk"],
    "risk":           ["risk","likelihood","impact","threat","exposure","mitigation"],
    "inventory":      ["capabilit","channels","motions","list of","catalog","functions","roles","portfolio of agents"],
    "status":         ["status","kanban","backlog","in progress","done","launched"],
    "visibility":     ["dashboard","control tower","visibility","kpis","scorecard","health"],
    "assertion":      ["one sentence","thesis","headline","big idea","point of view","the takeaway is"],
}

def infer_claim_types(text):
    t = " " + text.lower() + " "
    scores = {}
    for ct, cues in CLAIM_CUES.items():
        s = 0
        for cue in cues:
            if cue in t:
                s += 2 if len(cue) > 5 else 1
        if s:
            scores[ct] = s
    return sorted(scores.items(), key=lambda kv: -kv[1])

def score_visual(v, text, claim_types):
    t = " " + text.lower() + " "
    s = 0.0
    ct_rank = {ct: i for i, (ct, _) in enumerate(claim_types)}
    if v["claim"] in ct_rank:
        s += max(6 - ct_rank[v["claim"]] * 1.5, 1.5)
    for tag in v["tags"]:
        if tag.lower() in t:
            s += 3 if len(tag) > 8 else 2
    for w in re.findall(r"[a-z][a-z\-]{3,}", v["name"].lower()):
        if w in t:
            s += 1
    for w in re.findall(r"[a-z][a-z\-]{4,}", v["best_for"].lower()):
        if w in t:
            s += 0.5
    return s

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("claim", nargs="?", help="Free-text claim, slide title, or 'after this slide the audience should understand that ...'")
    ap.add_argument("--claim-type", help="Force a claim type (see --list-claims)")
    ap.add_argument("--family", help="data | strategy | process | gtm | ai | editorial | signature")
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--show", help="Print one visual by id")
    ap.add_argument("--list", nargs="?", const="all", help="List visuals (optionally by family)")
    ap.add_argument("--list-claims", action="store_true")
    ap.add_argument("--list-families", action="store_true")
    a = ap.parse_args()

    if a.list_claims:
        print("\n".join(sorted(CLAIM_CUES))); return
    if a.list_families:
        print("\n".join(sorted({v["family"] for v in CATALOG}))); return
    if a.list:
        for v in CATALOG:
            if a.list == "all" or v["family"] == a.list:
                print(f'{v["id"]:28} {v["family"]:10} {v["claim"]:14} {v["name"]}')
        return
    if a.show:
        v = next((x for x in CATALOG if x["id"] == a.show), None)
        if not v: sys.exit(f"unknown id {a.show}. Try --list")
        print(json.dumps(v, indent=2)); return

    text = a.claim or ""
    if not text and not a.claim_type:
        ap.print_help(); return

    claim_types = infer_claim_types(text) if text else []
    if a.claim_type:
        claim_types = [(a.claim_type, 99)] + [c for c in claim_types if c[0] != a.claim_type]

    pool = [v for v in CATALOG if not a.family or v["family"] == a.family]
    ranked = sorted(((score_visual(v, text, claim_types), v) for v in pool), key=lambda sv: -sv[0])
    ranked = [(s, v) for s, v in ranked if s > 0][: a.top]

    if a.json:
        print(json.dumps({
            "claim": text,
            "inferred_claim_types": claim_types[:4],
            "candidates": [{"score": round(s, 1), **v} for s, v in ranked],
        }, indent=2)); return

    print(f"CLAIM: {text or '(claim type ' + a.claim_type + ')'}")
    print("Inferred claim types:", ", ".join(f"{c} ({n})" for c, n in claim_types[:4]) or "none - state the claim more concretely")
    print()
    if not ranked:
        print("No match. Re-state the claim as 'the audience should understand that ...' or pass --claim-type."); return
    for i, (s, v) in enumerate(ranked, 1):
        print(f"{i}. {v['name']}  [{v['id']} | {v['family']} | claim={v['claim']} | render={v['render']}]  score {s:.1f}")
        print(f"   best for: {v['best_for']}")
        print(f"   example:  {v['example']}")
    print("\nRender routes: chart = matplotlib/native chart (see references/build-recipes.md);"
          " svg:<type> = python render_svg.py <type> spec.json; shapes = pptx/HTML shapes; text = typographic slide.")

if __name__ == "__main__":
    main()
