# Visual storytelling devices

These are the moves that make a deck feel designed rather than assembled. Use them to create pace between the data visuals and the frameworks. Read this file when storyboarding a deck (STEP 2) or when a single slide feels flat and you need a stronger frame.

Contents: 1. Narrative framing slides · 2. Comparison formats · 3. Proof and credibility visuals · 4. Editorial and media visuals · 5. Slide-level visual patterns · 6. Visual metaphors · 7. Deck rhythm

---

## 1. Narrative framing slides

Each of these is a slide *type* with a job. The takeaway title does most of the work; the visual is usually typographic or a single simple diagram.

| Framing slide | Job | Example title | Typical build |
|---|---|---|---|
| Contrarian opening | Break the audience's default frame in the first 10 seconds | "The problem is not that marketing has too little content. It has too little conviction." | `thesis_slide` / `hero_stat` |
| One chart that changes the conversation | Make the single most surprising data point undeniable | "Reply rates fell 60% while send volume tripled" | annotated chart, one accent |
| What has changed? | 3–5 external shifts that make the old playbook obsolete | "Four shifts made the 2022 playbook expire" | `stack` (why-now) or `columns` |
| The cost of doing nothing | Quantify inaction so the decision has a baseline | "Every quarter we wait costs ~$1.4M in leaked pipeline" | `hero_stat` + `waterfall` |
| The hidden constraint | Reveal the real bottleneck under the visible symptom | "The constraint is not volume. It is conversion at proposal." | `iceberg` or `funnel` with highlight |
| What most teams get wrong | Name the common error the audience is probably making | "Most teams automate the wrong half of the workflow" | `before_after` or `two_by_two` |
| The strategic choice | Frame the decision as a small number of real options | "There are only three moves" | `columns` (3 cards) or `choice_tree` |
| What winning looks like | Paint the future state concretely | "In 12 months, plays run themselves and humans coach" | signature operating-model visual |
| From / to | Compress the transformation into one look | "From activity metrics to learning velocity" | `before_after` |
| There are only three moves | Reduce complexity to an actionable set | "Unify signals. Codify plays. Run the loop." | `chevron` or `bridge` |
| Decision requested | Make the ask explicit with criteria and implication | "Decision: fund the 90-day pilot ($240K) or defer to FY27" | `table` (decision matrix) |
| One-page executive summary | The whole argument on one screen | Thesis + 3 proof points + ask | big-idea-plus-three layout |

## 2. Comparison formats

Side-by-side is the fastest way to make a distinction land. Always put the *old / wrong / symptom* side on the left in muted color and the *new / right / cause* side on the right in the accent color. Render with `before_after`.

- Old vs. new
- Symptom vs. root cause
- Activity metric vs. business metric
- What teams say vs. what data shows
- Conventional wisdom vs. our point of view
- Manual workflow vs. AI-enabled workflow
- Fragmented tools vs. integrated system
- Cost center vs. growth engine
- Feature vs. business outcome
- Individual optimization vs. system optimization

Rule: 3–5 rows per side, parallel grammar across the pair ("Volume KPIs" ↔ "Business KPIs"), never more than ~8 words per row.

## 3. Proof and credibility visuals

Proof slides earn the right to make the next claim. Rotate formats so the deck does not become a wall of logos or a wall of numbers.

| Proof visual | Use when | Build |
|---|---|---|
| Single large sourced metric with implication | One number carries the argument | `hero_stat` (value, label, implication, source) |
| Customer-logo strip | Only when the logos are relevant to *this* audience; never as filler | image strip, grayscale, ≤ 8 logos |
| Metric card: baseline → intervention → result | Show causality, not just outcome | `chevron` (3 steps) or `dumbbell` |
| Proof stack | Layer market, customer, product, and financial evidence | `stack` (4 layers) |
| Mini case study in three panels | Narrative proof: problem, intervention, result | `columns` (3) or `case_study_journey` |
| Testimonial + the precise outcome it supports | Pair a quote with the number it backs | `card` with quote mode |
| Benchmark line vs. peer median / best-in-class | Show where we stand | `bullet` |
| "Receipts" slide | Sources, experiments, quotes, examples in one place | `grid` or `table` |
| Execution-credibility timeline | Milestones already hit | `timeline` |
| Scorecard: current vs. target state | Show the gap you are closing | `table` or `grid` with status |

## 4. Editorial and media visuals

For newsletter, media, category-creation, and thought-leadership work (also in `library-editorial-media.md`):

- Editorial franchise map — recurring content pillars, formats, and audience jobs (`grid`)
- Content portfolio matrix — audience value vs. production effort (`two_by_two`)
- Audience-to-revenue flywheel (`signature_audience_flywheel`)
- Media business model map — audience, attention, products, sponsors, services, community (`orbit`)
- Newsletter growth loop — high-value issue → forwarding → subscription → data → better issue (`flywheel`)
- Content IP ladder — post → newsletter → report → webinar → workshop → advisory product (`ladder`)
- Signature-series architecture — flagship report, podcast, newsletter, events, community (`orbit`)
- Distribution ecosystem map — owned audience, social networks, video platforms, partners, search, communities (`orbit`)
- Creator operating system — research, production, publishing, distribution, analytics, repurposing (`chevron`, with `loop_back`)
- Content performance tree — reach, engagement, trust, leads, pipeline, revenue (`tree`)
- Thought-leadership wedge — sharp thesis first, category later (`wedge`)
- Attention-to-authority journey — discovery → repeat exposure → trust → subscription → conversation → intent (`chevron`)
- "What the market is saying" quote collage (`card`, quote mode)
- Signature visual metaphor — one metaphor reused until it becomes a brand asset

## 5. Slide-level visual patterns

Not every slide needs a chart or diagram. These layouts create pace and make concepts land.

| Pattern | When | Notes |
|---|---|---|
| Hero statistic | One oversized number, short label, small source | `hero_stat`; number in accent, ≥ 120pt |
| Two-number contrast ("73% did X, but only 19% did Y") | The gap between two figures is the story | `compare_bars`; highlight the second bar, label the gap |
| Hero statement | One memorable sentence, sparse support | `thesis_slide`; ≤ 14 words |
| Big idea + three proof points | Thesis left, evidence right | 40/60 split; proof points as 3 short cards |
| Annotated screenshot | Product, dashboard, workflow, or customer artifact with callouts | ≤ 4 callouts, numbered |
| Annotated chart | One key finding highlighted, everything else muted | use `highlight` in specs; one accent color |
| Timeline with inflection point | Make the critical moment visually dominant | `timeline` with the inflection highlighted |
| Three-card layout | Three choices, pillars, risks, or actions | `columns` (3) |
| Four-quadrant layout | Classification, not dense prose | `two_by_two`; ≤ 3 items per quadrant |
| Five-step chevron | Operating sequence | `chevron`; highlight the step that matters now |
| Center-and-orbit | Central idea with enablers around it | `orbit`; ≤ 8 satellites |
| Layer cake | Layers of technology, strategy, or operating model | `stack` |
| Split screen | Contrast two worlds, options, or operating models | `before_after` |
| Full-bleed quote | Customer, executive, or market quote with one highlighted phrase | typographic; highlight ≤ 6 words |
| Full-bleed photo with thesis overlay | Emotional reset or human stakes | use sparingly (≤ 2 per deck) |
| Visual metaphor with labels | Bridge, flywheel, compass, ladder, map, iceberg, maze | one metaphor per narrative |
| Dashboard montage | 3–6 KPI tiles plus a central trend | `dashboard`; only if the audience needs operational visibility |
| Progressive reveal | Show complexity in stages | build the full spec, then render subsets with `highlight` |
| One-screen decision slide | Options, criteria, recommendation, implication | `table` with `recommendation` |
| Executive takeaway banner | Short takeaway atop a detailed chart | the `title` field is the banner |
| Appendix deep-dive | Source tables, methodology, definitions | keep off the main flow |

## 6. Visual metaphors

Metaphors explain abstract strategy, but use them deliberately — one consistent metaphor per narrative is usually enough. Choose by what it communicates, then render with the matching diagram type.

| Metaphor | Communicates | Example | Render |
|---|---|---|---|
| Flywheel | Compounding momentum | Audience and pipeline reinforce each other | `flywheel` |
| Bridge | Transition | Legacy → AI-native operations | `bridge` |
| Iceberg | Hidden complexity | Surface-level pilots vs. underlying readiness | `iceberg` |
| Mountain / staircase | Maturity or ambition | Experimentation → transformation | `staircase` |
| Compass | Strategic direction | A category POV guiding priorities | `orbit` (4 points) |
| Map | Navigation and positioning | Market landscape or transformation path | `two_by_two` / `grid` |
| Ladder | Progression | Customer maturity or value realization | `ladder` |
| Funnel | Conversion and narrowing | Demand generation or qualification | `funnel` |
| Engine | Repeatable system | Content engine, pipeline engine | `chevron` with `loop_back` |
| Orbit | Ecosystem | Core platform surrounded by partners | `orbit` |
| River | Flow | Customer, data, or work moving through systems | Sankey (matplotlib) or `chevron` |
| Maze | Complexity | Fragmented buyer journey or tool landscape | `network` (dense) |
| Dominoes | Dependencies | One constraint causing downstream failures | `chevron` with risk highlight |
| Lighthouse | Guidance and differentiation | Clear narrative in a noisy market | `hero_stat` / thesis |
| Control tower | Visibility and orchestration | Revenue operations or AI governance | `dashboard` |
| Mosaic | Pieces forming a whole | Fragmented signals → customer intelligence | `grid` |
| Blueprint | Intentional design | Operating-model or transformation architecture | `stack` / signature operating model |
| Telescope | Future view | Market foresight and scenario planning | scenario bands (matplotlib) |
| X-ray | Root causes | Revealing hidden operational problems | `iceberg` / `tree` |
| Circuit | Connected system | AI / data / tool integrations | `network` |

## 7. Deck rhythm

A useful spine for a 12-slide executive deck. Each slide is tagged with its *beat*; the deck should alternate beats rather than run four charts or four frameworks in a row.

| # | Slide | Beat | Typical visual |
|---|---|---|---|
| 1 | Thesis or tension | assertion | `thesis_slide` / `hero_stat` |
| 2 | Evidence the issue is real | evidence | annotated chart, `funnel`, `dumbbell` |
| 3 | Why it matters now | explanation | why-now `stack` |
| 4 | Root cause or strategic insight | explanation | `iceberg`, `tree` |
| 5 | Future-state visual | assertion | signature operating model, `before_after` |
| 6 | Strategic choices | implication | `columns` (3), `choice_tree` |
| 7 | Recommended approach | assertion | `bridge`, `chevron` |
| 8 | Operating model or workflow | explanation | `swimlane`, `signature_signal_to_action` |
| 9 | Roadmap | implication | `columns` (now/next/later), `gantt` |
| 10 | Economics, impact, or KPI model | evidence | `waterfall`, `tree` (ROI), `timeline` (value realization) |
| 11 | Risks and mitigations | evidence | risk `two_by_two`, `table` |
| 12 | Decision or next step | implication | decision `table` |

A deck made entirely of charts feels analytical but forgettable; one made entirely of frameworks feels polished but unproven. Alternate assertion → evidence → explanation → implication. `audit_visual.py --storyboard` flags four-in-a-row of the same beat.

## The practical starter kit

If building a reusable template library, build these 20 first — they cover most B2B strategy and AI/GTM decks:

1. Executive thesis slide (`thesis_slide`) · 2. Before-vs-after transformation (`before_after`) · 3. Why-now stack (`stack`) · 4. Category landscape map (`grid`) · 5. Positioning quadrant (`two_by_two`) · 6. ICP card (`card`) · 7. Buying-committee map (`orbit`) · 8. Buyer journey (`columns` / `journey_curve`) · 9. Message house (`message_house`) · 10. Funnel with leakage (`funnel`) · 11. Waterfall bridge (`waterfall`) · 12. Pipeline coverage (`bullet`) · 13. Content-to-pipeline flywheel (`flywheel`) · 14. AI use-case prioritization matrix (`two_by_two`) · 15. Human–AI workflow (`swimlane`) · 16. AI capability stack (`stack`) · 17. Operating-model swimlane (`swimlane`) · 18. Now-next-later roadmap (`columns`) · 19. ROI tree / value realization (`tree` / `timeline`) · 20. Decision slide (`table` with recommendation)

Every one of these has a ready example spec in `assets/examples/`.
