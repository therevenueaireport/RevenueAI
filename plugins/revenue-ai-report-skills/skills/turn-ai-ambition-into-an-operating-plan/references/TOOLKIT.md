# Turn an AI Ambition Into an Operating Plan: Toolkit

**Use this file when:**
- There is an AI budget line and no plan that connects it to a number finance already tracks.
- The board asked "what is our AI plan?" and the current answer is a list of tools.
- Every team is buying its own AI tool and nobody can say which number any of them moves.
- Pilots keep starting from a vendor demo, then stall because nothing was baselined.

The SKILL.md holds the logic: five steps (strategic outcomes, chart friction, align capabilities, launch with control, evolve and expand), one deliverable each. This file holds the instruments for each deliverable, the scoring sheets, a decision table, and a worked plan.

---

## 1. The Five-Week Rhythm

One week per step is a working default. Larger organizations stretch Step 2, because workflow mapping is the slowest step.

| Week | Step | Question | Deliverable | Signed off by |
|---|---|---|---|---|
| 1 | Strategic outcomes | What is the number? | Outcome charter | CFO or finance lead |
| 2 | Chart friction | Where does work get stuck, and what does it cost? | Ranked friction map | Process owners |
| 3 | Align capabilities | What capability fits the top friction, and are we ready? | Capability match map and shortlist | RevOps and security |
| 4 | Launch with control | How do we test small? | Running pilot with controls | Pilot owner and decider |
| 5+ | Evolve and expand | Scale, kill, or govern? | Scaling blueprint and governance structure | CRO or CEO |

**Completion rule:** a step is done when a named person signs off on its deliverable, not when the meeting ends. Each deliverable is the entry ticket to the next step.

---

## 2. Inputs Checklist

| Input | Where it lives | Lookback | Why |
|---|---|---|---|
| The committed number (revenue, margin, win rate, cycle time, cost) | Annual plan, board deck, finance model | This fiscal year | Step 1 must be a number finance recognizes |
| Baseline for that number and its drivers | Finance model, CRM, BI | 4-8 quarters | Without it, no later result can be claimed |
| Leading indicators that drive the number | CRM reports, funnel dashboards | 4 quarters | The pilot will move a leading indicator first |
| The 2-3 workflows closest to the number | Process owners | Current | Scope for Step 2 |
| Tools, owners, data sources per workflow | Software inventory, expense reports, single sign-on app list | Current | Avoids buying a second tool for the same job |
| Hard constraints | Finance, IT security, HR | This year | Budget, headcount, security review length |
| Past AI pilots and their results | Team chat, project folders | 18 months | Tells you what was tried and why it stalled |

---

## 3. Step 1: Outcome Charter

```
OUTCOME CHARTER

Committed number:      [metric, exact definition finance uses]
Baseline:              [value, period, source]
Target:                [value by date]  Delta: [target minus baseline]
Gap analysis:          [what must change in the drivers to close the delta]
Leading indicators:    [2-3 measures that move before the number does]
Lagging indicator:     [the committed number]
Out of scope:          [things this plan will not try to move]
Owner:                 [one person]
Finance sign-off:      [name, date]
```

### Working backward from the number

| Layer | Question | Example |
|---|---|---|
| Strategic outcome | What did the business commit to? | Revenue per rep up |
| Lagging metrics | What confirms it after the fact? | Win rate by segment, revenue per rep |
| Leading metrics | What moves first? | Qualified meetings held, multithreaded accounts |
| Behaviors and tasks | What work produces the leading metrics? | Discovery prep, follow-up, stakeholder mapping |
| Gap | Where do current behaviors fall short? | Prep is skipped on half of first calls |

**Decision rule:** if a proposed initiative cannot be traced up this ladder to the committed number, it is cut from this plan (it may still be worth doing; it is not this plan).

---

## 4. Step 2: Friction Map

Map each workflow step by step. For each point where work gets stuck, classify and cost it.

| Friction type | What it looks like | Is AI the right instrument? |
|---|---|---|
| People | Skill gap, unclear role, low confidence, missing coaching | Rarely first. Train or coach; AI can support practice |
| Process | Unclear handoffs, extra approvals, rework, no standard | Fix the process first. Automating a broken process makes it fail faster |
| Technology | Swivel-chair work between tools, manual copying, no integration | Often yes |
| Data | Missing, duplicated, stale, or untrusted fields | Fix the data first. AI on bad data destroys trust fast |

**A skills gap is not fixed by a systems purchase.** Classify before you match.

### Friction scoring sheet

| # | Workflow step | Friction | Type | Cost per month (hours or money) | How measured | Distance to the number (1-3) | Rank |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |

**Distance to the number:**

| Score | Meaning |
|---|---|
| 3 | Directly moves a leading indicator in the charter |
| 2 | Moves a behavior that drives a leading indicator |
| 1 | Saves time with no named path to the number |

**Rank (rule of thumb):** sort by distance first, then by cost. A large friction with distance 1 ranks below a smaller friction with distance 3. Time saved without a named destination is not a result.

---

## 5. Step 3: Capability Match Map

| Top friction | Capability that fits | Data ready? (0-2) | Process ready? (0-2) | People ready? (0-2) | Readiness total | Already owned? |
|---|---|---|---|---|---|---|
| | | | | | | |

**Readiness scale:** 0 not ready, 1 partial, 2 ready. **Threshold (rule of thumb):** 5+ of 6 with no zero to proceed to launch. Any zero becomes a foundation task before the pilot.

**Already owned?** Check whether a platform you already pay for does this. If yes, the shortlist starts there.

### Vendor shortlist scoring

| Criterion | 1 | 2 | 3 | Weight |
|---|---|---|---|---|
| Features | Covers part of the friction | Covers the friction | Covers it and adjacent steps | Set by owner |
| Fit | Needs a new workflow | Fits with changes | Fits the current workflow | Set by owner |
| Security | Fails or unknown | Passes with exceptions | Passes review | Gate: 1 = out |
| Scale | Pilot only | Team scale | Company scale with admin controls | Set by owner |

**Initiative triage (for the backlog that does not make this plan):**

| Type | Description | Treatment |
|---|---|---|
| Compounding move | Close to the number, builds data or capability later moves use | Plan it now |
| Capability move | Builds a foundation (data, skills, governance) the plan needs | Plan it as a prerequisite |
| Noise move | Interesting, demo-driven, no path to the number | Park it, in writing |

---

## 6. Step 4: Pilot Controls Sheet

```
PILOT CONTROLS

Friction targeted:       [from the friction map, rank #]
Capability / tool:       [..]
Team:                    [one small team; assigned, not only volunteers]
Comparison group:        [team staying on current process]
Baseline (pre-AI):       [leading indicator value, period, source]
Success metrics:         [1-3, each with threshold, window, source]
Stop condition:          [written before launch; what ends the pilot early]
Guardrails:              [data limits, human review points, spend cap]
Feedback loop:           [how users report problems, how often reviewed, by whom]
Time box:                [start, end]
Decision date:           [booked now]
Owner:                   [one person]
```

---

## 7. Step 5: Scaling Blueprint and Governance

| Result at decision date | Action |
|---|---|
| Passed all success metrics, no stop condition | Scale in stages to the next team, with an assigned (not volunteer) cohort |
| Passed on usage, flat on the leading indicator | Kill or redesign. Usage is not outcome |
| Mixed | Default is stop; rerun only with new written criteria |
| Stop condition tripped | Kill. Record the reason |

### Governance structure (minimum)

| Element | What it is |
|---|---|
| Governance owner | One named person accountable for AI across revenue |
| Intake rule | New AI requests start from the outcome charter, not a demo |
| Register | Every AI tool and workflow: owner, cost, data touched, metric it serves |
| Monthly review | Cost, usage, quality, and the metric each workflow serves; at least one thing killed or changed |
| Duplicate check | No second tool for a capability already owned, without a written reason |

---

## 8. Decision Table and Red Flags

| If | Then |
|---|---|
| Finance does not recognize the Step 1 number | Stop. Rewrite the charter with finance |
| Top friction is people or process | The first move is training or process repair, not a tool |
| Readiness has a zero on data | Foundation task before launch |
| A platform you own already has the capability | Pilot that first |
| A step has more than one deliverable | Split it into more steps |
| The pilot has no stop condition | It does not launch |
| Someone wants to expand after a good demo | Expansion waits for the measured outcome |
| More than one pilot proposed for the first cycle | Pick the one closest to the number |

| Red flag | What it means |
|---|---|
| The plan opens with a tool name | Technology first; the number is missing |
| "Adoption" is the success metric | Reported adoption is not operational use |
| Every friction is a technology friction | Nobody looked at people, process, or data |
| Owners are teams, not people | Nobody owns it |
| No baseline captured | The result will not be claimable |
| Governance appears only in Step 5 slides | Pilots will fragment into sprawl |

---

## 9. Board-Ready Plan Template

```
AI OPERATING PLAN: [company], [fiscal year]

THE NUMBER
[Committed number: baseline to target by date. Finance sign-off: name.]

| Step | Deliverable | Owner | Date | Status |
| 1 Strategic outcomes | Outcome charter | | | |
| 2 Chart friction | Ranked friction map | | | |
| 3 Align capabilities | Capability match map and shortlist | | | |
| 4 Launch with control | Pilot running with controls | | | |
| 5 Evolve and expand | Scaling blueprint and governance | | | |

TOP FRICTIONS (ranked by distance to the number)
1. [friction, type, cost, distance]
2.
3.

PILOT
[Capability, team, baseline, success metric, stop condition, decision date]

PARKED (not in this plan, and why)
[noise moves, out-of-scope initiatives]

THREE ASSUMPTIONS THAT WOULD BREAK THE PLAN
1. [assumption]  How we will know early: [signal]
2.
3.

VERDICT AND NEXT ACTION
[One line], owner [name], by [date]
Reviewed by (someone who did the work): [name]
```

---

## 10. Worked Example (illustrative)

**Company:** Acme, a 400-person B2B software company. **Committed number:** new-business win rate from 22 percent to 26 percent this fiscal year (finance tracks it quarterly). **Constraints:** no new headcount; security review takes six weeks.

**Step 1. Outcome charter.** Baseline 22 percent (n=410 opportunities, last four quarters). Leading indicators: share of opportunities with economic buyer identified by stage 3; share with two or more engaged contacts. Gap analysis: won deals show both far more often than lost deals. Finance signed off.

**Step 2. Friction map (top four of eleven).**

| Friction | Type | Cost per month | Distance | Rank |
|---|---|---|---|---|
| Discovery prep skipped on many first calls because research takes too long | Technology | About 60 AE hours | 3 | 1 |
| Stakeholder data missing or stale in CRM | Data | Not costed; drives misses on leading indicator 2 | 3 | 2 |
| Managers do not coach multithreading | People | Not costed | 2 | 3 |
| Proposal drafting slow | Technology | About 80 AE hours | 1 | 4 |

**Reasoning.** Proposal drafting is the largest time cost, but it sits after the buyer has formed a view; no named path to win rate. It ranks fourth and is parked. Discovery prep ranks first because it feeds both leading indicators.

**Step 3. Capability match.** Discovery prep: account research and stakeholder summary. Readiness: data 1 (stakeholder fields stale), process 2, people 2. Total 5, no zero: proceed, with a stakeholder-data cleanup task for the pilot accounts. Already owned? The CRM's AI assistant drafts account summaries; it is switched off. Shortlist starts there, avoiding the six-week security review for a new vendor.

**Step 4. Pilot controls.** One team of 7 AEs (assigned), comparison team of 7. Baseline: economic buyer identified by stage 3 on 38 percent of the pilot team's opportunities. Success: 55 percent or more within 8 weeks. Stop condition: if prep is used on fewer than half of first calls by week 4, stop and diagnose. Decision date booked.

**Step 5 (planned).** If passed: extend to two more teams, assigned; register the workflow; monthly review. Governance owner: Head of RevOps.

**Three assumptions that would break the plan.**

1. Economic buyer identification drives win rate at Acme, not just correlates. Early signal: pilot opportunities with buyer identified do not convert better.
2. Stale stakeholder data can be cleaned for pilot accounts in two weeks. Early signal: cleanup still open at launch.
3. Managers will reinforce prep in deal reviews. Early signal: prep not mentioned in week 2 deal reviews.

**Next action.** Switch on the CRM's assistant for the pilot team. Owner: RevOps lead. By: Friday of week 3.

---

## 11. AI Assist

### Split the work

| Task | AI assistant | Human |
|---|---|---|
| Draft the outcome charter from your numbers | Yes | Finance confirms the number and baseline |
| Map workflows from process notes or interview transcripts | Yes | Process owners correct |
| Classify friction type | First pass | Owner checks people vs. process vs. technology vs. data |
| Cost each friction | Only from numbers you give it | You supply hours and rates |
| Readiness scoring | Draft | You know your data quality; it does not |
| Choose the pilot | No | Yes |

### Follow-up prompts (use after the Quick prompt)

1. "Trace every initiative in this plan up to the committed number: behavior, leading metric, lagging metric. Mark any initiative that cannot be traced, and move it to a 'parked' list."
2. "Classify each friction as people, process, technology, or data. For each people or process friction, tell me what non-AI fix should come first."
3. "Score each friction's distance to the number: 3 moves a leading indicator directly, 2 moves a behavior that drives one, 1 saves time with no named path. Re-rank."
4. "For every step, confirm there is exactly one deliverable, one named person as owner, and a date. List any that fail."
5. "List every number in this plan that I did not give you. Mark each as an assumption I must confirm."

### Check the AI's output for these errors

| Error this job invites | How to catch it |
|---|---|
| Plan opens with tools | First line must be the committed number |
| Filled gaps instead of flagging them | Prompt 5 |
| Every friction tagged "technology" | Prompt 2 |
| Time saved treated as outcome | Distance score of 1 means it is not ranked near the top |
| Teams as owners | Prompt 4 |
| Expansion planned before measurement | Step 5 must be conditional on the decision date result |

---

## 12. Common Mistakes

| Mistake | How to spot it | Fix |
|---|---|---|
| Starting with the tool | Shortlist exists before the charter | Write the charter first |
| Automating a broken process | Top friction is process; plan buys a tool | Repair the process first |
| Pilot with no controls | No baseline or stop condition | Use the controls sheet |
| Adoption theater | Success is "licences active" | Measure the leading indicator |
| No governance | Each team buys its own version | Register, intake rule, monthly review |

---

## 13. Two Versions

### 5-minute version
1. Write the committed number, baseline, and target.
2. Name the one workflow closest to it and its biggest friction. Classify the friction type.
3. If it is technology friction, name one capability and check whether you already own it.
4. Write one pilot with an owner, a baseline, a success metric, a stop condition, and a decision date.

### Deep version (board presentation or material budget)
- Five full weeks, one deliverable per week, each signed off.
- Friction map across all 2-3 workflows with costs from real time studies or system logs.
- Readiness scored with the data owner and security in the room.
- Pilot with an assigned team and a comparison team.
- Governance register and intake rule live before the second pilot starts.
- Three breaking assumptions, each with an early signal and an owner who checks it.

---
*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
