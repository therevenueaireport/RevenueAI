---
name: metric-health-dashboard
description: >
  Ongoing metric instrumentation, statistical process control, and anomaly detection skill.
  Designs and evaluates measurement systems — determining which leading and lagging indicators
  to track, whether metrics are healthy or drifting, and when a change is real signal vs.
  normal variance. Triggers on: "are these the right metrics," "what should I be tracking,"
  "is this metric healthy," "why isn't this moving," "anomaly," "something looks off,"
  "metric dashboard," "leading indicators," "lagging indicators," "KPI framework," "scorecard,"
  "statistical process control," "control chart," "normal variance," "is this change real,"
  "our metric dropped/spiked," "set up tracking for," "instrument this," "how do I measure
  if X is working," or any ongoing measurement and monitoring question. Complements
  ab-test-evaluator (point-in-time experiments) with continuous monitoring.
---

# Metric Health Dashboard

> Not a literal dashboard — a reasoning framework for designing measurement systems, evaluating metric health, and distinguishing signal from noise in ongoing data. The skill that answers: "Are we measuring the right things, and is what we're seeing real?"

---

## Purpose

Every initiative you run — a product launch, a GTM motion, an enablement program, client work — requires measurement. The three failure modes this skill prevents:

1. **Measuring the wrong things**: Tracking vanity metrics (page views) instead of value metrics (pipeline generated). Activity instead of outcomes. Lagging indicators without the leading indicators that predict them.

2. **No baseline, no context**: A metric without a baseline is just a number. "Our NPS is 42" means nothing until you know what it was before, what the industry range is, and what the variance looks like.

3. **Overreacting to noise**: A metric drops 10% in a week. Is it a crisis or Tuesday? Without understanding normal variance, every fluctuation triggers a fire drill. Statistical process control prevents this.

---

## Framework 1: Metric System Design

Use when you are setting up measurement for a new initiative, program, or business function.

### The Metric Hierarchy

Every well-instrumented initiative has four layers:

```
Layer 1: North Star Metric
  └── The ONE metric that defines success for this initiative

Layer 2: Input Metrics (Leading Indicators)
  └── Metrics that PREDICT movement in the North Star
  └── These are the levers — change these to change the North Star

Layer 3: Health Metrics (Guardrails)
  └── Metrics that must NOT degrade while optimizing the North Star
  └── These are the constraints — protect these while pushing the North Star

Layer 4: Diagnostic Metrics (Troubleshooting)
  └── Metrics you don't track daily but investigate when something breaks
  └── These explain WHY a higher-level metric moved
```

### Designing the Hierarchy

**Step 1: Name the North Star**

The North Star must be:
- **Outcome-oriented**: Measures value delivered, not activity performed
- **Influenceable**: The team can actually affect it through their work
- **Measurable**: Can be quantified reliably with current instrumentation
- **Timely**: Updates frequently enough to be useful for decisions

Bad North Stars: revenue (too lagging, too many confounders), NPS (infrequent, hard to attribute), "brand awareness" (unmeasurable in real-time).

Good North Stars: qualified pipeline generated, activation rate within 14 days, net revenue retention, time-to-first-value.

**Step 2: Identify Input Metrics**

Input metrics are the leading indicators — things that move BEFORE the North Star moves. They answer: "What behaviors and activities predict success?"

The test: "If this input metric improves, do we have a causal or strong correlational basis for believing the North Star will follow?" If the answer is "maybe" or "we hope so," it's not a reliable input metric.

**Common input metric patterns by domain:**

| Domain | North Star | Typical Input Metrics |
|---|---|---|
| Sales pipeline | Qualified pipeline ($) | Outbound activity volume, meeting conversion rate, ICP fit score |
| Marketing | Marketing-sourced pipeline | Content engagement → MQL conversion, paid channel efficiency, organic search visibility |
| Product adoption | Monthly active usage | Onboarding completion rate, feature activation within 7 days, support ticket volume (inverse) |
| Enablement | Quota attainment change | Training completion, coaching session frequency, skill assessment scores, time-to-first-deal post-training |
| Customer success | Net revenue retention | Health score, product usage depth, QBR completion, expansion opportunity identification rate |

**Step 3: Set Guardrails**

Guardrails prevent optimization tunnel vision. For every North Star push, ask: "What could break if we push too hard on this?"

Examples:
- Pushing pipeline volume → guardrail on deal quality (avg deal size, win rate)
- Pushing activation speed → guardrail on support ticket volume
- Pushing content volume → guardrail on engagement rate per piece
- Pushing outbound volume → guardrail on response rate, unsubscribe rate

**Step 4: Pre-specify Diagnostic Metrics**

You don't track these on a dashboard. You investigate them when a higher-level metric moves unexpectedly.

The diagnostic question: "If the North Star drops 15%, what would I look at first, second, and third to figure out why?"

Map the diagnostic tree in advance so the investigation is structured, not panicked.

---

## Framework 2: Baseline & Context Establishment

A metric is useless without context. Before tracking begins (or when evaluating an existing metric system), establish:

### Baseline Measurement

- **Historical baseline**: What has this metric done over the last 3, 6, 12 months? Calculate mean, median, standard deviation, and range.
- **Trend direction**: Is the baseline stable, trending up, or trending down? A "drop" from an uptrend is different from a drop from a stable baseline.
- **Seasonality**: Does this metric have weekly, monthly, quarterly, or annual patterns? Pipeline is seasonal. Web traffic has day-of-week effects. Ignoring seasonality guarantees false alarms.

### Variance Profile

Understanding normal variance is the foundation of signal detection.

- **Standard deviation**: How much does this metric typically fluctuate period-over-period?
- **Coefficient of variation (CV)**: Standard deviation ÷ mean. A CV of 0.1 means the metric is relatively stable. A CV of 0.5 means it's highly volatile. High-CV metrics need wider control limits before flagging anomalies.
- **Distribution shape**: Is the metric normally distributed, skewed, or multimodal? This affects which statistical process control rules apply.

### External Context

- **Industry benchmarks**: Where does this metric sit relative to industry norms? (Apply data-claims-auditor to any benchmark before trusting it.)
- **Peer comparisons**: If available, how does this metric compare to similar companies, teams, or cohorts?
- **Market context**: Are external factors (economic conditions, competitive moves, regulatory changes) likely to affect this metric regardless of internal actions?

---

## Framework 3: Statistical Process Control (SPC)

SPC is the discipline of distinguishing between **common cause variation** (normal fluctuations inherent in any process) and **special cause variation** (signals that something has genuinely changed).

### Control Chart Logic

A control chart plots a metric over time with three lines:

- **Center line**: The mean (or median for skewed data)
- **Upper Control Limit (UCL)**: Typically mean + 2-3 standard deviations
- **Lower Control Limit (LCL)**: Typically mean - 2-3 standard deviations

Points within the control limits represent normal variation. Points outside represent potential signals worth investigating.

### Detection Rules

**Standard Western Electric rules for identifying special cause variation:**

| Rule | Pattern | What It Signals |
|---|---|---|
| **Rule 1** | Single point beyond 3σ | Extreme outlier — investigate immediately |
| **Rule 2** | 2 of 3 consecutive points beyond 2σ (same side) | Emerging shift — early warning |
| **Rule 3** | 4 of 5 consecutive points beyond 1σ (same side) | Sustained drift — the process may be changing |
| **Rule 4** | 8+ consecutive points on the same side of the center line | Level shift — the baseline has moved |
| **Rule 5** | 6+ consecutive points trending in the same direction | Trend — something is driving directional change |

### Applying SPC to Business Metrics

Most business teams don't use SPC — they react to every week-over-week change as if it's meaningful. SPC provides the framework to ask: "Is this movement outside what I'd expect from normal variance?"

**Example application**:

```
Metric: Weekly qualified pipeline ($)
Historical mean: $180K/week
Standard deviation: $35K/week
Control limits: $110K (LCL) — $250K (UCL)

This week: $140K
Assessment: Within control limits. This is normal variance — not a crisis.
No action required unless subsequent weeks trigger Rule 3 or Rule 4.
```

vs.

```
This week: $95K
Assessment: Below LCL (Rule 1 triggered). This is a special cause signal.
Investigate: Check deal slippage, pipeline source mix, rep activity levels.
```

---

## Framework 4: Anomaly Assessment

When a metric moves unexpectedly, run this assessment before sounding the alarm.

### The Anomaly Checklist

1. **Data quality check**: Is the data correct? Tracking bugs, missing data, changed definitions, and pipeline updates are the most common "anomalies" that aren't real. Check this first — always.

2. **Seasonality check**: Is this movement consistent with known seasonal patterns? Compare to the same period last year, not just last week.

3. **SPC check**: Does this trigger any of the Western Electric rules, or is it within normal variance?

4. **Confounder check**: Did anything else change during this period? New product launch, pricing change, team restructure, major holiday, competitor move? Coincident changes make attribution uncertain.

5. **Magnitude check**: Even if the movement is real, is it large enough to matter? Apply the effect size lens from statistical-reasoning. A statistically detectable shift that's practically irrelevant doesn't warrant action.

### Anomaly Assessment Output

```
## Anomaly Assessment: [Metric Name]

Observed change: [What happened — absolute and percentage]
Period: [Timeframe]
SPC status: [Within limits / Rule triggered — specify which]

### Root Cause Investigation
- Data quality: [Clean / Suspect — why]
- Seasonality: [Consistent with pattern / Inconsistent]
- Concurrent changes: [List any confounders]
- Leading indicator signals: [Did input metrics predict this?]

### Assessment
- Signal probability: [High / Moderate / Low — i.e., how likely this is a real change vs. noise]
- Magnitude significance: [Practically meaningful / Detectable but minor]
- Recommended response: [Investigate further / Monitor next period / Take action / No action needed]
```

---

## Framework 5: Metric System Audit

Use when evaluating whether an existing measurement system is adequate. Run this audit when you inherit a metric system, when results aren't moving despite activity, or when there's a suspicion that the wrong things are being tracked.

### Audit Dimensions

| Dimension | Question | Red Flag |
|---|---|---|
| **Completeness** | Are all four layers present (North Star, Input, Guardrail, Diagnostic)? | Missing leading indicators — only tracking lagging outcomes |
| **Causal chain** | Do input metrics actually predict the North Star? | Tracking activity (emails sent) not outcomes (meetings booked) |
| **Baseline** | Does every metric have a documented baseline? | No baseline — can't determine if movement is meaningful |
| **Variance** | Is normal variance understood for each key metric? | Every fluctuation triggers a fire drill |
| **Timeliness** | Do metrics update frequently enough for decisions? | Quarterly NPS driving weekly decisions |
| **Attribution** | Can metric movements be attributed to specific actions? | Multiple initiatives running simultaneously with no controls |
| **Incentive alignment** | Do metrics reward the behavior you actually want? | Measuring meetings-booked incentivizes low-quality meetings |
| **Gaming resistance** | Can metrics be gamed without delivering real value? | Reps gaming activity metrics without pipeline impact |

### Audit Output

```
## Metric System Audit: [Initiative/Function]

Overall health: [Well-instrumented / Partially instrumented / Under-instrumented]

### Strengths
[What's working in the current measurement system]

### Gaps
[Missing layers, broken causal chains, absent baselines]

### Recommendations (prioritized)
1. [Highest impact fix]
2. [Second priority]
3. [Third priority]

### Quick Win
[One thing that can be implemented this week to improve measurement]
```

---

## Integration

- **statistical-reasoning**: The core reasoning overlay. Metric health dashboard applies statistical thinking specifically to ongoing measurement systems and monitoring.
- **ab-test-evaluator**: A/B tests are point-in-time experiments. Metric health dashboard is the continuous monitoring layer that tracks whether experiment results persist post-implementation.
- **bayesian-updater**: Metric trends over time are evidence that should update beliefs. A metric consistently trending in one direction is a Bayesian update on the health of the underlying initiative.
- **enablement-measure**: Enablement-measure is specifically scoped to training and coaching program measurement. Metric health dashboard covers broader business metric instrumentation. They share the leading/lagging indicator architecture but apply it to different domains.
- **monte-carlo**: When metric trends suggest multiple possible futures, Monte Carlo models the range of outcomes. Metric health dashboard identifies the trend; Monte Carlo projects where it leads.

---

*You can't manage what you don't measure — but you also can't manage what you measure wrong. This skill ensures the measurement is right.*

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt.*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
