# Prioritize AI Use Cases: Toolkit

**Use this file when:**
- You are planning a quarter or a half and have more AI ideas than people to build them.
- The loudest stakeholder's idea keeps jumping the queue and you need a method that holds up in the room.
- A vendor demo has created urgency for a use case nobody has scored.
- Several AI projects are running at once and none of them is finishing.

The SKILL.md holds the logic: list everything, score value as a countable outcome, score effort honestly, pick two, park the rest in writing. This file holds the intake sheet, the scoring rubrics, the capacity sheet, the ranking method, and a full worked example.

---

## 1. The sequence

| Step | What you do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1 | Collect every candidate, including the boring ones | Intake sheet (Section 2) | 10 min plus collection |
| 2 | Count real capacity | Capacity sheet (Section 3) | 5 min |
| 3 | Apply the two gates | Gate results (Section 4) | 5 min |
| 4 | Score value, confidence, effort, data, risk | Scoring table (Section 5) | 15 min |
| 5 | Rank and pick two | Ranked list (Section 6) | 5 min |
| 6 | Write the parked list with revisit triggers | Parked list (Section 7) | 5 min |

---

## 2. Intake sheet

One row per candidate. If a field cannot be filled, leave it blank; the blank is information.

| Field | What to write | Example |
|---|---|---|
| Use case | Verb plus object | "Draft account research briefs for AEs" |
| Requested by | Role | VP Sales |
| Problem it solves | In the requester's words | "Reps spend hours on research before first calls" |
| Current workaround | How it is done today | Manual browsing, notes in a doc |
| Outcome metric | One countable number | Research time per account; meetings per AE |
| Baseline exists? | Yes / No / Partly, and source | Partly, from a time sample |
| Data needed | What the AI must read | Account website, CRM history |
| Systems touched | Category | CRM, email |
| Who must change behavior | Roles and headcount | 40 AEs |
| Customer-facing? | Yes / No | No, drafts reviewed by AE |

### Where to find the boring candidates

| Source | What it surfaces |
|---|---|
| RevOps and sales ops request queue, last 90 days | Repeated manual requests |
| Team chat channels where people ask for numbers | Questions an analyst answers by hand each week |
| Manager calendars | Recurring prep meetings (forecast, pipeline, QBR) |
| Rep and CSM time samples | Admin work that crowds out selling |
| Support or CS ticket categories | Tagging, routing, and summarizing work |
| Last two quarters of post-mortems or lost-deal notes | Problems AI might address, and ones it cannot |

**Rule:** the boring candidates often win. They have data, a baseline, and a short path to a countable result.

---

## 3. Capacity sheet

| Person | Role | Share of time available for AI work | Weeks in period | Person-weeks |
|---|---|---|---|---|
| [ ] | [ ] | [ ] | [ ] | [ ] |
| | | | Gross total | [ ] |
| | | | Less interrupts and run-the-business (rule of thumb: 20-30 percent) | [ ] |
| | | | Real capacity | [ ] |

**Capacity rules:**
- Count only named people. "The team will find time" is zero.
- Include the time of the people who must change behavior if training or rollout falls on a manager or enablement.
- A use case that needs more than the real capacity is not cheap because it is exciting. It does not fit.

---

## 4. The two gates

Run these before scoring. A candidate that fails a gate is not ranked against the others; it is routed.

| Gate | Question | If it fails |
|---|---|---|
| Countable within a quarter | Will a number move, and be read, inside one quarter? | Goes behind every candidate that passes (SKILL.md decision rule 1) |
| Data exists | Does the AI have the data it needs today, in a usable state? | Becomes a data project first (SKILL.md decision rule 2). Score the data project, not the AI use case |

---

## 5. Scoring rubrics

### Value (1-5): a measurable outcome, not a story

| Score | Descriptor | Example |
|---|---|---|
| 5 | Moves a revenue driver (pipeline, win rate, retention, deal size) with a baseline in place | Renewal-risk flags acted on before renewal |
| 4 | Removes measurable time or cost on a known constraint, baseline in place | Forecast roll-up that takes managers hours each week |
| 3 | Measurable time saved, not on the binding constraint | Faster first drafts of internal documents |
| 2 | Quality improvement that is hard to count | "Better" emails with no reply-rate baseline |
| 1 | No measurable outcome; a story | "Makes us look innovative" |

### Confidence (multiplier)

| Level | Multiplier (rule of thumb) | When |
|---|---|---|
| High | 1.0 | The mechanism is proven inside your company or on a nearly identical workflow |
| Medium | 0.7 | Plausible, depends on a behavior change you have not tested |
| Low | 0.4 | Value rests on a vendor claim or an untested assumption |

### Effort (1-5): person-weeks including cleanup and behavior change

| Score | Person-weeks (rule of thumb) | Typical shape |
|---|---|---|
| 1 | Under 1 | Shared prompt and a paste kit, no integration |
| 2 | 1-2 | One integration or automation, small group to train |
| 3 | 3-4 | Data cleanup on a few fields, team-wide behavior change |
| 4 | 5-8 | Multiple systems, new review process, manager reinforcement |
| 5 | More than 8 | New data pipeline, customer-facing risk, cross-team change |

**Effort checklist.** Add up each line, not just setup:

| Effort line | Often missed? |
|---|---|
| Setup and configuration | No |
| Data cleanup to make inputs usable | Yes |
| Integration and testing | Sometimes |
| Training on judging output, not just using the tool | Yes |
| Manager reinforcement for the first month | Yes |
| Measurement: baseline and reads | Yes |
| Ongoing ownership after launch | Yes |

### Data dependency

| Status | Meaning | Action |
|---|---|---|
| Have | Data exists, populated, trusted | Proceed |
| Partial | Exists but incomplete or untrusted | Cleanup goes into effort |
| Missing | Not captured, or in a system the AI cannot reach | Data project first |

### Risk if it fails

| Level | Blast radius | Examples |
|---|---|---|
| Low | Internal, easy to reverse | Internal summaries, drafts a human reviews |
| Medium | Bad data enters a system others rely on | Wrong fields in the CRM feeding the forecast |
| High | Customers, brand, or compliance affected; hard to reverse | Automated outbound damaging the sending domain; customer-facing answers |

**Risk rule:** a High-risk candidate needs a written rollback plan and an owner before it can be picked. If neither exists, it is parked.

---

## 6. Ranking

**Priority score = Value x Confidence / Effort.**

Then:
1. Remove candidates that failed a gate. Route them (Section 4).
2. Sort the rest by priority score.
3. Use risk as the tie-breaker: lower risk first.
4. Pick the top two that fit inside real capacity together. Two maximum (SKILL.md decision rule 3).
5. Spend leftover capacity on funding the two properly (adoption, measurement), or on a data project for a gated candidate. Not on a third use case.

The score ranks; it does not decide. The numbers are structured judgment, and the ranking matters more than the decimals.

### Ranked list template

```
AI USE CASE PRIORITIES: [Team], [Period]       Real capacity: [ ] person-weeks

| Rank | Use case | Value | Conf | Effort | Score | Countable in qtr | Data | Risk | Decision |
|------|----------|-------|------|--------|-------|------------------|------|------|----------|
|      |          |       |      |        |       |                  |      |      | Start / Data project / Park / Defer / Kill |

START (two maximum)
1. [Use case]  Outcome metric: [ ]  Baseline: [ ]  Owner: [ ]  Read date: [ ]  Kill if: [ ]
2. [Use case]  Outcome metric: [ ]  Baseline: [ ]  Owner: [ ]  Read date: [ ]  Kill if: [ ]

DEFER, the exciting one: [Use case] because [reason]
DATA PROJECTS: [ ]
TRADE-OFFS MADE FOR POLITICAL REASONS: [What was picked over what, and what it costs]
```

---

## 7. Parked list

Write it down (SKILL.md process step 4). Revisit only when one of the two ships or dies (process step 5).

| Parked use case | Why parked | What would change that | Revisit trigger |
|---|---|---|---|
| [ ] | Low score / failed gate / no capacity / high risk | [Data project done, baseline captured, capacity added] | [Pick 1 ships or dies, or a dated event] |

---

## 8. Decision table

| If | Then |
|---|---|
| The loudest stakeholder's idea scores low | Show the score sheet; offer the revisit trigger; record it as parked, not rejected |
| An executive overrides the ranking | Do it, and write the trade-off: which pick it displaced and what that costs |
| A vendor demo created urgency | Score it like any other candidate; confidence is Low until proven in-house |
| Two candidates tie | Lower risk first; then the one with the earlier read date |
| A top pick needs data you do not have | Pick the data project instead; the AI use case waits |
| Real capacity fits only one | Start one. Do not start two underfunded |
| A team already runs three AI projects | Stop or park one before starting anything |
| Nothing passes the countable gate | Pick the candidate with the shortest path to a baseline and make measurement the first deliverable |

---

## 9. Red flags

| Red flag | What it usually means | Do this |
|---|---|---|
| Every candidate scores Value 5 | Scores are stories, not countable outcomes | Rescore with the rubric's examples beside you |
| Effort is all setup | Cleanup and behavior change missed | Fill the effort checklist |
| No candidate has a baseline | Nothing can be proven this quarter | Make baseline capture a deliverable of pick 1 |
| Three or more "active" picks | None is funded | Cut to two |
| The parked list lives in someone's head | It will be re-litigated every week | Publish it with revisit triggers |
| A customer-facing pick with no rollback plan | High blast radius, no exit | Park until an owner and rollback plan exist |
| Picks owned by "the team" | Nobody is accountable | One named owner per pick |

---

## 10. Worked example: Acme

*Illustrative. Acme is a fictional 400-person B2B software company. RevOps is planning next quarter.*

**Capacity.** One RevOps analyst at half time and one GTM engineer at a quarter time, for 13 weeks: 9.75 person-weeks gross. Less 25 percent for interrupts: about 7 person-weeks real.

**Candidates (eight, including the boring ones):**

| # | Use case | Value | Conf | Effort (1-5) | Score | Countable in qtr | Data | Risk |
|---|---|---|---|---|---|---|---|---|
| 1 | Account research briefs for AEs | 3 | 1.0 | 2 | 1.50 | Yes | Have | Low |
| 2 | Forecast roll-up automation | 4 | 1.0 | 3 | 1.33 | Yes, in 4 weeks | Partial: stage fields need cleanup, included in effort | Medium |
| 3 | Support-ticket tagging | 2 | 1.0 | 2 | 1.00 | Yes | Have | Low |
| 4 | Call summaries into CRM fields | 4 | 0.7 | 3 | 0.93 | Yes | Have | Medium |
| 5 | Renewal-risk scoring | 5 | 0.7 | 5 | Gated | No, needs a renewal cycle | Missing: product usage not in CRM | Medium |
| 6 | AI outbound sequencing | 4 | 0.4 | 5 | 0.32 | Unclear | Partial | High: domain reputation |
| 7 | AI-drafted proposals | 2 | 0.7 | 3 | 0.47 | Yes | Partial | Medium |
| 8 | Natural-language answer layer for the CRO | 3 | 0.7 | 5 | Gated | No, metric definitions not frozen | Partial | Medium |

**Reasoning.**
- Gates first. Renewal-risk scoring fails the data gate: usage data is not in the CRM. It becomes a data project. The answer layer fails the countable gate: metric definitions are still argued about, so no answer could be trusted this quarter.
- Ranking the rest: research briefs (1.50) and forecast roll-up (1.33) lead. Research briefs need about 2 person-weeks (prompt, paste kit, rollout to 40 AEs, baseline sample); the roll-up about 4 (stage-field cleanup, automation, manager training). Together about 6, inside the 7 available.
- Call summaries score well on value but carry Medium confidence because 40 reps must confirm fields every call, an untested behavior change. Parked, first in line.
- Ticket tagging is cheap and safe but low value. Parked; a candidate when capacity frees up.
- AI outbound sequencing is the exciting one. Value rests on a vendor claim (Low confidence), effort exceeds capacity, and a failure damages the sending domain, not just the quarter.

**Ranked list output.**

START
1. Account research briefs. Outcome: research time per first meeting, and first meetings per AE. Baseline: two-week time sample this month. Owner: sales enablement lead. Read date: week 6. Kill if: no change in research time after 4 weeks of use.
2. Forecast roll-up automation. Outcome: manager hours on forecast prep per week. Baseline: current 6 hours per manager. Owner: RevOps analyst. Read date: week 4 after launch. Kill if: managers still rebuild the roll-up by hand after 4 weeks.

DEFER, the exciting one: AI outbound sequencing, because value is unproven in-house, effort is over capacity, and the downside is domain reputation.

DATA PROJECT: pipe product usage into the CRM, next quarter, so renewal-risk scoring can pass the data gate.

PARKED: call summaries (revisit when pick 1 or 2 ships), ticket tagging, AI-drafted proposals, answer layer (revisit when metric definitions are signed off).

TRADE-OFF: the CRO asked for the answer layer. If the CRO overrides, the forecast roll-up moves to parked, and the first deliverable of the answer layer becomes signed metric definitions, not a launch. Written and shared with the CRO.

---

## 11. AI assist

| Work | AI assistant | Human |
|---|---|---|
| Turn a messy list of ideas into intake rows | Yes | Fill the blanks only you know |
| Propose value, effort, and risk scores | Draft | Change any score you disagree with; you know the data and the people |
| Fill the effort checklist per candidate | Yes | Check cleanup and behavior change are not zero |
| Compute scores and sort | Yes | Recompute the top four yourself |
| Choose the two picks | Draft | Decide, including the political trade-off |
| Write the parked list and trade-off note | Draft | Own the wording; it will be read by the stakeholders |

**Follow-up prompts to use after the Quick prompt:**

1. "For each use case, apply two gates: is the result countable within one quarter, and does the needed data exist today? List any that fail and what data project would unblock them."
2. "Score each remaining use case: value 1-5 using [paste the value rubric], confidence High, Medium, or Low with multipliers 1.0, 0.7, 0.4, and effort 1-5 in person-weeks including data cleanup, training, and manager reinforcement. Show the effort breakdown."
3. "My real capacity is [N] person-weeks. Which two fit together inside it? Show the total."
4. "Argue against your top pick as a skeptical CFO would. What would make it fail?"
5. "Write the parked list with one revisit trigger per item, and a two-line trade-off note for [stakeholder] explaining why their idea is parked."

**Check the AI's output for these errors:**

| Error this job invites | How to catch it |
|---|---|
| Inflated value from vendor-style claims | Every Value 4-5 has a baseline and a named metric |
| Effort counts setup only | The effort breakdown includes cleanup, training, reinforcement |
| More than two picks | Count the "start" items |
| Gated candidates ranked anyway | Check failed-gate items sit outside the ranking |
| Arithmetic errors in scores | Recompute the top four |
| Generic risk ("adoption risk") | Each risk names what breaks and who sees it |

---

## 12. Common mistakes

| Mistake | How to spot it | Fix |
|---|---|---|
| Ranking by excitement | Top picks match the most recent demo | Apply gates and rubric first |
| Ignoring data cleanup | Picks stall in week 3 on bad fields | Data status column, effort checklist |
| Starting three or more | Every project at 60 percent | Two maximum, fund them fully |
| Parking verbally | Same debate every planning meeting | Written parked list with triggers |
| Value as a story | "Transforms how reps work" | Rewrite as one countable number |
| No kill criteria on the picks | Projects never end | Write "kill if" with a date for each |
| Hidden political picks | Ranking and picks do not match | Write the trade-off explicitly |

---

## 13. The 5-minute version

1. List every candidate on one page.
2. Cross out any whose result cannot be counted this quarter, and any that need data you do not have (note those as data projects).
3. For the rest, write one countable outcome and a rough person-week effort, including cleanup and training.
4. Pick the two with the best outcome-to-effort trade-off that fit your real capacity together.
5. Write the rest as parked, with the trigger to revisit.

## The deep version

For half-year planning or when the picks will be contested:
- Collect candidates from every source in Section 2, not just the people in the room.
- Run a two-week time sample on the top five candidates' workflows to set baselines before scoring.
- Have two people score independently, then compare; discuss any score that differs by 2 or more.
- Review the ranking with finance and with the managers whose teams must change behavior.
- Write kill criteria and a read date for each pick before work starts.
- Publish the ranked list, parked list, and trade-offs where every stakeholder can see them, and revisit only on the written triggers.

---
*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
