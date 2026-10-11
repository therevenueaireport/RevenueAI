---
name: ab-test-evaluator
description: >
  Full-protocol A/B test and experiment evaluation skill. Use whenever designing, running,
  or evaluating any controlled experiment — A/B tests, multivariate tests, marketing
  experiments, sales methodology comparisons, enablement program pilots, or product feature
  tests. Triggers on: "A/B test," "experiment," "test results," "control group," "variant,"
  "statistical significance," "sample size calculation," "power analysis," "is this result
  significant," "how long should we run this test," "did this actually work," "split test,"
  "holdout," "lift," or any scenario comparing two or more approaches with data. Also trigger
  when someone presents experiment results that need methodology validation. Works alongside
  statistical-reasoning (core) and hands off to bayesian-updater for adaptive experiments.
---

# A/B Test Evaluator

> The full experiment protocol — from design through analysis to decision. Not just "is it significant?" but "was the experiment designed to answer the right question, and can we trust the answer it gave?"

---

## Purpose

Most A/B tests in GTM organizations are poorly designed, prematurely stopped, or incorrectly interpreted. The three most common failure modes:

1. **Underpowered tests**: Sample too small to detect the effect that matters. The test "fails" not because the intervention didn't work, but because the experiment couldn't detect it. (Type II error.)
2. **Peeking**: Checking results daily and stopping when p < 0.05. This inflates false positive rates dramatically — a test checked 10 times has roughly a 30% false positive rate, not 5%.
3. **Wrong metric**: Optimizing for a proxy metric (clicks) that doesn't connect to the business outcome (revenue). The test "succeeds" but the business doesn't move.

This skill prevents all three.

---

## Phase 1: Experiment Design

Before any test runs, answer these questions. If they can't be answered, the experiment isn't ready.

### 1.1 Hypothesis Specification

Frame the experiment as a formal hypothesis — not "let's see what happens."

- **Null hypothesis (H₀)**: The intervention has no effect on the primary metric. (Always the default.)
- **Alternative hypothesis (H₁)**: The intervention changes the primary metric by [direction and minimum meaningful magnitude].
- **Primary metric**: One metric. Not three. The ONE metric the decision hinges on.
- **Guardrail metrics**: Secondary metrics that must NOT degrade. (e.g., testing a new pricing page for conversion rate, with guardrails on average deal size and support ticket volume.)

**Why one primary metric matters**: Multiple primary metrics require multiple comparison corrections, which reduces power. Pick the one that matters most. Everything else is a guardrail or an exploratory metric.

### 1.2 Minimum Detectable Effect (MDE)

The MDE is the smallest effect worth detecting — not the effect you hope to see, but the smallest effect that would change your decision.

Ask the user: "If this intervention improved [metric] by X%, would you actually change anything? What about X/2%?" The answer defines the MDE.

Setting MDE too small requires enormous sample sizes. Setting it too large risks missing real effects. The right MDE is a business question, not a statistics question.

### 1.3 Power Analysis & Sample Size

Calculate the required sample size BEFORE the test starts. The inputs:

- **Baseline rate**: Current performance on the primary metric
- **MDE**: From step 1.2
- **Significance level (α)**: Usually 0.05. For high-stakes or multiple-test environments, consider 0.01.
- **Power (1 - β)**: Usually 0.80. For critical decisions, target 0.90.

**Sample size formula context**:
- For proportions (conversion rates, win rates): n per group ≈ 16 × (p)(1-p) / MDE²  (at α=0.05, power=0.80)
- For continuous metrics (revenue, deal size): n per group ≈ 16 × σ² / MDE²

If the required sample size is larger than what's available in a reasonable timeframe, the options are: accept a larger MDE, accept lower power, or acknowledge the test can't answer the question at the desired precision. Do NOT run an underpowered test and pretend the results are conclusive.

### 1.4 Duration Estimate

Sample size ÷ daily traffic rate = minimum runtime. Then add:

- **Full business cycle coverage**: Minimum one full week to capture day-of-week effects. For B2B with monthly cycles, longer.
- **Novelty/primacy effects**: New UI elements get extra attention initially. Plan a burn-in period or holdout window.
- **Pre-commit the runtime**: Write it down before launching. "We will run for [X] days and analyze on [date]." No peeking with intent to stop.

---

## Phase 2: During the Experiment

### 2.1 Monitoring (Not Peeking)

There's a difference between monitoring for data quality issues and peeking at results to decide whether to stop.

**Acceptable monitoring:**
- Sample Ratio Mismatch (SRM): Are the groups balanced? A significant imbalance in group sizes signals a randomization bug. Check this early.
- Data pipeline health: Are events logging correctly? Any outages or tracking failures?
- Guardrail alerts: If a guardrail metric moves beyond a pre-set threshold, investigate (but this is a safety check, not a success check).

**Not acceptable:**
- Checking the primary metric p-value daily and stopping when it crosses 0.05
- Reporting "trending toward significance" to stakeholders mid-test
- Adding more variants mid-test without adjusting the analysis plan

### 2.2 Sequential Testing (When Continuous Monitoring Is Required)

If the business genuinely needs the ability to stop early (e.g., a test that might be actively harming revenue), use a sequential testing framework that controls for multiple looks:

- **Alpha spending functions** (O'Brien-Fleming, Pocock): Pre-allocate the significance budget across planned interim analyses
- **Always-valid p-values / confidence sequences**: Modern methods that allow continuous monitoring without inflating false positives

If sequential testing isn't being used, the rule is simple: don't look until the pre-committed end date.

---

## Phase 3: Analysis

### 3.1 Pre-Analysis Checklist

Before computing any test statistic:

- [ ] Confirm sample sizes match expectations from power analysis
- [ ] Check for Sample Ratio Mismatch (chi-square test on group sizes)
- [ ] Verify no data quality issues during the test window
- [ ] Confirm the analysis plan hasn't changed since the test launched

### 3.2 Primary Metric Analysis

**Report all of these — not just the p-value:**

| Element | What It Tells You |
|---|---|
| **Point estimate** | The observed difference (absolute and relative) |
| **Confidence interval** | The range of plausible true effects |
| **P-value** | Probability of seeing this result if the null is true |
| **Effect size** | Practical magnitude of the difference |
| **Power achieved** | Given the observed variance and sample size, what was the actual power? |

**Interpreting the results:**

- **Significant + large effect**: Act on it. The intervention works and the magnitude justifies the cost.
- **Significant + tiny effect**: The intervention "works" but may not be worth the implementation cost. Run the cost-benefit analysis.
- **Not significant + adequate power**: The intervention likely doesn't have a meaningful effect. Accept the null.
- **Not significant + low power**: Inconclusive. The test couldn't answer the question. This is NOT evidence that the intervention doesn't work — it's evidence that the experiment was too small. Say so directly.

### 3.3 Guardrail Metrics

Evaluate each guardrail independently. A test that lifts the primary metric but degrades a guardrail needs a judgment call, not a formula. Surface the tradeoff to the user with the numbers on both sides.

### 3.4 Segment Analysis (Exploratory Only)

Post-hoc segmentation (did the treatment work better for enterprise vs SMB?) is exploratory, not confirmatory. Any "discoveries" from segment analysis need to be validated in a follow-up test. Label them clearly as hypotheses, not conclusions.

---

## Phase 4: Decision & Documentation

### 4.1 Decision Framework

| Result | Recommendation |
|---|---|
| Clear win (significant, meaningful effect, no guardrail damage) | Ship it. Document the expected impact. |
| Marginal win (significant but small, or guardrail concerns) | Quantify the tradeoff. Let the decision-maker decide based on strategic priorities. |
| Inconclusive (not significant, underpowered) | Do NOT declare "no effect." Name it as inconclusive. Recommend retest with adequate power or accept the uncertainty. |
| Clear loss (significant negative effect) | Kill it. Document the learning. |

### 4.2 Documentation Template

Every completed test should produce a brief record:

```
## Experiment: [Name]
- Hypothesis: [H₁ in plain language]
- Primary metric: [metric] | Baseline: [X] | MDE: [Y]
- Duration: [dates] | Sample: [n per group]
- Result: [Win / Loss / Inconclusive]
- Effect: [point estimate] [95% CI]
- Guardrails: [all clear / concerns noted]
- Decision: [Ship / Kill / Retest]
- Key learning: [one sentence]
```

---

## Common Traps This Skill Prevents

1. **"We ran the test and it's significant!"** → But was the test powered correctly? Did you peek? What's the effect size?
2. **"The test didn't work, the intervention failed."** → Was the test powered to detect the MDE? If not, the test failed, not the intervention.
3. **"Let's just run it for a week and see."** → A week of what volume? What effect are you trying to detect? Without a power analysis, you're flipping coins.
4. **"We found that enterprise customers responded better."** → Post-hoc segmentation is hypothesis generation, not confirmation. Label it as such.
5. **"It's p = 0.06, almost significant."** → There is no "almost." The pre-set threshold is the threshold. If the result is close, the right answer is "inconclusive, consider a larger replication."

---

## Integration

- **statistical-reasoning**: The core framework. A/B test evaluator is the specialized deep-dive when the core skill identifies an experiment that needs full protocol treatment.
- **bayesian-updater**: When you want to run adaptive experiments or update beliefs iteratively (rather than fixed-horizon frequentist testing), hand off to bayesian-updater.
- **metric-health-dashboard**: The ongoing monitoring layer. A/B tests produce point-in-time results; metric-health-dashboard tracks whether the effect persists post-ship.
- **Experiment log**: Keep a running record of experiment patterns — common power shortfalls, typical MDEs by metric type, recurring design mistakes — so future experiment design starts from better priors.

---

*A well-designed experiment is the only reliable way to know if something works. This skill makes sure the experiment is actually well-designed.*

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt.*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
