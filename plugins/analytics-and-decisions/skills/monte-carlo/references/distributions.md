# Distribution Selection Guide

## Why Distributions Matter

The distribution you assign to a variable determines the shape of possible outcomes.
Using the wrong distribution is like using the wrong map — you'll navigate confidently
to the wrong destination.

Rule of thumb: when in doubt, use a triangular distribution (min, mode, max). It's
intuitive, easy to parameterize, and better than a normal distribution for most
business variables.

---

## Distribution Catalog

### Normal (Gaussian)
**Shape:** Symmetric bell curve around the mean
**Use when:** Variable is the sum of many small independent factors
**Business examples:** Daily website traffic (large sites), aggregated monthly revenue (stable business)
**Parameters:** mean, standard deviation
**Caution:** Rarely appropriate for business metrics — most business variables are skewed.
Real-world things go wrong more dramatically than they go right.

### Triangular
**Shape:** Triangle defined by min, mode (most likely), max
**Use when:** You have a gut estimate (mode) and can bound the range
**Business examples:** Campaign conversion rates, project timelines, sales cycle length
**Parameters:** min, mode, max
**Best default choice for most business modeling.** Easy to elicit from stakeholders.

### Log-Normal
**Shape:** Right-skewed — long tail on the positive side
**Use when:** Variable is always positive and has occasional large outliers
**Business examples:** Revenue per deal, content virality (most posts normal, some explode),
customer lifetime value, time-to-close
**Parameters:** mean of log, std dev of log (or convert from desired mean/std)
**Use this for anything involving money or engagement — these are almost always right-skewed.**

### Beta
**Shape:** Flexible — can be symmetric, left-skewed, or right-skewed, bounded [0,1]
**Use when:** Variable is a rate or percentage
**Business examples:** Conversion rate, open rate, click-through rate, win rate
**Parameters:** alpha, beta (derived from mean and sample size)
**The correct distribution for rates.** If you have a 3% conversion rate from 500 trials,
use Beta(15, 485) — it captures the uncertainty from sample size.

### Uniform
**Shape:** Flat — every value equally likely between min and max
**Use when:** You truly have no idea, just bounds
**Business examples:** Almost never appropriate for real analysis. Use triangular instead.
**Parameters:** min, max
**The "I give up" distribution.** If you find yourself using this, you need more data.

### Poisson
**Shape:** Discrete, right-skewed for low rates
**Use when:** Counting events per time period
**Business examples:** Support tickets per day, inbound leads per week, bugs per sprint
**Parameters:** lambda (average rate)

### Exponential
**Shape:** Right-skewed, memoryless
**Use when:** Modeling time between events
**Business examples:** Time between customer purchases, time between inbound leads
**Parameters:** lambda (rate = 1/mean)

### PERT (Modified Triangular)
**Shape:** Like triangular but with more weight near the mode
**Use when:** Same as triangular but you're more confident in the mode
**Business examples:** Project duration estimates, cost estimates
**Parameters:** min, mode, max (internally weighted 4x toward mode)
**Good alternative to triangular when your mode estimate is data-backed.**

---

## Decision Framework: Which Distribution?

```
Is it a rate/percentage (0-100%)?
  → Beta distribution

Is it always positive and could have rare large values?
  → Log-Normal

Is it a count of events?
  → Poisson

Do you just have min/likely/max estimates?
  → Triangular (weak confidence) or PERT (strong confidence in mode)

Is it truly symmetric with no bounds?
  → Normal (rare in business)

Do you genuinely have no clue?
  → Triangular with wide bounds (NOT uniform)
```

---

## Parameterization Tips

### From Historical Data (Best)
If you have 20+ data points, fit the distribution to the data.
The engine script's `fit_distribution()` function handles this.

### From Logged Performance Data (Good)
If you have logged performance data (dashboards, CRM exports, past prediction logs), extract:
- Mean and standard deviation from logged metrics
- Min and max observed values
- Use these to parameterize Beta (for rates) or Log-Normal (for counts/revenue)

### From Expert Estimates (Acceptable)
Ask the user for three numbers: optimistic, realistic, pessimistic.
Map to: min, mode, max → use Triangular or PERT.

### From Gut Feel (Last Resort)
Use very wide Triangular distributions. Flag the variable as "low confidence"
in the output. This is where the devil's advocate layer is most critical.

---

## Correlation Modeling

Variables are rarely independent. When modeling multiple variables:

### Common Positive Correlations
- Content quality ↔ Engagement rate (better content → more engagement)
- Ad spend ↔ Impressions (more spend → more impressions, diminishing returns)
- Team morale ↔ Output quality (happier team → better work)
- Market conditions ↔ Multiple business metrics (rising tide lifts all boats)

### Common Negative Correlations
- Volume ↔ Quality (more output often → lower per-unit quality)
- Speed ↔ Thoroughness (faster → less careful)
- Price ↔ Conversion rate (higher price → lower conversion, usually)

### How to Handle
Use a correlation matrix in the simulation. The engine script accepts a correlation
matrix parameter. When in doubt, use 0.3 for mild correlation, 0.6 for moderate,
0.8 for strong.

**Devil's advocate note on correlations:** In crisis scenarios, correlations spike.
Things that are mildly correlated in good times become strongly correlated when
things go wrong. The black swan scenario should model correlation = 0.8+ across
all negative variables.
