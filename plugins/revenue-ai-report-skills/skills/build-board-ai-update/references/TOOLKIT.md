# Board AI Update Toolkit: Spend Status, Method Lines, Failure Report, Bet Cards, and Hard Questions

**Use this file when:**
- Board prep starts this week and AI spend needs its own page.
- AI spend is now large enough to appear as a budget line, and a director has started asking what it bought.
- The last update was a slide of adoption numbers and you need one that survives a skeptical director.
- You stopped a tool this period and need to report it as evidence of discipline, not as an embarrassment.

The SKILL.md holds the logic. This file holds the instruments. Run them in the order below.

---

## 1. The Build Sequence

| Step | What you do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1 | Pull the full spend list from finance | Spend inventory (Section 2) | 10 min if finance has it ready |
| 2 | Classify each line: working, unproven, stopped | Spend split (Section 3) | 10 min |
| 3 | Write one method line per claimed return | Results table (Section 4) | 15 min |
| 4 | Pick the failure to report; write it up | Failure report (Section 5) | 10 min |
| 5 | Write a bet card for each next-period bet | Bet cards with success and kill criteria (Section 6) | 15 min |
| 6 | Write the verdict sentence last | One sentence (Section 7) | 5 min |
| 7 | Rehearse the hard questions | Answers you can say without notes (Section 8) | 15 min |
| 8 | Finance reviews every number | Signed-off page | Before the deck locks |

**Write the verdict last.** Written first, it becomes the claim the rest of the page has to defend.

---

## 2. Step 1: The Spend Inventory

| What | Where (system category) | Period | Watch for |
|---|---|---|---|
| AI platform and seat contracts | Finance / accounts payable, contract repository | This period, and annualized | Multi-year prepayments booked in one period |
| AI features bundled into existing tools | Contract renewals and upgrade invoices | This period | Uplifts nobody labeled as AI |
| Consumption and usage-based charges | Vendor invoices, cloud billing | This period | Spikes at quarter end |
| Services and implementation | Accounts payable | This period | Consultants paid to set up AI tools |
| Internal time | Owner estimates of hours at loaded cost | This period | Stated as an estimate, clearly labeled |
| Seats bought outside procurement | Expense reports, corporate cards | This period | Shadow spend that changes the total |

**Rule:** the total on the board page must match what finance would say if a director asked them directly.

---

## 3. Step 2: Working, Unproven, Stopped

| Status | Criteria (all must be true) | What goes on the page |
|---|---|---|
| **Working** | Measured result against a baseline; method stated in one line; at least one full period in production; result reached a business metric or a cost line | Spend, result, method line |
| **Unproven** | Running, but any working criterion is missing: no baseline, under one period, no method, or the result is activity (usage, logins) rather than outcome | Spend, what will prove it, by when |
| **Stopped** | Shut off or not renewed this period | Spend this period, total sunk spend, reason code, lesson |

### Tie-breakers

| Situation | Status |
|---|---|
| Strong result, but only from the vendor's dashboard | Unproven until your system shows it |
| Time saved measured well, nothing downstream measured | Working only if the board line says "time," not "revenue" |
| Good result in the first month only | Unproven. Wait for a full period |
| Wound down but contract runs to next period | Stopped, with remaining committed spend shown |
| Paused for a fix, will restart | Unproven, with the restart condition |

---

## 4. Step 3: The Method Line

Every claimed return carries its method in one line (SKILL.md rule).

**Format:** `[Metric] moved from [baseline] to [result] over [period], measured in [system], compared with [baseline type].`

### Method strength ladder

| Level | Method | Board reading |
|---|---|---|
| 4 | Holdout or control group (some teams, regions, or accounts without the tool) | Strong. Can claim the tool caused it |
| 3 | Before and after with a measured baseline from the same system | Reasonable. Other changes could explain part of it; say which |
| 2 | Trend compared with prior periods, no fixed baseline | Weak. Present as "associated with" |
| 1 | Self-report, survey, vendor case math | Not a result. Classify as unproven |

### Time is not revenue

| What you have | How to say it |
|---|---|
| Minutes saved per person, measured | "[X] hours per week returned to the team." Stop there |
| Hours saved plus a measured change in what people did with them | "[X] hours returned; [activity] rose from [a] to [b] in the same period." Do not convert to revenue |
| A revenue claim | Only with level 3 or 4 method, and finance agreement on the figure |

---

## 5. Step 4: The Failure Report

A period with zero failures reads as a period with no measurement (SKILL.md rule).

### Reason codes

The Reversal Ledger (a framework from The Revenue AI Report, [therevenueaireport.com/frameworks/reversal-ledger](https://www.therevenueaireport.com/frameworks/reversal-ledger)) codes reversals into six reasons. Use them so failures are comparable period to period.

| Code | Meaning |
|---|---|
| DATA | Data exposure, leakage, or compliance failure |
| HALLUCINATION | Brand or accuracy risk from generated output |
| DIAGNOSTIC | Could not explain what the AI did or why |
| ECONOMICS | Cost per outcome exceeded the manual baseline |
| INTEGRATION | Technical or workflow break with the existing stack |
| ADOPTION | People stopped using it |

### Failure report template

```
FAILURE REPORTED: [tool or initiative]
Reason code:        [one of six]
What happened:      [one sentence, factual]
How we detected it: [the check or metric that caught it]
When we stopped:    [week N of M; date]
Spend:              [this period] / [total sunk] / [remaining committed, if any]
What it taught us:  [one sentence]
What we changed:    [the process change that applies to every future bet]
```

**Which failure to report:** the one with the clearest lesson that changes future decisions, not the smallest or the least embarrassing. If you stopped several, list them all in the spend split and write up one.

---

## 6. Step 5: The Bet Card

No new bet without kill criteria (SKILL.md rule).

```
BET: [name]                       Owner: [name]
Hypothesis:        If we [do X], [metric] will move from [baseline] to [target] by [date].
Spend requested:   [this period] / [committed beyond]
Success criteria:  [metric, threshold, date, system it is measured in]
Kill criteria:     [metric or event that stops it, threshold, date]
Guardrails:        [what must not get worse: quality, complaints, data incidents]
Review:            [date the board will see the result]
```

### Good and weak criteria

| Weak | Why it fails | Strong |
|---|---|---|
| "Improve rep productivity" | No metric, no threshold | "Opportunities created per rep per month from 4.0 to 4.6 by end of Q2, CRM" |
| "Kill if it doesn't work" | Nobody can tell when | "Kill if cost per qualified meeting exceeds our human baseline for two consecutive months" |
| "Monitor quality" | No trigger | "Kill if sampled error rate on customer-facing answers exceeds 2 in 100 in any weekly review" |
| No guardrail | Wins on one metric while damaging another | "Spam complaint rate stays under our sending threshold" |

---

## 7. Step 6: The Verdict Sentence

### Formulas

| Situation | Formula |
|---|---|
| Mixed results (most periods) | "AI returned measured value in [N] of [M] initiatives this period, [share] of spend; [share] is unproven, and we stopped [K], including [one]." |
| Strong period | "[Initiative] moved [metric] from [a] to [b], measured against a holdout; the rest of the program is [status]." |
| Thin period | "We cannot yet show a return on most AI spend; [share] is unproven, and next period we [measure / cut] [what]." |

### Tests

| Test | Pass |
|---|---|
| A director could repeat it to another director | Under 35 words, one idea |
| Contains a number | At least one count or share |
| Does not overclaim | Says "measured value," not "transformation" |
| Mentions what was stopped or unproven | Yes |

---

## 8. Step 7: The Hard Question Bank

Pick the three most likely for your board and rehearse them out loud.

| Question | What a good answer contains |
|---|---|
| "What did we get for this money, in revenue?" | The working lines with method, then plainly: the rest is not yet shown in revenue |
| "Why is half of it unproven?" | What will prove each unproven line, by when, and what you will cut if it does not |
| "How do you know the tool caused that, and not something else?" | Method level; what else changed; holdout plan if none exists |
| "Why did we buy the one you stopped?" | The original hypothesis, what was missing (usually kill criteria), what changed |
| "Are we spending too much or too little compared with peers?" | Avoid peer benchmarks you cannot source. Answer with your own cost per outcome |
| "What is the risk exposure?" | Customer-facing tools, data handled, the review process, any incidents |
| "What would you cut if we asked for 30 percent less?" | A ranked list, ready |
| "Who owns this?" | One name per initiative and one name for the program |
| "Is time saved turning into anything?" | The measured downstream activity, or an honest "not yet" |
| "When will we know?" | Dates from the bet cards |

---

## 9. The Output Template (ready to fill)

```
AI UPDATE: [Period]                 Prepared by: [name]    Finance review: [name, date]

VERDICT
[One sentence]

SPEND SPLIT
| Status | Initiatives | Spend | Share |
| Working | | | |
| Unproven | | | |
| Stopped | | | |
| Total | | | 100% |

WHAT IS WORKING
| Initiative | Result | Method line |

WHAT IS UNPROVEN
| Initiative | Spend | What will prove it | By when | Cut if |

FAILURE REPORTED
[Failure report, Section 5]

NEXT PERIOD'S BETS
[Bet cards, Section 6, one row each in the deck; full cards in the appendix]

ASK OF THE BOARD
[Decision or input needed, if any. Risk appetite is the board's call (SKILL.md limitation)]
```

---

## 10. Worked Example: Acme, One Quarter

*Illustrative only. Acme is a fictional 400-person B2B software company. All figures are invented.*

### Inventory and classification

| Initiative | Spend this quarter | Status | Reasoning |
|---|---|---|---|
| Call summaries into CRM | 45,000 | Working | 22 min per rep per day saved across 50 reps, CRM timestamps, before-after with measured baseline |
| Renewal risk scoring | 60,000 | Working | At-risk cohort renewal rate from 76% to 84% vs prior two quarters, billing data, finance reviewed |
| Outbound agent | 120,000 | Unproven | Meetings booked tracked only in vendor dashboard |
| Content drafting | 25,000 | Unproven | Output up, no downstream metric |
| Forecast assistant | 70,000 | Unproven | Live for seven weeks; under one period |
| AI email agent | 55,000 | Stopped | ECONOMICS: cost per qualified meeting above SDR baseline for two months |
| Website chat assistant | 30,000 | Stopped | HALLUCINATION: see failure report |
| AI meeting scheduler | 15,000 | Stopped | ADOPTION: under 10 of 60 reps using it after eight weeks |

### Spend split

| Status | Initiatives | Spend | Share |
|---|---|---|---|
| Working | 2 | 105,000 | 25.0% |
| Unproven | 3 | 215,000 | 51.2% |
| Stopped | 3 | 100,000 | 23.8% |
| **Total** | **8** | **420,000** | **100%** |

### Method lines

- **Call summaries:** "Rep admin time fell from 41 to 19 minutes per day over Q2 vs Q1, measured in CRM activity timestamps, compared with a measured Q1 baseline. First meetings per rep rose from 6 to 7 per week in the same period; we do not claim the tool caused it." (Level 3. Time, not revenue.)
- **Renewal risk:** "Renewal rate in the at-risk cohort rose from 76% to 84% over Q1-Q2 vs the prior two quarters, measured in billing data. CS coverage also changed in the same period; we attribute the change to the combination, not the model alone." (Level 3.)

### Failure reported

```
FAILURE REPORTED: Website chat assistant
Reason code:        HALLUCINATION
What happened:      The assistant quoted discontinued pricing to prospects.
How we detected it: Sales ops sampled 200 conversations in week 9; 11 contained wrong pricing.
When we stopped:    Week 9 of a 12-month contract; stopped the same day.
Spend:              30,000 this quarter / 30,000 total sunk / 60,000 remaining committed, under negotiation
What it taught us:  We launched a customer-facing tool with no weekly sampled review.
What we changed:    Every customer-facing AI tool now launches with a named reviewer, a weekly sample, and an error-rate kill criterion.
```

### Bets for next quarter (rows)

| Bet | Spend | Success | Kill | Review |
|---|---|---|---|---|
| Forecast assistant, continue | 70,000 | Commit forecast error from 12% to 9% by end of Q4, CRM snapshots vs closed | Error not below 11% by end of Q4 | Q4 board |
| Outbound agent: measure or stop | 120,000 | Opportunities from agent-booked meetings, CRM source field, vs one holdout territory | Cost per opportunity above SDR baseline for two months | Q4 board |
| AI renewal briefs for CSMs (new) | 10,000 | CSM prep time per renewal down by a third, quality score held | Brief useful rate under half of renewals after 30 | Q4 board |

### Verdict

> AI returned measured value in two of eight initiatives this quarter, a quarter of spend; half is unproven, and we stopped three, including a website assistant that quoted wrong prices.

**Reasoning:** two working initiatives at 105,000 of 420,000 is exactly 25 percent. Unproven is 51 percent, so "half" is accurate. Naming the chat failure in the verdict pre-empts the hardest question.

### Rehearsed hard questions

| Question | Answer |
|---|---|
| "What did we get in revenue?" | "Not shown yet. Renewal risk is the closest: the at-risk cohort renewed at 84% vs 76%. Call summaries returned time, not revenue." |
| "Why keep the outbound agent at 120,000?" | "Because next quarter it gets a holdout territory and a kill line. If cost per opportunity beats the SDR baseline, it stays. If not, we stop it at the Q4 review." |
| "Why did we launch chat without review?" | "We had no rule. Now every customer-facing tool has a named reviewer, a weekly sample, and a kill threshold." |

---

## 11. Decision Table and Red Flags

| If you see | It means | Do this |
|---|---|---|
| Unproven is more than half of spend (rule of thumb) | Program runs on belief | Lead with the measurement plan, not the wins |
| No stopped items | Nothing is being measured hard enough to fail | Look again. If truly none, say what you would stop and at what threshold |
| Every result is level 1 or 2 method | No causal claim is safe | Present as associations; propose one holdout next period |
| Adoption metrics on the results page | Activity presented as outcome | Move to an appendix |
| Total spend differs from finance's figure | The page will be challenged on the first number | Reconcile before sending |
| A bet with a success line and no kill line | Open-ended commitment | Add kill criteria or drop the bet |
| Time saved converted to dollars of revenue | Fails the quality check | Restate as hours |

### Optional cross-check: the Proof Gap

The Proof Gap (a framework from The Revenue AI Report, [therevenueaireport.com/frameworks/proof-gap](https://www.therevenueaireport.com/frameworks/proof-gap)) divides AI spend by verified, incremental AI-influenced pipeline in the same quarter. The Report's thresholds: under 1.0x is defensible, 1.0x to 4.0x is a watch, above 4.0x on a rolling four-quarter basis triggers a review. Use it only for pipeline-claiming spend with at least one full quarter in production.

---

## 12. AI Assist: Splitting the Work

| Task | AI assistant | Human |
|---|---|---|
| Classify spend into working, unproven, stopped | Drafts using Section 3 criteria | Confirms each with the initiative owner |
| Write method lines | Drafts from pasted figures | Checks method level honestly |
| Compute split and shares | Yes | Finance reconciles |
| Draft failure report and bet cards | Yes | Sets the actual kill thresholds |
| Generate hard questions | Yes, more than three | Picks the three this board will ask |
| Decide risk appetite | Never | The board (SKILL.md limitation) |

### Follow-up prompts after the Quick prompt

1. "Classify each line as working only if it has a measured baseline, a stated method, at least one full period in production, and a result in a business metric or cost line. Otherwise unproven. Show the missing criterion for each unproven line."
2. "Write one method line per working result in this format: metric moved from baseline to result over period, measured in system, compared with baseline type. Rate each method: holdout, before-after with baseline, trend only, or self-report."
3. "Find every place where time saved is described as revenue, pipeline, or dollars. Rewrite each as hours."
4. "Write the failure report using this reason code list: DATA, HALLUCINATION, DIAGNOSTIC, ECONOMICS, INTEGRATION, ADOPTION. Include how we detected it and what process changed."
5. "For each bet, write success and kill criteria with a metric, threshold, date, and system. Flag any I gave you that are vague."
6. "Give me ten questions a skeptical director would ask about this page, ranked by likelihood. For the top three, draft answers using only my figures."
7. "List every number in your output and where in my input it came from. Flag any you computed or inferred."

### Errors this job invites, and how to check

| AI error | How to spot it | Fix |
|---|---|---|
| Inflates the verdict | Words like "transformative," "significant" | Apply the verdict tests in Section 7 |
| Converts time to revenue | Dollar figure from hours times salary presented as return | Follow-up prompt 3 |
| Invents peer benchmarks | "Industry average" with no source you supplied | Delete. Answer with your own cost per outcome |
| Softens the failure | Passive voice, no reason code, no sunk spend | Use the template verbatim |
| Shares that do not sum | 99 or 101 percent | Re-add by hand |
| Kill criteria that are not testable | "If results disappoint" | Follow-up prompt 5 |

---

## 13. Common Mistakes

| Mistake | How to spot it | Fix |
|---|---|---|
| Leading with adoption | First chart is weekly active users | Lead with the verdict and the spend split |
| Hiding the stopped tools | Total in the split is lower than finance's | Show all three statuses, always |
| One failure, no lesson | "We stopped X" with nothing after | Fill "what we changed" |
| A new number format every quarter | Board cannot compare periods | Keep the same template and the same statuses |
| Pitching next period's bets as certain | No kill criteria | Bet cards, every time |
| Not rehearsing | Hesitation on the first question | Say the three answers out loud before the meeting |

---

## 14. The 5-Minute Version

1. Get the total AI spend from finance. One number.
2. Name the initiatives with a measured result and the method. Everything else is unproven.
3. Name what you stopped and why, in one line.
4. Write: "AI returned measured value in [N] of [M] initiatives; we stopped [K]."
5. Prepare one honest answer to "what did we get in revenue?"

## 15. The Deep Version

For annual planning boards, material AI budget increases, or after a public or customer-facing incident.

| Addition | What it adds |
|---|---|
| Rolling four-period view of the spend split | Shows whether unproven spend is converting to working or stopped |
| Holdout designs for the two largest unproven lines | Causal evidence next period |
| Cost per outcome for every working line | A denominator for every dollar |
| Full reversal log with reason codes and sunk spend | Board sees a pattern, not an anecdote |
| Risk register for customer-facing and data-handling tools | Answers the exposure question before it is asked |
| Pre-read sent a week early with the three hard questions answered | Meeting time goes to decisions |

---
*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
