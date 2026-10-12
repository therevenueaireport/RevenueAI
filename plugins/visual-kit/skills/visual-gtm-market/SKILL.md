---
name: visual-gtm-market
description: "Build a MARKET, CUSTOMER, or GTM visual for B2B positioning, category, product marketing, demand, and revenue. Use for TAM/SAM/SOM, market and category maps, perceptual positioning, competitive grids and battlecards, \"why now\" stacks, SWOT/five competitive forces/PESTLE, segmentation, ICP cards, buying-committee and stakeholder maps, buyer journeys, message house and messaging pyramid, value-prop fit map, proof and evidence ladders, objection maps, funnels and pipeline coverage/hygiene, content engines and flywheels, lifecycle and land-and-expand, and ROI trees. Triggers on \"positioning map\", \"message house\", \"ICP\", \"buying committee\", \"pipeline coverage\", \"category map\", \"content engine\", or a GTM passage that visual-cue flagged. Renders via visual-master, which ships 5 signature GTM/AI visuals."
---

# Visual GTM & Market

The highest-leverage family for B2B positioning, category creation, product marketing, demand generation, and revenue strategy. This is where the signature visuals live.

## Claim -> visual

| The claim is about... | Use |
|---|---|
| Market opportunity | TAM/SAM/SOM; market or category map |
| A differentiated position | perceptual positioning map |
| How we win vs alternatives | competitive grid / battlecard; feature matrix; competitive-alternatives map |
| Urgency | "why now" stack; market-forces diagram; PESTLE / five competitive forces / SWOT |
| Target customers | segmentation map; ICP card; account-tiering pyramid; persona card |
| Who decides | buying-committee map; stakeholder-influence matrix |
| The buyer's path | buyer journey; buyer-question ladder ("why change -> why now -> why us") |
| Positioning & messaging | message house; messaging pyramid; narrative arc; value-prop fit map |
| Evidence behind claims | proof architecture; evidence ladder; objection map |
| Attention -> revenue | demand engine; content engine / atomization; distribution waterfall; audience flywheel |
| Pipeline | funnel with leakage; pipeline coverage; pipeline-hygiene map; win/loss map |
| Customer growth | lifecycle map; land-and-expand; health score; expansion whitespace; ROI tree; value-realization timeline |

## Signature visuals (reuse as IP)

**visual-master** ships five brand-neutral templates in `assets/signature/`: the **AI-native revenue operating model**, **signal-to-action architecture**, **audience -> authority -> pipeline flywheel**, **category-creation narrative map**, and **AI maturity ladder**. Reuse the same one across decks, posts, and workshops - repetition is what turns a diagram into intellectual property.

## Discipline

- A positioning map's two axes must be the two dimensions buyers actually trade off - not two flattering ones.
- Logos and quotes are proof only when relevant; use sparingly.
- Title = the takeaway ("Our category exists because incumbents can't solve the buyer's real problem"), not "Market landscape".

## Build

Render through **visual-master**: `assets/signature/` for the five, `scripts/render_svg.py` (gtm family) otherwise; shortlist with `scripts/select_visual.py "<claim>" --family gtm`. Related: **visual-ai-systems**, **visual-strategy-diagrams**, **visual-storytelling**, **visual-cue**.

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt. License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
