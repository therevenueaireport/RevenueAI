# Sequence AI Changes Without Breaking Revenue: Toolkit

**Use this file when:**
- You are about to change a live revenue workflow with AI and the current quarter still has to land.
- A pilot worked and you are deciding how to take it to the whole team.
- A previous change broke something quietly and you want the next one to fail loudly and small.
- Two teams want to move at different speeds on a shared workflow and you need an order both can live with.

The SKILL.md holds the logic: the five moves of SLING, a framework from The Revenue AI Report ([framework](https://www.therevenueaireport.com/frameworks/sling)), which are S: set the foundation, L: layer it in, I: iterate in parallel, N: nudge, don't shove, and G: ground truth every number, plus the decision rules. SLING is the sequencing rule; the level of ambition you are climbing toward (Optimize, Amplify, Reinvent) comes from OAR, also a framework from The Revenue AI Report ([framework](https://www.therevenueaireport.com/frameworks/oar)). Each section below is tagged with the SLING move it serves. This file holds the instruments: scoring sheets, move cards, the warning-signal and rollback design, and a worked sequence.

---

## 1. The Sequencing Session

| Step | What you do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1 | Write the end state and the protected number | One-line target, one protected metric | 10 min |
| 2 | Map the workflow and its dependencies | Dependency map (Section 3) | 15 min |
| 3 | Check the foundation | Foundation check (Section 4) | 10 min |
| 4 | Capture the baseline before anything changes | Baseline record (Section 5) | 10 min, then 2-4 weeks of data |
| 5 | Break the change into moves and score each | Move scoring sheet (Section 6) | 15 min |
| 6 | Order the moves | Ordered move list | 5 min |
| 7 | Write a move card for each, with signal and rollback | Move cards (Section 8) | 15 min |
| 8 | Flag approval-gated moves | Approval list | 5 min |
| 9 | Process owner reviews the order | Signed-off sequence | 15 min |

**The protected number:** name the one revenue metric that must not drop while you change things (inbound conversion, renewal rate, meetings booked, forecast accuracy). Every early warning signal ladders to it.

---

## 2. Inputs Checklist

| Input | Where it lives | Lookback | Why |
|---|---|---|---|
| Current workflow, step by step | Process owner interview, existing runbook | Current | You cannot sequence what you have not drawn |
| Protected metric history | CRM reports, BI dashboard | 2-4 quarters | Shows normal variance, so you set signals above noise |
| Weekly variance of the protected metric | Same | 12+ weeks | Sets the warning threshold |
| Systems the workflow reads and writes | CRM, marketing automation, routing tool, data warehouse | Current | Every write is a rollback problem |
| Who touches each step today | Org chart, queue assignments | Current | Names the owner and the rollback caller |
| Past incidents on this workflow | Ticket history, team chat, post-mortems | 12 months | Tells you where it broke before |
| Calendar constraints | Finance and sales calendar | Next 2 quarters | No irreversible move in the last 3 weeks of a quarter (rule of thumb) |

---

## 3. Dependency Map

The AI assistant cannot see your dependencies. Fill this before asking it to sequence anything.

| Workflow step | Reads from | Writes to | Downstream consumer | Breaks silently if wrong? |
|---|---|---|---|---|
| [e.g., Inbound reply] | [Form data, CRM contact] | [Email, CRM activity] | [Routing rule, SDR queue, attribution report] | [Yes / No] |

**Rule:** any step marked "breaks silently" needs a warning signal on its downstream consumer, not on the step itself.

---

## 4. Foundation Check (SLING S: set the foundation)

Score each line before any AI touches the workflow.

| Item | 0 Not ready | 1 Partial | 2 Ready |
|---|---|---|---|
| Field definitions agreed for the fields the AI will read | Disputed or undocumented | Documented, not enforced | Documented and enforced |
| Duplicate records in the affected objects | Common, unmeasured | Measured, being fixed | Measured and low enough the owner accepts it |
| Identity: one owner per account and contact | Multiple owners common | Rules exist, exceptions common | Rules enforced |
| Stage and status hygiene | Stale stages and close dates common | Cleaned once | Cleaned and checked weekly |
| Live-data test: AI run on an unfiltered slice | Not done | Done on curated data only | Done on live data, failures counted by cause |

**Threshold (rule of thumb):** total 7+ of 10 with no zero on the live-data test before Move 1 ships. A zero anywhere means the first move is a foundation fix, not an AI move. If failures on the live-data test trace mostly to data rather than the model, fix the data first.

---

## 5. Baseline Record (SLING G: ground truth every number)

Capture this before the switch is flipped. Without it, no later number can be claimed.

```
BASELINE RECORD
Protected metric:        [name and exact definition]
Baseline period:         [dates, at least 4 weeks; 8+ if volume is low]
Baseline value:          [value, with n]
Normal weekly range:     [low to high across the baseline weeks]
Comparison group:        [team, region, or segment that will NOT get the change yet]
Known outside factors:   [pricing change, campaign, seasonality, headcount change]
Captured by / date:      [name, date]
```

**Comparison group rule:** keep one group on the old process for at least the first two moves. It is the only clean way to separate the AI effect from the market.

---

## 6. Move Scoring Sheet

Break the target change into moves small enough to describe in one sentence. Score each.

| Dimension | 1 | 2 | 3 |
|---|---|---|---|
| Reversibility | Undo in a day, no residue | Undo in a week, some cleanup | Cannot be undone in a week, or leaves records you cannot reconstruct |
| Blast radius | One person or one small queue | One team or one segment | Whole function or customer-facing at scale |
| System-of-record impact | Reads only | Writes to a staging field or task | Writes to live fields, routing, or customer-facing channels |
| Human in the loop | Human approves every output | Human samples outputs | No human before the customer or the record |
| Signal speed | Warning shows within days | Within 2-3 weeks | Only at quarter end or later |

**Risk score = sum (5 to 15).** Rule of thumb:

| Score | Treatment |
|---|---|
| 5-7 | Ship with a weekly signal check |
| 8-10 | Ship to one team first; comparison group required |
| 11-15 | Approval-gated. Written approval, named approver, evidence from earlier moves required |

Any move scoring 3 on reversibility is approval-gated regardless of total.

---

## 7. Ordering Rules

Apply in this order. Earlier rules win.

| # | Rule | Source (SLING move) |
|---|---|---|
| 1 | Foundation fixes before any AI move | S: set the foundation |
| 2 | Reversible before irreversible, even if the irreversible move pays more | SKILL decision rule |
| 3 | Read-only before write; staging field before live field | L: layer it in |
| 4 | Never change the system of record and the workflow in the same move | SKILL decision rule |
| 5 | One team or segment before all; volunteers then assigned cohort before everyone | N: nudge, don't shove |
| 6 | Human approves, then human samples, then human audits after the fact | N: nudge, don't shove |
| 7 | Small Optimize moves may run alongside one larger Reinvent bet, on separate workflows | I: iterate in parallel |
| 8 | No irreversible move in the closing weeks of a quarter | Calendar |

**The assigned cohort step:** pilots run on volunteers and curated data. Before an all-team move, run one cohort that did not ask for the change, on live data. If it holds there, it is real.

---

## 8. Move Card Template

```
MOVE [#]: [one sentence: what changes]

What changes:           [the single thing that is different]
What stays untouched:   [systems, steps, people explicitly not changing]
Who it touches:         [team, queue, segment, volume per week]
Risk score:             [R_ B_ S_ H_ Sig_ = total]
Approval-gated?         [No / Yes: approver name, evidence required]

Early warning signal:   [metric, in a system someone already reads]
Threshold:              [value and duration, e.g., "below X for 5 business days"]
Checked by / cadence:   [name, weekly day]

Rollback step:          [the exact action that restores the prior state]
Rollback caller:        [one named person who can call it without a meeting]
Rollback time budget:   [hours or days to complete]
Residue after rollback: [records, emails, or routing that cannot be undone]

Exit criteria to next move: [what must be true, for how long, before the next move ships]
```

### Designing the warning signal

| Test | Pass |
|---|---|
| Lives in a system the checker already opens weekly | Yes, no new dashboard required |
| Leads the protected metric | Moves within days, not at quarter end |
| Threshold sits outside normal weekly variance | Set from the baseline range, not a guess |
| Has a duration | "For 5 business days," not a single bad day |
| Names the checker | One person, one day of the week |

### Designing the rollback

| Test | Pass |
|---|---|
| Is a single action or a short list | A toggle, a routing rule revert, a permission removal |
| Has been rehearsed once | Run it in a test environment or on a single record before the move ships |
| Names residue | What cannot be pulled back (sent emails, changed owners, overwritten fields) |
| Caller can act alone | No committee needed to stop the bleeding |

---

## 9. Decision Table and Red Flags

| If | Then |
|---|---|
| The foundation check has a zero | Move 1 is the fix. AI moves wait |
| No baseline exists | Capture 4+ weeks before Move 1, even if it delays launch |
| A move changes the system of record and the workflow | Split it into two moves |
| A warning signal needs a new dashboard | Pick a different signal, or the signal will not be checked |
| The process owner disagrees with the order | Their objection is a dependency you missed. Map it |
| Two teams want different speeds | Let the faster team go first; the slower team becomes your comparison group |
| A signal trips | Roll back first, diagnose second. Do not debug in production |
| A move passes its exit criteria early | Hold for the full period anyway; early variance is noise |

| Red flag | What it means |
|---|---|
| Every move is scored low risk | Moves are too large, or scoring was rushed. Re-split |
| "We will monitor it" with no named checker | Nobody will |
| Rollback is "turn off the tool" for a move that writes records | Rollback ignores residue |
| The plan ends at the irreversible move | No exit criteria for scale; you will ship and stop measuring |
| The pilot group is the plan's only evidence | Volunteer bias; add an assigned cohort |
| Launch date set before the baseline window ends | The number will not be claimable |

---

## 10. Worked Example (illustrative)

**Company:** Acme, a 400-person B2B software company. **Target:** AI drafts, routes, and sends all inbound replies. **Today:** three SDRs reply manually; inbound converts to meetings at 20 percent over the last two quarters; weekly range 17 to 23 percent. **Protected number:** inbound-to-meeting conversion. **Rollback tolerance:** one week.

**Dependency map, key line:** routing writes the owner field in your CRM, which drives territory credit and the attribution report. Breaks silently if wrong: yes.

**Foundation check:** field definitions 2, duplicates 1, identity 1 (leads often match two accounts), hygiene 2, live-data test 0. Total 6. Move 1 becomes a foundation fix.

**Baseline record:** 8 weeks, 20 percent (n=610 inbound leads), comparison group: the EMEA inbound queue stays manual through Move 3.

**Scored moves:**

| Move | R | B | S | H | Sig | Total | Gate |
|---|---|---|---|---|---|---|---|
| 1. Fix lead-to-account matching; run AI drafts on 200 live leads offline, count failures by cause | 1 | 1 | 1 | 1 | 1 | 5 | No |
| 2. AI drafts, SDR edits and sends, one SDR | 1 | 1 | 2 | 1 | 1 | 6 | No |
| 3. AI drafts for all three SDRs, SDR sends | 1 | 2 | 2 | 1 | 1 | 7 | No |
| 4. AI suggests the route into a staging field; SDR confirms | 1 | 2 | 2 | 1 | 2 | 8 | One team first |
| 5. AI sends replies without review on low-intent forms only | 2 | 2 | 3 | 3 | 1 | 11 | Yes |
| 6. AI routes directly into the live owner field | 3 | 2 | 3 | 3 | 2 | 13 | Yes |

**Reasoning on the order.** Moves 1-3 are reversible in a day and change one thing each. Move 4 separates the routing decision from the routing write, so the system-of-record change is isolated. Move 6 is last because owner history cannot be reconstructed once overwritten and the attribution report silently inherits errors. Move 5 comes before 6 because sent emails are residue but do not corrupt records.

**Move card, Move 2 (abridged):**

| Field | Entry |
|---|---|
| What changes | One SDR uses AI drafts for inbound replies |
| What stays | Routing, sending, CRM fields, other two SDRs |
| Warning signal | That SDR's reply-to-meeting rate, in the weekly SDR report, below 16 percent for 5 business days |
| Rollback | SDR stops using the draft panel; same hour |
| Caller | SDR manager |
| Exit criteria | 3 weeks at or above baseline range, edit rate tracked |

**Approval list:** Move 5 (customer-facing, no human review) and Move 6 (irreversible write to owner field). Approver: CRO. Evidence required: Moves 3 and 4 at baseline or better for 4 weeks against the EMEA comparison queue, and a rehearsed rollback.

**Verdict and next action:** proceed with Moves 1-2. Owner: RevOps lead. Check date: four weeks out.

---

## 11. AI Assist

### Split the work

| Task | AI assistant | Human |
|---|---|---|
| Break the target into one-sentence moves | Yes | Check each move changes one thing |
| Score moves on the sheet | First pass | Process owner corrects reversibility and residue |
| Propose warning signals | Yes | Confirm each exists in a system someone reads |
| Map dependencies | No, it cannot see them | Yes |
| Name rollback callers and approvers | No | Yes |
| Decide whether to proceed | No | Yes |

### Follow-up prompts (use after the Quick prompt)

1. "Here is my dependency map: [paste]. Re-check the sequence. Which moves touch a step marked 'breaks silently', and what downstream signal would catch it?"
2. "Score each move 1-3 on reversibility, blast radius, system-of-record impact, human in the loop, and signal speed. Show the scores in a table. Mark any move with reversibility 3 as approval-gated."
3. "Find any move that changes the system of record and the workflow at the same time. Split it."
4. "For each move, list what cannot be undone after rollback: sent messages, overwritten fields, changed owners."
5. "Write the exit criteria for each move: what must be true, for how long, before the next move ships."

### Check the AI's output for these errors

| Error this job invites | How to catch it |
|---|---|
| Moves that bundle two changes | Each move must fit one sentence with one verb |
| Warning signals from systems you do not have | Ask "where exactly does this number live today?" |
| Rollback "disable the tool" with residue ignored | Run prompt 4 |
| Thresholds inside normal variance | Compare to your baseline weekly range |
| Optimistic reversibility on write moves | Any move that writes to live records is at least 2 |
| Big-bang final move | Final move should still be scoped to a segment or have a comparison group |

---

## 12. Common Mistakes

| Mistake | How to spot it | Fix |
|---|---|---|
| Skipping the foundation | Move 1 is an AI move with a foundation score under 7 | Insert the fix as Move 1 |
| No baseline | Launch date precedes baseline window | Delay or accept the result is unprovable |
| Rip and replace | A move removes a working system | Thread through it first |
| The shove | One move goes to the whole function | Split by team or segment |
| Post-mortem blames the tool | Nobody checks which move was skipped | Run the SLING skipped-move check: S foundation, L layer, I iterate, N nudge, G ground truth. The skipped move is usually the first or the last |

---

## 13. Two Versions

### 5-minute version
1. Name the protected number and confirm a baseline exists.
2. List the moves. Put anything that writes to live records or reaches customers last.
3. For the first move only: one warning signal someone already reads, one rollback caller.
4. Ship Move 1. Sequence the rest after its first week.

### Deep version (customer-facing or system-of-record change)
- Full dependency map signed by the process owner.
- 8+ week baseline with a comparison group held back through the approval-gated moves.
- Rollback rehearsed for every move scoring 2+ on reversibility.
- Live-data test with failures counted by cause before Move 1.
- Assigned (not volunteer) cohort before any all-team move.
- Written approval for each gated move, with the evidence attached.
- Skipped-move post-mortem scheduled at the end, whatever the outcome.

---
*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
