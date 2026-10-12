# Core data visuals

Use when the audience needs magnitude, trend, comparison, composition, distribution, flow, or relationship. Most of these render with matplotlib / native pptx charts (`render=chart`) — see build-recipes.md. The ones marked `svg:` have a diagram renderer.

Columns: **Visual** · **Best for** (the claim it answers) · **Example use** · **Claim type** (what `select_visual.py` matches on) · **Render** (`chart` = matplotlib/native chart; `svg:<type>` = `render_svg.py <type>`; `shapes` = pptx/HTML shapes; `text` = typographic slide).

| Visual | Best for | Example use | Claim | Render |
|---|---|---|---|---|
| Bar chart | Comparing discrete categories | Pipeline by segment, revenue by product line | comparison | `chart` |
| Horizontal bar chart | Ranking many categories with long labels | Top customer objections, top content topics | ranking | `chart` |
| Grouped bar chart | Comparing categories across 2-4 series | CAC by channel across quarters | comparison | `chart` |
| Stacked bar chart | Showing composition and total | Pipeline by stage or source | composition | `chart` |
| 100% stacked bar | Showing mix changes over time | Revenue mix by segment, channel, or plan | composition | `chart` |
| Diverging bar chart | Showing positive vs. negative movement | What customers love vs. complain about | comparison | `chart` |
| Waterfall chart | Explaining movement from one number to another | ARR bridge, pipeline bridge, budget variance | bridge | `svg:waterfall` |
| Variance waterfall | Plan versus actual | Why bookings missed or exceeded target | bridge | `svg:waterfall` |
| Line chart | Showing change over time | MQLs, ARR, retention, site traffic, activation | trend | `chart` |
| Multi-line chart | Comparing trends | Growth by region, product, or cohort | trend | `chart` |
| Area chart | Showing total volume and trend | Total demand volume over time | trend | `chart` |
| Stacked area chart | Showing how a total changes in composition | Traffic source contribution over time | composition | `chart` |
| Slope chart | Showing before/after change | Category perception before and after repositioning | before_after | `svg:slope` |
| Bump chart | Showing changing rankings | Brand rank, keyword rank, channel rank by quarter | ranking | `chart` |
| Sparkline | Showing a compact trend beside a KPI | Pipeline trend next to pipeline total | trend | `chart` |
| Bullet chart | Showing performance against a target | 78% of quarterly target achieved | target | `svg:bullet` |
| Progress bar | Showing simple completion | Launch readiness, operating-plan completion | target | `shapes` |
| Gauge or dial | Showing status against a threshold (only when the audience already understands the scale) | Health score in a familiar 0-100 scale | target | `shapes` |
| Dot plot | Comparing many values cleanly | Conversion rate by campaign | comparison | `chart` |
| Lollipop chart | A lighter alternative to bars | Pipeline contribution by source | comparison | `chart` |
| Two-value dot plot | Comparing two values per category | Current vs. target conversion rates | comparison | `chart` |
| Dumbbell chart | Showing the distance between two values | Pre- versus post-AI productivity | before_after | `svg:dumbbell` |
| Scatter plot | Showing relationships and outliers | Spend versus pipeline; satisfaction versus retention | relationship | `chart` |
| Bubble chart | Adding a third variable to a scatter plot | Market size, growth, and competitive intensity | relationship | `chart` |
| Quadrant chart | Classifying items on two strategic dimensions | High-value/high-feasibility AI use cases | prioritization | `svg:two_by_two` |
| Heatmap | Showing intensity across two dimensions | Segment x use-case demand; week x channel activity | intensity | `chart` |
| Calendar heatmap | Showing patterns over dates | Content publishing cadence and engagement | intensity | `chart` |
| Matrix heatmap | Mapping many items against criteria | Competitive feature comparison | comparison | `chart` |
| Histogram | Showing the distribution of a metric | Deal-size distribution | distribution | `chart` |
| Box plot | Comparing distributions and outliers | Sales cycle by segment | distribution | `chart` |
| Violin plot | Showing distribution shape | Time-to-value across customer cohorts | distribution | `chart` |
| Pareto chart | Showing the few drivers behind most impact | Top objections causing most deal losses | ranking | `chart` |
| Treemap | Showing hierarchical composition | Revenue by region, segment, and account | composition | `chart` |
| Sunburst chart | Showing layered hierarchy | Product portfolio or customer segmentation | composition | `chart` |
| Mosaic (variable-width stacked bar) chart | Showing two dimensions of market composition | Segment size and vendor share | composition | `chart` |
| Funnel chart | Showing stage conversion | Visitor -> lead -> opportunity -> customer | flow | `svg:funnel` |
| Conversion staircase | A more analytical funnel | Stage counts plus conversion and leakage | flow | `svg:funnel` |
| Sankey diagram | Showing flow between stages or categories | Lead source -> sales motion -> outcome | flow | `chart` |
| Alluvial diagram | Showing movement between states over time | Segment migration, plan upgrades, retention paths | flow | `chart` |
| Cohort retention chart | Showing retention by acquisition cohort | Product activation and renewal analysis | trend | `chart` |
| Cohort heatmap | Showing behavior over time by cohort | Usage, retention, expansion, or engagement by cohort | intensity | `chart` |
| Survival curve | Showing attrition over time | Customer or user retention duration | trend | `chart` |
| Control chart | Showing whether a process is stable | Weekly lead-quality rate against expected variation | trend | `chart` |
| Run chart | Showing operational performance over time | Ticket resolution, demo conversion, activation time | trend | `chart` |
| Tornado chart | Showing sensitivity analysis | Which assumptions most affect the revenue plan | sensitivity | `chart` |
| Tornado risk chart | Comparing upside/downside impact | Risks to launch, forecast, or strategic bet | sensitivity | `chart` |
| Fan chart | Showing uncertainty ranges | Forecast scenarios and confidence bands | uncertainty | `chart` |
| Scenario bands | Showing base, upside, and downside paths | ARR outlook under different conversion assumptions | uncertainty | `chart` |
| Goal tree with numbers | Showing KPI drivers | ARR target decomposed into pipeline, win rate, ACV | hierarchy | `svg:tree` |

49 visuals. Get the full record for any of them with `python scripts/select_visual.py --show <id>`; list ids with `--list data`.
