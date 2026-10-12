# F: Feedback

The step-five playbook: directional calibration against a standard, plus the spaced reinforcement that keeps skills from decaying. Accelerates Level 3 (Conscious Competence) toward Level 4 (Unconscious Competence).

**Use this file when:**
- Reps "practice but don't improve," or "plateau and stop growing."
- Designing a coaching cadence, a feedback system, or a reinforcement schedule after training.
- Feedback is happening but nothing changes, or reps hear different things from different managers.
- You are deploying AI call review or AI scoring and need rules for how its feedback reaches reps.

---

## 1. What Feedback is for, and what breaks without it

Feedback answers one question: "Am I moving toward good or toward bad?" It is directional. The learner needs to know which way they are heading, not just whether they "did it."

Feedback in LOPAFT is a measurement, not a check-in. "How did it go?" is a conversation. "Your D3 was a 2 on this call; here is the moment; here is the one adjustment" is Feedback.

| Feedback does | Failure if missing |
|---|---|
| Calibrates the learner against the standard | Application degrades into reinforcing bad habits. Reps get faster at the wrong thing. |
| Converts errors into the next rep's focus | Same mistake repeated for weeks |
| Spaces reinforcement over time | The skill decays along the forgetting curve after the program ends |
| Shows progress | Learners stop investing in a skill they cannot see improving |

**What breaks most often.** Without measurement against a standard, the operator does not know if the work got better. Second most common: feedback that is not safe. Group feedback in front of peers kills adoption. Feedback has to be safe before it can be honest.

**Feedback runs from Practice onward.** In Practice it is immediate and inside the rep (see P-practice.md). In Application it becomes a weekly system. After the program it becomes spaced reinforcement. This file covers all three.

---

## 2. The science you are applying

| Principle | Research base | What it means for Feedback |
|---|---|---|
| Forgetting curve | Memory research | Without review, recall drops steeply soon after learning, then levels off. Each well-timed review flattens the curve. |
| Spacing effect | Memory research, widely replicated | Reviews spread over time produce more durable learning than the same reviews massed together. |
| Retrieval practice | Testing-effect research | Recalling or performing from memory strengthens learning more than re-reading or re-watching. |
| Box-based spaced review | Spaced-review practice | Items you get right move to longer review intervals; items you miss move back to short ones. A simple way to run spacing by individual. |
| Three feedback questions | Feedback research | Where am I going? (feed up) How am I going? (feed back) Where to next? (feed forward) |
| Feedback can backfire | Meta-analytic feedback research | Feedback interventions do not always improve performance; a meaningful share make it worse, especially when feedback draws attention to the self rather than the task. |
| Situation-Behavior-Impact | Leadership-development practice | Situation, Behavior, Impact: anchor feedback in a specific moment and an observable behavior. |
| Feedforward | Executive-coaching practice | Focus on the next attempt, not a post-mortem on the last one. |
| Statistical process control | Quality-engineering research | Not every week-to-week change is real. Separate signal from noise before reacting. |

---

## 3. Design patterns

### Pattern A: One adjustment

Every feedback moment ends with one specific behavioral adjustment. Not a list. A list overloads working memory and reads as a verdict. Pick the adjustment with the most leverage on the current focus behavior.

### Pattern B: Task, not self (avoid backfire)

| Self-focused (avoid) | Task-focused (use) |
|---|---|
| "You're not a natural at discovery." | "At 12:40 the buyer said 'it's slowing us down,' and the next question was about timeline. Ask how they measure the slowdown first." |
| "Great call!" | "D5 was a 4: the buyer owned the next action. Keep that." |
| "You need to be more consultative." | "D2 stopped at one layer three times. Next call, ask 'what does that cause?' once more each time." |

### Pattern C: Standard-referenced, clip-anchored

Feedback cites the rubric line and a timestamped moment. Scores route attention; clips change behavior. A coaching note without a clip is an opinion.

### Pattern D: Self-assessment before external assessment

The learner scores first, then sees the coach or AI score. The gap between the two (calibration gap) is a leading indicator: as competence grows, self-scores converge with expert scores. Track it (see enablement-measure).

### Pattern E: Spaced reinforcement schedule

Rule of thumb: expanding intervals after initial learning, adjusted per person by performance (box-based review logic).

| Touch | When (after initial practice) | Format | Time |
|---|---|---|---|
| 1 | Day 1 | Retrieval: write the five behaviors and one example question each from memory | 5 min |
| 2 | Day 3 | One scenario question or a 2-min AI roleplay rep on the weakest behavior | 5 min |
| 3 | Day 7 | Live call review against the rubric with manager | 20 min |
| 4 | Day 14 | Unlabeled clip scoring (discrimination check) plus own call self-score | 10 min |
| 5 | Day 30 | Live call review; calibration gap check | 20 min |
| 6 | Day 60 | Retrieval scenario on far-transfer situations | 10 min |
| 7 | Day 90 | Delayed check: live calls plus a teach-back (see T-teach.md) | 30 min |

Box-review rule: if the learner performs at standard at a touch, the next interval expands. If not, the next touch returns to the previous interval for that behavior.

**Retrieval, not re-exposure.** Each touch asks the learner to recall or perform, not to rewatch the training. Re-watching feels productive and does less.

### Pattern F: Feedback sources and what each is good for

| Source | Good for | Weak at |
|---|---|---|
| Self | Building calibration and ownership | Accuracy early on |
| Peer | Volume, vicarious learning, scoring practice | Authority on hard calls |
| Manager | Judgment, context, motivation, accountability | Volume and consistency across managers |
| AI | Instant, consistent, full-coverage mechanical scoring | Judgment, context, motivation; correctness depends on calibration |
| Buyer | The real outcome signal | Usually indirect and delayed |

LOPAFT's division of labor: AI provides instant mechanical feedback; humans provide judgment.

### Pattern G: Signal before reaction

Weekly skill scores bounce. Before praising or intervening on a single week, ask whether the movement is outside normal variance. A rep whose D3 rate drops one week may be noise; three consecutive weeks below their own average is a pattern. See metric-health-dashboard for control-chart rules.

---

## 4. Exit criteria: Feedback has done its job

Feedback targets the transition from Level 3 to Level 4. Feedback never fully ends; its cadence widens as competence stabilizes.

| Signal | Still Level 3 | Moving to Level 4 |
|---|---|---|
| Live performance | At standard on most calls with weekly coaching | At standard across spaced checks, with coaching cadence widened |
| Calibration gap | Self-score differs from expert by a level or more | Self-score usually matches expert score |
| Delayed retention | Performance drops when the touch interval widens | Holds at standard at 30-, 60-, and 90-day checks |
| Under load | Drops the behavior on complex or stressful calls | Keeps it on complex calls without visible effort |
| Self-correction | Fixes errors after review | Catches and fixes during the call |
| Feedback source | Needs external feedback to see errors | Generates own accurate feedback |

**Decision rules**
- If scores plateau for three or more weeks, check the feedback first: is it one adjustment, clip-anchored, task-focused, and acted on in the next rep? Then check spacing: has reinforcement stopped?
- If the calibration gap is not shrinking, the learner is not using the standard. Return to O discrimination drills on that behavior.
- If a rep holds at standard across widening intervals, move them into Teach for that behavior.
- If feedback from different managers conflicts, stop and recalibrate managers before giving more feedback.
- If a rep disputes an AI score and is right, the rubric or tool needs fixing. Treat disputes as training signal for the system.

---

## 5. Instruments and templates

### 5.1 Weekly coaching session (20 minutes, one rep)

| Min | Block | What happens |
|---|---|---|
| 0-3 | Feed up | Restate the current focus behavior and the standard |
| 3-7 | Rep self-assessment | Rep shares self-score on one live call and the moment they chose |
| 7-13 | Clip review | Watch the moment together. Manager scores against the rubric. Discuss only the difference. |
| 13-16 | One adjustment | Manager and rep agree on one behavioral adjustment |
| 16-19 | Rehearse | Rep rehearses the adjusted moment once, out loud |
| 19-20 | Feedforward commitment | Rep states when they will use it next; manager logs it |

### 5.2 Coaching note (Situation-Behavior-Impact plus feedforward)

```
Rep: ______   Date: ______   Focus behavior: ______
Situation: [call, timestamp] ______
Behavior: [what was said or done, verbatim if possible] ______
Impact: [how the buyer responded / what it did to the deal] ______
Score (1-4): ___   Rep's self-score: ___   Gap: ___
One adjustment: ______
Next call to use it on: ______   Check date: ______
Clip link: ______
```

### 5.3 Coaching session quality self-check (manager)

- [ ] I coached only the current focus behavior.
- [ ] The rep self-assessed before I gave my score.
- [ ] My feedback cited a timestamped moment.
- [ ] I gave one adjustment, not a list.
- [ ] The feedback was about the task, not the person.
- [ ] The rep rehearsed the adjustment in the session.
- [ ] We agreed on when the rep will use it next.
- [ ] The session was private.

### 5.4 Spaced reinforcement tracker (per rep)

| Behavior | Touch 1 (d1) | Touch 2 (d3) | Touch 3 (d7) | Touch 4 (d14) | Touch 5 (d30) | Touch 6 (d60) | Touch 7 (d90) | Current interval |
|---|---|---|---|---|---|---|---|---|

Mark each touch: at standard (S) or below (B). Two B results in a row on a behavior resets that behavior to the day-7 interval and adds a Practice round.

### 5.5 Feedback system audit

- [ ] A written standard (rubric with anchors) exists and managers are calibrated to it.
- [ ] Every rep receives standard-referenced feedback on live work at a defined cadence.
- [ ] Feedback is private.
- [ ] Coaching notes cite clips.
- [ ] Self-assessment precedes external assessment.
- [ ] Calibration gap is tracked per rep.
- [ ] A spaced reinforcement schedule exists beyond the program end date.
- [ ] Reinforcement uses retrieval, not re-exposure.
- [ ] AI scores are calibrated against humans before reps see them.
- [ ] Reps can dispute an AI score, and disputes are reviewed.

**Scoring**: 9-10 = strong. 6-8 = gaps that will cause plateaus. Below 6 = feedback is opinion or absent.

---

## 6. Feedback in the AI era

AI call review changes the economics of Feedback. A manager could listen to a couple of calls per rep per week. A call-review tool scores every call. The bandwidth constraint that made feedback a program-level activity is gone. The judgment constraint is not.

| Shift | Implication |
|---|---|
| Full-coverage scoring | Feedback can be based on patterns across all calls, not one sampled call |
| Instant mechanical feedback | Reps can see rubric scores minutes after a call, tightening the loop |
| Consistency | A model applies the same rubric to every rep. Consistent is not correct: it applies the wrong parts of a rubric evenly too. |
| Automated nudges | Systems can detect a pattern and send the rep a nudge without a manager writing it |
| Spaced retrieval at scale | AI can generate scenario questions and short roleplays for each spaced touch, personalized to each rep's weak behavior |

**Rules for AI feedback**
1. **Calibrate before release.** Score a sample of calls by hand and by the tool. Publish agreement per rubric line. Do not show reps scores on lines that fail.
2. **Patterns, not single calls.** Machine feedback on one call reads as surveillance. Rule of thumb used in practice: a behavior must show up across several calls in a short window (for example, three calls in two weeks) before a nudge fires.
3. **Private, with evidence.** Nudges go to the rep directly, with timestamps and one suggested phrase. Never in a public channel. Public leaderboards of AI-detected weakness kill adoption fast.
4. **Managers audit the machine.** Managers see every nudge sent to their team and can pause a bad pattern until it is retuned.
5. **Reps can dispute.** A one-click dispute read by a human. Disputes are the training signal for the rubric. Track the dispute rate.
6. **Scores route attention; humans coach.** The AI decides where to look. The manager decides what it means and delivers the adjustment. LOPAFT is explicit: AI gives mechanical feedback, humans give judgment.
7. **Feedback on the rep's judgment of the AI.** When reps correct AI reviews, compare their corrections to the manager's view. That is feedback on the second skill.

---

## 7. Worked example (illustrative)

> **Program scenario (illustrative, used in all six step files).** A 12-AE mid-market team is rolling out a new discovery method and an AI call-review tool at the same time. Two frontline managers (6 AEs each), one enablement lead, one RevOps analyst. The method has five scored behaviors: **D1** Hypothesis opener, **D2** Layered problem questions, **D3** Quantified impact confirmed by the buyer, **D4** Buying process mapped, **D5** Dated next step agreed live. The AI tool scores every recorded call against D1-D5 and drafts a call review. The AEs' second skill is judging that review: catching wrong or missing scores before acting on it. Traffic light: red. Program: 10 weeks plus a day-90 check. The week-0 baseline (enablement-assess) placed most AEs at Level 1 or 2 on D3 and D4, and at Level 1 on judging AI output.

**Feedback runs from week 2 (inside Practice) through day 90 and beyond.**

**System design**

| Layer | Design |
|---|---|
| Inside Practice (weeks 2-5) | Observer gives one adjustment per rep; immediate retry (see P-practice.md) |
| Weekly coaching (weeks 3-10) | 20-minute session per AE per week, agenda 5.1. Manager picks the clip from the AI tool's lowest-scoring behavior for that AE, then verifies it by listening. |
| AI scores to reps | D1, D3, D5 visible from week 3. D2 and D4 visible from week 6, after recalibration passed. |
| AI nudges | Fire only when a behavior is below standard on 3 calls in 2 weeks. Sent privately with two timestamps and one suggested question. Managers audit weekly. |
| Disputes | One-click; enablement lead reviews weekly |
| Spaced touches | Schedule in 5.4, starting from each behavior's first live week. Retrieval items generated by AI from the rubric, reviewed by the enablement lead before release. |
| Calibration gap | AE self-score versus manager score, logged in every coaching note |
| Reporting | RevOps tracks per-AE behavior rates with control limits; flags only Rule-triggered changes (metric-health-dashboard) |

**What happened (illustrative)**
- **Week 5 plateau.** Four AEs' D3 scores were flat for three weeks. The enablement lead audited coaching notes against 5.3. On one team, notes listed three or four adjustments per session and few cited clips. That manager moved to one-adjustment, clip-anchored notes after a joint session with the enablement lead (see enablement-coach). D3 for that team moved up within two weeks.
- **Disputes as signal.** In week 4, several AEs disputed D5 scores: the tool gave a 2 when the next step was agreed live but the calendar invite went out minutes after the call. The rubric line was clarified and the tool reconfigured. Dispute rate on D5 dropped afterward.
- **Calibration gap.** By week 8, most AEs' self-scores matched their manager's score on most behaviors. Two AEs still self-scored D4 a level high. Both received one O discrimination drill on D4 and a tighter touch interval.
- **Noise versus signal.** In week 7, team-level D2 dropped sharply. RevOps checked before anyone reacted: the week had a holiday and a cluster of renewal calls the rubric was not designed for. Within control limits once renewal calls were excluded. No intervention.
- **Spacing.** At the day-30 touch, D1 and D5 held for nearly everyone; their intervals expanded. D4 slipped for three AEs; their D4 interval reset to day 7 with a Practice round.

**Status at week 10**

| Signal | Result |
|---|---|
| At standard across widening intervals on all five behaviors | 7 AEs: move into Teach for those behaviors and keep the day-60 and day-90 touches |
| Holding most behaviors, one behavior on a reset interval | 4 AEs: continue weekly coaching on that behavior only |
| Extended timeline (low volume) | 1 AE: simulated reps plus monthly live review |

---

## 8. Anti-patterns

| Anti-pattern | Why it fails | Fix |
|---|---|---|
| "How did it go?" as feedback | No standard, no direction | Rubric score plus clip plus one adjustment |
| The feedback list | Overload; reads as a verdict; nothing changes | One adjustment |
| Group feedback on individual performance | Kills safety, then honesty, then adoption | Private by default |
| Feedback about the person | Can lower performance | Task-focused, behavior-specific |
| Program ends, reinforcement ends | Forgetting curve wins | Spaced touches to day 90 and beyond |
| Re-watching training as reinforcement | Feels productive, does less | Retrieval: recall or perform from memory |
| Reacting to every weekly wiggle | Fire drills over noise | Control limits before reacting |
| Uncalibrated AI scores shown to reps | Reps stop trusting the tool and the program | Publish human-versus-tool agreement; hide failing lines |
| Machine feedback on single calls | Reads as surveillance | Pattern thresholds |
| Manager reads AI scores instead of coaching | Scores without judgment do not change behavior | Scores route attention; managers coach with clips |
| Managers not calibrated to each other | Reps hear conflicting standards | Monthly manager calibration (see O-observe.md) |

---

## Related

- `A-application.md`: Feedback runs on live application.
- `T-teach.md`: next step for reps holding at standard across spaced checks.
- `O-observe.md`: the rubric and anchors Feedback measures against.
- `enablement-measure`: calibration gap, behavior change rate, and four-level training-evaluation metrics.
- `enablement-coach`: manager feedback quality.
- `metric-health-dashboard`: signal versus noise on skill trends.

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). LOPAFT framework by Jonathan Kvarfordt. Licensed CC BY 4.0.*
