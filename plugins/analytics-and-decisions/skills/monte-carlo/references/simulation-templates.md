# Simulation Templates

Pre-built variable sets and devil's advocate checklists for common analysis types.
These are starting points — always customize to the specific situation.

---

## Template 1: Content / Audience Growth Projection

**Use when:** Projecting newsletter subscribers, social followers, community members, course enrollments

### Variables
| Variable | Distribution | Typical Range | Notes |
|----------|-------------|---------------|-------|
| Current audience size | Fixed | Actual number | Starting point |
| Organic growth rate (monthly) | Beta | 2-8% | Based on historical or industry |
| Content publishing frequency | Triangular | Min/planned/max per week | Model consistency drops |
| Conversion rate (viewer → subscriber) | Beta | 1-5% | Depends on channel |
| Churn / unsubscribe rate | Beta | 0.5-3% monthly | Often underestimated |
| Viral coefficient | Log-Normal | 0.1-0.5 | How many new people each subscriber brings |
| Platform algorithm factor | Triangular | 0.7-1.3x | Algorithm boost or suppression |

### Devil's Advocate Checklist
- [ ] Have you modeled audience fatigue? Growth rates decline as audience matures
- [ ] What if a platform algorithm change cuts organic reach by 40%?
- [ ] What if a competitor enters your niche and splits attention?
- [ ] Are you accounting for seasonality? (Summer slumps, holiday spikes)
- [ ] What if your content production drops by 50% for 2 months? (Health, travel, competing priorities)
- [ ] Is your churn rate based on enough data or just the honeymoon period?

### Correlated Risks
- Publishing frequency drop → growth rate drop (less content = less discovery)
- Algorithm suppression → churn increase (less visibility = subscribers forget you exist)

---

## Template 2: Campaign ROI Modeling

**Use when:** Evaluating paid campaigns, product launches, promotional initiatives

### Variables
| Variable | Distribution | Typical Range | Notes |
|----------|-------------|---------------|-------|
| Total campaign spend | Fixed or Triangular | Budget ± 10% | Include hidden costs |
| Impressions / reach | Log-Normal | Based on spend level | Platform-specific |
| Click-through rate | Beta | 0.5-3% | Highly variable by channel |
| Landing page conversion | Beta | 1-10% | Depends on offer/audience fit |
| Average deal value | Log-Normal | Historical range | Right-skewed |
| Sales cycle length (days) | Log-Normal | 14-90 | Longer = more uncertainty |
| Close rate (from qualified lead) | Beta | 10-40% | Depends on lead quality |
| Customer acquisition cost | Derived | Spend / Customers | Calculated, not input |

### Devil's Advocate Checklist
- [ ] Is your conversion rate from a similar audience, or are you extrapolating?
- [ ] What if ad costs increase 30% mid-campaign? (Platform auction dynamics)
- [ ] What if your best performing creative fatigues after week 2?
- [ ] Are you accounting for the leads that never close? (Pipeline leakage)
- [ ] What's the opportunity cost of this spend? What else could it fund?
- [ ] If the campaign underperforms by 50%, can you pivot or are you locked in?
- [ ] Are you measuring incrementality or just attribution? (Would some of these sales happen anyway?)

### Correlated Risks
- Higher spend → higher CPM (diminishing returns at scale)
- Lower lead quality → longer sales cycle AND lower close rate
- Market downturn → lower deal values AND longer cycles simultaneously

---

## Template 3: Revenue / Financial Forecasting

**Use when:** Projecting quarterly/annual revenue, evaluating pricing changes, modeling new revenue streams

### Variables
| Variable | Distribution | Typical Range | Notes |
|----------|-------------|---------------|-------|
| Active pipeline value | Fixed | Current CRM data | Starting point |
| New pipeline creation rate (monthly) | Log-Normal | Historical ± variance | |
| Win rate | Beta | Historical rate | By segment if possible |
| Average contract value | Log-Normal | Historical range | |
| Sales cycle length | Log-Normal | Historical range | |
| Churn / contraction rate | Beta | 5-15% annually | Existing revenue at risk |
| Expansion rate | Beta | 5-20% annually | Upsell/cross-sell on base |
| Seasonal factor | Triangular by quarter | 0.8-1.2x | Q4 often strongest |

### Devil's Advocate Checklist
- [ ] Is your pipeline real or inflated? (Pipeline hygiene audit)
- [ ] What if your top 3 deals all slip to next quarter?
- [ ] What happens if a key competitor drops prices 20%?
- [ ] Are you modeling the deals you'll lose, not just the ones you'll win?
- [ ] What if hiring takes 2 months longer than planned? (Capacity constraint on sales)
- [ ] Is your expansion rate sustainable or driven by one-time factors?
- [ ] What's the concentration risk? (If top 2 customers churn, what happens?)

### Correlated Risks
- Economic downturn → lower win rate + longer cycle + smaller deals simultaneously
- Key employee departure → pipeline creation AND close rate both drop
- Competitor funding round → price pressure + longer evaluations

---

## Template 4: Enablement Program Impact

**Use when:** Modeling expected outcomes of a training/coaching program

### Variables
| Variable | Distribution | Typical Range | Notes |
|----------|-------------|---------------|-------|
| Program enrollment rate | Beta | 60-95% | Voluntary vs mandatory matters |
| Completion rate | Beta | 40-85% | Biggest variance driver |
| Knowledge retention (30-day) | Beta | 30-70% | Almost always overestimated |
| Behavior change rate | Beta | 15-40% | The hard part |
| Performance impact per changed behavior | Triangular | 5-25% improvement | Metric-specific |
| Time to competency (weeks) | Log-Normal | 4-16 | Depends on complexity |
| Manager reinforcement factor | Triangular | 0.5-2.0x | Multiplier on behavior change |
| Regression rate (monthly) | Beta | 5-15% | Skills decay without practice |

### Devil's Advocate Checklist
- [ ] Is completion rate based on similar programs or wishful thinking?
- [ ] What if managers don't reinforce? (Manager factor drops to 0.5x)
- [ ] Are you measuring actual behavior change or just satisfaction scores?
- [ ] What if 30% of participants are at the wrong LOPAFT level for this content?
- [ ] Is there a competing initiative that will distract from this program?
- [ ] What's the cost of doing nothing? (Baseline isn't always flat — it might be declining)
- [ ] Are you accounting for the observer effect? (Improvement during observation that fades)

### Correlated Risks
- Low manager reinforcement → high regression rate (the #1 program killer)
- Wrong LOPAFT level → low completion AND low behavior change
- Competing priorities → low enrollment AND low engagement simultaneously

---

## Template 5: Pricing / Packaging Sensitivity

**Use when:** Evaluating price changes, new tier structures, or bundling strategies

### Variables
| Variable | Distribution | Typical Range | Notes |
|----------|-------------|---------------|-------|
| Current conversion rate | Beta | Historical data | Baseline |
| Price elasticity | Triangular | -0.5 to -2.0 | How sensitive is demand to price? |
| Competitive price point | Triangular | Market research | Anchoring effect |
| Perceived value score | Triangular | 1-10 | Survey or inferred |
| Willingness to pay | Log-Normal | Survey data | Right-skewed |
| Switching cost factor | Triangular | 0.1-0.9 | Higher = more lock-in |
| Volume at new price | Derived | Elasticity model | Calculated |
| Revenue at new price | Derived | Volume × Price | The answer |

### Devil's Advocate Checklist
- [ ] Is your elasticity estimate based on actual data or theory?
- [ ] What if competitors match your price change within 30 days?
- [ ] Are you accounting for the signaling effect? (Price = quality perception)
- [ ] What's the churn risk from existing customers at the new price?
- [ ] Have you modeled the transition period? (Short-term pain vs long-term gain)
- [ ] Is your willingness-to-pay data from the right customer segment?

---

## Using Templates with Historical Data

When you have accumulated enough data points for a given metric:

1. Pull historical metrics from your system of record (CRM, analytics, past logs)
2. Fit distributions to actual observed data (not guesses)
3. Identify which variables have high vs low certainty from the observed spread
4. Run the simulation with data-backed distributions
5. Compare the simulation output to the next batch of actuals
6. Log the calibration result back to `monte-carlo-predictions.md`

Over time, this creates a virtuous cycle:
- More data → better distributions → more accurate simulations → better decisions
- Better decisions → better outcomes → more data (and the loop compounds)
