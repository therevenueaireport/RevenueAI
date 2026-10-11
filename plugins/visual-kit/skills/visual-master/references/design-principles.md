# Design principles for visual moves

Read this when deciding *how* to draw a visual you have already selected, when a draft looks busy, or when the user pushes back that a slide "doesn't land." These principles are the reason behind every default in `render_svg.py` and every check in `audit_visual.py`.

## 1. Make every visual answer a question

Before selecting a chart or diagram, complete this sentence:

> "After seeing this slide, the audience should understand that ______."

Examples of good completions:

- "Enterprise pipeline is growing, but conversion is the constraint."
- "Our category opportunity is created by a buyer problem incumbents do not solve."
- "The AI opportunity is not one tool — it is a redesigned workflow."
- "We should invest in the high-impact, low-governance-risk use cases first."

That sentence becomes the **title** of the visual (the takeaway, not the topic). If the visual does not make the sentence obvious in a few seconds, simplify it: fewer elements, one highlight, or a different form.

Bad titles (topics): "Pipeline analysis", "Market overview", "AI roadmap", "Q3 update".
Good titles (claims): "Conversion — not volume — is the Q4 pipeline constraint", "Enablement, not product, gates the launch".

Why this matters: executives read the title, glance at the picture to confirm it, and move on. If the title is a topic, they have to do the analysis themselves, and most will not.

## 2. Match visual form to the claim

The claim type decides the form. `select_visual.py` encodes this; the short version:

| Claim | Form |
|---|---|
| Change over time | line (or slope / dumbbell for two points) |
| Comparison across categories | bars (horizontal when labels are long) |
| Explaining a change in a total | waterfall |
| Prioritization or relationship | scatter / quadrant / 2×2 |
| Flow and leakage | funnel, Sankey |
| Choices and tradeoffs | matrix / decision table / tradeoff triangle |
| Sequence and ownership | chevron / swimlane |
| Reinforcing loop | flywheel |
| Timing and dependency | roadmap / gantt / timeline |
| Hierarchy or drivers | tree / pyramid / stack |
| Hidden cause | iceberg |
| Transition | bridge / before-after |
| A strategic point, not an analytical one | a single sentence |

Common mismatches to avoid: a pie for comparison (use bars); a line for unordered categories; a funnel for anything that is not stage conversion; a flywheel for a linear process (use chevron); a 2×2 with 15 items (use a table or ranked bars); a Gantt for a roadmap whose dates are fake (use now/next/later).

## 3. Reduce cognitive load

- **One primary message per slide.** A second idea is a second slide.
- **One focal point.** Highlight the story element in the accent color; mute everything else in gray. The `highlight` field in every spec exists for this.
- **Label directly.** Put values and names on the marks, not in a distant legend.
- **Color has meaning, not decoration.** Default roles: accent = current / the story; accent2 = recommended / future / positive; risk = risk / negative / attention; gray = context. Keep the same roles on every slide of a deck.
- **No 3D, no decorative gauges, no crowded legends, no rainbow palettes.** These add ink without adding meaning.
- **Detail budget.** Show only enough to support the decision in the room; the rest goes to the appendix. Rough limits (enforced as warnings by `audit_visual.py`): ≤ 6 chevron steps, ≤ 7 funnel stages, ≤ 6 flywheel nodes, ≤ 7 stack layers, ≤ 8 waterfall steps, ≤ 4 columns, ≤ 10 points on a 2×2, ≤ 3 bullets per card.
- **Typography does hierarchy.** Title 32–40pt, labels 17–22pt, sublabels 15–16pt, source 14pt. Bold is for the one thing that matters.

## 4. Neutral palette and brand handoff

This skill is brand-agnostic. The default palette is deliberately neutral (blue accent, green positive, orange risk, grays) so the *structure* reads first. When the user supplies brand colors, map them onto the same roles — do not add roles (illustrative dark palette shown; substitute your brand's values):

```json
"palette": {"bg": "#0F172A", "ink": "#FFFFFF", "muted": "#CBD5E1", "line": "#334155", "context": "#1E293B",
            "accent": "#38BDF8", "accent2": "#34D399", "risk": "#FBBF24", "font": "Inter, Arial, sans-serif"}
```

Dark backgrounds: raise `ink` to white, keep `context` a few steps lighter than `bg`, and make sure `accent` passes contrast on `bg`. Never let the brand palette re-introduce a rainbow: pick one accent, one positive, one risk, and grays.

## 5. Create pacing across the deck

Alternate four beats — **assertion, evidence, explanation, implication**. A run of four charts feels like a report; a run of four frameworks feels like a consulting template. The 12-slide spine and the storyboard audit live in `storytelling-patterns.md` §7.

Slide density guidance that pairs well with these visuals: ≤ 5 bullets (3 preferred), ≤ 12 words per bullet, ≤ 6 data points in a chart, ≤ 5 steps in a process, one idea per slide.

## 6. Accessibility and reproduction

- Contrast: text on fills must pass 4.5:1 (the renderer auto-picks white or ink text on fills, but check custom palettes).
- Do not encode meaning in color alone — pair color with position, label, or icon (✓ / ✕, "risk", "recommended").
- Export at 2× (`--scale 2`) for slides and docs; 1080×1080 or 1200×627 for social; keep SVG when the destination is HTML.
- Fonts: the SVG uses a system-safe stack. If a brand font is required in PPTX, rebuild the visual with native shapes (see `build-recipes.md`) so the font is editable.
