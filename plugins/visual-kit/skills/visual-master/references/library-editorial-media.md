# Editorial and media visuals

Use for newsletter, media, category-creation, and thought-leadership work: content engines, audience flywheels, IP ladders, distribution ecosystems.

Columns: **Visual** · **Best for** (the claim it answers) · **Example use** · **Claim type** (what `select_visual.py` matches on) · **Render** (`chart` = matplotlib/native chart; `svg:<type>` = `render_svg.py <type>`; `shapes` = pptx/HTML shapes; `text` = typographic slide).

| Visual | Best for | Example use | Claim | Render |
|---|---|---|---|---|
| Editorial franchise map | Recurring content pillars, formats, and audience jobs | Newsletter franchises mapped to audience needs | inventory | `svg:grid` |
| Content portfolio matrix | Audience value versus production effort | Which content formats to double down on | prioritization | `svg:two_by_two` |
| Audience-to-revenue flywheel | How audience compounds into revenue | Audience -> authority -> pipeline -> proof -> audience | loop | `svg:signature_audience_flywheel` |
| Media business model map | Audience, attention, products, sponsors, services, community | How a media brand monetizes | system | `svg:orbit` |
| Newsletter growth loop | High-value issue -> forwarding -> subscription -> data -> better issue | How the newsletter grows itself | loop | `svg:flywheel` |
| Content IP ladder | Post -> newsletter -> report -> webinar -> workshop -> advisory product | How content becomes intellectual property and products | maturity | `svg:ladder` |
| Signature-series architecture | Flagship report, podcast, newsletter, events, community | How the flagship properties relate | architecture | `svg:orbit` |
| Distribution ecosystem map | Owned audience, LinkedIn, YouTube, partners, search, communities | Where content travels | system | `svg:orbit` |
| Creator operating system | Research, production, publishing, distribution, analytics, repurposing | The weekly content machine | sequence | `svg:chevron` |
| Content performance tree | Reach, engagement, trust, leads, pipeline, revenue | How content metrics roll up to revenue | hierarchy | `svg:tree` |
| Thought-leadership wedge | A sharp thesis that earns attention before expanding into a broader category | Narrow POV wedge into category ownership | positioning | `svg:wedge` |
| Attention-to-authority journey | Discovery -> repeat exposure -> trust -> subscription -> conversation -> commercial intent | How a stranger becomes a buyer | sequence | `svg:chevron` |
| What the market is saying collage | Quotes from executives, customers, analysts, and creators | Market sentiment in the market's own words | proof | `svg:card` |
| Signature visual metaphor | A repeatable brand asset | One metaphor reused across decks, posts, and reports | assertion | `svg` |

14 visuals. Get the full record for any of them with `python scripts/select_visual.py --show <id>`; list ids with `--list editorial`.
