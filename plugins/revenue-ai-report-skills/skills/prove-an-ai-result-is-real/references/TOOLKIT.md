# Prove an AI Result Is Real: Toolkit

**Use this file when:**
- An AI result is going into a board or executive update and you need it to survive a question from finance.
- A vendor case study is being used to justify a renewal or an expansion.
- One strong month is being described as a trend.
- You are the skeptic in the room and want a fair, repeatable way to test a claim instead of an argument.

The SKILL.md holds the logic: five checks, a verdict, the next piece of evidence, a board paragraph. This file holds the claim intake card, the pass/partial/fail descriptors, the comparison and noise tests, the board-language rules, and a full worked example.

---

## 1. The sequence

| Step | What you do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1 | Write the claim exactly as made | Claim intake card (Section 2) | 5 min |
| 2 | Score the five checks | Scorecard (Section 3) | 15 min |
| 3 | Run the comparison and noise tests | Confounder list, noise read (Section 4) | 10 min |
| 4 | Assign the verdict | Verdict (Section 5) | 2 min |
| 5 | Pick the single next piece of evidence | Next evidence with owner and date (Section 6) | 3 min |
| 6 | Write the board paragraph | Paragraph (Section 7) | 5 min |
| 7 | Review with one person who did the work | Corrections | Before sharing |

---

## 2. Claim intake card

Thin input produces a confident, wrong answer (SKILL.md process step 1). Fill every line before scoring.

```
CLAIM INTAKE CARD
Claim, verbatim:          ["The AI SDR generated 40 percent more meetings in August"]
Who made the claim:       [Internal team / vendor / analyst / a manager in a meeting]
The exact number:         [Value, unit, and the two numbers it was calculated from]
Metric definition:        [How the system defines it, e.g. "meeting = held, not booked"]
Time window:              [Start and end dates]
Comparison period:        [What it was compared with, and why that period]
Source system:            [CRM, call recorder, billing, product analytics, survey, vendor dashboard]
Model and inputs known?:  [Which model or tool version, what prompt or configuration, what data it read]
Owner, by name:           [A person, not a team or a tool]
Failure line written?:    [Yes, with the line / No]
What else changed:        [Hiring, events, pricing, territories, campaigns, comp, definitions]
Sample size:              [Count of events behind the number in each period]
```

**Rule:** if "the two numbers it was calculated from" cannot be filled, stop. A percentage without its numerator and denominator cannot be checked.

---

## 3. The five-check scorecard

The five checks follow the SKILL.md process steps 2-6. The Quick prompt words two of them differently: "the number comes from a system rather than a survey" is tested inside Provenance, and "the comparison period holds" is tested in Section 4 and applies to every verdict.

| Check | Pass | Partial | Fail |
|---|---|---|---|
| 1. Provenance | Number comes from a system of record; definition unchanged across both periods; model, configuration, and inputs are known | System number, but the definition, data hygiene, or configuration changed during the window | Survey, self-report, or vendor dashboard only; or model and inputs unknown |
| 2. Repeatability | Result held in two or more independent runs, periods, or teams | Two runs, but the second is too short or too small to read | One instance. An anecdote (SKILL.md decision rule 1) |
| 3. Outcome tied to money | Metric is revenue, retention, gross margin, win rate, or cycle time | An input with a measured, stable link to an outcome (e.g. meetings with a known meeting-to-opportunity rate) | Activity only: emails sent, drafts, hours saved, logins |
| 4. Named owner | One named person owns the outcome and will be asked about it | A named person owns the tool, not the outcome | A team, a vendor, or nobody (SKILL.md decision rule 2) |
| 5. Failure mode written | A kill or replace line was written before the result came in | A line exists but was written after, or is vague ("if it does not work") | No line. The result cannot be falsified (SKILL.md decision rule 3) |

### Provenance checklist: is the system number telling the truth?

A system number can still be wrong if the record drifted from reality. Check these before giving Provenance a pass.

| Drift point | What to check |
|---|---|
| Stage definitions | Did exit criteria or stage names change during either period? |
| Amount fields | Is the same amount field (ARR, total contract value, list price) used in both periods? |
| Closed-lost handling | Was there a bulk cleanup that closed stale opportunities in one period? |
| Meeting or activity definitions | Booked vs held; logged automatically vs manually |
| Attribution fields | Who or what sets the "AI-sourced" flag, and when? |
| Backfills | Was data imported or corrected after the fact for one period only? |
| Model or configuration | Did the tool version, prompt, or settings change mid-window? |

---

## 4. Comparison and noise tests

### Is the comparison period fair?

| Comparison used | Strength | Watch for |
|---|---|---|
| Holdout group in the same period | Strong | Groups must be similar before the AI started |
| Staggered start across teams | Good | Teams differ in mix; compare each to its own pre-period too |
| Same period last year | Moderate | Market, pricing, and headcount changed in a year |
| Prior month or quarter | Weak | Seasonality, quarter-end effects, one-off events |
| "Before we had the tool," undefined | Very weak | Baseline often picked after the result |
| Vendor's other customers | Not a comparison | Different companies, selected success stories |

### Confounder checklist

List everything that changed in the window. Each one is a competing explanation the claim must account for.

| Category | Examples |
|---|---|
| People | New hires, departures, ramped cohort, manager changes |
| Demand | Events, campaigns, launches, seasonal peaks, a competitor's exit |
| Commercial | Pricing, discount policy, packaging, promotions |
| Coverage | Territory changes, account reassignments, new segments |
| Incentives | Comp plan, spiffs, quotas |
| Measurement | Definition changes, cleanups, new tracking |
| Selection | Who got the tool first (often the best performers) |

### Noise test: is the change bigger than normal variation?

1. Pull the same metric for the last 6-12 periods before the AI.
2. Note the lowest and highest value.
3. If the claimed value sits inside that range, it is not distinguishable from a normal period. Say so.

**Sample size rule of thumb:** when either period rests on fewer than about 30 events (deals closed, meetings held), treat any change as directional only. A swing of a few deals moves the percentage a lot.

**Regression to the mean:** if the AI was started because the prior period was unusually bad, some recovery was likely anyway. Ask why the start date was chosen.

---

## 5. Verdict

| Verdict | Rule of thumb | What you may say |
|---|---|---|
| Real | Passes all five checks, comparison fair, change outside normal variation | "Repeatable result, owned, with a written failure line" |
| Promising | At least three passes, no fail on Provenance or Repeatability, confounders named | "Early result; a second run is under way" |
| Anecdote | Fails Repeatability, or the change sits inside normal variation | "One good period; not yet a result" |
| Not supported | Fails Provenance, or a confounder explains the change as well as the AI does | "We cannot attribute this change to the AI" |

**Rule:** the verdict tests the strength of the claim, not the value of the tool (SKILL.md limitation). An "Anecdote" verdict does not mean stop the tool. It means stop saying the result.

---

## 6. The single next piece of evidence

Find the weakest check, then pick the one piece of evidence that would move it to pass.

| Weakest check | Evidence that moves it |
|---|---|
| Provenance | Recompute both periods from the system of record with one fixed definition; finance confirms the source |
| Repeatability | A second run in a new period or team, with the same definition and the known confounders held out |
| Outcome tied to money | The conversion from the activity metric to the outcome, measured on the same records |
| Named owner | A person accepts ownership of the outcome in writing |
| Failure mode | A kill or replace line written now, before the next run reads |
| Comparison | A holdout group or staggered start for the next period |

Write it as: **[Evidence], owned by [name], read on [date].**

---

## 7. Board paragraph

### Template

```
[Metric] moved from [before] to [after] over [window], measured in [system].
[What else changed in the window, named.]
[What we can and cannot attribute to the AI, in one sentence.]
[The next run: what, who, when, and the line at which we stop or replace it.]
```

### Words the evidence must earn

| Word or phrase | Allowed only when |
|---|---|
| "Proven," "caused," "drove" | Verdict is Real, with a holdout or staggered comparison |
| "Trend" | Three or more periods in the same direction |
| "ROI" or "return" | Revenue or savings verified by finance, not hours saved |
| "Up to X percent" | Never. It reports the best case as the result |
| "Transformed," "game-changing" | Never in a board paragraph |
| "Early," "directional," "not yet isolated" | Use freely; they are honest |

**Finance test (SKILL.md quality check):** read the paragraph as the CFO. If any sentence invites "how do you know?", either answer it in the paragraph or remove the sentence.

---

## 8. Vendor case study checklist

| Question | Why it matters |
|---|---|
| What were the two numbers behind the percentage? | Percentages hide small bases |
| Over what window, compared with what? | Prior-month comparisons flatter |
| What else changed at that customer? | Case studies rarely list confounders |
| Is the metric an outcome or an activity? | Activity gains rarely survive as revenue |
| How many customers tried it, and is this the best one? | Case studies are selected successes |
| Can we speak to the person who owned the result there? | Tests whether an owner existed |
| Would the result reproduce on our data quality? | Their CRM is not your CRM |

**Rule:** a vendor case study can justify a test. It cannot justify a renewal or expansion on its own.

---

## 9. Red flags

| Red flag | What it usually means | Do this |
|---|---|---|
| Only a percentage, no base numbers | Small base or cherry-picked window | Ask for numerator and denominator |
| "In our best region" or "top reps" | Selection effect | Ask for all users and non-users |
| Result announced the week it happened | No time to check provenance | Run the scorecard before it goes further |
| Survey says "saves time" | Perception, not result (SKILL.md decision rule 4) | Find the system metric |
| Comparison is the worst prior month | Regression to the mean | Use the prior 6-12 periods' range |
| Metric definition changed in the window | Apples to oranges | Recompute both periods on one definition |
| "The tool owns it" | No accountable person | Name an owner before the next read |
| Every AI claim this year was a success and no tool was ever shut off | [Optimization Theater](https://www.therevenueaireport.com/frameworks/optimization-theater) (a pattern named by The Revenue AI Report): activity reported as outcome | Score every claim in the deck, not just this one |
| No one can say what would have counted as failure | Unfalsifiable | Write the line now |

---

## 10. Worked example: Acme

*Illustrative. Acme is a fictional 400-person B2B software company. Its enablement team rolled out an AI deal-coaching assistant to mid-market AEs at the start of Q2.*

**Claim, as made in the leadership meeting:** "The AI coaching assistant raised mid-market win rate from 20 percent to 26 percent in Q2."

**Intake card (abridged).**

| Field | Entry |
|---|---|
| The exact number | Q1: 50 won of 250 closed = 20%. Q2: 52 won of 200 closed = 26% |
| Source system | CRM closed-won and closed-lost report |
| Comparison | Q1 |
| Owner | "The enablement team" |
| Failure line | None written |
| What else changed | Discount approval threshold raised in May. RevOps bulk-closed 40 stale Q1 opportunities as closed-lost on the last day of Q1 |
| Sample | 250 and 200 closed opportunities |

**Reasoning, check by check.**

1. Provenance: Partial. The source is the CRM, which is good. But the Q1 bulk cleanup put 40 stale opportunities into Q1's closed-lost. Removing them: 50 won of 210 = 23.8 percent. The real move is about 23.8 to 26 percent, not 20 to 26.
2. Repeatability: Fail. One quarter, one segment.
3. Outcome tied to money: Pass. Win rate is an outcome.
4. Named owner: Partial. A team, not a person. The enablement director owns the tool; nobody owns the win rate claim.
5. Failure mode: Fail. No line was written before Q2.

**Comparison and noise.** Prior six quarters, with stale opportunities excluded the same way, ranged from 21 to 25 percent. Q2's 26 percent is just above the top of that range, after correcting the definition. Confounder: the discount change in May could raise win rate on its own. Selection: all mid-market AEs got the tool, so there is no holdout.

**Verdict: Anecdote.** It fails Repeatability, and the corrected change sits at the edge of normal variation with a commercial confounder in the same window.

**Next evidence.** A Q3 read comparing AEs who used the assistant on at least half their late-stage deals with AEs who did not, matched on tenure, with discount rate reported for both groups and stale-opportunity cleanup excluded. Owned by the enablement director, read on the first business day after Q3 close. Failure line, written now: if users and non-users differ by less than 2 points of win rate at similar discount, stop citing the assistant as a win-rate driver.

**Board paragraph.**
"Mid-market win rate was 26 percent in Q2, measured in the CRM, compared with 23.8 percent in Q1 once a year-end cleanup of stale deals is excluded. Discount approval rules also changed in May, so we cannot yet attribute the change to the AI coaching assistant. In Q3 we will compare assistant users with matched non-users at similar discount levels; the enablement director owns the read, and if the gap is under 2 points we will stop citing the assistant as a win-rate driver."

**What the review with the person who did the work changed.** The enablement director pointed out that 4 AEs never activated the tool. They became the start of the Q3 comparison group.

---

## 11. AI assist

| Work | AI assistant | Human |
|---|---|---|
| Turn a claim and notes into the intake card | Yes | Fill the base numbers and owner yourself |
| Score the five checks with reasons | Draft | Confirm each against the evidence, not the tone |
| List confounders | Yes, prompt it with your calendar of changes | Add what only you know |
| Compute the noise range and corrected numbers | Yes, show the arithmetic | Recompute |
| Write the board paragraph | Draft | Check every word against Section 7 |
| Decide whether to share | No | You and the person who did the work |

**Follow-up prompts to use after the Quick prompt:**

1. "Restate the claim as two base numbers for each period. If my paste does not contain them, say so and stop."
2. "List every change in the same window that could explain the result: people, demand, commercial, coverage, incentives, measurement, selection. For each, say whether it would push the number up or down."
3. "Here are the last [N] periods of this metric: [paste]. Is the claimed value outside that range? Show the range."
4. "Rewrite the board paragraph so it contains no word the evidence cannot support. Remove 'proven,' 'drove,' 'trend,' and 'ROI' unless the scorecard earns them."
5. "What single piece of evidence, owned by whom and read when, would move the weakest check to pass?"

**Check the AI's output for these errors:**

| Error this job invites | How to catch it |
|---|---|
| Passing a check on confident wording | Each pass cites a specific fact from your intake card |
| Inventing a comparison period or baseline | Every number traces to your paste |
| Treating a vendor dashboard as a system of record | Provenance says which system, and whether finance agrees |
| Missing the definition change | Ask directly: did any definition change in either period? |
| Board paragraph that hedges the caveat into the last clause | The caveat sits in its own sentence |
| Percentage arithmetic errors | Recompute from the base numbers |

---

## 12. Common mistakes

| Mistake | How to spot it | Fix |
|---|---|---|
| Testing the tool instead of the claim | The verdict says "the tool is bad" | Verdict is about the claim's strength |
| Accepting a percentage alone | No base numbers on the card | Get numerator and denominator |
| Skipping the noise test | No prior-period range written | Pull 6-12 periods |
| Owner as a team | "Enablement owns it" | One name |
| Writing the failure line after the result | Line matches what happened | Write it before the next run |
| Board paragraph with "drove" on an anecdote | Word list in Section 7 | Downgrade the word |
| Sharing without the person who did the work | Corrections arrive after the board meeting | Review first (SKILL.md process step 8) |

---

## 13. The 5-minute version

1. Write the claim with its two base numbers. If you cannot, stop there.
2. Ask: one period or more than one? One is an anecdote.
3. Ask: system number or survey? Survey is a perception.
4. Name everything else that changed in the window.
5. Write one sentence: what moved, what else changed, what you cannot yet attribute.

## The deep version

For a board update, a large renewal, or a claim that will drive an expansion:
- Rebuild both periods from the system of record with finance, on one fixed definition.
- Pull 12 prior periods for the noise range and chart them with the claimed period.
- Design the next run as a holdout or staggered start, with the failure line signed by the owner before it begins.
- Interview the person who did the work and one user who did not adopt.
- If the claim is about revenue, cross-check it against [the Proof Gap](https://www.therevenueaireport.com/frameworks/proof-gap) (a framework from The Revenue AI Report: AI spend divided by verified, incremental AI-influenced pipeline; under 1.0x defensible, 1.0x to 4.0x watch, over 4.0x on a rolling four quarters triggers a review).
- Keep a claim log: every AI result cited to leadership, its verdict, and what happened at the next read.

---
*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
