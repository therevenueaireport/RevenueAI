---
name: visual-strategy-diagrams
description: "Build a NARRATIVE or ARGUMENT diagram - the kind that carries a point, not data. Use for pyramids, flywheels and virtuous cycles, Venn and overlap, 2x2 and nine-box matrices, iceberg, bridge and chasm, before/after, then-now-next, three-horizon, strategy cascade, choice and decision trees, tradeoff and magic triangle, value chain, causal loop, spectrum and continuum, and the one-sentence thesis. Triggers on \"show the strategy\", \"make a 2x2 / flywheel / pyramid / bridge\", \"our point of view vs conventional wisdom\", \"the strategic choice\", \"from/to\", or a strategy passage that visual-cue flagged. Renders via visual-master (scripts/render_svg.py). Pair with visual-cue and visual-storytelling."
---

# Visual Strategy Diagrams

These carry an **argument**, not data. Reach for one when the point is a relationship between ideas - a hierarchy, a loop, a choice, a transition - that a sentence flattens.

## Claim -> diagram

| The claim is about... | Use |
|---|---|
| Layers / hierarchy of an idea | pyramid (inverted for inputs -> a decision) |
| A reinforcing, compounding loop | flywheel / virtuous cycle |
| Overlap of 2-3 concepts | Venn; concentric or onion for nested levels |
| Visible outcome vs hidden cause | iceberg |
| Current state -> future state | bridge (chasm when the gap itself is the point) |
| A transformation | before/after split; then-now-next |
| Present / emerging / future bets | three-horizon |
| Linked strategic decisions | strategy cascade (where to play / how to win) |
| A decision with branches | choice tree; decision matrix when you're recommending |
| Tension among three goals | tradeoff / magic triangle |
| Classifying items on two axes | 2x2; nine-box for more granularity |
| How value is created | value chain |
| Feedback loops / side effects | causal loop diagram |
| A continuum with stages | spectrum / continuum with thresholds |
| The whole story in one line | one-sentence thesis slide |

## Discipline

- **One consistent metaphor per narrative** - don't mix a bridge and a mountain in the same argument.
- Prefer the simplest form that holds the claim: a flywheel for a linear thing is really a chevron (use **visual-process-maps**); a 2x2 with 15 dots is a table.
- Limits: <=6 flywheel nodes, <=10 dots on a 2x2, <=30 words of labels at slide size.
- Title states the takeaway; the diagram proves it in a few seconds.

## Build

Render through **visual-master** `scripts/render_svg.py` (strategy family). Shortlist with `scripts/select_visual.py "<claim>" --family strategy`, and open visual-master's `references/library-strategy-diagrams.md` for neighbors when the top pick feels off. Related: **visual-cue** (detection), **visual-storytelling** (framing), **visual-gtm-market** (positioning-specific frames).

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt.*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
