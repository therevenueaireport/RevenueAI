---
name: monte-carlo
description: >
  Monte Carlo simulation with built-in devil's advocate and visual scenario pathways. Models ranges of outcomes (good, bad, better, catastrophic) with statistically significant pattern detection and actionable decision paths for each scenario. Fights optimism bias by default. Triggers on: "what could happen," "model this," "simulate," "forecast," "Monte Carlo," "risk analysis," "what if," "stress test," "devil's advocate," "scenarios," "range of outcomes," "best case worst case," or evaluating any decision under uncertainty. Logs predictions so they can be compared to actuals, improving calibration over time. Use when the user shares performance data and wants to project forward.
---

# Monte Carlo Analysis — Probabilistic Decision Intelligence

## Core Philosophy

Most projections are single-point estimates dressed up with confidence. "We expect 5,000
newsletter subscribers by Q3." That's not analysis — that's a wish with a timeline.

This skill produces probability distributions AND scenario pathways. Instead of
"5,000 subscribers," you get a visual map showing five statistically distinct futures,
what drives each one, how likely each is, and what to DO in each scenario.

The devil's advocate is not a checklist — it's a scenario architect. It builds the
"bad" and "catastrophic" pathways with the same rigor as the "good" pathways, and
assigns concrete decision recommendations to each.

---

## The Five Scenario Pathways

Every Monte Carlo analysis classifies outcomes into five statistically significant
zones, each with its own narrative, drivers, and recommended actions:

### 1. Exceptional (P90+) — "Everything clicks"
- **Color:** Blue
- **Probability:** ~10%
- **Purpose:** Understand what has to go perfectly right. Don't plan for this, but
  know what to do if you land here (scale fast, reinvest, capture the moment).
- **Decision path:** Acceleration moves — what to double down on

### 2. Strong (P65-P90) — "Above plan, sustainable"
- **Color:** Green
- **Probability:** ~25%
- **Purpose:** The optimistic-but-realistic zone. Things went well, not magically.
- **Decision path:** Lean-in moves — where to push harder

### 3. Base (P35-P65) — "Plan for this"
- **Color:** Gray
- **Probability:** ~30%
- **Purpose:** The planning number lives here. This is what you resource against.
- **Decision path:** Stay-the-course moves — what to maintain and monitor

### 4. Underperform (P10-P35) — "Things went sideways"
- **Color:** Orange
- **Probability:** ~25%
- **Purpose:** The devil's advocate primary zone. What specifically went wrong, and
  what's the playbook to recover or pivot?
- **Decision path:** Correction moves — specific interventions to get back on track

### 5. Catastrophic (<P10) — "Worst realistic case"
- **Color:** Red
- **Probability:** ~10%
- **Purpose:** Not fear-mongering — survival planning. If this happens, is it
  survivable? What's the exit ramp? What should you NOT do?
- **Decision path:** Protection moves — cut losses, preserve optionality, pivot hard

---

## Simulation Protocol

### Step 1: Define the Question

Get clarity on what we're modeling. The simulation is only as good as the question.

**Required inputs:**
- **Outcome metric**: What are we measuring? (revenue, subscribers, engagement, etc.)
- **Time horizon**: Over what period?
- **Decision context**: What choice does this inform?

**Clarifying questions to ask the user:**
- What does "success" look like numerically?
- What's your gut estimate? (One input, not the answer)
- What are you most uncertain about?
- What could go wrong that you haven't planned for?

### Step 2: Map Variables with Devil's Advocate

For every variable that affects the outcome, define:

1. **Base estimate** — The user's best guess or historical average
2. **Distribution type** — See references/distributions.md
3. **Range** — Realistic minimum and maximum
4. **Correlation** — Dependencies on other variables
5. **Adversarial scenario** — What breaks this assumption, and what cascades from it?

The devil's advocate doesn't just flag risks — it architects specific failure pathways:

**For each major assumption, build a failure chain:**
```
[Assumption breaks] → [Immediate impact] → [Cascade effects] → [Outcome zone shift]
```

Example:
```
"Post 5x/week" fails → Output drops to 2x/week → Algorithm deprioritizes account
→ Organic reach drops 40% → Growth stalls → Outcome shifts from Base to Underperform
RECOMMENDED ACTION: Pre-build content buffer of 15 posts before launching growth push
```

Rules:
- Challenge EVERY assumption, not just obvious ones
- Model correlated failures (when one thing breaks, what else breaks?)
- Include at least one black swan chain per simulation
- For every failure chain, include a specific recommended action
- The median should feel slightly uncomfortable — that's good calibration

### Step 3: Build and Run the Simulation

Use `scripts/monte_carlo_engine.py` to run the simulation. The engine handles:
- Random sampling from defined distributions
- Scenario classification into the five pathways
- Statistical significance testing between scenario zones
- Sensitivity analysis (which variables drive the most variance)
- Pathway narrative generation
- Interactive HTML visualization

**Standard configuration:**
- **Iterations**: 10,000 (default) — increase to 50,000 for high-stakes decisions
- **Scenario zones**: Exceptional/Strong/Base/Underperform/Catastrophic
- **Significance threshold**: p < 0.05 for pattern detection between zones

### Step 4: Generate the Scenario Pathway Report

The HTML report must include ALL of these sections:

**1. Planning Dashboard (top of report)**
- P50 as the prominent planning number
- Full percentile ladder (P10 through P90)
- One-line summary of what this simulation models

**2. Outcome Distribution Histogram**
- Color-coded by scenario zone (blue/green/gray/orange/red)
- Vertical lines marking zone boundaries
- Hover tooltips with exact counts and percentages

**3. Scenario Pathway Cards (the key differentiator)**
Each scenario zone gets a card showing:
- **Zone name and probability range**
- **What drives this scenario** — Which variables had to land where for this zone
- **Statistical pattern** — What's significantly different about this zone vs Base
- **The story** — A 2-3 sentence narrative of what this world looks like
- **Recommended actions** — Specific moves to make IF you find yourself here
- **Early warning signals** — What leading indicators tell you you're heading here
- **Transition triggers** — What could push you from this zone into an adjacent one

**4. Sensitivity Tornado Chart**
- Which variables have the most impact on outcome variance
- Color-coded by direction (green = positive driver, red = negative driver)
- Ranked by impact magnitude

**5. Devil's Advocate Panel**
- Failure chains for each major assumption
- Correlated failure scenarios (when multiple things break at once)
- Black swan scenario narrative
- The "uncomfortable truth" — the single most important risk most people would ignore

**6. Risk Mitigation Playbook (NEW)**
Consolidates every downside risk with specific, pre-emptive actions:
- Auto-generated from sensitivity analysis (ranked by impact score)
- Each risk shows: severity (HIGH/MEDIUM/LOW), failure chain, and specific mitigation
- User-provided mitigations via `risk_mitigations` in config JSON:
  ```json
  "risk_mitigations": [
    {"risk": "Platform algorithm change", "severity": "HIGH", "severity_color": "#ef4444",
     "mitigation": "Diversify to 3 channels before growth push", "when_to_act": "Before month 2"}
  ]
  ```
- Purpose: Answer "how do I stay out of the red and orange zones?"
- Every risk must have an action — no risk without a playbook

**7. Path to Exceptional Panel (NEW)**
Analyzes what statistically drives the best outcomes and provides an acceleration playbook:
- **Upside drivers**: Variables significantly higher in Strong/Exceptional zones (z-scores)
- **Downside anchors**: Variables significantly lower in bad zones (what drags you down)
- **Acceleration playbook**: User-provided phased action plan via `acceleration_playbook`:
  ```json
  "acceleration_playbook": [
    {"phase": "Month 1-2", "action": "Build 4-newsletter buffer and test 3 lead magnets",
     "target": "Identify winning lead magnet", "measure": "Conversion rate by source"}
  ]
  ```
- Purpose: Answer "how do I get from Base to Exceptional?"
- Shows the specific levers to pull and in what order

**8. Decision Matrix**
A summary table mapping scenarios to actions:
| If outcome lands in... | Probability | Action | Priority |
|----------------------|------------|--------|----------|
| Exceptional | ~10% | [Specific acceleration move] | Have ready |
| Strong | ~25% | [Specific lean-in move] | Plan for |
| Base | ~30% | [Specific maintenance move] | Default plan |
| Underperform | ~25% | [Specific correction move] | Have ready |
| Catastrophic | ~10% | [Specific protection move] | Contingency |

### Step 5: Log the Prediction

After every simulation, append an entry to a predictions log the user keeps
(for example, `monte-carlo-predictions.md` in their working folder):

```markdown
## [DATE] — [TOPIC] — [OUTCOME METRIC]
**Question:** [What were we modeling?]
**Key assumptions:** [Top 3 variables and their distributions]
**Predictions:**
- P10: [value] | P25: [value] | P50: [value] | P75: [value] | P90: [value]
**Scenario pathways generated:** [Y/N — link to HTML report if saved]
**Devil's advocate top flag:** [Single most important risk]
**Decision made:** [What the user decided based on this]
**Actual outcome:** [PENDING — fill in when data arrives]
**Calibration note:** [PENDING — which zone did the actual land in?]
---
```

---

## Common Simulation Templates

See `references/simulation-templates.md` for pre-built models for:
- Content/audience growth projection
- Campaign ROI modeling
- Product launch revenue forecasting
- Pricing sensitivity analysis
- Resource allocation optimization
- Enablement program impact modeling

Each template includes default distributions, typical variables, devil's advocate
failure chains, and scenario-specific action recommendations.

---

## Closing the Calibration Loop

1. **History feeds Monte Carlo**: Historical performance data (CRM exports, dashboards,
   past logs) becomes the baseline for distributions. Real data > guesses.

2. **Monte Carlo feeds the predictions log**: Predictions get logged. When actuals arrive,
   compare them to the predicted zones. If you're consistently optimistic, widen
   bear-case ranges in future simulations.

3. **Devil's advocate feeds skill improvement**: When a flagged risk actually
   materializes, that's high-signal learning for the relevant skill.

4. **Scenario pathways feed decision review**: After outcomes are known, reviewing
   which pathway actually played out (and whether the recommended actions were right)
   improves future action recommendations.

---

## Anti-Patterns

- **Never present a single number as "the forecast"** — Always show the range
- **Never show scenarios without actions** — Every zone needs a "what to do" playbook
- **Never hide the orange and red zones** — If the user only sees green, the sim failed
- **Never skip the failure chains** — "What could go wrong" is half the value
- **Never simulate without sensitivity analysis** — Which variables matter most is
  often more valuable than the forecast itself
- **Never present the devil's advocate as a wall of text** — It must be visual,
  structured, and actionable, not a list of worries

---

## Output Format

All Monte Carlo outputs should be produced as interactive HTML artifacts when the
analysis is substantial (3+ variables, decision-grade). For quick back-of-napkin
estimates (1-2 variables, directional), inline text with the distribution summary
is sufficient.

The HTML report uses the engine's `generate_html_report()` function, which produces
a dark-themed dashboard with the sections described above. The scenario pathway
cards are the centerpiece — they're what make this different from a basic histogram.

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt. License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
