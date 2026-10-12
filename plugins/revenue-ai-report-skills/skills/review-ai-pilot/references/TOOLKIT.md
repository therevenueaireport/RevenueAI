# Review an AI Pilot: Toolkit

**Use this file when:**
- A pilot period is ending and someone needs to make a go, fix, or stop call this week.
- A pilot is about to be extended a second time and nobody has said what would count as failure.
- The vendor is pointing at one number, the team is pointing at another, and finance is pointing at the invoice.
- You are about to start a pilot and want the review to be easy later (use Section 2 first).

The SKILL.md holds the logic. This file holds the instruments: the criteria card, the evidence checklist, the scoring sheet, the call rules, the decision record, and a worked example.

---

## 1. The sequence, with time boxes

| Step (from SKILL.md) | What you actually do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1. Find the pre-pilot criteria | Locate the dated document. Check the date against the first results | Criteria card (Section 2), or "no criteria" finding | 10 min |
| 2. Score against those criteria only | Fill the scoring sheet (Section 4) with evidence from Section 3 | Pass / miss / ambiguous per criterion | 15-20 min |
| 3. Make the call | Apply the call rules (Section 5). Fix gets one change, one deadline | One word: go, fix, or stop | 5 min |
| 4. Write it down | Fill the decision record (Section 6) where the next reviewer will find it | Decision record | 10 min |
| 5. If stop: record learning and cost | Reason code, sunk cost, what you would do differently | Stop entry | 5 min |

**The date rule:** a criterion counts only if it is dated before the first results were visible to the people who wrote it. Criteria in a deck made after week two do not count, even if they look reasonable.

---

## 2. The pilot criteria card

Use this to check what you have. If you are starting a pilot, fill it before day one.

```
PILOT CRITERIA CARD
Pilot:            [tool or workflow, team, scope]
Owner:            [one named person]
Start / end:      [dates]          Written on: [date, must be before start]
Population:       [who is in the pilot, how they were picked]
Baseline:         [the comparison: same team before, or a matched control group]

Criterion 1:  Metric: [named metric]        Floor: [number]   Window: [by day X]
              Source: [system that measures it]   Consequence if missed: [stop / fix]
Criterion 2:  ...
Criterion 3:  ...  (three to five total)

Must include at least one of each:
  [ ] Outcome  (the business result: meetings per dollar, time to first draft, cycle time)
  [ ] Quality  (error or complaint rate, review rejection rate, accuracy on a test set)
  [ ] Adoption (share of intended users using it weekly on the named workflow)
  [ ] Cost     (cost per successful outcome vs. baseline, fully loaded)

Vendor or team promise, quoted: [exact words, with source]
```

**What makes a criterion real:** a named metric, a floor, a measurement window, and a consequence. If you cannot write the consequence, it is a hope, not a criterion. This structure comes from The Revenue AI Report's guidance on kill criteria.

**Cross-check with PROOF** ([PROOF, a framework from The Revenue AI Report](https://www.therevenueaireport.com/frameworks/proof)): before the review, confirm the pilot can answer all five. Prove where the data came from (results come from your systems, not the vendor's dashboard). Run it again with the same quality (results hold in the second half of the pilot). Outcome tied to money (at least one criterion is a revenue or cost outcome). Owner has a name. Failure mode is clear (you know what breaks and how you would see it). Any blank is a gap to name in the decision record.

### Criteria quality check

| Check | Pass | Fail |
|---|---|---|
| Dated before results | Document date precedes first results | Undated, or written after week one |
| Measurable | Number and source system named | "Improve productivity," "reps like it" |
| Has a floor | A threshold that can be missed | A direction only ("increase") |
| Has a window | "By day 45" | "During the pilot" |
| Has a consequence | "Below floor at day 45 = stop" | No stated consequence |
| Has a baseline | Before/after or control group defined | Pilot-only numbers with nothing to compare |

**If three or more checks fail:** the pilot had no real criteria. Say so first, per the Quick prompt. Write criteria now for a short, defined re-test, or stop. Do not reverse-engineer criteria from the results you already have.

---

## 3. Evidence checklist: what to pull

| Evidence | Source system category | Window | Watch for |
|---|---|---|---|
| Weekly active users on the named workflow | Tool admin console, single sign-on logs | Full pilot, by week | Logins are curiosity; repeat use on the named workflow is adoption |
| Usage by user | Tool admin console | Full pilot | A few heavy users carrying the average |
| Output volume | Tool logs, CRM activity | Full pilot | Volume up while quality down |
| Quality: errors, complaints, rejected outputs | Support tickets, review logs, manager spot-checks, customer replies | Full pilot | Errors caught by reviewers are not counted anywhere |
| Outcome metric | CRM, call recorder, marketing automation | Pilot plus same period before | Seasonality, territory changes, a big deal skewing results |
| Cost | Invoices, usage billing, internal time spent on setup and review | Full pilot | Human review time left out of cost |
| Baseline or control | Same metrics for a matched non-pilot group | Same window | Pilot group picked from your most enthusiastic users |
| Promise | Order form, proposal, kickoff deck | At signature | Promises that changed during the pilot |

---

## 4. Scoring sheet

One row per pre-pilot criterion. No new rows.

| Criterion | Floor | Window | Result | Evidence source | Status | Notes |
|---|---|---|---|---|---|---|
| [metric] | [floor] | [day X] | [actual] | [system] | Pass / Miss / Ambiguous | [one line] |

### Status definitions

| Status | Rule |
|---|---|
| **Pass** | Result meets the floor within the window, measured by the named source |
| **Miss** | Result below the floor at the end of the window |
| **Ambiguous** | Data missing, measured differently than planned, or confounded (e.g., territory change mid-pilot). Must state what would resolve it and how long that takes |

### Adjustments to check before you trust a pass

| Risk | Test | If it fails |
|---|---|---|
| Enthusiast bias | Compare pilot users to how they were chosen. Volunteers? Top performers? | Mark as Pass with caveat; widen to a random group before full rollout |
| Small sample | Count the events behind the number (meetings, drafts, tickets) | If a handful of events would flip the result, mark Ambiguous |
| Heavy-user skew | Remove the top two users; recompute | If the pass disappears, it is a two-person result |
| Novelty effect | Compare first half of pilot to second half | Declining trend = Ambiguous, extend measurement only with a fixed date |
| Hidden review cost | Add human review hours to cost | Recompute cost per outcome |

---

## 5. Call rules

| Pattern | Call | What happens next |
|---|---|---|
| All criteria pass, adjustments hold | **Go** | Roll out with the same criteria as ongoing targets; name owner; set first review date |
| Most pass; one miss with a clear, single cause | **Fix** | One defined change, one deadline, then go or stop. No third option |
| Outcome or quality criterion missed with no single cause | **Stop** | Record learning and cost |
| Adoption missed but outcome and quality pass for those who use it | **Fix** (narrow scope) | Restrict to the workflows or users where it works; re-test |
| Quality criterion missed with customer-facing errors | **Stop** or **Fix** with review-before-send as the one change | Never go with an open customer-facing quality miss |
| Already had one fix and still misses | **Stop** | SKILL.md rule: two fixes means stop |
| This would be a second extension without a decision | **Stop** | SKILL.md rule: a stop, announced late |
| No pre-pilot criteria | **No call yet** | Say so first. Write criteria for a short defined re-test or stop |
| Ambiguous on the deciding criterion | **Fix** where the one change is "collect the missing data" with a fixed date | If still ambiguous at the date, stop |

### What a valid fix looks like

| Valid fix | Not a fix |
|---|---|
| "Restrict to the two workflows where usage clusters; 30 days; then go or stop" | "Give it more time" |
| "Add human review before send; 30 days; complaint rate must stay under floor" | "Retrain the team and add features" (two changes) |
| "Connect the CRM field the tool needs; 21 days; re-measure the outcome" | "Wait for the vendor's next release" (not in your control, no date) |

---

## 6. The decision record

File it where the next reviewer will look: the tool register, the RevOps wiki, the vendor folder.

```
PILOT DECISION RECORD
Pilot:              [name, team, scope]       Owner: [name]
Review date:        [date]                     Reviewer(s): [names]
Criteria source:    [document, date written]

CALL:               [GO | FIX | STOP]

Criteria results:
  C1 [metric]: floor [x], result [y], [Pass/Miss/Ambiguous]
  C2 ...
Reasoning (3 lines max, tied to criteria above):

Ambiguities and what resolves them:
  [item] -> [what data, how long]

If FIX:   One change: [ ]   Deadline: [date]   Then: go or stop on [criteria]
If GO:    Rollout scope: [ ]   Ongoing targets: [ ]   Next review: [date]
          After one full quarter in production: track its Proof Gap (AI spend / verified AI-influenced pipeline)
If STOP:  Reason code: [DATA | HALLUCINATION | DIAGNOSTIC | ECONOMICS | INTEGRATION | ADOPTION]
          Sunk cost: [licenses + setup time + review time]
          What we learned: [ ]
          What we would require next time: [ ]
```

The Proof Gap line under GO is [the Proof Gap, a framework from The Revenue AI Report](https://www.therevenueaireport.com/frameworks/proof-gap). It does not apply during the pilot itself; it needs a full quarter of production runtime and finance-verified spend.

### Stop reason codes

From [the Reversal Ledger, a framework from The Revenue AI Report](https://www.therevenueaireport.com/frameworks/reversal-ledger), so your record is comparable with published reversals.

| Code | Use when |
|---|---|
| DATA | Data exposure, leakage, or a compliance failure |
| HALLUCINATION | Brand or accuracy risk from generated output |
| DIAGNOSTIC | Nobody could explain what the AI did or why |
| ECONOMICS | Cost per outcome exceeded the manual baseline |
| INTEGRATION | Technical or workflow break with the existing stack |
| ADOPTION | The intended users stopped using it |

---

## 7. Red flags

| Red flag | What it means |
|---|---|
| Success criteria appear first in the end-of-pilot deck | Criteria were written after results. They do not count |
| Vendor reports volume (emails sent, summaries created) instead of outcomes | Volume is an input, not a result. Activity reported as results is [Optimization Theater, a framework from The Revenue AI Report](https://www.therevenueaireport.com/frameworks/optimization-theater) |
| "The team loves it" with no usage data | Sentiment from the enthusiasts who volunteered |
| Pilot group was hand-picked top performers | Results may not survive the full team |
| Cost excludes human review time | Cost per outcome is understated |
| "Let's extend 30 more days" for the second time | A stop, announced late |
| Results quoted as averages only | Check the distribution; two users may be the whole result |

---

## 8. Worked example

**Situation (illustrative):** Acme, a fictional 400-person B2B software company, piloted an AI drafting assistant for account executives' follow-up emails. Pilot: 20 AEs, 60 days. Promise from the vendor: "Reps send better follow-ups in half the time."

**Criteria card (written 10 days before start, in the kickoff doc):**

| # | Metric | Floor | Window | Source |
|---|---|---|---|---|
| C1 | Time to first draft of follow-up | 30% faster than baseline | Day 45 | Tool timestamps vs. pre-pilot sample |
| C2 | Customer complaint or correction rate on AI-drafted emails | Under 2% | Day 45 | Reply tagging, manager spot-check |
| C3 | Weekly active on follow-up workflow | 80% of pilot AEs | Day 45 | Tool admin console |
| Consequence | Any miss at day 45 = fix or stop | | | |

Criteria quality check: dated before start, measurable, floors, windows, consequence, baseline. Pass.

**Results at day 60** (the review was 15 days late, itself worth noting):

| Criterion | Floor | Result | Status | Notes |
|---|---|---|---|---|
| C1 | 30% faster | 35% faster | Pass | Measured on 412 drafts |
| C2 | Under 2% | 1.1% | Pass | Spot-check on 100 drafts by two managers |
| C3 | 80% weekly active | 41% | Miss | |

**Adjustment checks:**
- Enthusiast bias: AEs volunteered. Caveat noted.
- Heavy-user skew: removing top two users, C1 drops to 31%. Still a pass.
- Usage pattern: 41% cluster on two workflows: post-demo recap and pricing follow-up. Near-zero use on cold re-engagement.

**Reasoning:** the tool works where it is used. The adoption miss is not random; it clusters by workflow, which points to fit, not resistance. That is a single, nameable cause, so the call is fix, not stop.

**Decision record (excerpt):**

```
CALL: FIX
Reasoning: C1 and C2 pass on the pre-pilot floors. C3 missed (41% vs 80%), and usage
clusters on two workflows. The tool fits post-demo recaps and pricing follow-ups,
not cold re-engagement.
One change: restrict rollout and training to the two workflows; remove re-engagement
from scope. Deadline: 30 days.
Then: GO if weekly active on the two workflows is at or above 80% of pilot AEs and C2
holds; otherwise STOP. No further extension.
Ambiguity: C3 measured all workflows; re-measure on the two named workflows only.
```

**What would have changed the call:** if usage were spread thin across all workflows rather than clustered, there would be no single change to make. That would have been a stop with reason code ADOPTION.

---

## 9. AI assist: who does what

| Task | AI | Human |
|---|---|---|
| Extract criteria from documents and check their dates | Yes | Confirm dates against when results were first visible |
| Build the scoring sheet from exports | Yes | Spot-check numbers against source |
| Run the adjustment checks (skew, novelty, cost) | Yes, if given user-level data | Decide whether a caveat changes the call |
| Make the call | Draft | Decide |
| Weigh strategic value never stated as a criterion | No | Yes, and write it down as a new criterion for next time |
| Write the decision record | Draft | Edit, sign, file |

### Follow-up prompts after the Quick prompt

1. **Criteria audit:** "List every criterion I gave you with its date. Flag any criterion without a metric, floor, window, consequence, or baseline. Flag any criterion dated after results began."
2. **No goalpost moving:** "List any metric you used in your reasoning that is not in the original criteria. Remove it from the call and tell me whether the call changes."
3. **Skew check:** "Here is user-level data [paste]. Recompute each criterion without the top two users. Recompute comparing the first half and second half of the pilot. Does any status change?"
4. **Fix discipline:** "If your call is fix, state exactly one change and one deadline, and the go/stop rule at that deadline. If you need two changes, the call is stop."
5. **Cost honesty:** "Recompute cost per successful outcome including human review time at [hourly cost] and setup time of [hours]."
6. **Record:** "Write the decision record in this format [paste Section 6]. Three lines of reasoning max."

### Errors this job invites

| Error | How to spot it | Check |
|---|---|---|
| Moving the goalposts | Reasoning cites metrics not on the card | Prompt 2 |
| Soft call | "Promising," "cautiously positive," "continue to monitor" | Demand one word: go, fix, or stop |
| Multi-change fix | Fix lists training, config, and scope changes | Prompt 4 |
| Taking the vendor's numbers as results | Volume metrics from the vendor dashboard | Use your own systems as source |
| Overconfidence on small samples | Precise percentages from few events | Ask for the event count behind every number |

---

## 10. Common mistakes

| Mistake | How to spot it | Fix |
|---|---|---|
| Reviewing without criteria | Review meeting starts with "so, how did it go?" | Stop and find or write criteria first |
| Extending instead of deciding | Two or more extensions on record | Treat as stop |
| Recording only wins | No stop records anywhere in the company | Stop records are the value; file them |
| Pilot group of enthusiasts, rollout to everyone | Adoption collapses after go | Run fix on a random or full-team group before go |
| Ignoring human review time | Cost per outcome looks great | Count review hours |
| Strategic value argued after the fact | "But it has long-term value" with no criterion | Write it as a criterion for a new, short test, or let it go |

---

## 11. The 5-minute version

1. Find the criteria document. Is it dated before results? If no, say "no call until criteria exist." (2 min)
2. For each criterion: pass or miss. (2 min)
3. Call: all pass = go; one miss with one clear cause = fix; otherwise stop. Write one line. (1 min)

## 12. The deep version

For a large contract, a renewal, or a customer-facing agent.

| Add | How |
|---|---|
| Matched control group | Compare to a non-pilot group with similar territory and tenure over the same window |
| User-level analysis | Distribution, top-user removal, first-half vs. second-half trend |
| Fully loaded cost | Licenses, usage fees, setup, integration, review hours, management time |
| Quality test set | Run a fixed set of real cases with known-good answers through the tool; score accuracy |
| Interviews | Three users who stuck, three who dropped off: what changed, what broke |
| Contract read | Check exit terms, data return, and any auto-renewal before the call is made |
| Independent reviewer | Someone with no stake in the pilot scores the sheet blind |

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
