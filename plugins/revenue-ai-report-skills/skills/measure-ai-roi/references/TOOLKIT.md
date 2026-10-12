# Measure AI ROI: Toolkit

**Use this file when:**
- A renewal, budget review, or board meeting needs a verdict on one AI investment, and "people like it" will not survive the CFO.
- You are about to expand a pilot to more seats and need to know whether the first seats earned anything.
- Someone has handed you an ROI slide built on hours saved and you need to take it apart fairly.
- You are buying something new and want the measurement designed before the contract is signed.

The SKILL.md holds the logic. This file holds the sheets, the tables, and a full worked case. Run them in the SKILL.md process order.

The method uses three frameworks from The Revenue AI Report: [OAR](https://www.therevenueaireport.com/frameworks/oar) (Optimize, Amplify, Reinvent: the three levels of AI ambition, chosen after the diagnosis), [the Proof Gap](https://www.therevenueaireport.com/frameworks/proof-gap) (AI spend divided by verified, incremental AI-influenced pipeline), and [Optimization Theater](https://www.therevenueaireport.com/frameworks/optimization-theater) (the pattern of reporting activity and time savings as if they were revenue). This toolkit is built to keep a case out of Optimization Theater.

---

## 1. The sequence, with time and output

| Step | What you do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1 | Name the outcome, owner, period, baseline | Outcome card | 15 min if data exists |
| 2 | Decompose the outcome into drivers | Driver tree with baselines | 15 min |
| 3 | Pick one driver, map what controls it | Constraint map | 20 min |
| 4 | Test AI fit and readiness separately | Fit and readiness scores, dependency list | 15 min |
| 5 | Classify Optimize, Amplify, or Reinvent | OAR level with justification | 5 min |
| 6 | Full cost, before and after, the return ladder, verdict | Investment case (template in Section 9) | 30-60 min |

**The order rule:** never start at step 6. If the tool was bought before steps 1-5 were done, do them now, after the fact, and say so in the case. A benefit story written after purchase is the most common way ROI gets inflated.

---

## 2. Step 1: The outcome card

```
OUTCOME CARD
Strategic outcome:     [A business result, e.g. "Net-new ARR from mid-market"]
Owner:                 [One named role, e.g. VP Sales, Mid-Market]
Measurement period:    [e.g. Two full quarters after go-live]
Baseline value:        [The number before AI, with its date range]
Baseline source:       [System and report name, e.g. CRM closed-won report]
Baseline stability:    [How much it moved quarter to quarter before AI]
Why this outcome:      [The plan or board goal it serves]
```

**Baseline rules (rule of thumb):**

| Situation | Minimum baseline window |
|---|---|
| Metric moves weekly (activity, meetings, response time) | 8-12 weeks |
| Metric moves monthly (pipeline created, conversion rates) | 2 quarters |
| Metric depends on deals closing (win rate, deal size, cycle length) | One full sales cycle, or 2 quarters, whichever is longer |
| Strong seasonality | Same period last year as well as the prior period |

If baseline stability is wide (the metric swung a lot quarter to quarter before AI), any after-change smaller than that swing is noise until proven otherwise. Write the swing down now so nobody argues about it later.

---

## 3. Step 2: Driver trees

Pick the tree that matches the outcome. Fill a baseline for every driver, not just the one you hope moved.

| Outcome | Drivers | Formula |
|---|---|---|
| Revenue growth (new business) | Opportunity count, average deal size, win rate, cycle length | Sales velocity = opps x deal size x win rate / cycle days |
| Pipeline generation | Accounts worked, contact rate, meeting rate, meeting-to-opportunity rate | Pipeline = accounts x contact rate x meeting rate x opp rate x deal size |
| Net revenue retention | Gross churn, contraction, expansion | NRR = (start ARR - churn - contraction + expansion) / start ARR |
| Seller productivity | Selling time, activities per selling hour, conversion per activity | Output per rep = selling hours x activity rate x conversion |
| Cost to serve (CS, support) | Accounts per CSM, cases per account, time per case | Cost = headcount cost / accounts covered |

**Driver selection rule:** choose the driver with the largest credible gap between baseline and target that you have a plausible mechanism for. Do not pick the one the vendor's demo featured.

---

## 4. Step 3: The constraint map

For the chosen driver, record what actually governs it. One line per row. Mark the binding constraint with a star.

| Layer | Question | Example finding |
|---|---|---|
| Tasks | What work produces this driver? | AEs research accounts and write first emails |
| Process | What sequence and handoffs? | SDR books meeting, AE runs it, AE creates opp |
| Workflow | Where does the work actually happen? | Browser tabs, CRM, email, notes doc |
| Data | What data does the work depend on, and is it trusted? | Account fit fields 60 percent populated |
| Integrations | Which systems must talk? | CRM to email to call recorder |
| People | Who does it, how many, how loaded? | 40 AEs, 15 percent ramping |
| Skills | Can they do it well today? | Research is shallow, emails generic |
| Ownership | Who is accountable for the driver? | Nobody owns opp creation rate below VP |
| Incentives | What does comp reward? | Bookings only, not opp creation |
| Controls | What review or approval sits in the path? | Manager approves opp stage 2 |

**The binding-constraint test:** if you removed this constraint tomorrow, would the driver move? If the honest answer is "only if something else also changed," it is not the binding constraint.

---

## 5. Step 4: AI fit and readiness, scored separately

### AI fit sheet (can AI change the binding constraint?)

Score 0-2 per row. 0 = no, 1 = partly, 2 = yes.

| Fit question | Score |
|---|---|
| Is the binding constraint a task AI does well (summarize, draft, classify, retrieve, extract, route)? | |
| Is the input data available to the AI at the moment the work happens? | |
| Can a human check the AI output faster than doing the task by hand? | |
| Is a wrong output cheap to catch before it reaches a customer or the forecast? | |
| Does the time or quality gain land on the binding constraint, not beside it? | |

**Rule of thumb:** 8-10 strong fit; 5-7 fit with conditions, write them down; 0-4 choose another intervention (SKILL.md decision rule 3).

### Readiness sheet (can the organization absorb it?)

| Dependency | Ready / Gap / Blocker | Owner | Fix before go-live? |
|---|---|---|---|
| Process documented | | | |
| Data fields populated and trusted | | | |
| Integrations live and tested | | | |
| People trained on judging output, not just clicking | | | |
| Manager reinforcement in the rhythm (1:1s, reviews) | | | |
| Ownership of the metric named | | | |
| Incentives not working against the change | | | |
| Controls defined (what AI may and may not do unreviewed) | | | |

**Rule:** any Blocker means the investment cannot reach the metric yet. Fix it or price the fix into full cost.

---

## 6. Step 5: OAR classification

| Level | What changes | Typical evidence | What to measure | Wrong if |
|---|---|---|---|---|
| Optimize | Same task, faster or cheaper | Time per task down, same workflow | Time per task, then whether freed time became output | You claim the operating model changed |
| Amplify | Workflow, ownership, or decision quality changes inside the current model | Different handoffs, new review step, better decisions | The driver itself (conversion, win rate, accuracy) | Only task time was measured |
| Reinvent | A different operating model built from first principles | Roles, coverage model, or motion redesigned | The strategic outcome and unit economics | Seats were added to the old model |

**Classification rule:** classify by what actually changed in the operating model, not by what the vendor category claims. Most first-year tools are Optimize. Saying so is not a failure; reporting Optimize as Reinvent is.

**OAR mistakes to catch (from the OAR framework):**
- Reinvent language, Optimize work. The gap between the label and the reality is where reported return disappears.
- OAR before diagnosis. Choosing a level before outcome, driver, constraint, and readiness are known turns the framework into branding.
- Treating Optimize as failure. For a low-maturity team it is the right first level; the failure is staying there while claiming otherwise.

---

## 7. Step 6a: The full cost sheet

| Cost line | How to compute | Often missed? |
|---|---|---|
| Licenses and platform | Contract value for the period | No |
| Usage or overage fees | Actual invoices, not quoted | Sometimes |
| Implementation and services | One-time, spread over the contract term | Sometimes |
| Admin time | Hours per week x loaded hourly cost x weeks | Yes |
| Enablement time | Trainer hours plus learner hours x loaded cost | Yes |
| Manager time | Review, coaching, and QA hours | Yes |
| Integration and maintenance | Engineering or RevOps hours to build and keep it running | Yes |
| Data cleanup required to make it work | Project hours or vendor cost | Yes |
| Displaced tool savings | Subtract only if the old contract actually ended | Overclaimed |

**Loaded cost rule of thumb:** use salary plus benefits and overhead, not salary alone. Ask finance for the loaded rate they already use; do not invent one.

---

## 8. Step 6b: The return ladder

Every claimed benefit goes on exactly one rung. A benefit climbs only with the evidence in the right column.

| Rung | What it is | Counts as money? | Evidence needed to climb to the next rung |
|---|---|---|---|
| 1. Activity | The tool was used (logins, drafts, summaries) | No | Proof time or quality changed per task |
| 2. Capacity | Time freed or quality raised per task | No, it is a maybe | Proof the freed time became more output (meetings, opps, accounts covered) |
| 3. Savings | Cost actually removed (contract ended, hire not made, overtime cut) | Yes, if finance confirms | A budget line that went down |
| 4. Contribution | Driver moved beyond the comparison group (more opps, higher conversion) | Projected only | Those opps closed at a known rate |
| 5. Revenue | Incremental bookings or retained ARR, verified in the CRM | Yes | None, this is the top |

**Ladder rules:**
- Savings require a budget line that went down. "We avoided a hire" counts only if the hire was approved and then cancelled.
- Contribution is a projection until the deals close. Label it "projected" in every sentence that uses it.
- Never add rungs together. Capacity hours valued at salary plus revenue double-counts the same rep time.

### Attribution designs, strongest first

| Design | How it works | Strength | Use when |
|---|---|---|---|
| Randomized holdout | Random subset of reps or accounts does not get the tool | Strong | You can control rollout and wait a cycle |
| Staggered rollout | Teams start on different dates; compare each against not-yet-started teams | Good | Full rollout is planned anyway |
| Matched comparison | Pick non-users matched on tenure, segment, prior performance | Moderate | Rollout already happened unevenly |
| Before and after, trend-adjusted | Compare to baseline and subtract the pre-existing trend or seasonal pattern | Weak to moderate | No comparison group exists |
| Users vs non-users, unmatched | Compare people who chose to use it with those who did not | Weak, biased | Never as the sole basis: top performers adopt first |
| Self-reported time saved | Survey | Activity evidence only | Never for the money rungs |

---

## 9. The investment case template

```
AI INVESTMENT CASE: [Tool or initiative]          Prepared by: [Role]   Date: [ ]
Decision needed:   [Renew / expand / fix / stop]  By: [Date]

1. OUTCOME
   Strategic outcome:        [ ]
   Owner / period:           [ ] / [ ]
   Baseline (source, window):[ ]
   Pre-AI variability:       [ ]

2. DRIVER AND CONSTRAINT
   Driver chosen and why:    [ ]
   Binding constraint:       [ ]
   AI fit score (0-10):      [ ]  Conditions: [ ]
   Readiness blockers:       [ ]  Fixed? [Y/N]

3. OAR LEVEL
   Level:                    [Optimize / Amplify / Reinvent]
   Evidence for level:       [What changed in the operating model]

4. FULL COST (period)
   Licenses [ ] + services [ ] + admin [ ] + enablement [ ] + manager [ ] + integration [ ] = TOTAL [ ]

5. RESULT ON THE ORIGINAL METRIC
   Metric | Baseline | After | Comparison group change | Incremental change
   [ ]    | [ ]      | [ ]   | [ ]                     | [ ]

6. RETURN LADDER
   Activity:     [ ]
   Capacity:     [ ]   (not money)
   Savings:      [ ]   (finance-confirmed? Y/N)
   Contribution: [ ]   (projected)
   Revenue:      [ ]   (verified)

7. ATTRIBUTION
   Design used:              [ ]
   Limits:                   [Sample size, window, confounders]
   Unmeasurable items:       [Listed, not assumed away]

8. VERDICT
   [Keep / Expand / Fix / Stop]
   Payback from our numbers: [ ]
   Board sentence (with caveat): [ ]
   What would change the verdict: [Metric, threshold, date]
```

---

## 10. Verdict decision table

| If | Verdict | Caveat it must carry |
|---|---|---|
| No baseline exists | Fix: measure first, renew short or month-to-month | "No ROI claim is possible yet" |
| Activity and capacity only, freed time not converted | Keep or Fix, priced as a capacity tool | "Capacity, not revenue" |
| Driver moved beyond comparison group, deals not yet closed | Keep, do not expand | "Projected contribution; revisit after one sales cycle" |
| Revenue rung reached with a comparison group, cost covered | Expand to the next segment with the same measurement | "Result from [segment, period]; may not transfer" |
| Driver did not move and readiness blockers remain | Fix the blockers, set a dated re-test | "Not a test of the tool yet" |
| Driver did not move, readiness was fine | Stop, or rebid against a different constraint | "Missed the bought outcome" |
| Missed bought outcome but helped elsewhere | Say both: miss on thesis, plus the side benefit on its own rung | "The original case failed" |

**Tool-level spend check.** The Proof Gap divides AI spend by verified, incremental AI-influenced pipeline for the same period. Its published thresholds: under 1.0x defensible, 1.0x to 4.0x watch, over 4.0x on a rolling four quarters triggers a review against the [Reversal Ledger](https://www.therevenueaireport.com/frameworks/reversal-ledger) (a framework from The Revenue AI Report: a running record of AI tools revenue teams shut off, with reason codes and cost). Apply it per tool as a cross-check, never as a replacement for the ladder. Do not use it before one full quarter in production.

---

## 11. Red flags

| Red flag | What it usually means | Do this |
|---|---|---|
| ROI slide built on "hours saved x salary" | Capacity dressed as money | Move it to rung 2; ask where the hours went |
| Usage high, driver flat | Tool is used beside the constraint, not on it | Re-run the constraint map |
| Only users who adopted are compared | Selection bias; best reps adopt first | Use matched comparison or staggered rollout |
| Result window shorter than the sales cycle | Win rate and revenue cannot be read yet | Report contribution as projected |
| Baseline chosen after results came in | Cherry-picked window | Lock the baseline window in writing before reading results |
| Vendor supplied the impact numbers | Not independent | Rebuild from your CRM and invoices |
| Every metric improved at once | Something else changed too (pricing, territory, market) | List concurrent changes; adjust or caveat |
| Cost shows invoice only | Hidden people cost | Fill the full cost sheet |
| AI reporting grows each quarter, revenue metrics flat, no tool ever shut off | Optimization Theater | Run the Proof Gap and ask which tool should be stopped |
| "Savings" with no budget line down | Avoided cost that was never real | Reclassify as capacity |

---

## 12. Data checklist

| Data | System category | Lookback |
|---|---|---|
| Driver values by rep, team, week | CRM reports | Baseline window plus result window |
| Opportunity created date, stage history, close date, amount | CRM | 4 quarters minimum |
| Tool usage by user and week | Vendor admin console | Since go-live |
| Rollout dates by user | Vendor console or enablement records | Since go-live |
| Invoices and contract terms | Finance or procurement | Contract term |
| Admin, enablement, manager hours | Time estimates from owners, confirmed by their managers | Since purchase |
| Concurrent changes (pricing, comp, territories, headcount, launches) | Leadership calendar, comp plan, product notes | Baseline and result windows |
| Loaded hourly rates | Finance | Current |

---

## 13. Worked example: Acme

*Illustrative. Acme is a fictional 400-person B2B software company with 55 account executives selling to mid-market.*

**Situation.** Acme bought an AI account-research and email-drafting assistant for 40 of its 55 AEs. The 15 AEs on one regional team were held off the tool until after the renewal decision because of a territory change, which gives a comparison group. The renewal decision is due in six weeks. The CFO asked: "Did it pay back?"

**Step 1, outcome card.** Outcome: net-new ARR from mid-market. Owner: VP Sales. Period: the two quarters after go-live. Baseline: the two quarters before go-live, from the CRM closed-won report. Pre-AI variability: opportunity creation per AE moved between 8.6 and 9.4 per quarter over the prior four quarters.

**Step 2, driver tree.** Baseline per quarter: opps created 9.0 per AE, average deal size $38,000, win rate 22 percent, cycle 95 days. Leadership's diagnosis from the baseline: deal size, win rate, and cycle are near plan; opportunity count is 15 percent below plan. Driver chosen: opportunity count.

**Step 3, constraint map (abridged).** Task: AEs self-source a third of their opps through account research and first emails. Binding constraint (starred): AEs spend about 5 hours a week researching and writing, and outbound emails are generic, so reply rates are low. Data: account fit fields mostly populated. Incentives: bookings only.

**Step 4, fit and readiness.** Fit score 8 of 10 (research and drafting are strong AI tasks; output is checked before sending; condition: AEs must edit, not blast). Readiness: one Gap (no manager review of AI-drafted emails), no Blockers.

**Step 5, OAR.** Optimize. Same task, same workflow, done faster and with more account context. Nobody's role or the coverage model changed.

**Step 6, full cost, year one.**

| Line | Computation | Amount |
|---|---|---|
| Licenses | 40 seats, annual contract | $72,000 |
| Implementation | One-time services | $15,000 |
| RevOps admin | 3 hrs/week x 50 weeks x $75 loaded | $11,250 |
| Enablement | 40 AEs x 3 hrs x $90 loaded | $10,800 |
| Total | | $109,050 |

**Result on the original metric (per AE per quarter, two-quarter average).**

| Metric | Baseline | After | Comparison group (15 AEs, not yet on tool) | Incremental |
|---|---|---|---|---|
| Opps created | 9.0 | 10.4 | 9.1 to 9.8 (+0.7) | +0.7 per AE |
| Opps reaching stage 2 | 48% | 44% | 48% to 47% | Slight quality drop, watch |
| Win rate | 22% | Not readable, few opps closed | | Unknown |

**Reasoning.** The treated group gained 1.4 opps per AE; the comparison group gained 0.7 with no tool, which matches a seasonal lift seen the prior year. So only 0.7 per AE is incremental: 28 extra opps per quarter across 40 AEs. That is outside the pre-AI variability band, so it is likely real. But the window is under two cycles, so no win rate exists for these opps yet, and stage-2 conversion slipped. That means contribution is projected and the quality of AI-sourced opps is an open question.

**Return ladder.**
- Activity: 38 of 40 AEs active weekly.
- Capacity: AEs report about 2 hours a week saved on research. Not counted as money.
- Savings: none. No contract ended, no hire cancelled.
- Contribution (projected): 28 opps x $38,000 = about $1.06M incremental pipeline per quarter. At the baseline 22 percent win rate that projects about $234,000 bookings per quarter. If AI-sourced opps convert worse, as the stage-2 slip hints, this is too high.
- Revenue (verified): not yet.

**Proof Gap cross-check.** Quarterly cost about $27,000 against about $1.06M incremental pipeline: roughly 0.03x, well inside defensible, but only on pipeline, not bookings.

**Verdict: Keep, do not expand.** Renew the 40 seats for 12 months. Hold the 15-seat expansion until one full sales cycle of AI-sourced opps has closed.

**Board sentence.** "The research assistant added about 0.7 opportunities per AE per quarter beyond a comparison team, about $1M of incremental pipeline a quarter against about $109,000 a year in full cost; these opportunities have not closed yet and progress to stage 2 slightly less often, so we are renewing at current size and will decide on expansion when their win rate is known next quarter."

**What would change the verdict.** If AI-sourced opps win at under half the baseline rate after one cycle, downgrade to Fix (add manager email review). If they win at or near baseline, expand to the 15 remaining AEs with the same measurement.

---

## 14. AI assist

| Work | AI assistant | Human |
|---|---|---|
| Build the driver tree from your description | Yes | Confirm the formula matches how your CRM defines each field |
| Compute full cost and incremental change | Yes, show the arithmetic | Check every input against the invoice and report |
| Classify OAR | Draft | Decide; you know what changed in the operating model |
| Assign benefits to ladder rungs | Draft | Approve each rung move |
| Spot red flags in a vendor ROI deck | Yes | Decide what to ask the vendor |
| Write the board sentence | Draft | Own the caveat and the commitment |

**Follow-up prompts to use after the Quick prompt:**

1. "Show every number you used, its source in my paste, and the arithmetic, line by line. Mark any number you estimated or assumed."
2. "Put each claimed benefit on one rung: activity, capacity, savings, contribution, revenue. For each, state the evidence that would move it up one rung."
3. "What else changed in the same window that could explain the result? Ask me about pricing, territories, headcount, comp, launches, and seasonality."
4. "Rewrite the verdict for a skeptical CFO in two sentences. Keep the caveat. Do not add any number I did not give you."
5. "What single measurement, taken by what date, would most change this verdict?"

**Check the AI's output for these errors:**

| Error this job invites | How to catch it |
|---|---|
| Hours saved multiplied by salary and called ROI | Search the output for any "hours x rate" line on a money rung |
| Invented baselines or win rates | Every number must trace to your paste (prompt 1) |
| Projected pipeline reported as revenue | Look for "revenue" or "return" next to unclosed opps |
| Arithmetic slips in ratios and percentages | Recompute the incremental change and cost total yourself |
| Confident attribution with no comparison group | Check the attribution design line names a real design |
| Verdict without a caveat | The board sentence must contain a limit |

---

## 15. Common mistakes

| Mistake | How to spot it | Fix |
|---|---|---|
| Measuring the tool, not the outcome | The case opens with features | Start from the outcome card |
| Baseline from memory | No report name or date range | Pull the CRM report and lock the window |
| Counting adoption as success | "90 percent weekly active" is the headline | Adoption is rung 1 |
| Ignoring the comparison group's change | Before and after only | Subtract the comparison change |
| Calling Optimize "transformation" | No role or workflow changed | Reclassify to Optimize |
| Netting out a tool that was not cancelled | Displaced savings with the old contract still live | Remove the line |
| One verdict for the whole AI stack | Several tools blended | One case per investment |

---

## 16. The 5-minute version

For a renewal email due today:
1. Write the outcome the tool was bought for, in one line.
2. Write the before number and the after number for that outcome. If you have no before number, the verdict is "Fix: measure first."
3. Write the full cost: invoice plus admin hours times a loaded rate.
4. Put each claimed benefit on a ladder rung. Strike anything on rung 1 or 2 from the money column.
5. Write the verdict and one caveat.

## The deep version

For a board review, a large expansion, or a contested renewal:
- Run all six steps with the sheets above, and get finance to sign the cost sheet.
- Use a staggered rollout or randomized holdout for the next expansion, designed before seats are added.
- Read the driver monthly for two full sales cycles, by segment and by rep tenure.
- Track opportunity quality (stage progression, win rate, deal size) for AI-touched opps separately from the rest.
- Compute the Proof Gap on a rolling four quarters for the whole AI stack, then break it down by tool.
- Pre-register the verdict thresholds: write "expand if X, fix if Y, stop if Z" with dates before results come in.

---
*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
