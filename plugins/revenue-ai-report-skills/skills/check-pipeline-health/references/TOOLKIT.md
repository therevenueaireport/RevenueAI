# Pipeline Health Toolkit: Export Checklist, Coverage Math, Leak Finder, and the Weekly Inspection List

**Use this file when:**
- A quarter or half is starting and you need to know, with math, whether the pipeline can carry the number.
- The forecast says yes and the pipeline looks thin, or the reverse, and you need to know which is lying.
- You are about to commit a number to the board and want the assumptions written down first.
- You have an AI-drafted pipeline read and need to check it used your numbers, not industry ratios.

The SKILL.md holds the process and the decision rules. This file holds the instruments.

---

## 1. The Sequence

| Step | What you do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1 | Export open pipeline with the fields in Section 2 | Clean export | 20 min |
| 2 | Pull your historical conversion and cycle numbers | Rate card | 30 min the first time; reuse after |
| 3 | Run the truth checks on the export | List of records that cannot be trusted as entered | 20 min |
| 4 | Reclassify stale deals | Live vs presumed-dead pipeline | 10 min |
| 5 | Do the math: expected value, gap, true coverage | Yes/no verdict with math shown | 20 min |
| 6 | Find and rank the three leaks by dollars at risk | Leak table | 20 min |
| 7 | Validate leaks with the managers who own those stages | Confirmed or corrected leaks | 30 min |
| 8 | Write the inspection list and one dated fix per leak | Inspection list | 15 min |

---

## 2. Step 1: Export Checklist

Pull from your CRM for every open opportunity expected to close in the period, plus the next period (for coverage of what comes after).

| Field | Why | Common problem |
|---|---|---|
| Opportunity ID, owner, segment | Grouping, ownership of leaks | Inactive owners |
| Stage | Conversion math | Stages without written exit criteria |
| Amount, and which amount it is (annual, total contract, first year) | Value math | Mixed amount types rolled up as one |
| Expected close date | Timing | Pushed repeatedly with no buyer reason |
| Created date | Total age | Missing on migrated records |
| Date entered current stage | Age in stage | Not tracked; ask your admin for stage history |
| Next step and next step date | Staleness | Blank, or filler like "following up" |
| Last buyer activity date (meeting held, email reply) | Staleness | Only rep activity is tracked |
| Forecast category | Comparison with the forecast | Set by instinct, not rule |
| Contact roles, economic buyer identified (yes/no) | Single-threading risk | Rarely filled |
| Close date push count | Slip pattern | Not tracked; use field history if available |

---

## 3. Step 2: Your Rate Card

Use your real historical numbers only (SKILL.md Step 2). Pull the last four to six quarters, same segment and motion.

| Stage | Historical stage-to-close win rate (by value) | Average days in this stage | Average days from this stage to close | Count of deals behind the rate |
|---|---|---|---|---|
| Stage 1 | | | | |
| Stage 2 | | | | |
| Stage 3 | | | | |
| Stage 4 | | | | |
| Overall from creation | | | | |

**Historical coverage requirement:** the pipeline-to-target ratio at the start of past periods that ended at or near target. A simple first estimate is 1 divided by your overall win rate from creation for deals that can close in the period. Record the ratio you actually needed, not the one people quote.

**When the rate card is unreliable** (say so in the read, per the SKILL.md limitation):

| Situation | What to do |
|---|---|
| Fewer than about 30 closed deals behind a stage rate | Use a wider window or combine segments; label the rate as low confidence |
| Pricing, product, segment, or sales motion changed in the last two quarters | Use only post-change data, even if thin, and widen the range |
| Stage definitions changed | Rates before the change do not apply to the new stages |
| Large deals dominate value | Calculate rates by count and by value; use the more conservative |

---

## 4. Step 3: Truth Checks on the Export

Pipeline usually lies by drift, not fraud. Check these six places before doing any math.

| Check | How | Red line (rule of thumb) |
|---|---|---|
| Stages without exit criteria | Can each manager state what must be true to enter each stage? | Any stage nobody can define |
| Next steps | Share of deals with a dated next step in the future | Many blank, past-dated, or filler |
| Amounts | Are all amounts the same type? | Mixed types in one roll-up |
| Close dates | Deals pushed two or more times | Pushed repeatedly with no buyer reason |
| Buying group | Share of late-stage deals with an economic buyer identified | Late-stage deals with no economic buyer |
| Forecast category | Does category follow a written rule? | Category set by instinct |

Fix what you can before the math. What you cannot fix, list as an assumption.

---

## 5. Step 4: Reclassify Stale Deals

**Rule (SKILL.md):** deals aged past twice the average cycle count as dead until a buyer action proves otherwise.

Apply it at stage level: compare each deal's age in its current stage with twice the historical average days in that stage. Also check total age against twice the average full cycle for deals of that size.

| Status | Definition | Treatment in the math |
|---|---|---|
| Live | Within twice the stage average and a buyer action in the last 30 days | Count at historical rate |
| At risk | Within twice the average but no buyer action in 30 days | Count, and put on the inspection list |
| Presumed dead | Past twice the stage average or twice the full cycle | Count at zero until a buyer action (meeting held, written reply, document returned) |

A buyer action is something the buyer did. A rep's email or call attempt is not a buyer action.

---

## 6. Step 5: The Math

### Worksheet

```
PIPELINE MATH: [period]
Target:                                   [$]
Closed to date:                           [$]
Remaining target (A):                     [$]
Days left in period:                      [n]

Per stage (live and at-risk deals only, and only stages whose average days to close fit in the days left):
  Stage [x]: value [$] x historical rate [%] = expected [$]
  Stage [y]: value [$] x historical rate [%] = expected [$]
Expected from pipeline (B):               [$]
Gap (A - B):                              [$]   Verdict: [yes if B >= A, else no]

Coverage
  Headline coverage (all open pipeline / A):          [x]
  True coverage (live pipeline that can close in time / A): [x]
  Historical requirement:                              [x]

Assumptions (every one named):
  1.
  2.
```

**Timing rule of thumb:** exclude stages whose average days to close exceed the days left in the period, or count them only at the historical in-period close rate if you track it. Early-stage value at the start of a period usually belongs to the next one.

**Decision rule (SKILL.md):** if true coverage is below your historical requirement, it is a pipeline problem, not a closing problem. Say so in the verdict.

---

## 7. Step 6: The Leak Finder

Look for leaks in the three places the Quick prompt names, plus concentration risk, then rank the top three by dollars at risk.

| Leak type | How to detect | How to size dollars at risk |
|---|---|---|
| Coverage shortfall | True coverage below historical requirement | The gap (A - B) |
| Age past cycle | Value in presumed-dead or at-risk deals | Expected value those deals would add if live |
| Stage where deals die | A stage converting well below its historical rate this period and last | Value in that stage x (historical rate - current rate) |
| Concentration | One deal's full amount is a large share of expected value | That deal's expected value; note the full amount as exposure |
| Slip pattern | Close dates pushed two or more times | Expected value of pushed deals |

**Decision rule (SKILL.md):** if a stage converts under half the historical rate for two periods, inspect the stage definition, not the reps.

**Aggregates hide single-deal risk** (SKILL.md limitation). Always list any deal whose full amount is more than about a fifth of expected value (rule of thumb), whatever its rank.

### Leak table template

| Rank | Leak | Evidence | Dollars at risk | Owner | Fix | Date |
|---|---|---|---|---|---|---|

---

## 8. Step 8: The Weekly Inspection List

| What to inspect | Who | Question to answer this week |
|---|---|---|
| Every presumed-dead deal | Deal owner with manager | What buyer action happened, and when? If none, close it or move it back a stage |
| Every at-risk deal | Deal owner | What is the buyer-verified next step and date? |
| Every deal above the concentration line | Manager and leader | Who is the economic buyer, what is their process, and what could stop it this period? |
| Deals pushed twice or more | Manager | What changed on the buyer side? |
| The leaking stage | Stage owner and RevOps | Are the exit criteria written and followed? |

### Manager validation questions (Step 7)

1. Does this leak match what you see in deal reviews? If not, which number is wrong?
2. Which three deals in this leak would you bet on, and why?
3. What would a buyer have to do this week for you to believe the stale deals are alive?
4. Is there anything in your pipeline that is not in the CRM yet? (Name it and add it, or exclude it.)

---

## 9. Red Flags

| Red flag | What it usually means | What to do |
|---|---|---|
| Headline coverage looks healthy, true coverage does not | Early-stage and stale value inflating the number | Report both coverages side by side |
| Forecast commit higher than expected value from the math | Instinct ahead of evidence, or a big deal carrying the commit | Ask which deals close the difference and inspect them |
| Average age in a stage well above the historical average | Deals parked, not progressing | Reclassify stale deals |
| A stage converting at half its rate for two periods | Stage definition broken | Inspect definitions before blaming reps |
| Close dates cluster on the last week of the period | Dates set to the period end, not the buyer's plan | Ask for the buyer's date for each |
| Many late-stage deals without an economic buyer | Single-threaded deals | Put on the inspection list |
| AI read quotes "typical" conversion rates | Used benchmarks, not your data | Rerun with your rate card |
| Pipeline growth credited to an AI tool is measured in meetings booked or touches | Activity reported as pipeline: the [Proof Gap, a concept from The Revenue AI Report](https://www.therevenueaireport.com/frameworks/proof-gap) between AI activity and AI-attributable revenue | Count only accepted, qualified opportunities in the math |

---

## 10. Worked Example: Acme

*Fictional and illustrative. All numbers are made up for the example.*

**Context:** Acme, a 400-person B2B software company, week one of the quarter. Target $3.0M, closed $0.4M (early closes from last quarter's slips). Remaining: $2.6M. Days left: 80. The forecast commit from managers is $2.9M.

**Rate card (last five quarters, by value):**

| Stage | Win rate to close | Avg days in stage | Avg days to close |
|---|---|---|---|
| Stage 1 | 8% | 30 | 110 |
| Stage 2 | 18% | 35 | 80 |
| Stage 3 | 35% | 25 | 45 |
| Stage 4 | 60% | 15 | 20 |

Historical requirement: periods that hit target started with about 4x headline coverage, or about 2.5x on deals that could close in time.

**Pipeline export (expected to close this quarter):**

| Stage | Deals | Value | Avg age in stage | Notes |
|---|---|---|---|---|
| Stage 1 | 50 | $5.0M | 20 days | |
| Stage 2 | 36 | $3.6M | 55 days | 14 deals ($1.5M) older than 70 days in stage |
| Stage 3 | 15 | $2.0M | 22 days | One deal is $0.6M |
| Stage 4 | 6 | $0.8M | 10 days | |

**Stale reclassification:** twice the Stage 2 average is 70 days. The 14 deals past 70 days ($1.5M) have no buyer action in 30 days. Presumed dead. Live Stage 2: $2.1M.

**Timing:** Stage 1 needs 110 days on average to close; 80 remain. Excluded from the in-quarter math (assumption 1).

**Math:**

| Stage | Live value | Rate | Expected |
|---|---|---|---|
| Stage 4 | $0.8M | 60% | $0.48M |
| Stage 3 | $2.0M | 35% | $0.70M |
| Stage 2 | $2.1M | 18% | $0.38M |
| Total (B) | | | $1.56M |

Gap: $2.6M - $1.56M = $1.04M. **Verdict: no.**

| Coverage | Calculation | Result |
|---|---|---|
| Headline | $11.4M / $2.6M | 4.4x (looks above the 4x history) |
| True | ($0.8M + $2.0M + $2.1M) / $2.6M | 1.9x (below the 2.5x history) |

**Reasoning:** headline coverage says healthy; true coverage says not. Most of the difference is Stage 1 value that cannot close this quarter and stale Stage 2 value. By the decision rule this is a pipeline problem, not a closing problem. The $2.9M commit is $1.3M above what the pipeline supports.

**Leaks, ranked by dollars at risk:**

| Rank | Leak | Evidence | Dollars at risk | Owner | Fix | Date |
|---|---|---|---|---|---|---|
| 1 | Coverage shortfall | True coverage 1.9x vs 2.5x needed | $1.04M gap | VP Sales | Late-stage pipeline push: expansion offers to current customers with short cycles; reset the commit | Plan by Friday week 1 |
| 2 | Stale Stage 2 | 14 deals, $1.5M, past twice the stage average | $0.27M expected if revived | Stage 2 managers | Buyer-verified next step or close-out on all 14 | End of week 2 |
| 3 | Concentration | One Stage 3 deal: full amount $0.6M is 38% of the $1.56M expected; outcome is binary | $0.21M expected; $0.6M exposure | Deal owner and VP | Meet the economic buyer; confirm signing process and date | End of week 2 |

**Assumptions named:** (1) Stage 1 excluded for timing; a few may close faster. (2) Rates assume no change in motion; pricing changed two quarters ago, so Stage 2 and 3 rates rest on the last two quarters only, about 40 deals. (3) Stale deals counted at zero until a buyer action.

**Manager validation:** Stage 2 managers agreed 9 of the 14 stale deals were dead and closed them out; 5 had a buyer meeting in the last week that was never logged. Revised Stage 2 live value: $2.5M; expected rises by about $0.07M. Verdict unchanged.

---

## 11. AI Assist

### Split the work

| Task | AI assistant | Human |
|---|---|---|
| Export cleanup | Flag mixed amounts, blank next steps, push counts | Fix the records or note the assumptions |
| Rate card | Compute rates from a closed-deal export | Decide the window; flag motion changes |
| Stale reclassification | Apply the twice-average rule per deal | Confirm buyer actions with owners |
| Math and leaks | Calculate, rank, show work | Check the arithmetic on the top lines |
| Validation | Draft questions per manager | Hold the conversations |
| Inspection list | Generate per-owner lists | Run the inspection |

### Follow-up prompts to use after the Quick prompt

1. "Show every calculation line by line: value per stage, rate used, expected value, total, gap. Use only the numbers I pasted. List every assumption."
2. "Reclassify each deal: live, at risk, or presumed dead, using twice the historical average days in its stage and the last buyer action date. Show the list of presumed-dead deals with value."
3. "Calculate headline coverage and true coverage (live deals in stages that can close in [n] days). Compare both to my historical requirement of [x]."
4. "Rank the leaks by dollars at risk, defined as expected value lost or the gap. Name separately any single deal whose full amount exceeds about a fifth of expected value."
5. "For each leak, write one dated fix with an owner role, and the question the stage owner should answer this week."
6. "List the stages converting under half their historical rate for two periods, and draft the questions to test the stage definition."

### Errors this job invites, and how to catch them

| AI error | How to spot it | Fix |
|---|---|---|
| Uses industry coverage ratios ("3x is standard") | A ratio you did not give | Rerun with "use only my numbers"; delete the line |
| Arithmetic slips | Totals do not add | Recompute the top two stages by hand |
| Counts stale deals at full rate | No reclassification step shown | Prompt 2 |
| Counts early-stage value that cannot close in time | Expected value includes Stage 1 at the start of a period | Prompt 3 |
| Blames reps for a stage leak | Fix is "coach the reps" on a two-period stage drop | Apply the stage-definition rule |
| Vague verdict ("cautiously optimistic") | Not yes or no | Require yes or no with the math |

---

## 12. Common Mistakes

| Mistake | How to spot it | Fix |
|---|---|---|
| Treating headline coverage as health | Only one coverage number reported | Report true coverage beside it |
| Using industry benchmarks | Rates not traced to your CRM | Build the rate card |
| Keeping dead deals to protect coverage | Same deals stale every quarter | Apply the twice-average rule every time |
| Fixing everything | Ten leaks, no owners | Three leaks, one fix each, dated |
| Reporting to the board without assumptions | Number with no conditions | Attach the assumptions list |

---

## 13. The 5-Minute Version

1. Write remaining target and days left.
2. For each stage that can close in time, multiply live value by your historical stage-to-close rate. Add them up.
3. Compare to the remaining target: yes or no.
4. List every deal older than twice its stage average. Those count as zero.
5. Name the one biggest deal and the one question you need answered on it this week.

## 14. The Deep Version

For board commits, plan-setting, or a quarter that looks off track.

| Addition | What it adds |
|---|---|
| Rate card by segment and deal size | Big deals and small deals convert differently |
| In-period close rates by stage and week of quarter | Timing math that matches your actual pattern |
| Deal-by-deal review of everything above the concentration line | Single-deal risk the aggregate hides |
| Pipeline creation needed for next period, from your cycle times | Shows whether this quarter's leak becomes next quarter's miss |
| Stage exit criteria written and audited on a sample | Fixes the stage leaks at their source |
| Weekly rerun with the same rate card | Trend in true coverage, not a one-time read |

---
*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
