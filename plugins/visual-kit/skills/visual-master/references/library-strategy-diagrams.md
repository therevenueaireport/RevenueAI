# Strategy and narrative diagrams

Use when the slide must communicate an argument, not report data: hierarchy, loops, transitions, tradeoffs, choices, contrasts, continua.

Columns: **Visual** · **Best for** (the claim it answers) · **Example use** · **Claim type** (what `select_visual.py` matches on) · **Render** (`chart` = matplotlib/native chart; `svg:<type>` = `render_svg.py <type>`; `shapes` = pptx/HTML shapes; `text` = typographic slide).

| Visual | Best for | Example use | Claim | Render |
|---|---|---|---|---|
| Pyramid | Showing hierarchy or layers | Brand strategy: category -> narrative -> proof -> campaigns | hierarchy | `svg:pyramid` |
| Inverted pyramid | Showing broad inputs narrowing to a decision | Market signals -> insight -> strategic choice | hierarchy | `svg:pyramid` |
| Flywheel | Showing reinforcing loops | Content -> audience -> trust -> pipeline -> customer proof | loop | `svg:flywheel` |
| Virtuous cycle | Explaining compounding advantage | Better data -> better AI -> better workflow -> more data | loop | `svg:flywheel` |
| Venn diagram | Showing overlap between 2-3 concepts | Where AI capability, customer need, and GTM readiness meet | overlap | `svg:venn` |
| Concentric circles | Showing core and surrounding layers | Core platform, products, ecosystem, market context | hierarchy | `svg:concentric` |
| Onion diagram | Showing nested levels | Strategy, operating model, process, tools, behaviors | hierarchy | `svg:concentric` |
| Iceberg | Showing visible outcomes versus hidden causes | Missed pipeline target versus positioning/process issues | hidden_cause | `svg:iceberg` |
| Mountain or ascent | Showing maturity, journey, or ambition | AI adoption maturity from experimentation to reinvention | maturity | `svg:staircase` |
| Staircase | Showing sequential progress or maturity | From ad hoc marketing to AI-native GTM | maturity | `svg:staircase` |
| Ladder | Showing hierarchy or progression | Value ladder, buyer maturity, capability maturity | maturity | `svg:ladder` |
| Bridge | Showing movement from current state to future state | Legacy GTM -> AI-enabled revenue operating model | transition | `svg:bridge` |
| Chasm | Showing a gap to overcome | Point solution adoption versus enterprise transformation | transition | `svg:bridge` |
| Before-and-after split | Showing a transformation | Old operating model versus new model | before_after | `svg:before_after` |
| Then / now / next timeline | Showing evolution | Evolution of customer expectations or company strategy | evolution | `svg:columns` |
| Three-horizon chart | Showing present, emerging, and future bets | Core business, adjacencies, and new AI-native offerings | portfolio | `svg:columns` |
| Strategic choices cascade | Showing linked strategic decisions | Where to play, how to win, capabilities, systems | decision | `svg:cascade` |
| Choice tree | Showing decision branches | Build, buy, partner, or defer | decision | `svg:tree` |
| Decision matrix | Making an explicit recommendation | AI vendors scored by security, capability, cost, speed | decision | `svg:table` |
| Tradeoff triangle | Showing tensions among three goals | Speed, quality, and cost; scale, relevance, efficiency | tradeoff | `svg:triangle` |
| Magic triangle | Showing a three-part system | Brand, demand, and customer proof | system | `svg:triangle` |
| Four-box framework | Categorizing concepts | Urgent/important; known/unknown; build/buy/partner/wait | classification | `svg:two_by_two` |
| Two-by-two matrix | Prioritization and segmentation | Impact versus effort; market attractiveness versus ability to win | prioritization | `svg:two_by_two` |
| Nine-box matrix | More granular prioritization | Segment attractiveness x competitive position | prioritization | `svg:grid` |
| Portfolio map | Showing investments across dimensions | Products by growth rate and strategic fit | portfolio | `chart` |
| Capability evolution map | Showing maturity of capabilities | Custom vs. productized vs. commodity AI components | maturity | `svg:scatter_labels` |
| Value chain diagram | Showing how value is created | Awareness -> evaluation -> purchase -> adoption -> expansion | sequence | `svg:chevron` |
| Ecosystem map | Showing stakeholders and dependencies | Customer, partners, platforms, influencers, data providers | system | `svg:orbit` |
| System map | Showing interdependent components | AI system, data sources, governance, workflows, users | system | `svg:network` |
| Causal loop diagram | Showing feedback loops and unintended effects | Content volume, saturation, trust, and conversion | loop | `svg:network` |
| Logic model | Connecting actions to outcomes | Inputs -> activities -> outputs -> outcomes -> impact | sequence | `svg:chevron` |
| Theory of change | Explaining why a program should work | Thought leadership -> category education -> demand creation | sequence | `svg:chevron` |
| Jobs-to-be-done map | Showing customer context and desired outcomes | Trigger, functional job, emotional job, social job | customer | `svg:columns` |
| Customer value map | Connecting pains, gains, and product value | Buyer problems -> capability -> business impact | customer | `svg:columns` |
| Problem-solution-proof | A simple persuasive structure | Market pain -> strategic answer -> quantified evidence | argument | `svg:columns` |
| Tension-insight-resolution | Framing a compelling narrative | AI increases output but decreases differentiation | argument | `svg:columns` |
| Myth vs. reality | Challenging a false belief | More content equals more demand | contrast | `svg:before_after` |
| Old rules / new rules | Making a category argument | Old funnel metrics versus AI-era attention metrics | contrast | `svg:before_after` |
| Contrast pair | Clarifying a distinction | Automation versus agency; efficiency versus advantage | contrast | `svg:before_after` |
| Spectrum | Showing a continuum | Tactical AI use -> strategic AI transformation | continuum | `svg:spectrum` |
| Continuum with thresholds | Showing stages and decision points | Experimenting -> scaling -> governing -> reinventing | continuum | `svg:spectrum` |
| Spectrum with archetypes | Segmenting by maturity | Skeptics, explorers, operators, AI-native leaders | continuum | `svg:spectrum` |
| One-sentence thesis slide | Anchoring the story | The next GTM advantage is not more automation-it is faster learning. | assertion | `text` |

43 visuals. Get the full record for any of them with `python scripts/select_visual.py --show <id>`; list ids with `--list strategy`.
