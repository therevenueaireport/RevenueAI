# Market, customer, and GTM visuals

Use for positioning, category creation, product marketing, demand generation, ABM, sales motions, customer lifecycle, proof, and revenue strategy.

Columns: **Visual** · **Best for** (the claim it answers) · **Example use** · **Claim type** (what `select_visual.py` matches on) · **Render** (`chart` = matplotlib/native chart; `svg:<type>` = `render_svg.py <type>`; `shapes` = pptx/HTML shapes; `text` = typographic slide).

| Visual | Best for | Example use | Claim | Render |
|---|---|---|---|---|
| TAM / SAM / SOM circles | Framing market opportunity | Broad market, addressable market, reachable initial segment | market | `svg:concentric` |
| Market map | Showing category landscape | Vendors by category, adjacent tools, buyers, influencers | market | `svg:grid` |
| Competitive landscape | Showing competitor groups | Suites, point solutions, services, emerging entrants | market | `svg:grid` |
| Perceptual positioning map | Showing differentiated market position | Ease of use versus enterprise depth | positioning | `svg:two_by_two` |
| Competitive battlecard grid | Showing how to win against alternatives | Strengths, weaknesses, proof, traps, objections | competitive | `svg:table` |
| Feature comparison matrix | Comparing product capabilities | Capability coverage by vendor | comparison | `svg:table` |
| Category map | Defining a new market frame | Legacy categories, emerging category, adjacent spaces | positioning | `svg:venn` |
| Category creation wedge | Showing initial beachhead | Narrow urgent use case expanding into a broader platform | positioning | `svg:wedge` |
| Why now? stack | Showing forces creating urgency | Technology shift, buyer pressure, economics, regulation | urgency | `svg:stack` |
| Market forces diagram | Showing external drivers | Customer change, competition, technology, policy, economy | urgency | `svg:orbit` |
| PESTLE wheel | Structuring external analysis | Political, economic, social, technological, legal, environmental | market | `svg:orbit` |
| Porter's Five Forces | Showing industry structure | Supplier power, buyer power, substitutes, rivalry, entrants | market | `svg:orbit` |
| SWOT matrix | Summarizing internal/external position | Strengths, weaknesses, opportunities, threats | classification | `svg:two_by_two` |
| Opportunity solution tree | Connecting outcomes, opportunities, and solutions | Revenue objective -> customer barriers -> strategic plays | hierarchy | `svg:tree` |
| Segmentation map | Showing target customer groups | By company size, maturity, need, buying motion | customer | `svg:grid` |
| Ideal customer profile card | Making an ICP concrete | Firmographics, triggers, pains, buying committee | customer | `svg:card` |
| Account tiering pyramid | Showing ABM prioritization | Tier 1, Tier 2, Tier 3 accounts | hierarchy | `svg:pyramid` |
| Persona card | Humanizing a buyer | Goals, metrics, fears, objections, influence | customer | `svg:card` |
| Buying committee map | Showing stakeholders and power | Champion, economic buyer, user, blocker, procurement | customer | `svg:orbit` |
| Stakeholder influence matrix | Showing who to engage | Influence versus support | prioritization | `svg:two_by_two` |
| Buying journey map | Showing stages and questions | Problem recognition -> evaluation -> consensus -> selection | customer | `svg:columns` |
| Buyer question ladder | Showing information needed by stage | Why change? -> Why now? -> Why us? | sequence | `svg:ladder` |
| Message house | Organizing positioning | Core promise, pillars, proof points, supporting messages | message | `svg:message_house` |
| Messaging pyramid | Showing hierarchy of communication | Category thesis -> value proposition -> capabilities -> proof | message | `svg:pyramid` |
| Narrative arc | Structuring a market story | Status quo -> disruption -> stakes -> new way -> proof | argument | `svg:journey_curve` |
| StoryBrand-style journey | Centering the customer | Customer problem -> guide -> plan -> success | argument | `svg:chevron` |
| Value proposition canvas | Connecting buyer needs and offer | Jobs, pains, gains versus products, relievers, creators | customer | `svg:columns` |
| Proof architecture | Showing evidence behind claims | Customer evidence, product evidence, market evidence, ROI | proof | `svg:stack` |
| Evidence ladder | Ranking claim strength | Assertion -> example -> data -> customer proof -> independent validation | proof | `svg:ladder` |
| Objection map | Showing concerns and responses | Risk, cost, complexity, switching, proof | competitive | `svg:table` |
| Competitive alternatives map | Showing what buyers do instead | Do nothing, build internally, use incumbent, use new category | competitive | `svg:columns` |
| Sales motion map | Showing routes to market | Self-serve, PLG, sales-led, partner-led, enterprise | inventory | `svg:columns` |
| Channel mix map | Showing role of each channel | Paid, owned, earned, partner, community, outbound | inventory | `svg:grid` |
| Demand engine diagram | Showing how attention becomes revenue | Audience -> engagement -> intent -> pipeline -> expansion | sequence | `svg:chevron` |
| Content engine | Showing content repurposing | Research -> flagship asset -> newsletter -> social -> sales -> events | sequence | `svg:chevron` |
| Content atomization map | Showing one idea becoming many formats | Report -> webinar -> clips -> posts -> email -> enablement | hierarchy | `svg:tree` |
| Editorial calendar | Showing content cadence | Themes, formats, audience, distribution, owner | timing | `svg:gantt` |
| Distribution waterfall | Showing priority distribution sequence | Owned audience -> partners -> social -> paid amplification | sequence | `svg:staircase` |
| Community flywheel | Showing audience compounding | Content -> participation -> relationships -> advocacy -> insight | loop | `svg:flywheel` |
| Event experience map | Designing an event as a journey | Invitation -> registration -> attendance -> follow-up -> community | customer | `svg:columns` |
| Campaign architecture | Showing integrated campaign components | Theme, audience, assets, channels, offers, measurement | architecture | `svg:stack` |
| Account journey orchestration | Showing multi-touch ABM plays | Intent signal -> ads -> executive content -> SDR outreach -> event | sequence | `svg:timeline` |
| Lead-scoring model | Showing how signals combine | Fit, intent, engagement, recency, opportunity context | hierarchy | `svg:tree` |
| Revenue funnel map | Linking marketing activity to bookings | Reach -> engaged accounts -> qualified pipeline -> closed-won | flow | `svg:funnel` |
| Pipeline coverage visual | Showing target versus available pipeline | Required coverage by segment and quarter | target | `svg:bullet` |
| Pipeline hygiene map | Showing quality dimensions | Completeness, velocity, stage accuracy, next step, risk | inventory | `svg:grid` |
| Win/loss insight map | Showing patterns from deal outcomes | Reasons won/lost by segment, competitor, stage | comparison | `chart` |
| Customer lifecycle map | Showing acquisition through expansion | Land -> activate -> adopt -> retain -> expand -> advocate | sequence | `svg:chevron` |
| Land-and-expand model | Showing growth motion | Initial use case -> team -> department -> enterprise | sequence | `svg:concentric` |
| Customer health score | Showing risk and opportunity | Usage, sentiment, support, adoption, commercial status | target | `svg:dashboard` |
| Expansion opportunity map | Showing whitespace | Account teams versus products/modules/regions | intensity | `chart` |
| Voice-of-customer collage | Making qualitative research tangible | Short anonymized quotes grouped by theme | proof | `svg:card` |
| Quote wall | Adding emotional proof | Customer statements with a few highlighted phrases | proof | `svg:card` |
| Case-study journey | Showing transformation evidence | Problem -> intervention -> outcome -> business result | proof | `svg:chevron` |
| ROI tree | Showing financial impact | Efficiency, conversion, retention, expansion, risk reduction | hierarchy | `svg:tree` |
| Value realization timeline | Showing when benefits arrive | 30-day, 90-day, 180-day outcomes | timing | `svg:timeline` |

56 visuals. Get the full record for any of them with `python scripts/select_visual.py --show <id>`; list ids with `--list gtm`.
