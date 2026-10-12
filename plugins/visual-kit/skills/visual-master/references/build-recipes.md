# Build recipes — rendering a selected visual on each surface

Read this at STEP 3 once you know *which* visual to make and *where* it will live. The scripts do the drawing; this file tells you which script, which spec, and how to land the result in a deck, an artifact, a document, or a social image.

Contents: 1. The three renderers · 2. Spec conventions · 3. Surface recipes (pptx, HTML/SVG artifact, docx/pdf, social PNG) · 4. Native-shape rebuilds in pptx · 5. Chart types not covered by the scripts · 6. Brand palette handoff

---

## 1. The three renderers

| Route (from catalog `render`) | Script | Output | Use for |
|---|---|---|---|
| `svg:<type>` | `python scripts/render_svg.py <type> spec.json -o out.svg --png` | SVG + PNG (2×) | 43 diagram types: strategy, process, GTM, AI, metaphors, 5 signature visuals |
| `chart` | `python scripts/chart.py <kind> spec.json -o out.png` (or `--svg`) | PNG / SVG | 12 data-chart kinds: bar, hbar, grouped_bar, stacked_bar, line, area, scatter, dot, histogram, pareto, tornado, scenario |
| `shapes` / `text` | native pptx shapes or HTML/CSS | editable | progress bars, gauges, thesis slides, hero statements — see §4 |

List what exists: `render_svg.py --types`, `chart.py --kinds`. Print a starting spec: `render_svg.py --example flywheel`, `chart.py --example line`. Every example is also saved in `assets/examples/` (diagram specs as `<type>.json`, chart specs as `chart_<kind>.json`).

Catalog routes that need a library the scripts do not bundle (Sankey, alluvial, treemap, sunburst, mosaic, bump, cohort heatmaps, calendar heatmap, box/violin, fan chart): use §5.

## 2. Spec conventions (both scripts)

```json
{
  "title": "Takeaway sentence, not a topic",
  "subtitle": "optional framing line",
  "source": "optional — required for anything with numbers",
  "width": 1600, "height": 900,
  "palette": { "accent": "#...", "accent2": "#...", "risk": "#...", "bg": "#...", "ink": "#...", "muted": "#...", "line": "#...", "context": "#...", "font": "..." },
  "highlight": [indexes],
  "data": { ...see --example... }
}
```

- `highlight` is how you make the annotated-chart pattern: list the index(es) of the story element; everything else is drawn in `context` gray. Leave it empty when all elements matter equally.
- Sizes: 1600×900 for 16:9 slides; 1600×1200 for documents; 1080×1080 (square) or 1200×627 (landscape) for professional-network posts; 1080×1350 for portrait social.
- Units: put currency symbols first (`"$M"`, `"$K"`) and suffixes last (`"%"`, `"x"`, `" hrs/wk"`); the scripts format `$12.0M`, `+$4.8M`, `42%` correctly.
- Always run `python scripts/audit_visual.py spec.json --type <type>` before rendering. Fix any FAIL (topic title) and take WARNs seriously (too many elements, missing source).

## 3. Surface recipes

### 3a. Slide decks (PPTX) — with your deck tool

Use whatever deck tool or library you already work with (python-pptx below) for deck mechanics; this recipe covers only how visuals land on slides.

1. Render the visual at 2× (`--png` uses `--scale 2` by default; chart.py saves at 200 dpi).
2. Match the palette to the deck theme *before* rendering (§6) so the image and the slide share `bg`.
3. Insert the PNG full-bleed in the content zone, keeping the slide title separate from the image title: either set `"title": ""` in the spec and put the takeaway in the slide's title placeholder (preferred — the title stays editable and searchable), or keep the title inside the image and leave the placeholder empty. Never both.
4. For visuals the audience will edit later (roadmaps, RACI, decision tables), rebuild with native shapes/tables instead (§4). Charts with real data should be native pptx charts when the deck owner will update numbers; use `chart.py` output when the chart is a one-time exhibit.

python-pptx insertion (16:9, 13.333×7.5 in):
```python
from pptx import Presentation
from pptx.util import Inches
prs = Presentation(); prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
s = prs.slides.add_slide(prs.slide_layouts[5])          # title-only layout
s.shapes.title.text = "Conversion — not volume — is the Q4 constraint"
s.shapes.add_picture("funnel.png", Inches(0.6), Inches(1.4), width=Inches(12.1))
prs.save("deck.pptx")
```
Native chart (editable data) — bar with one highlighted category:
```python
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.dml.color import RGBColor
cd = CategoryChartData(); cd.categories = ["Enterprise", "Mid-market", "SMB"]; cd.add_series("Pipeline $M", (3.1, 8.4, 1.2))
ch = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.6), Inches(1.4), Inches(12), Inches(5.6), cd).chart
ch.has_legend = False; ch.plots[0].has_data_labels = True; ch.value_axis.visible = False
pts = ch.plots[0].series[0].points
for i, hexcol in enumerate(["C7CBD1", "2563EB", "C7CBD1"]):
    pts[i].format.fill.solid(); pts[i].format.fill.fore_color.rgb = RGBColor.from_string(hexcol)
```

### 3b. HTML / SVG artifact (web page, dashboard, interactive)

- Inline the SVG from `render_svg.py` directly into the page (`<div class="vis">…svg markup…</div>`); it scales with `width:100%; height:auto` and stays crisp. Do not link to an external file.
- For theme-aware pages, pass a palette whose `bg` is transparent-friendly (`"bg": "#FFFFFF"` then strip the first `<rect>` with a one-line regex) and set colors via CSS variables if the diagram must flip between light and dark.
- If the artifact needs live interactivity (hover, filters), hand the *data* to an interactive charting library instead of a static SVG; keep this skill's selection and the takeaway title.
- If your environment has a page/artifact design skill or style guide, apply it before writing the page.

### 3c. Documents (docx / pdf) — with your document tool

- Render at 1600×1200 (4:3 reads better inline than 16:9) or 1600×900 for wide figures; insert at 6–6.5 in width.
- Keep the takeaway as the figure caption *and* in the image title — readers skim captions.
- docx: `doc.add_picture("fig.png", width=Inches(6.3))` then a caption paragraph in the "Caption" style. Number figures sequentially and reference them in the text.
- Put source lines inside the image (`"source"` field) so the figure remains self-contained when copied.

### 3d. Social / newsletter images (PNG)

- Sizes: 1080×1080 square, 1200×627 link-preview, 1080×1350 portrait. Set `"width"`/`"height"` in the spec.
- Fewer elements than a slide: ≤ 4 steps, ≤ 5 nodes, one highlight. Bump label sizes if the renderer's defaults look small at square aspect (edit the `size=` arguments or post-scale).
- `hero_stat`, `compare_bars` (two-number contrast), `before_after`, `chevron`, `flywheel`, `two_by_two`, and `staircase` are the most shareable forms.
- Export PNG at scale 2; social platforms compress images, so avoid thin 1px lines and light-gray text under 14px.

## 4. Native-shape rebuilds in pptx

Use native shapes when the deck owner must edit text later or the brand font must be preserved. Map the diagram to shapes:

| Diagram | Native build |
|---|---|
| chevron | `MSO_SHAPE.CHEVRON` per step, first one `PENTAGON`; sub-labels as text boxes below |
| columns / now-next-later | 3 rounded rectangles + header bars; items as bullet text |
| stack / layer cake | stacked rounded rectangles, width 70%, 6–8pt gaps |
| two_by_two | 4 rectangles + 2 lines; items as small ovals with text boxes |
| before_after | 2 rounded rectangles with header bars; ✕ / ✓ prefixes |
| table / decision matrix | native table; highlight column via cell fill |
| timeline | line + ovals + text boxes; `MSO_CONNECTOR.STRAIGHT` for the line |
| flywheel / orbit | ovals on a circle (compute positions with `cos/sin`) + `BLOCK_ARC` shapes between them |
| progress bar / gauge | two overlapping rounded rectangles (track + fill) / `BLOCK_ARC` |
| thesis / hero stat | text boxes only; hero number ≥ 120pt in accent |

Always apply the same color roles (accent / accent2 / risk / context) to native shapes so image-based and native visuals look like one system.

## 5. Chart types not covered by the scripts

| Visual | Fastest path |
|---|---|
| Sankey / alluvial | `plotly.graph_objects.Sankey` → `fig.write_image()` (needs kaleido) or an HTML artifact; color the one flow that matters, gray the rest |
| Treemap / sunburst | `plotly.express.treemap` / `sunburst`; ≤ 2 levels visible |
| Mosaic (variable-width stacked bar) | matplotlib: variable-width `bar()` with `left` offsets from cumulative segment sizes |
| Bump chart | matplotlib lines of rank per period; invert y; label at both ends |
| Cohort heatmap / calendar heatmap | `seaborn.heatmap` with a single-hue sequential palette; annotate cells |
| Box / violin | `seaborn.boxplot` / `violinplot`; gray boxes, accent for the segment in question |
| Fan chart | `fill_between` bands at 50/80/95% with decreasing alpha |
| Sparkline row | small matplotlib axes with all spines off, in a grid next to KPI values |
| Control / run chart | `chart.py line` plus `axhline` for mean and ± limits |

Whichever library you use, keep the rules: takeaway title, one accent, muted context, direct labels, no legend if labels fit, source line.

## 6. Brand palette handoff

This skill ships neutral. When the user gives brand colors, build the palette *once* per deck and reuse it in every spec (the values below are an illustrative dark palette; substitute your brand's):

```bash
cat > palette.json <<'EOF'
{"bg":"#0F172A","ink":"#FFFFFF","muted":"#CBD5E1","line":"#334155","context":"#1E293B","accent":"#38BDF8","accent2":"#34D399","risk":"#FBBF24","font":"Inter, Arial, sans-serif"}
EOF
python - <<'EOF'
import json, glob
pal = json.load(open("palette.json"))
for f in glob.glob("specs/*.json"):
    s = json.load(open(f)); s["palette"] = pal; json.dump(s, open(f, "w"), indent=2)
EOF
```

Role mapping when the brand has more colors than roles: primary brand color → `accent`; the "success / growth" color → `accent2`; the "warning / attention" color → `risk`; everything else stays gray. Do not assign a fourth chromatic role; if the brand insists on a gradient, apply it only to hero elements (cover, thesis slide), not to data.
