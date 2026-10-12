---
name: visual-storytelling
description: "Add the NARRATIVE and PROOF layer that makes a deck or document feel designed, not assembled - framing slides, comparison layouts, credibility visuals, editorial/media visuals, slide-level layouts, metaphors, and deck pacing. Use for openers and \"what changed / why now / cost of doing nothing / the strategic choice / what winning looks like / from-to / decision requested\" slides; side-by-side comparisons; proof stacks, metric cards, hero stats, quote walls, mini case studies, benchmarks; editorial visuals for newsletter and media work; slide layouts (hero statement, big idea + 3 proof, three-card, split-screen); and visual metaphors. Triggers on \"make this land / feel designed\", \"opener\", \"proof slide\", \"comparison slide\", \"one metaphor for this\", \"storyboard the deck\", or an editorial or framing need that visual-cue flagged. Renders via visual-master."
---

# Visual Storytelling

Not every point is a chart. This is the layer that gives a deck or document **pace** and makes it feel designed - framing, comparison, proof, editorial, layout, and metaphor. A deck of all charts is forgettable; a deck of all frameworks is unproven. Alternate.

## Framing moves

Contrarian opener - "one chart that changes the conversation" - "what changed" (3-5 external shifts) - "cost of doing nothing" - "the hidden constraint" - "what most teams get wrong" - "the strategic choice" - "what winning looks like" - from/to - "there are only three moves" - "decision requested" - one-page executive summary.

## Comparison formats (side-by-side)

old/new - symptom/root-cause - activity metric/business metric - what teams say/what data shows - conventional wisdom/our POV - manual/AI-enabled workflow - fragmented tools/integrated system - cost center/growth engine - feature/outcome.

## Proof & credibility

Single large sourced metric + implication - metric card (baseline -> intervention -> result) - proof stack (market / customer / product / financial) - three-panel mini case study - testimonial + the exact outcome it supports - benchmark vs peer median - a "receipts" slide (sources, experiments, quotes) - milestone timeline that shows execution - current-vs-target scorecard.

## Editorial & media (newsletter / category / thought leadership)

Editorial franchise map - content-portfolio matrix (value x effort) - audience-to-revenue flywheel - media business-model map - newsletter growth loop - content-IP ladder (post -> newsletter -> report -> workshop -> advisory) - signature-series architecture - distribution ecosystem map - creator operating system - content performance tree (reach -> engagement -> trust -> leads -> pipeline -> revenue) - thought-leadership wedge - attention-to-authority journey - quote collage - a signature visual metaphor that becomes a repeatable brand asset.

## Slide-level layouts

Hero statistic - hero statement - big idea + three proof points - annotated screenshot / chart - timeline with inflection - three-card - four-quadrant - five-step chevron - center-and-orbit - layer cake - split screen - full-bleed quote / photo - progressive reveal - one-screen decision - takeaway banner - appendix deep-dive.

## Metaphors (one per narrative)

Flywheel (momentum) - bridge (transition) - iceberg (hidden complexity) - mountain (ambition) - compass (direction) - map (positioning) - ladder (progression) - engine (repeatable system) - orbit (ecosystem) - lighthouse (differentiation) - control tower (visibility) - mosaic (pieces -> whole) - blueprint (design). Pick one and hold it across the whole narrative.

## Pacing - the 12-slide spine

Thesis/tension -> evidence -> why now -> root cause -> future state -> strategic choices -> recommendation -> operating model -> roadmap -> economics/KPIs -> risks -> decision. Alternate **assertion / evidence / explanation / implication**; never four charts or four frameworks in a row; end on a decision slide.

## Build

Render individual pieces through **visual-master**: `scripts/render_svg.py`, the patterns in `references/storytelling-patterns.md`, and `scripts/audit_visual.py --storyboard storyboard.json` for deck pacing. Related: **visual-cue** (detection), and the five family spokes for the visual that goes inside the frame.

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt (Coach K). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
