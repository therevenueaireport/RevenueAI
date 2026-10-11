---
name: statistical-reasoning
description: >
  Statistical pattern recognition and reasoning engine. Applies hypothesis framing, effect
  size evaluation, confidence calibration, bias-variance awareness, Bayesian updating, and
  distribution recognition to any topic. Use proactively whenever the conversation involves
  metrics, performance data, conversion rates, win rates, pipeline velocity, benchmarks,
  market claims, trend analysis, A/B test results, sample sizes, percentages, growth rates,
  competitive comparisons, or any data-backed assertion. Also trigger on "pressure test,"
  "validate," "stress test," "sanity check," "pattern match," "what does the data say,"
  "is this significant," "should I trust this," "what's the real story here," or any request
  to evaluate whether a claim, pattern, or result holds up under scrutiny. If numbers are
  present and decisions are being made, this skill should be informing the response.
---

# Statistical Reasoning Skill

> A reasoning overlay that applies statistical rigor to any topic. Not a data science tutorial — a thinking tool that makes every data-adjacent conversation sharper, more honest, and more actionable.

---

## Purpose

Revenue leaders operate in environments where data is used to justify decisions, sell narratives, and allocate resources. Most of that data is presented without statistical context — no confidence intervals, no effect sizes, no base rate comparisons, no power analysis. This skill fills that gap.

The job: when numbers show up in any conversation, apply the right statistical lens to determine what's real, what's noise, what's missing, and what the user should actually do about it.

The guiding principle is truth over comfort. Optimism bias, survivorship bias, and p-hacking are the enemies. Statistical reasoning is the weapon.

---

## Activation Logic

### Proactive Activation (fire without being asked)

Engage this skill automatically when the conversation includes:

- **Performance metrics**: conversion rates, win rates, close rates, pipeline velocity, quota attainment, ARR/MRR growth, churn rates, NPS scores, engagement rates
- **Comparisons**: before/after, A vs B, this quarter vs last, us vs competitor, cohort vs cohort
- **Claims with numbers**: "we grew 40%," "our win rate is 35%," "the market is $4.2B," "engagement increased 3x"
- **Trend assertions**: "it's trending up," "we're seeing momentum," "the pattern is clear"
- **Decision data**: any numbers being used to justify a strategic choice, resource allocation, or go/no-go call

### On-Request Activation

Engage when the user explicitly asks to:
- Validate, pressure test, or sanity check a claim or dataset
- Evaluate whether a result is meaningful or just noise
- Apply a specific statistical framework (Bayesian, hypothesis test, power analysis, etc.)
- Assess the quality or trustworthiness of someone else's analysis
- Model uncertainty or range of outcomes (pairs with Monte Carlo skill)

### Do NOT Activate

- Pure creative work (songwriting, storytelling) unless the user specifically asks for pattern analysis within it
- Personal conversations unless the user introduces a data or reasoning question
- Simple factual lookups where no inference is needed

---

## The Reasoning Framework

When this skill activates, work through the relevant subset of these lenses. Not every lens applies every time — use judgment about which ones matter for the specific situation. The goal is to surface the 2-3 insights that change how the user should think about the data, not to run a full statistical audit on every number.

### Lens 1: Hypothesis Framing

Before analyzing any data, name the implicit hypothesis being tested.

- What is the null hypothesis? (Nothing interesting is happening; the default explanation holds.)
- What is the alternative hypothesis? (The claim being made or implied.)
- Is the evidence structured to actually test this hypothesis, or is it anecdotal?

Most business conversations skip this step entirely. Naming the hypothesis forces clarity about what would actually constitute evidence — and what wouldn't.

### Lens 2: Sample & Base Rate Check

Ask whether the data is large enough, representative enough, and contextualized enough to support the conclusion.

- **Sample size**: Is n large enough to detect the effect being claimed? A 5-point win rate change measured across 12 deals is noise. Across 1,200 deals, it might be signal.
- **Base rate**: What's the baseline? "30% conversion rate" means nothing without knowing the industry average, historical average, or expected rate. A 30% conversion in enterprise software is outstanding. In e-commerce checkout, it's a disaster.
- **Selection bias**: Who's in the sample? Is it representative of the population being generalized to, or is it cherry-picked (top performers, best quarter, surviving companies)?
- **Survivorship bias**: Are we only looking at the winners? The graveyard of failed companies that did the same thing isn't visible in the dataset.

### Lens 3: Effect Size & Practical Significance

Statistical significance is not the same as practical significance. This lens asks: even if the pattern is real, does it matter?

- **Magnitude**: How big is the effect in real-world terms? A "statistically significant" 0.3% improvement in email open rates is not worth re-architecting the nurture program.
- **Cohen's d equivalent thinking**: Is this a small, medium, or large effect relative to the domain? Frame it in terms the user can act on.
- **Cost-benefit**: Does the size of the effect justify the cost of the action it implies? A real but tiny improvement might not be worth the engineering sprint to implement.

### Lens 4: Confidence & Uncertainty Calibration

Every claim should carry a confidence estimate — not as false precision, but as intellectual honesty about what we know and don't know.

- **Confidence interval thinking**: What's the plausible range around this estimate? A reported "35% win rate" from 50 opportunities has a wide confidence interval. From 5,000 opportunities, it's tight.
- **Bayesian updating**: When new data arrives, how should it update our prior beliefs? If everything we knew before suggested a 25% win rate and one quarter shows 35%, the posterior is probably somewhere between — not an immediate conclusion that "we've improved."
- **Stated confidence**: When delivering analysis, state confidence level explicitly. "High confidence this is a real pattern" vs "Moderate confidence — the signal is there but the sample is thin" vs "Low confidence — this could easily be noise."

### Lens 5: Confounders & Alternative Explanations

Before accepting a causal story, ask what else could explain the pattern.

- **Correlation ≠ causation**: The most abused relationship in business analytics. Two things moving together doesn't mean one causes the other. A third variable (or pure coincidence) might explain both.
- **Confounders**: What variables weren't controlled for? Seasonality, market conditions, team changes, pricing changes, competitive moves — all can masquerade as the effect of an intervention.
- **Regression to the mean**: Extreme performance in one period tends to revert toward average in the next. A "turnaround" after a terrible quarter might just be reversion, not the new strategy working.

### Lens 6: Distribution & Variance Awareness

Not all data is normally distributed. Expert reasoning accounts for the shape of the data.

- **Skewness**: Revenue data, deal sizes, and response times are often right-skewed. Reporting the mean is misleading — the median tells a more honest story.
- **Variance**: Two teams with the same average performance can have wildly different consistency. High variance means the average is less predictive of any individual outcome.
- **Outlier impact**: A single whale deal can move a quarterly average dramatically. Understand whether the pattern holds with and without outliers.

### Lens 7: Multiple Comparisons & Cherry-Picking

When many things are tested or many metrics are tracked, some will look significant by pure chance.

- **The multiple comparisons problem**: Test 20 features and expect 1 false positive at α = 0.05. When someone reports "we found that X works," ask how many things they tested to find that one winner.
- **Narrative cherry-picking**: Selecting the metric that tells the best story while ignoring the ones that don't. If pipeline is up but win rate is down and cycle time is longer — the full picture matters.
- **Time window selection**: Choosing the start and end dates that make the trend look best. Always ask: does this hold across different time windows?

---

## Output Modes

### Quick Read (conversational)

When the data point is simple or the conversation is moving fast, weave the statistical insight into the natural reply. No headers, no framework labels. Just the insight that changes the decision.

**Example pattern**: "That 40% growth number looks strong on the surface, but it's off a small base quarter — we're talking about going from $50K to $70K in pipeline. The percentage is real but the absolute dollar movement is modest. I'd want to see if Q3 holds before calling it a trend."

### Deep Dive (structured)

When the user asks to pressure test, validate, or do serious analysis, use this structure:

```
## Claim Under Test
[State the hypothesis clearly]

## What the Data Shows
[Present the evidence — what's actually there]

## What's Missing
[Gaps in the data — sample size, base rate, confounders, time horizon]

## Statistical Assessment
[Apply the relevant lenses — effect size, confidence, alternative explanations]

## Confidence Level: [High / Moderate / Low]
[One sentence explaining why]

## So What
[The actionable takeaway — what the user should do, decide, or investigate further]
```

### Red Flag Mode

When a number or claim is being used to drive a major decision and the statistical foundation is weak, lead with the concern. Don't bury it. Truth over comfort applies directly here.

**Pattern**: "Before we act on this — [specific concern]. The data shows [what it actually shows], but [what's missing or misleading]. I'd recommend [specific step to de-risk the decision] before committing."

---

## Integration with Other Skills

- **Monte Carlo**: When statistical reasoning identifies uncertainty, hand off to Monte Carlo for scenario modeling. Statistical reasoning diagnoses the uncertainty; Monte Carlo quantifies the range of outcomes.
- **Pattern log**: After any significant statistical analysis, log the pattern for compounding. If certain types of claims keep needing the same correction (e.g., small sample sizes in pipeline reports), that pattern should inform future proactive activation.
- **data-claims-auditor**: When writing newsletters, LinkedIn posts, or reports that cite data, QA the statistical claims before publication. Credibility depends on intellectual rigor — publishing a sloppy data claim damages it.

---

## Calibration Principles

These principles govern how the skill balances rigor with practicality:

1. **Proportional depth**: Match the depth of analysis to the stakes of the decision. A Slack-level question gets a Slack-level answer with the key statistical insight. A board-level decision gets the full framework.

2. **Name the uncertainty, don't hide behind it**: "It depends" is not an answer. "It depends on whether the sample holds across segments — here's how to check" is an answer.

3. **Lead with the actionable insight**: The user doesn't need a statistics lecture. They need to know what the numbers actually mean for the decision in front of them. The statistical reasoning is the engine; the strategic implication is the output.

4. **Healthy skepticism, not cynicism**: The default posture is "trust but verify." Not every number is wrong. The skill's job is to identify which numbers need more scrutiny — not to tear down every data point as insufficient.

5. **Make the invisible visible**: The highest-value move is often surfacing what's NOT in the data — the missing comparison, the unasked question, the confound no one mentioned. This is where statistical reasoning earns its keep.

---

*This skill makes data-driven decisions honest. Every number tells a story — this skill makes sure it's the true one.*

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt. License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
