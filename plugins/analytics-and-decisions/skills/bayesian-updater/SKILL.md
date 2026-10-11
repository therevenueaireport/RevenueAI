---
name: bayesian-updater
description: >
  Formal Bayesian belief-updating framework. Applies prior, likelihood, and posterior
  reasoning to business hypotheses, strategic bets, market assumptions, and any situation
  where evidence is accumulating over time. Triggers on: "what should I believe now,"
  "update my thinking," "how does this change things," "given what we just learned,"
  "Bayesian," "prior," "posterior," "what are the odds now," "likelihood," "how confident
  should I be," "I keep seeing signals that," "another data point on," or any situation
  where evidence arrives in sequence and beliefs need calibrated updating. Also trigger
  when making a bet under uncertainty and wanting to formalize confidence rather than
  gut-feel it. Complements ab-test-evaluator for adaptive experimentation.
---

# Bayesian Updater

> Formalize what you believe, quantify how new evidence changes it, and track your confidence over time. Not academic Bayesian statistics — operational belief management for decisions under uncertainty.

---

## Purpose

Revenue leaders make dozens of strategic bets every month — on markets, on messaging, on hires, on product direction, on competitive positioning. Each bet carries an implicit belief: "I think X is true with roughly Y% confidence." New evidence arrives constantly — customer conversations, market data, competitor moves, internal metrics — and that evidence should update those beliefs.

The problem: without a framework, beliefs update inconsistently. Strong priors resist contradictory evidence (confirmation bias). Dramatic single data points get overweighted (anchoring). And no one tracks how much confidence has actually shifted over time.

This skill makes belief-updating explicit, trackable, and honest.

---

## The Bayesian Update Cycle

### Step 1: State the Prior

Before any new evidence, name the belief and its current confidence level.

**Prior specification framework:**

```
Belief: [Clear, falsifiable statement]
Prior confidence: [0-100%]
Prior basis: [What this confidence is based on — data, experience, pattern recognition, gut]
Prior quality: [Strong / Moderate / Weak]
```

**Prior quality definitions:**

| Quality | Basis | How Much Should New Evidence Move You? |
|---|---|---|
| **Strong** | Multiple data sources, direct experience, large samples, validated frameworks | Slowly — it takes substantial contradictory evidence to move a strong prior |
| **Moderate** | Some data, analogous experience, reasonable inference from adjacent domains | Moderately — meaningful evidence in either direction should shift you |
| **Weak** | Gut feel, single anecdote, unfamiliar domain, small sample, secondhand report | Quickly — you don't have much basis, so even modest evidence should update significantly |

**The honesty check**: Most people overrate their prior quality. If the user says "I'm 80% confident" but the basis is two customer conversations and a blog post, the prior quality is Weak — which means the 80% confidence is probably not well-calibrated. Name this directly: calibrated honesty beats false confidence.

### Step 2: Evaluate the New Evidence

When new information arrives, assess it on three dimensions before updating:

**Evidence strength:**
- **Diagnostic power**: How much does this evidence discriminate between the hypothesis being true vs false? Evidence that's equally likely under both scenarios has zero diagnostic power and should move your beliefs minimally.
- **Sample quality**: Is this a rigorous study, a controlled experiment, a representative dataset? Or an anecdote, a self-selected sample, a vendor case study?
- **Independence**: Is this genuinely new information, or is it the same signal repackaged? Three articles citing the same source are one data point, not three.

**Evidence assessment template:**

```
New evidence: [What was observed or learned]
Diagnostic power: [High / Medium / Low] — [why]
Sample quality: [High / Medium / Low] — [why]
Independence: [New signal / Partially redundant / Same source repackaged]
Overall evidence weight: [Strong / Moderate / Weak]
```

### Step 3: Compute the Posterior

Update the belief based on the evidence weight relative to the prior quality.

**Practical update rules** (not formal Bayes' theorem computation — operationally useful heuristics that approximate Bayesian reasoning for business contexts):

| Prior Quality | Evidence Weight | Update Magnitude |
|---|---|---|
| Strong prior | Weak evidence | Minimal shift (1-5 points) |
| Strong prior | Strong evidence | Moderate shift (5-15 points) |
| Weak prior | Weak evidence | Small shift (5-10 points) |
| Weak prior | Strong evidence | Large shift (15-30 points) |
| Moderate prior | Moderate evidence | Moderate shift (5-15 points) |

**Direction**: Evidence consistent with the belief increases confidence. Evidence contradicting it decreases confidence. Evidence orthogonal to it doesn't change confidence but may change the framing of the question.

**Posterior output:**

```
Updated belief: [Same statement — beliefs don't change wording mid-update]
Posterior confidence: [Updated 0-100%]
Shift: [+/- X points from prior]
Shift rationale: [One sentence explaining why this magnitude]
Remaining uncertainty: [What would further increase or decrease confidence]
```

### Step 4: Track the Trajectory

Over time, the sequence of updates tells a story. If a belief has been updated 5 times in the same direction, that's convergence — confidence should be building. If updates oscillate, the signal is noisy and confidence should be moderate regardless of any single data point.

**Belief trajectory pattern:**

```
Belief: [Statement]
Update history:
  1. [Date/context] — Prior: 60% → Evidence: [X] → Posterior: 55% (↓5)
  2. [Date/context] — Prior: 55% → Evidence: [Y] → Posterior: 45% (↓10)
  3. [Date/context] — Prior: 45% → Evidence: [Z] → Posterior: 50% (↑5)
Current confidence: 50%
Trajectory: Oscillating — signal is mixed
Recommendation: [Hold / Act / Investigate further]
```

---

## Decision Thresholds

Not every belief needs to reach 95% confidence before acting. The right threshold depends on the cost of being wrong and the cost of waiting.

| Decision Type | Act Threshold | Rationale |
|---|---|---|
| Reversible, low-cost | 55-60% | Cheap to try, cheap to undo. Bias toward action. |
| Reversible, moderate-cost | 65-70% | Worth a meaningful bet, but keep the escape hatch. |
| Irreversible, high-cost | 80-85% | Hire, major investment, strategic pivot. Need high confidence. |
| Irreversible, existential | 90%+ | Company-defining bets. Demand convergent evidence from independent sources. |

When the user is deciding *whether to act*, map the decision type to the threshold. If current confidence exceeds the threshold, recommend action. If it doesn't, name specifically what evidence would get it there.

---

## Cognitive Bias Countermeasures

The Bayesian framework is only as good as the honesty of the inputs. These biases corrupt the update process:

### Confirmation Bias
**The trap**: Overweighting evidence that confirms existing beliefs, underweighting evidence that contradicts them.
**The countermeasure**: For every confirming data point, explicitly ask: "What would I expect to see if my belief were WRONG? Is that what I'm seeing?" If the evidence is equally consistent with both hypotheses, it has low diagnostic power and shouldn't move confidence much.

### Anchoring
**The trap**: The first number or estimate encountered disproportionately influences all subsequent updates.
**The countermeasure**: When stating priors, name the anchor explicitly. "My prior of 70% is anchored to [specific source]. If I hadn't seen that source, I'd probably be at [different number]." This makes the anchor visible and challengeable.

### Base Rate Neglect
**The trap**: Ignoring how common or rare something is in the general population when evaluating specific evidence.
**The countermeasure**: Always start with the base rate. "Before considering any specific evidence, how common is this outcome in the reference class?" Then update from there.

### Narrative Seduction
**The trap**: A compelling story makes the hypothesis feel more probable than the data warrants.
**The countermeasure**: Separate the quality of the narrative from the quality of the evidence. A beautifully told case study is still n=1.

---

## Output Modes

### Quick Update (conversational)

When the user mentions a new data point in passing and the belief update is straightforward:

**Pattern**: "That moves my confidence on [belief] from roughly [X]% to [Y]%. The evidence is [strong/moderate/weak] because [reason]. Still [above/below] the threshold to [act/change course]."

### Formal Update (structured)

When the user asks to formally track or pressure-test a belief:

Use the full Prior → Evidence → Posterior → Trajectory structure from the cycle above.

### Decision Gate

When confidence has crossed (or is approaching) an action threshold:

**Pattern**: "On [belief], we've accumulated [N] updates over [timeframe], and confidence has converged to [X]%. Given this is a [decision type] decision with an act threshold around [Y]%, I recommend [act/hold/investigate]. The remaining risk is [specific uncertainty]. To close that gap, we'd need [specific evidence]."

---

## Integration

- **statistical-reasoning**: The core framework. Bayesian updater goes deep on belief tracking; statistical-reasoning provides the lenses for evaluating whether evidence is trustworthy in the first place.
- **ab-test-evaluator**: Frequentist experiments produce point-in-time pass/fail results. Bayesian updater is the complement for situations where evidence arrives sequentially and the user wants to track belief evolution rather than wait for a fixed-horizon test.
- **monte-carlo**: When a belief reaches actionable confidence, Monte Carlo can model the range of outcomes if the user acts on it. Bayesian updater says "I'm 75% confident this is true." Monte Carlo says "If it's true, here's the distribution of what happens next."
- **data-claims-auditor**: When evaluating third-party claims, the auditor assesses evidence quality. Those quality ratings feed directly into the Bayesian update as evidence weight.
- **Calibration log**: Track calibration over time. When beliefs that were held at 80% confidence turn out wrong, that's a signal that the user's (or the team's) confidence calibration needs adjustment.

---

## Calibration Note

Perfect Bayesian reasoning is computationally intractable for real-world business decisions with dozens of variables. This skill uses calibrated heuristics — the update magnitudes, the quality categories, the threshold tables — that approximate Bayesian reasoning in a practically useful way. The precision is in the structure and honesty of the process, not in the decimal points of the numbers.

The goal: the user's beliefs become more accurate over time because the updating process is disciplined, the evidence is evaluated rigorously, and the biases are named and countered.

---

*Beliefs should update like a thermostat — responding to real signals, not overreacting to noise, and converging toward truth over time.*

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt. License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
