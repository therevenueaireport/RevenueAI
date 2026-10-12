# Set AI Pilot Kill Criteria: Toolkit

**Use this file when:**
- A vendor demo went well and someone wants to sign a pilot this week.
- A stakeholder says "let's just try it and see."
- A pilot is already running and nobody can say what result would end it.
- You are writing the order form and want the fail conditions in the contract, not in a slide.

The SKILL.md holds the logic. This file holds the instruments: the anatomy of a criterion, a criteria bank by pilot type, threshold-setting methods, a kill-condition coverage check built on the Reversal Ledger's reason codes, the charter template, and a worked charter.

---

## 1. The Charter Session

| Step | What you do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1 | Write the goal as one number, with its baseline | Goal line | 5 min |
| 2 | Pick 3-5 pass criteria from the bank (Section 4) | Draft criteria | 5 min |
| 3 | Set each threshold and record why | Threshold log | 10 min |
| 4 | Name the data source and checker for each | Measurement plan | 5 min |
| 5 | Write 2+ automatic kill conditions and the off switch | Kill list | 5 min |
| 6 | Book the decision meeting; get the signature | Signed charter | Before day one |

**Stop rule:** if Step 1 cannot be written, the pilot does not start. Say so in writing.

---

## 2. Anatomy of a Criterion

A criterion has five parts. Missing any one, it is a hope, not a criterion.

| Part | Question | Example |
|---|---|---|
| Metric | What exactly is counted? | Qualified meetings held per dollar of pilot spend |
| Threshold | What value passes or fails? | At or above human baseline by day 60 |
| Window | Measured over what period? | Rolling 4 weeks, checked weekly |
| Source | Which system, which report, who pulls it? | CRM meeting report, RevOps, Mondays |
| Consequence | What happens when it fails? | Pilot ends; no renewal conversation |

### Pass criteria vs. kill conditions

| | Pass criterion | Kill condition |
|---|---|---|
| Judged when | At the decision meeting | The moment it trips |
| Purpose | Proves the tool earned production | Stops harm regardless of other results |
| Typical metric | Efficiency, quality, conversion | Complaints, compliance, data exposure, runaway cost, brand damage |
| Who acts | The decider | Anyone named, without a meeting |
| Overridden by | Kill conditions | Nothing |

---

## 3. Inputs Checklist

| Input | Where it lives | Lookback | Why |
|---|---|---|---|
| Baseline for the goal metric | CRM, BI dashboard, engagement platform | Two prior quarters | Thresholds are relative to the baseline |
| Normal weekly variance of that metric | Same | 12+ weeks | A threshold inside normal noise passes or fails by luck |
| Fully loaded pilot cost | Order form, internal hours estimate | Pilot period | Per-dollar metrics need the real denominator |
| Data the tool will touch | Vendor documentation, IT review | Current | Shapes the kill conditions |
| Existing compliance limits | Legal, marketing ops | Current | Do-not-contact lists, consent rules, retention |
| Decider's calendar | Their assistant | Pilot end date | The meeting gets booked now |

---

## 4. Criteria Bank by Pilot Type

Pick from these. Adapt the threshold to your baseline. Every threshold below is a starting rule of thumb, not a benchmark.

### Outbound and prospecting agents

| Type | Metric | Starting threshold |
|---|---|---|
| Pass | Qualified meetings held per fully loaded dollar, vs. human baseline | At parity by mid-pilot, clearly above by the end |
| Pass | Meeting-to-opportunity conversion vs. human-sourced meetings | Within a stated band of baseline (e.g., not more than 20 percent below) |
| Pass | Share of sequences needing no manual repair | Majority by mid-pilot, rising |
| Pass | Weekly random audit of sent messages (factual accuracy, offer fit, tone) | Pass rate at or above a bar set before launch |
| Kill | Spam complaint or unsubscribe rate | Above your sending-domain safety limit in any week |
| Kill | Any send to a suppression or do-not-contact list | One instance |
| Kill | Sending-domain reputation drop | Any warning from your deliverability monitoring |

### Drafting and assistant tools (email, call summaries, proposals)

| Type | Metric | Starting threshold |
|---|---|---|
| Pass | Weekly active use among assigned users, not volunteers | Majority of assigned users by mid-pilot |
| Pass | Edit rate on outputs before use | Falling across the pilot |
| Pass | Factual error rate on a seeded or sampled set | Below a bar set before launch |
| Pass | Named reinvestment of time saved, measured | Hours redirected to a named revenue activity, counted |
| Kill | Customer-facing factual error with commercial impact | One instance |
| Kill | Sensitive data sent outside approved boundaries | One instance |

### Forecasting, scoring, and analytics tools

| Type | Metric | Starting threshold |
|---|---|---|
| Pass | Accuracy vs. the current method on the same deals | Better than current method at a fixed horizon |
| Pass | Explainability: share of outputs a manager can trace to inputs | Majority |
| Pass | Decision change: number of decisions made differently because of it | Counted and logged |
| Kill | Output cannot be explained when challenged | Repeated on material deals |
| Kill | Writes to live CRM fields without approval | One instance |

### Customer-facing agents (support, success, chat)

| Type | Metric | Starting threshold |
|---|---|---|
| Pass | Resolution without escalation, on a defined set of intents | Above a stated rate |
| Pass | Customer satisfaction on agent-handled cases vs. human | Not below a stated band |
| Kill | Wrong answer on pricing, contract, or policy | One instance reaching a customer |
| Kill | Escalation path fails (customer cannot reach a human) | One instance |

### Criteria to refuse

| Proposed criterion | Why refuse it | Replace with |
|---|---|---|
| "Reps like it" | No threshold, no source | Weekly active use among assigned users |
| Volume of emails, touches, or summaries | Volume is an input, not an outcome | Outcome per dollar |
| Hours saved | Time saved is not revenue unless it is redirected | Hours saved and where they went, counted |
| Headcount reduction | The cut-staff business case tends to end in rehiring | Capacity redirected to named work |
| Vendor-reported metrics only | Grading their own homework | Your system as source |

---

## 5. Setting Thresholds

Record the method used for every threshold. The SKILL.md limitation is real: thresholds are judgment calls.

| Method | Use when | How |
|---|---|---|
| Baseline-relative | You have 2+ quarters of history | Threshold = baseline plus the lift that covers cost, outside normal weekly variance |
| Break-even | The tool replaces spend | Threshold = the value at which cost per outcome equals current cost per outcome |
| Floor from policy | Compliance, brand, legal | Threshold set by the policy owner, not the pilot owner |
| Decider's line | No history exists | Ask the decider: "What number would make you stop?" Write their answer verbatim |

**Variance check:** if the proposed threshold sits inside the baseline's normal weekly range, it will pass or fail by noise. Widen the window or raise the threshold.

**Volunteer correction:** pilots staffed with volunteers on clean data overstate production results. Either assign the pilot group, or require a stricter threshold and a second assigned-cohort check before scale.

---

## 6. Kill Condition Design

| Test | Pass |
|---|---|
| Automatic | Trips on a monitored signal, not on someone's opinion |
| Fast | Detectable within a day or a week, not at the pilot's end |
| Owned | One named person can stop the tool without a meeting or vendor ticket |
| Rehearsed | The off switch was tested once before day one |
| In the contract | The order form says the pilot ends, without penalty, when it trips |

**Minimum set (rule of thumb):** one harm condition (complaints, wrong answers to customers, compliance breach) and one cost condition (spend ceiling or cost per outcome far above baseline).

### Coverage check against the Reversal Ledger reason codes

The Reversal Ledger, a framework from The Revenue AI Report ([framework](https://www.therevenueaireport.com/frameworks/reversal-ledger)), is a running record of AI tools revenue teams have shut off, coded by why. Its six reason codes are the ways tools actually die in production, so use them to check that your kill conditions and pass criteria cover each one that applies to this tool.

| Reason code | What it means | Covered in this charter by |
|---|---|---|
| DATA | Data exposure, leakage, or compliance failure | Kill: sensitive data outside approved boundary; send to a suppression list |
| HALLUCINATION | Brand or accuracy risk from generated output | Kill: wrong price, term, or policy reaching a customer; pass: audit error rate |
| DIAGNOSTIC | Nobody can explain what the AI did or why | Pass: explainability share; kill: output cannot be explained when challenged |
| ECONOMICS | Cost per outcome exceeds the manual baseline | Pass: outcome per fully loaded dollar; kill: spend ceiling |
| INTEGRATION | Technical or workflow break with the existing revenue stack | Kill: writes to live fields without approval; pass: sequences needing no manual repair |
| ADOPTION | Reps or CSMs stopped using it | Pass: weekly active use among assigned users |

**Rule:** if a code applies to this tool and nothing in the charter would catch it, add a criterion or write down why the risk is accepted. Before signing, check whether the tool or its category already appears in the live Ledger, and read the reason; a tool's presence reflects specific implementations that failed, not a verdict on the category.

---

## 7. Decision Table and Red Flags

| If | Then |
|---|---|
| Nobody can state the goal as a number | Do not start. Write "pilot declined: no measurable goal" |
| A criterion has no data source | Delete it. Do not keep it as a stretch |
| The vendor is the only source for a metric | Add a criterion from your own system, or treat the vendor number as unverified |
| The decider will not sign before day one | The pilot has no decider. Escalate or decline |
| Pass criteria met, kill condition tripped | Stop. Kill overrides pass |
| Mixed result at the decision meeting | Default is stop. Extension only with new written criteria and a new date |
| Vendor asks to extend "to get more data" | Only if the charter set a sample size that has not been reached |
| Usage high, outcome flat | The tool is liked, not working. Fails on outcome |

| Red flag | What it means |
|---|---|
| Charter written after the pilot starts | Criteria will be fitted to results |
| Decision date "to be scheduled" | It will drift into a renewal |
| All criteria are usage metrics | Nothing tests whether revenue moved |
| No kill conditions, "we'll keep an eye on it" | Nobody can stop it |
| Business case depends on cutting staff | Refuse the framing; measure capacity redirected |
| Pilot group hand-picked | Expect production results below pilot results |

---

## 8. Charter Template

```
AI PILOT CHARTER

Tool / vendor:          [tool, category]
Workflow it changes:    [one sentence]
Goal (as a number):     [metric] from [baseline, with n and period] to [target] by [date]
Pilot period:           [start] to [end]   Length: [days]
Fully loaded cost:      [licence + implementation + internal hours]
Pilot group:            [who; assigned or volunteer; size]
Comparison group:       [who stays on the current process]
Decider:                [one name, one title]

PASS CRITERIA (3-5; all must pass unless stated)
| # | Metric | Threshold | Window | Source / checker | Why this number |
| 1 |        |           |        |                  |                 |

KILL CONDITIONS (2+; any one ends the pilot)
| # | Condition | Detected by | Who stops it | Off switch tested on |
| 1 |           |             |              |                      |

MEASUREMENT PLAN
Weekly pull:   [day, who, which report]
Weekly audit:  [random sample size, scored on what, by whom]
Shared with:   [decider, process owner]

DECISION MEETING
Date / time:   [booked today, does not move]
Attendees:     [decider plus the measurement owner]
Possible outcomes: Go to production / Stop / Extend with new written criteria only

CONTRACT TERMS (confirm in the order form)
- Pilot ends without penalty if a kill condition trips
- No auto-renewal into a paid term without the decision meeting outcome
- Your data, logs, and outputs returned or deleted on stop

Signed:        [decider, date, before day one]
```

---

## 9. Worked Example (illustrative)

**Company:** Acme, a 400-person B2B software company. **Tool:** an AI drafting assistant for customer success managers, writing renewal-risk follow-ups after calls. **Pilot:** 60 days. **Cost:** licence plus about 20 internal hours. **Decider:** VP Customer Success.

**Goal as a number.** First attempt: "CSMs save time." Rejected, not an outcome. Second: "Follow-up sent within one business day after at-risk calls rises from the current 45 percent (n=140 calls, last two quarters) to 75 percent." Accepted, because the renewal team already links slow follow-up to churn on at-risk accounts.

**Pass criteria.**

| # | Metric | Threshold | Window | Source | Why this number |
|---|---|---|---|---|---|
| 1 | Follow-up within one business day on at-risk calls | 75% or higher | Last 4 weeks of pilot | CRM activity report, RevOps | Baseline weekly range was 35-55%; 75 sits well outside noise |
| 2 | Factual errors in a random weekly sample of 10 drafts | No more than 1 per sample, last 4 weeks | Weekly | CS manager audit sheet | Any higher and CSMs stop trusting it |
| 3 | Weekly active use among the 8 assigned CSMs | 6 of 8 by day 30 | Weekly | Tool admin log | Assigned, not volunteers, so this tests real adoption |
| 4 | Hours saved redirected to proactive outreach on yellow accounts | Outreach count up, logged | Pilot period | CRM task report | Time saved only counts if it goes somewhere |

**Kill conditions.**

| # | Condition | Detected by | Who stops it |
|---|---|---|---|
| 1 | Any draft sent to a customer stating a wrong price, term, or commitment | CSM flag plus weekly audit | CS operations lead, same day |
| 2 | Customer data sent outside the approved data boundary | IT log review | IT security lead, same day |

**Reasoning.** Criterion 3 was kept despite being a usage metric because the group is assigned; usage from conscripts says more than usage from volunteers. A vendor-proposed criterion, "drafts generated per week," was refused as volume. A proposed criterion, "CSM satisfaction survey," was deleted: no baseline and no threshold anyone would act on.

**Outcome at day 60 (illustrative).** Criterion 1: 71 percent. Criteria 2-4 passed. No kill condition tripped. **Decision:** stop, per the charter. The VP chose to run a new 45-day pilot with a rewritten workflow step, new written criteria, and a new date, rather than extend the old one. The charter made "close enough" a decision instead of a drift.

---

## 10. AI Assist

### Split the work

| Task | AI assistant | Human |
|---|---|---|
| Draft criteria from the goal | Yes | Delete any without a source you actually have |
| Suggest kill conditions for this tool type | Yes | Confirm each can be detected fast |
| Set thresholds | Suggest methods only | Set numbers from your baseline; record why |
| Write the charter document | Yes | Decider reads and signs |
| Draft contract language | First pass | Legal reviews |

### Follow-up prompts (use after the Quick prompt)

1. "For each criterion, name the exact system and report the number comes from. If you are not sure we have it, mark it UNVERIFIED."
2. "Here is our baseline and its weekly range for the last 12 weeks: [paste]. Flag any threshold that falls inside the normal range."
3. "Which of these criteria measure volume or usage rather than an outcome? Replace each with an outcome per dollar or a quality measure."
4. "For each kill condition, describe how it would be detected within one week and who could stop the tool without a meeting."
5. "Write three clauses for the order form: pilot ends without penalty on a kill condition, no auto-renewal without the decision meeting, and data return on stop."

### Check the AI's output for these errors

| Error this job invites | How to catch it |
|---|---|
| Criteria for data you do not collect | Prompt 1; check each source yourself |
| Benchmarks presented as facts | Ask where each number comes from; replace with your baseline |
| Usage and volume dressed as success | Prompt 3 |
| Kill conditions that need a meeting to trigger | Prompt 4 |
| More than five pass criteria | Cut to the 3-5 the decider would act on |
| Vague decision outcomes ("evaluate next steps") | Outcomes must be go, stop, or extend with new written criteria |

---

## 11. Common Mistakes

| Mistake | How to spot it | Fix |
|---|---|---|
| Criteria written to match early results | Charter dated after day one | Write and sign before day one |
| Decider gives a nod, not a signature | No signed copy | Get the signature or decline |
| Threshold without a reason | "Why this number" column empty | Record the method from Section 5 |
| Kill switch never tested | Nobody has pressed it | Test once before launch |
| Extension by default | Decision meeting ends in "more data" | Extension needs new written criteria and a date |
| Volunteer pilot, production rollout | Pilot group self-selected | Assign the group or add an assigned-cohort check |

---

## 12. Two Versions

### 5-minute version
1. Write the goal as one number with its baseline.
2. Three pass criteria, each with a threshold and a source.
3. Two kill conditions: one harm, one cost.
4. Book the decision meeting. Send the charter to the decider and get a written yes.

### Deep version (contract over a material sum, customer-facing, or autonomous)
- Baseline from two prior quarters with weekly variance, and a comparison group.
- Assigned pilot group, not volunteers.
- Weekly random audit of outputs with a scored sheet and a named reviewer.
- Kill conditions written into the order form; off switch rehearsed.
- Fully loaded cost including internal hours, so per-dollar metrics are honest.
- Data return and deletion terms agreed with legal.
- A pre-agreed scale plan: what production looks like if it passes, so a pass leads to a decision, not another pilot.
- After a full quarter in production (not during the pilot, which is too short), track the Proof Gap, a framework from The Revenue AI Report ([framework](https://www.therevenueaireport.com/frameworks/proof-gap)): total AI spend divided by verified, incremental AI-influenced pipeline, on a rolling four-quarter view. The framework treats under 1.0x as defensible, 1.0x to 4.0x as a watch, and over 4.0x as the trigger for a Reversal Ledger review. Write the production kill threshold into the scale plan now, so the go decision carries its own exit.

---
*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
