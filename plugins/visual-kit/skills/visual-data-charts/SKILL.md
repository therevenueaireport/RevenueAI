---
name: visual-data-charts
description: "Choose and build the right DATA chart for a claim about magnitude, trend, comparison, distribution, composition, flow, or relationship. Use whenever you need to show numbers - \"chart these\", \"compare X across segments\", \"trend over time\", \"where does the funnel leak\", \"distribution of deal sizes\", \"what's driving the total\", \"plot spend vs pipeline\", or a passage of quantitative prose that visual-cue flagged. Covers bar/line/area families, waterfall/bridge, scatter/bubble/quadrant, funnel/Sankey, cohort/retention, distribution (histogram/box/violin), Pareto, treemap, heatmap, bullet/progress, and uncertainty (fan/scenario/tornado). Renders through visual-master (scripts/chart.py). Pair with visual-cue for detection and visual-storytelling for framing."
---

# Visual Data Charts

Numbers on a slide or page are a claim waiting for a shape. Pick the shape from the **claim**, not from the data you happen to have.

## Claim -> chart

| The claim is about... | Use | Avoid |
|---|---|---|
| Comparing discrete categories | bar (horizontal when labels are long or many) | pie |
| Comparing across 2-4 series | grouped bar | |
| Composition + total | stacked bar; 100% stacked for **mix over time** | |
| Change over time | line; multi-line to compare trends | bar |
| Total volume over time | area / stacked area | |
| Before -> after across many items | slope or dumbbell | |
| Explaining a change in a total | waterfall / bridge (variance waterfall = plan vs actual) | |
| Performance vs a target | bullet chart; progress bar for simple completion | decorative gauge |
| Relationship / outliers | scatter; bubble to add a 3rd variable | |
| Prioritization on two dimensions | quadrant / 2x2 | |
| Intensity across two dimensions | heatmap (calendar / matrix / cohort variants) | |
| Distribution of a metric | histogram; box or violin to compare distributions | |
| The few drivers behind most impact | Pareto | |
| Hierarchical composition | treemap / sunburst | |
| Stage conversion & leakage | funnel / conversion staircase | |
| Flow between stages | Sankey / alluvial | |
| Retention by cohort | cohort retention chart / heatmap; survival curve | |
| Sensitivity / uncertainty | tornado; fan chart / scenario bands | |
| A KPI decomposed into drivers | goal tree with numbers | |

## Discipline

- **Title = the takeaway sentence** ("Conversion, not volume, is the Q4 constraint"), never "Pipeline analysis".
- **Highlight one element** in an accent color; mute everything else to gray. Label directly; drop the legend when labels fit.
- Respect limits: <=7 funnel stages, <=6 data points shown on a slide, no 3D, no rainbow palettes, no gauges-as-decoration.
- **Never invent numbers.** No point yet? State the data in words, or render two candidates and ask which claim to make.

## Build

Render through **visual-master**: `scripts/chart.py` covers the 12 core kinds; `references/build-recipes.md` gives one-line paths for Sankey, treemap, cohort heatmap, box/violin, and fan chart. If the pick isn't obvious, run `scripts/select_visual.py "<claim>" --family data`. Then place per surface: pptx (PNG, or native chart when numbers will change), inline SVG in HTML, figure+caption in docs. **Look at the rendered PNG before delivering.** Related: **visual-cue** (detection), **visual-storytelling** (framing the chart on the page).

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt.*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
