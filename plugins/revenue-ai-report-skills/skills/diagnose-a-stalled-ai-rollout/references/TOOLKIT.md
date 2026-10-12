# Stalled Rollout Toolkit: Evidence Pull, Rung Scoring, and the Two-Week Fix Library

**Use this file when:**
- Usage fell after launch week and you need a cause, not a theory.
- Someone has proposed another training session and you suspect training is not the gap.
- You owe the CRO or CEO a defensible read on why a rollout is not working and what happens next.
- One team adopted the tool and another did not, and you need to know why.

This file holds the instruments. The SKILL.md holds the logic. The ladder is LOPAFT (Learn, Observe, Practice, Apply, Feedback, Teach), created by Jonathan Kvarfordt ([LOPAFT, a framework from The Revenue AI Report](https://www.therevenueaireport.com/frameworks/lopaft)). It is a diagnostic, not a curriculum: you are looking for the lowest missing rung, not designing a new program.

---

## 1. The diagnostic sequence

| Step | What you do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1 | Rule out a tool problem | Tool check: pass or stop | 5 min |
| 2 | Pull the usage data and segment it | Four-bucket usage table | 10 min |
| 3 | Collect rung evidence: artifacts and quotes | Evidence list per rung | 15 min, plus 3-5 short interviews |
| 4 | Score each rung pass, partial, missing | Six-row card | 10 min |
| 5 | Name the lowest failing rung | Root cause with reasoning | 5 min |
| 6 | Pick the two-week fix | Fix card with owner and check | 5 min |
| 7 | Review with someone who ran the rollout | Signed card | 10 min |

---

## 2. Step 1: Is it the tool or the adoption?

The ladder explains adoption, not whether the tool is any good. A bad tool fails every rung and no fix will hold. Check this first.

| Check | Tool problem if | Adoption problem if |
|---|---|---|
| Power users | Nobody uses it regularly, including the people who asked for it | A few people use it daily and get value |
| Output quality on a clean test | Output is wrong or unusable on a well-formed input | Output is usable when the input is good |
| Workflow fit | Using it adds steps to the work it was meant to remove | It saves time for people who use it correctly |
| Data access | It cannot reach the data it needs (CRM fields empty, permissions missing) | Data is there; people are not using it |
| Complaints | Complaints are about errors, speed, or access | Complaints are about not knowing how or when |

**Rule:** if three or more lines point to the tool, stop this diagnosis. Escalate as a tool or data problem, and do not fund an adoption fix.

---

## 3. Step 2: Pull and segment the usage data

| Data | System category | How far back | What to look for |
|---|---|---|---|
| Per-user activity | Tool admin console, SSO sign-in logs | Launch date to today, weekly | Weekly active users by team and manager |
| Use on the named workflow | Tool logs, CRM activity fields | Same | Repeat use on the job it was bought for, not logins |
| Training attendance | Calendar, learning platform | Launch period | Who attended, who watched a recording, who did neither |
| Artifacts produced | Shared drives, enablement platform | Launch period | Decks, SOPs, examples, sandboxes, scorecards that exist |
| Manager reviews | Coaching notes, scorecards | Since launch | Any measured review of the AI-assisted work |
| Output samples | The tool itself, sent emails, CRM notes | Last 30 days | 10 recent outputs for a quality spot check |

### Four-bucket segmentation

| Bucket | Definition | What a large bucket usually signals |
|---|---|---|
| Never started | No sessions since launch | Learn (or access) |
| Tried and stopped | 1-3 sessions, none in the last 3 weeks | Observe or Practice |
| Occasional | Some use, not weekly on the named workflow | Apply or Feedback |
| Weekly on the named workflow | Repeat use on the intended job | Healthy. Check Teach |

### Usage curve shapes

| Shape | Common rung signal |
|---|---|
| Low from day one | Learn: people did not know what it was for, or could not get in |
| Spike in launch week, then a steep fall | Observe or Practice: people tried, could not tell good from bad, or got burned on a live customer |
| Steady but output quality is poor | Feedback: nobody measures the work, so bad habits set |
| Strong in one team, weak in another | Look at the managers. Usually Feedback or Apply differs by manager |
| Healthy usage, falls when a person leaves | Teach: the skill lived in one head |

---

## 4. Step 3: Collect evidence for each rung

### Artifact checklist

| Rung | Evidence that it existed | Evidence that it did not |
|---|---|---|
| Learn | Launch email, SOP, deck, recorded session, attendance record | Only a vendor announcement; no written how-to |
| Observe | A library with both good and bad examples, annotated with why | Only vendor demo examples, or only good examples |
| Practice | Sandbox, role play, dry-run exercises with no customer | First use was on a live prospect or customer |
| Apply | A named workflow, a named owner, the tool placed in the live process | Use was optional and nobody said which deals or tasks |
| Feedback | A written standard and scores against it | Check-ins, "how is it going," or usage counts only |
| Teach | Peers teaching it, a new hire trained by a peer | Only the enablement team can explain it |

### Interview bank (10-15 minutes each, 3-5 people)

Talk to at least two people who stopped, one who still uses it, and one manager. Ask for specifics, not opinions.

| Rung | Question |
|---|---|
| Learn | Walk me through how you found out what this tool was for. What did you get in writing? |
| Observe | Show me an example of a good output. Can you show me a bad one? How do you tell them apart? |
| Practice | Where did you first try it? Was a customer on the other end? |
| Apply | Which part of your week is it supposed to replace? Who told you that? |
| Feedback | Has anyone scored or reviewed your AI-assisted work against a standard? What did it say? |
| Teach | If a new hire started tomorrow, could you show them how to use it well? What would you tell them? |
| Any | What was the moment you stopped using it? |

### Coding quotes to rungs

| What people say | Likely rung |
|---|---|
| "I wasn't sure what it was for" / "I missed the training" | Learn |
| "I didn't know what a good one looked like" / "I couldn't tell if it was right" | Observe |
| "It made something up and I sent it to a buyer" / "I didn't want to try it on a real deal" | Practice |
| "It's not part of how we actually work" / "My manager never asks for it" | Apply |
| "Nobody ever looked at what I produced" / "I don't know if I'm doing it well" | Feedback |
| "Ask [one person], they're the only one who gets it" | Teach |

**Rule:** a quote is evidence. A guess about why people stopped is not. Mark every rung verdict with its source.

---

## 5. Step 4: Score each rung

| Rung | Pass | Partial | Missing |
|---|---|---|---|
| Learn | Written explanation of what, when, and why, received by the full audience | Explained once verbally, or reached part of the audience | No explanation beyond an announcement |
| Observe | Good and bad examples from your own work, annotated with why | Good examples only, or vendor examples only | No examples |
| Practice | At least one safe rep per person with no customer on the line | Optional sandbox few used, or practice for some teams only | First use was live |
| Apply | Named workflow, named owner, built into the live process | Encouraged, not placed in a specific step | Fully optional |
| Feedback | Work scored against a written standard, results shared privately | Informal review, or a standard that exists but is not used | Usage counts only, or nothing |
| Teach | Peers can teach it; a new hire has been trained by a peer | One or two people could teach it | Only the program owner can explain it |

**What "good" means for an AI tool.** For most revenue AI tools the skill is judging the output, not producing it. A usable standard for Observe and Feedback covers three judgments: is this true (no invented claims, numbers match the source), is this right for this buyer and stage, and should we act on it at all.

---

## 6. Step 5: Name the root cause

| Rule | Why |
|---|---|
| The root cause is the lowest rung marked partial or missing | A higher rung cannot hold when the one under it is missing |
| If two rungs tie on evidence, choose the lower one | Fixing the higher one first will not stick |
| Learn marked partial with a large "never started" bucket wins over everything above it | People cannot fail at Practice if they never began |
| Teach alone missing, all else passes, usage is healthy | Not a stall. The skill is fragile. Fix Teach before the next hire class |
| Different teams fail at different rungs | Write one card per team. Do not average them |

Write one sentence explaining why each rung above the root cause cannot be fixed first. If you cannot, recheck the scoring.

---

## 7. Step 6: The two-week fix library

One rung, one fix, two weeks. Every check must be readable from a system you already have.

| Rung | Two-week fix (deliverable) | Owner | Measurable check |
|---|---|---|---|
| Learn | One-page written how-to: what it is for, when to use it, the first three steps. Re-sent to everyone, with access confirmed | Enablement | Percent of the audience with one session on the named workflow (admin console) |
| Observe | Six annotated examples from your own work, three pass and three fail, each with the reason | Enablement plus one top user | Managers score ten outputs each against the examples; agreement within one point |
| Practice | Three drills of five outputs each, with errors deliberately planted, done with no customer on the line | Enablement | Drill scores (planted errors found), then weekly active use on the named workflow |
| Apply | Place the tool in one named step of the live process, with an owner, for one team first | Front-line manager | Percent of target tasks completed with the tool (CRM or tool logs) |
| Feedback | A written scoring standard and a weekly private score of five outputs per person | Front-line manager | Scores logged weekly; quality trend over two cycles |
| Teach | Two peers each run a 15-minute session for a colleague or new hire using the examples | Enablement plus the peers | Learner completes one scored output at standard without help |

**Rule of thumb for the re-check:** look at weekly use on the named workflow at day 14 and day 30 after the fix starts. If the target rung now passes and usage has not moved, re-score the next rung up.

---

## 8. Decision table

| If | Then |
|---|---|
| Three or more tool-check lines point to the tool | Stop. Escalate the tool or data problem |
| A leader proposes another training event and Learn already passes | Decline it. Show the card. Fund the root-cause fix instead |
| First live use was the first use | Practice is missing, whatever usage shows |
| Only usage counts exist, no quality read | Feedback is missing |
| One team succeeded with the same tool | Compare that team's card to the others. The difference is the fix |
| Usage is fine but a power user just left and use dropped | Teach. Treat the skill as fragile |
| You have usage data but no quotes | Do the interviews before naming a root cause |

---

## 9. Red flags

| Red flag | What it usually means |
|---|---|
| "We trained everyone" as the full answer | Learn passed; nobody checked the rungs above it |
| Feedback delivered in a group meeting | Feedback is unsafe. People stop trying rather than be corrected in public |
| Examples library holds only good examples | Observe is partial. People cannot see where they stand |
| Managers do not use the tool | Apply and Feedback will fail. Managers cannot score what they do not understand |
| The fix list has six items | Not a diagnosis. Pick one rung |
| Success measured in logins | Logins measure curiosity. Repeat use on a named workflow measures adoption |

---

## 10. The output: rollout diagnostic card

```
ROLLOUT DIAGNOSTIC CARD

Tool and workflow:      [What it is for, in one line]
Audience and launch:    [Teams, headcount, launch date]
Tool check:             [Pass / stop, with reason]
Usage:                  Never started [%] | Tried and stopped [%] | Occasional [%] | Weekly on workflow [%]
Curve shape:            [Description]

Rung      | Evidence (source)                      | Verdict
Learn     |                                        | Pass / Partial / Missing
Observe   |                                        |
Practice  |                                        |
Apply     |                                        |
Feedback  |                                        |
Teach     |                                        |

Root cause:             [Rung]
Why not higher rungs:   [One sentence per rung above]
Shown vs inferred:      [What the evidence shows] / [What is inference]

Two-week fix:           [Deliverable]
Owner:                  [Name/role]   Start: [date]   Re-check: [day 14 date], [day 30 date]
Measurable check:       [Metric and the system it comes from]
Reviewed by:            [Person who ran the rollout]
```

---

## 11. Worked example: Acme (illustrative)

Acme is a fictional 400-person B2B software company. All numbers are illustrative.

**Rollout.** AI-drafted follow-up emails inside the sales engagement tool, launched to 55 AEs and SDRs across four teams. Launch: a 45-minute live session, recorded, plus a written one-page guide. Enablement also built a library of eight annotated drafts, four good and four bad. Reps were told to "start using it on your next follow-ups."

**Tool check.** Five reps use it daily and say it saves them an hour a week. Clean test drafts are usable. Data access is fine. Pass: this is an adoption problem.

**Usage.** Never started: 9 percent. Tried and stopped: 51 percent. Occasional: 27 percent. Weekly on the workflow: 13 percent. Curve: 58 percent active in week one, falling steeply by week three. Team 2 sits well above the others.

**Quotes.** "It put last year's pricing in a draft and I nearly sent it to a CFO." "I don't want to test it on a live deal." From a Team 2 rep: "My manager had us run ten drafts on old closed-lost accounts first."

**Card** (Teams 1, 3, and 4, which behaved alike; Team 2 noted where it differs).

| Rung | Evidence | Verdict |
|---|---|---|
| Learn | Guide and recorded session; 91 percent started at least once | Pass |
| Observe | Eight annotated examples, good and bad, from Acme's own deals | Pass |
| Practice | No sandbox; first use was on live prospects, except Team 2 | Missing (Team 2: pass) |
| Apply | "Use it on follow-ups," no named step or owner | Partial |
| Feedback | No standard used; managers check usage counts only | Missing |
| Teach | Only the enablement lead could explain how to judge a draft | Missing |

**Root cause: Practice.** Learn and Observe pass on evidence. Reps knew what good looked like but met their first real error on a live buyer, and the quote shows trust broke at that moment. **Why not Feedback first:** scoring live drafts would mean correcting mistakes already sent to buyers, which makes people stop using the tool rather than improve. **Why not Apply first:** placing the tool into a mandatory step before reps trust it would push errors into more live emails. Team 2 is the natural experiment: same tool, same training, safe reps, higher use.

**Fix.** Three drills over two weeks, five drafts each, on closed-lost accounts, with one planted error per draft: an out-of-date price, a commitment the buyer never made, a wrong stakeholder. Owner: enablement lead, with the Team 2 manager co-running. **Check:** drill scores (planted errors found) logged per rep, and weekly use on the named workflow from the engagement tool's activity report. Re-check at day 14 and day 30. Feedback is the next rung to fix if Practice passes and quality is still uneven.

**What evidence shows vs inference.** Shown: Practice was absent for three of four teams, and Team 2 differs on exactly that rung. Inferred: the pricing incident spread by word of mouth and drove the week-two drop. Flagged for the reviewer.

---

## 12. AI assist

### Split the work

| Task | AI assistant | Human |
|---|---|---|
| Segment usage data into four buckets | Compute | Confirms the export covers the named workflow |
| Code interview quotes to rungs | Draft | Checks each coding against the original words |
| Score each rung | Propose with cited evidence | Decides, especially on partial versus missing |
| Name the root cause | Propose | Confirms with someone who ran the rollout |
| Draft the fix and planted-error drills | Draft | Checks every planted error is actually wrong and realistic |

### Follow-up prompts after the Quick prompt

```text
For each rung verdict, quote the exact piece of my evidence it rests on. Any verdict without a quote, change to "no evidence" and tell me what to collect.
```

```text
Here are my interview notes: [paste]. Map each quote to the rung it most likely points to, with one line of reasoning. Flag any quote that could point to two rungs.
```

```text
Explain why each rung above the root cause cannot be fixed first. If any of them could, say so and re-check your root cause.
```

```text
Build the two-week fix for the root-cause rung only. Give me the deliverable, the owner role, the daily or weekly steps, and a check I can read from [system]. Do not include training sessions unless the root cause is Learn.
```

### Check the AI's output for these errors

| Error this job invites | How to spot it |
|---|---|
| Recommends more training by default | The fix is a session or a refresher, and the root cause is not Learn |
| Picks the most visible rung, not the lowest | Root cause is Feedback or Apply while a lower rung is partial |
| Fixes all six | The output has a plan per rung |
| Invents evidence | A verdict cites something you never supplied |
| Treats usage as quality | Feedback marked pass because usage numbers are tracked |
| Blames the reps | Root cause written as "low motivation" or "resistance to change" |

---

## 13. Common mistakes and how to spot them

| Mistake | How to spot it | Fix |
|---|---|---|
| Diagnosing from usage alone | No quotes in the evidence column | Run three interviews first |
| Averaging across teams | One card for a company where teams behave differently | One card per team |
| Calling a live deal "practice" | Practice marked pass, first use was with a customer | Re-score as missing |
| Calling a check-in "feedback" | Feedback marked pass, no written standard | Re-score as partial or missing |
| A fix bigger than two weeks | The fix needs a new tool, a reorg, or a quarter | Cut to the smallest deliverable that moves the rung |
| No re-check date | The card ends at the fix | Put day 14 and day 30 on a calendar |

---

## 14. The 5-minute version

1. Confirm a few people get real value from the tool. If nobody does, it is a tool problem.
2. Ask two people who stopped: "When did you stop, and what happened just before?"
3. Ask: did people see good and bad examples, and did they get a safe try before a live customer?
4. Mark the lowest rung with a "no" as the root cause.
5. Write one two-week fix for that rung, an owner, and the usage number you will check on day 14.

## The deep version (high-stakes or company-wide rollouts)

- Run a separate card for each team or manager, and compare the strongest team's card to the weakest.
- Interview five or more people per team, including at least one manager and one new hire.
- Spot-check ten real outputs per team against the three judgments: true, right for this buyer, worth acting on.
- Run the fix on one team first and use another as a comparison before rolling it out.
- After the root-cause rung passes, re-score the full ladder at day 30 and move to the next rung up. Do not call the rollout fixed until Teach passes.

---
*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
