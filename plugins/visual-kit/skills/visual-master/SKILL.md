---
name: visual-master
description: >
  Picks the right visual for every claim and builds it - charts, strategy diagrams, process/operating-model
  visuals, GTM and AI frameworks, metaphors, and deck storyboards - from a 250-visual library with bundled
  SVG/PNG/matplotlib renderers, a selector script, and a takeaway-title audit. Brand-neutral; applies any palette.
  ALWAYS use when the user is making or improving a slide deck, presentation, keynote, webinar, board/exec deck,
  one-pager, report figure, dashboard, social or newsletter graphic, or says "what visual/chart/diagram should I
  use", "make this visual", "turn this into a flywheel/funnel/2x2/roadmap/waterfall/framework", "storyboard this
  deck", "this slide doesn't land", "make it look designed", or wants a strategy, workflow, AI system, or operating
  model explained visually - even if they only say "add a chart" or "put this on a slide". Use alongside your deck,
  document, and brand tooling: this skill decides WHAT to draw and renders it; those handle file mechanics and styling.
---

# Visual Master

A strong deck is a sequence of **visual moves**, not a sequence of slides. This skill turns a claim into the one visual that makes it obvious, and turns a deck outline into a storyboard that alternates assertion, evidence, explanation, and implication. It is brand-agnostic: the defaults are neutral, and the user's palette drops in at build time.

Everything routes through four questions: *What should the audience understand after this slide? Which form makes that obvious? What does the spec look like? Where does it land?*

## What's in the box

| Path | What it is | When to open |
|---|---|---|
| `scripts/select_visual.py` | Deterministic recommender over the 250-visual catalog | STEP 2, every time |
| `scripts/render_svg.py` | 43 diagram types → SVG/PNG (strategy, process, GTM, AI, metaphors, 5 signature visuals) | STEP 4 for anything that is not a data chart |
| `scripts/chart.py` | 12 data-chart kinds with the design rules baked in | STEP 4 for data charts |
| `scripts/audit_visual.py` | Takeaway-title, element-count, source, and deck-pacing checks | STEP 3 and STEP 5 |
| `scripts/catalog.json` | The library as data (id, best_for, example, claim, render route) | rarely directly; the selector reads it |
| `references/library-*.md` | The six visual families as tables (data, strategy, process, GTM, AI, editorial) | when the selector's top picks feel wrong or you want the neighbors |
| `references/storytelling-patterns.md` | Framing slides, comparison formats, proof visuals, slide-level patterns, metaphors, the 12-slide spine, starter kit | storyboarding a deck; a slide feels flat |
| `references/design-principles.md` | The "answer a question" test, form-to-claim mapping, cognitive load, palette roles, pacing | a draft looks busy; user pushback |
| `references/build-recipes.md` | How to land visuals in pptx, HTML/SVG, docx/pdf, social PNG; native-shape rebuilds; uncovered chart types | STEP 4 |
| `assets/signature/` | 5 signature visuals as neutral templates (SVG + PNG + spec) | AI-native GTM / media strategy decks |
| `assets/examples/` | A ready spec for every diagram type and chart kind | copy, edit, render |

## Workflow

### STEP 0 — Classify the request

Three shapes of request arrive; handle the one you have:

- **Single visual** ("make a funnel for this", "chart these numbers", "a graphic for a social post") → STEPS 1–5 once.
- **Deck / document with many visuals** ("build the board deck", "add visuals to this report") → STEP 1 for each slide, then a storyboard (STEP 2b), then build.
- **Advice only** ("what visual should I use for…") → STEPS 1–3 and stop at the spec; offer to build.

If the surface (pptx, HTML, docx, PNG) is not stated, infer it from context (a deck request → pptx; "post" → PNG; "page/dashboard" → HTML) and say what you assumed. If the user names brand colors or brand guidelines exist in context, collect the palette now (see `build-recipes.md` §6); otherwise use the neutral default and say so once.

### STEP 1 (REQUIRED) — State the claim before choosing a form

For every visual, complete: **"After seeing this, the audience should understand that ______."** Write it as a full sentence with a verb — it becomes the title. If you cannot complete the sentence, you do not yet have a visual to make; ask the user for the point, or derive it from the data and confirm.

The difference this makes: "Pipeline analysis" gives the audience homework; "Conversion — not volume — is the Q4 pipeline constraint" gives them the conclusion and lets the chart prove it.

### STEP 2 — Select the visual

Run the selector with the claim sentence (it infers the claim type and ranks the library):

```bash
python scripts/select_visual.py "Enterprise pipeline is growing but conversion is the constraint" --top 5
python scripts/select_visual.py "…" --family ai        # narrow to a family: data | strategy | process | gtm | ai | editorial | signature
python scripts/select_visual.py --show waterfall       # full record for one visual
```

Read the top candidates and pick using the form-to-claim rules (short version): change over time → line; category comparison → bars; explaining a change in a total → waterfall; prioritization/relationship → scatter or 2×2; flow and leakage → funnel/Sankey; choices and tradeoffs → matrix; sequence and ownership → chevron/swimlane; reinforcing loop → flywheel; timing → roadmap; hierarchy/drivers → tree/stack; hidden cause → iceberg; transition → bridge/before-after; a strategic (not analytical) point → a single sentence. When the selector's picks feel off, open the matching `references/library-*.md` and choose a neighbor — the selector is a shortlist, not a verdict.

Prefer the simplest form that carries the claim. A 2×2 with 15 dots is a table; a flywheel for a linear process is a chevron; a Gantt with invented dates is a now/next/later.

**STEP 2b — Storyboard (decks only).** Write a storyboard before building anything, as JSON so it can be audited:

```json
{"deck_title": "...", "slides": [
  {"n": 1, "takeaway": "Faster learning, not more automation, is the next GTM edge", "visual": "thesis_slide", "mode": "assertion"},
  {"n": 2, "takeaway": "Pipeline grew 40% while conversion fell 9 pts", "visual": "dumbbell", "mode": "evidence", "source": "CRM FY26"},
  {"n": 3, "takeaway": "Four shifts made the 2022 playbook expire", "visual": "stack", "mode": "explanation"}
]}
```
```bash
python scripts/audit_visual.py --storyboard storyboard.json
```
Use the 12-slide spine and the beat rule in `references/storytelling-patterns.md` §7: alternate **assertion → evidence → explanation → implication**, end with a decision slide, never four charts or four frameworks in a row. Share the storyboard with the user before rendering a long deck — it is far cheaper to move slides on paper.

### STEP 3 — Write the spec and audit it

Start from the example for the chosen type and edit the data:

```bash
python scripts/render_svg.py --example two_by_two > specs/s07.json   # diagrams
python scripts/chart.py --example line > specs/s02.json               # data charts
python scripts/audit_visual.py specs/s07.json --type two_by_two
```

Spec rules that matter (full detail in `build-recipes.md` §2):
- `title` = the STEP 1 sentence. `source` whenever numbers appear.
- `highlight` = the index(es) of the story element; everything else renders in gray. This is how an annotated chart is made — use it on almost every data visual.
- Respect the element limits the audit warns about (≤ 6 chevron steps, ≤ 7 funnel stages, ≤ 6 flywheel nodes, ≤ 4 columns, ≤ 10 points on a 2×2). Overflow goes to a second visual or the appendix.
- Size for the surface: 1600×900 slides · 1600×1200 docs · 1080×1080 / 1200×627 social.
- `palette` = the user's brand roles if given, else omit.
- Spec options cover most add-ons: `loop_back` and `gate` on swimlane/chevron, `marker` on staircase/ladder, `note` on funnel, `recommendation` on table, `gap_label` on compare_bars. Reach for these before hand-drawing extra SVG; if something is truly missing, extend the spec/renderer rather than building a one-off.
- Label budget: a diagram that needs more than ~30 words of labels at slide size is two visuals. Nothing below ~14px at 1600 wide.

Fix every FAIL before rendering; a FAIL is almost always a topic-label title.

### STEP 4 — Build for the surface

```bash
python scripts/render_svg.py two_by_two specs/s07.json -o out/s07.svg --png   # SVG + 2× PNG
python scripts/chart.py line specs/s02.json -o out/s02.png                    # PNG (add --svg for SVG)
```

Then follow `references/build-recipes.md` §3 for the destination: pptx (insert PNG, or rebuild natively when the owner must edit text; native charts when numbers will change), HTML/SVG artifact (inline the SVG), docx/pdf (figure + caption), social PNG (fewer elements, bigger labels). Chart types the scripts do not cover (Sankey, treemap, cohort heatmap, box plot, fan chart…) have one-line paths in §5.

**Look at what you rendered.** Open the PNG (Read tool) before delivering. Check: the highlighted element is the one the title talks about; nothing overflows its box; labels are legible at the final size; the title reads as a claim.

### STEP 5 — QA and deliver

Run the storyboard audit again for decks, then the checklist:

- [ ] Every visual's title states a takeaway; the visual proves it in a few seconds
- [ ] One focal point per visual; context muted; color roles consistent across the deck (accent = story/current, accent2 = recommended/positive, risk = risk/negative, gray = context)
- [ ] Direct labels; no 3D, gauges-for-decoration, rainbow palettes, or legends where labels fit
- [ ] Beats alternate; the deck ends with a decision / next-step slide; detail lives in the appendix
- [ ] Numbers carry a source; brand palette applied if one was given
- [ ] Rendered files viewed, not just generated

**Deliverable format.** For a single visual: the rendered file(s) plus a two-line note — the claim it makes and why this form (one sentence each). For a deck: the storyboard table (slide · takeaway · visual · beat) in the reply, the rendered visuals, and the assembled file from your deck or document tool. Do not narrate the library; the user wants the visual, not the catalog.

## Worked example

**Request:** "Board slide: we grew pipeline 40% but bookings are flat — make it land."

**STEP 1:** "Pipeline volume is up 40%, but proposal-stage conversion fell from 31% to 19%, so bookings did not move."

**STEP 2:** `select_visual.py "pipeline grew 40% but conversion at proposal fell and bookings are flat"` → funnel / conversion staircase / dumbbell. Two claims are hiding here (volume up; conversion down). Funnel with `highlight` on the proposal stage shows both in one form; the dumbbell would need a second slide for volume. Choose **funnel** (`svg:funnel`).

**STEP 3:** spec — title as above; stages Visitors → Leads → Opportunities → Proposals → Customers with this year's counts; `show_conversion: true`; `highlight: [3]`; `note`: "Proposal-stage conversion: 31% → 19% YoY"; `source`: "CRM, FY26 vs FY25". Audit: PASS.

**STEP 4:** `render_svg.py funnel s.json --png`; insert PNG on a title-only pptx slide with the title in the placeholder (spec title set to ""). View the PNG — the orange "leak" label sits on the proposal row, everything else is gray.

**STEP 5:** Two-line note back: *Claim: growth is real but it dies at proposal. Form: a funnel with one highlighted stage shows volume and leakage together, so the board sees the constraint without reading a table.*

## Signature visuals

Five reusable, brand-neutral templates for AI-native GTM and media strategy work live in `assets/signature/` (spec + SVG + PNG each): **AI-native revenue operating model**, **signal-to-action architecture**, **audience → authority → pipeline flywheel**, **category-creation narrative map**, **AI maturity ladder**. Edit the spec's labels, apply the palette, re-render. Reuse the same one across decks, posts, and workshops — repetition is what turns a diagram into intellectual property.

## Edge cases

- **No data, only a narrative** → strategy/process families and the framing slides in `storytelling-patterns.md` §1; never fake numbers.
- **Data but no point** → run `select_visual.py` on the raw description, render two candidates quickly, and ask the user which claim they want to make; then finish properly.
- **User asks for a pie chart** → build bars (or a 100% stacked bar for mix) and say why in one line; if they insist, make a clean two-slice pie at most.
- **Too much content for one slide** → split by claim, not by data; each slide keeps one takeaway.
- **Existing deck to improve** → read it, write a storyboard of what is there (takeaway or "topic only" per slide), audit it, and fix the FAIL/WARN slides first.
- **Dark brand background** → set `bg`, raise `ink` to white, keep `context` slightly lighter than `bg`, check accent contrast.

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt (Coach K). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
