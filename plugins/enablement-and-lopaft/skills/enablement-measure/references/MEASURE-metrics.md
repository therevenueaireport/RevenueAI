# MEASURE: Metrics, Instruments, and ROI for Enablement Programs

**Use this file when:**
- You are designing the measurement plan for a new enablement, coaching, or AI-adoption program and need exact metric definitions, formulas, and owners.
- A leader asks "is training working?" and the only numbers on hand are completions, logins, and satisfaction scores.
- You need a comparison group so the result is not confounded by territory, seasonality, a pricing change, or a new comp plan.
- You owe a CFO or CRO an ROI figure and want one that survives scrutiny.

This file is the depth layer for `enablement-measure`. For control charts and signal-versus-noise rules on ongoing metrics, use `metric-health-dashboard`. For sample size, power, and test analysis, use `ab-test-evaluator`. Learner baselines come from `enablement-assess`.

---

## 1. The Measurement Chain

Every enablement metric sits on one link of a five-link chain. A program is only proven when the chain holds from left to right.

| Link | Question | Example metric (AI call-review rollout) | Type |
|---|---|---|---|
| 1. Access | Can they use it? | Seats provisioned, training attended | Adoption |
| 2. Usage | Do they use it in the workflow? | % of eligible calls with an AI review opened within 24h | Adoption |
| 3. Capability | Can they do the skill to standard? | Rubric score on scored practice reps | Learning |
| 4. Behavior | Do they do it on live work? | Rubric score on live calls, scored by manager or AI against the standard | Behavior |
| 5. Outcome | Did the business number move? | Stage 2 to Closed Won rate vs comparison group | Results |

**Rule:** Never report a link without the link to its right, unless you label it "leading indicator, outcome not yet measurable." A login count reported alone is the start of Optimization Theater (the author's name for AI programs that produce activity reporting without revenue movement).

### Separating adoption from behavior from outcome

The most common enablement measurement error is treating adoption as success. "Logins = success" fails for three reasons:

1. **Access is not use.** A rep can log in to dismiss a notification.
2. **Use is not skill.** A rep can open the AI call review and ignore every recommendation.
3. **Skill is not outcome.** A rep can execute the behavior perfectly in a market where it does not move the number. That is a program design problem, and you only find it if you measure link 5 separately.

| If you see | It means | Do this |
|---|---|---|
| High adoption, flat behavior | People touch the tool or content but have not changed how they work | Check Observe and Feedback: is there a written standard and is anyone scoring against it? |
| Rising behavior, flat outcome (after enough cycle time) | The behavior is not the lever, or the outcome window is too short | Re-check the causal hypothesis. Confirm the outcome window covers at least one sales cycle |
| Low adoption, rising outcome in the cohort | Something else moved the number | Check the comparison group. Do not claim the win |
| High adoption, rising behavior, rising outcome vs comparison | The chain holds | Report it, with the comparison and the range |

**Design rule:** Every program dashboard shows adoption, behavior, and outcome in separate, labeled rows. Never blend them into one "program health" score. Blended scores let adoption hide a behavior failure.

---

## 2. The Metric Library

Each metric has a definition, formula, source, cadence, and type. "Leading" means it moves before the business outcome. "Lagging" means it confirms after the fact.

### 2.1 Level 1: Reaction (K1)

The four-level training evaluation model (Reaction, Learning, Behavior, Results) is the base. K1 is the weakest evidence; collect it cheaply and do not over-weight it. Published work on performance-focused learner surveys is the practical guide here: ask about likely application, not enjoyment.

| Metric | Formula | Source | Cadence | Lead/Lag |
|---|---|---|---|---|
| Attendance rate | Attended sessions / scheduled sessions, per learner | LMS or calendar | Per session | Leading |
| Pre-work completion | Learners who completed pre-work / learners assigned | LMS | Per session | Leading |
| Relevance score | Mean of item R1 below | Post-session pulse | Per session | Leading |
| Intent to apply | % answering 4 or 5 on item R2 | Post-session pulse | Per session | Leading |
| Commitment specificity | % of Q3 open-text answers that name a specific behavior and situation | Post-session pulse, coded | Per session | Leading |

**Three-item post-session pulse (use exactly this, under 60 seconds):**

| Item | Scale |
|---|---|
| R1. "What we covered today applies to deals or accounts I am working this month." | 1 Strongly disagree to 5 Strongly agree |
| R2. "I will use this on a live call, email, or account in the next 7 days." | 1 Strongly disagree to 5 Strongly agree |
| Q3. "What will you do differently this week, and on which deal or account?" | Open text |

Code Q3 answers as Specific (names behavior and situation), Vague (names behavior only), or Empty. Shrinking Q3 specificity is an early stall signal (see `enablement-momentum`).

### 2.2 Level 2: Learning (K2)

| Metric | Formula | Source | Cadence | Lead/Lag |
|---|---|---|---|---|
| Knowledge gain | Post-test score minus pre-test score, per learner, same item bank | LMS assessment | Pre, mid, post | Lagging for K2 |
| Calibration accuracy | % of good/bad examples a learner classifies the same way the calibrated standard does | Observe exercise | Per Observe session | Leading |
| Confidence shift | Change in self-rated confidence on the target skill (1 to 5) | Pulse survey | Weekly or biweekly | Leading |
| Retention check | Score on a 5-item retrieval quiz 2 to 4 weeks after the session, no notice | LMS or form | Spaced | Leading |

Retention checks use retrieval practice (the testing effect) as both measurement and reinforcement. A learner who passed the post-test but fails the spaced check has hit the forgetting curve; schedule Feedback reps, not another session.

### 2.3 Level 3: Behavior (K3)

This is the level that most programs skip, and the one that matters most. Behavior is measured on live work, against a written rubric.

| Metric | Formula | Source | Cadence | Lead/Lag |
|---|---|---|---|---|
| Live rubric score | Mean rubric score (1 to 4) on the target behavior across scored live artifacts | Call recordings, emails, CRM notes, scored by manager or AI against the rubric | Weekly | Leading for outcomes |
| Behavior frequency | Eligible situations where the behavior appeared / eligible situations | Call recording trackers, CRM fields | Weekly | Leading |
| Behavior change rate | Learners whose live score rose 1+ rubric level from baseline and held for 2 consecutive scoring periods / all learners | Scored artifacts | Biweekly | Leading |
| Self-assessment accuracy | Mean absolute gap between learner self-score and calibrated score | Self-score form plus manager score | Biweekly | Leading |
| Coaching delivered to standard | Coaching sessions held that meet the session standard / sessions planned | Manager coaching log | Weekly | Leading |
| Time to first live application | Days from Practice completion to first scored live use | Practice log plus scored artifacts | Per learner | Leading |

**Scoring standard for live behavior (example rubric, discovery questioning):**

| Score | Descriptor |
|---|---|
| 1 | Behavior absent. Rep pitches before establishing a problem. |
| 2 | Behavior present but surface. Asks a scripted question, does not follow up on the answer. |
| 3 | Behavior to standard. Asks about the problem, follows up at least twice, confirms impact in the buyer's words. |
| 4 | Behavior adapted. Does all of 3 and tailors the follow-ups to the buyer's role and the deal stage. |

**Inter-rater rule:** Before scoring begins, have every scorer (managers and any AI scorer) score the same 5 artifacts. If any two scorers differ by 2+ points on any artifact, run a calibration session before live scoring. Re-check calibration monthly. An uncalibrated rubric produces noise that looks like data.

### 2.4 Level 4: Results (K4)

| Metric | Formula | Source | Cadence | Lead/Lag |
|---|---|---|---|---|
| Stage conversion | Opportunities advancing from stage X to Y / opportunities entering stage X, in window | CRM | Monthly | Lagging |
| Win rate | Closed Won / (Closed Won + Closed Lost), on opportunities created after program start | CRM | Monthly, judged quarterly | Lagging |
| Sales cycle length | Median days from opportunity creation to close, Closed Won only | CRM | Monthly | Lagging |
| Average deal size | Mean or median ACV on Closed Won | CRM | Quarterly | Lagging |
| Ramp time | Days from start date to a defined productivity threshold (for example, first quota-attaining month) | CRM plus HRIS | Per hire | Lagging |
| Pipeline per rep | Qualified pipeline created per rep per month | CRM | Monthly | Lagging |
| Gross revenue retention / expansion | Standard definitions, for CSM programs | Billing, CRM | Quarterly | Lagging |

**Cohort rule:** Measure K4 on work that started after the program. A deal that was 80% done when the rep took the training is not evidence either way.

### 2.5 Level 5: ROI

A conservative training-ROI method adds a fifth level: return on investment, calculated after isolating the program's effect and converting it to money. Section 6 gives the method and a worked example.

---

## 3. Metrics by LOPAFT Step

LOPAFT (Learn, Observe, Practice, Apply, Feedback, Teach) tells you which rung a learner or team is on. Each rung has a deliverable and a metric that proves the rung is working. When a rung metric is missing or failing, the rungs above it cannot hold. Fix the lowest failing rung first.

| Step | Deliverable | Leading metric | Pass threshold (rule of thumb) | Evaluation level |
|---|---|---|---|---|
| L: Learn | Session, SOP, launch doc | Knowledge check pass rate; R1 relevance | 80%+ pass; R1 mean 4.0+ | K1, K2 |
| O: Observe | Examples library with good and bad samples | Calibration accuracy on good/bad classification | 80%+ agreement with standard | K2 |
| P: Practice | Sandbox, role play, dry runs, no customer | Practice reps per learner; practice rubric trend | Planned reps completed; score rising | K2 to K3 boundary |
| A: Apply | First live reps with a named owner | Time to first live application; behavior frequency | First live rep within 7 days of Practice; frequency rising weekly | K3 |
| F: Feedback | Scoring against a written standard | Coaching delivered to standard; self-assessment accuracy | 90%+ of planned sessions; gap shrinking | K3 |
| T: Teach | Peer teach-back, next-hire walkthrough | Teach-back completion and quality score | Each learner completes 1 teach-back scored 3+ | K3 (durability) |

All thresholds above are rules of thumb. Set your own at design time and write them down before launch so you cannot move the goalposts.

**Diagnostic read:** If behavior is flat, walk this table from the top. The first rung that fails its threshold is the root cause. High Learn scores with low calibration accuracy means Observe is missing. Good practice scores with slow time to first live application means Apply has no owner or no trigger. Rising frequency with flat rubric scores means Feedback is not measuring against a standard.

---

## 4. Data Sources in a Typical Revenue Stack

You do not need new systems. You need to know which existing system holds each link of the chain.

| Source | What it holds | Metrics it feeds | Watch out for |
|---|---|---|---|
| CRM | Opportunities, stages, dates, amounts, owners, activity logs | All K4 metrics; behavior frequency via required fields | Stage definitions that changed mid-program; reps back-filling fields |
| Call recording / conversation intelligence | Recordings, transcripts, keyword trackers, talk ratios, AI-generated scores | Live rubric score, behavior frequency | Tracker hits are not behavior quality; a keyword can be said badly |
| LMS or content platform | Enrollments, completions, assessment scores, content views | K1, K2 | Completion is not learning; time-on-page is not attention |
| AI tool usage logs (admin console) | Active users, sessions, feature use, prompts run, outputs generated, outputs accepted or edited | Adoption metrics, workflow coverage, acceptance rate | Seat counts and session counts inflate; separate "opened" from "used output" |
| Sales engagement platform | Sequences, steps, reply and meeting rates | Behavior frequency (for SDR programs), pipeline leading metrics | Volume changes swamp quality changes |
| Manager coaching log (form or CRM object) | Session date, skill coached, artifact reviewed, adjustment given, commitment | Coaching delivered to standard | Logs filled after the fact from memory |
| Survey tool | Pulses, confidence, Q3 commitments | K1, confidence shift | Survey fatigue; keep pulses to 3 items |
| HRIS | Start dates, tenure, role changes, territory changes | Ramp time; comparison group matching | Mid-program role changes contaminate cohorts |

### AI-tool usage metrics, ranked by evidence strength

| Rank | Metric | Formula | What it proves |
|---|---|---|---|
| Weakest | Seats provisioned | Count | Purchase happened |
| | Logged in (any) | Users with 1+ session / seats | Curiosity |
| | Weekly active users | Users active in 3+ of last 4 weeks / eligible users | Habit forming |
| | Workflow coverage | Eligible workflow events where the tool was used / eligible events | Embedded in the job |
| | Output acceptance | Outputs used with light or no edit / outputs generated | Output meets the bar |
| Strongest | Output quality to standard | Sampled outputs scoring 3+ on the rubric / sampled outputs | The work got better |

Report the bottom two rows alongside the top rows, always. Also track the reverse: outputs a human had to override or redo. A rising override rate is a quality signal, not a failure to hide.

---

## 5. Comparison Groups and Holdouts

Without a comparison group, any outcome change is confounded with everything else that changed in the same quarter: a price change, a new territory model, seasonality, a strong product release, a market shift. Pick the strongest design your org will tolerate.

### 5.1 Design options

| Design | How | Strength | Use when |
|---|---|---|---|
| Randomized by team (cluster randomization) | Randomly assign whole teams or pods to program now vs later | Strongest | 6+ comparable teams; leadership accepts a delay for some |
| Staggered rollout (stepped wedge) | All teams get the program, in waves; each wave serves as comparison for the next | Strong; politically easy | Most revenue orgs. Default choice |
| Matched comparison | Pick non-program reps matched on tenure, segment, territory, baseline metric | Moderate | Program is opt-in or limited to one region |
| Pre/post with trend adjustment | Compare cohort to its own baseline, adjusted for trailing trend and seasonality | Weak | No comparison possible. Label results "directional" |
| Participant estimate (training-ROI method) | Participants and managers estimate % of improvement due to program, discounted by their confidence | Weakest, but structured | Last resort, or as a cross-check |

**Randomize teams, not reps.** Reps on the same team share a manager, a territory type, and team chat channels. Randomizing reps within a team leaks the program into the comparison group.

### 5.2 Difference-in-differences

The standard read for staggered or matched designs:

```
Program effect = (Program group after - Program group before)
               - (Comparison group after - Comparison group before)
```

This removes changes that hit both groups equally (pricing, seasonality, market). It does not remove changes that hit only one group. Check for those in the confounder log.

**Parallel trends check:** Plot both groups' metric for the 3 to 6 periods before launch. If the lines were already diverging, difference-in-differences will mislead. Find a better comparison group or report pre/post as directional only.

### 5.3 Sample size reality

Win rate is a proportion measured on opportunities, but opportunities are clustered inside reps and teams. That clustering shrinks your effective sample size. The design effect (Kish) is:

```
Design effect = 1 + (m - 1) x ICC
Effective n = actual n / design effect
```

where m is opportunities per cluster and ICC is the intra-cluster correlation. Even a small ICC with many opportunities per rep shrinks effective sample size sharply.

Use `ab-test-evaluator` for the power calculation. Rule of thumb: most single-team enablement programs cannot detect a few-point win rate change within one quarter. Plan for that up front:
- Pick a primary outcome with more events (stage conversion often has more events than win rate).
- Lengthen the window to cover at least one full sales cycle.
- Let behavior metrics (K3) carry the evidence chain, and report the outcome as a range.

### 5.4 Confounder log

Keep a dated log from day one. Every entry: date, change, which group it touched, expected effect direction.

| Date | Change | Touches | Expected effect |
|---|---|---|---|
| [date] | [e.g., price increase on mid tier] | [Both / Program / Comparison] | [e.g., lower win rate] |

Review it before every readout. If a confounder hit only one group, say so in the readout.

### 5.5 Holdout ethics and politics

- Frame the comparison group as "wave 2," not "the control." Everyone gets the program.
- Give the comparison group the program content after the measurement window, not the coaching cadence mid-window.
- Pre-register the design: write down groups, primary metric, window, and decision rule before launch, and share it with the sponsor. This is what makes the result credible later.

---

## 6. ROI Calculation (Conservative Training-ROI Method)

### 6.1 Formulas

```
Benefit-cost ratio (BCR) = Program benefits / Program costs
ROI (%) = (Program benefits - Program costs) / Program costs x 100
```

Benefits are monetary values of isolated improvements, converted to profit contribution, not revenue. Costs are fully loaded.

### 6.2 Conservative standards (apply all)

The method's guiding principles are built to make ROI claims defensible. The ones that matter most for revenue teams:

1. **Isolate the effect.** Use the comparison group. If none, use participant estimates discounted by confidence.
2. **Use profit contribution, not bookings.** Multiply incremental revenue by gross margin.
3. **Count only first-year benefits** for short programs. Do not project multi-year gains.
4. **Fully load costs**, including participant and manager time.
5. **Use the most conservative alternative** when estimates differ.
6. **Report intangibles separately.** Morale, manager confidence, and retention signals go in a separate row with no dollar value.
7. **No data, no improvement.** If a group did not report, assume no benefit for it.

### 6.3 Cost checklist

| Cost item | How to calculate |
|---|---|
| Design and development | Hours x loaded hourly rate |
| Delivery | Facilitator hours x rate, plus any external fees |
| Participant time | Learner hours in sessions, practice, pre-work x loaded rate |
| Manager time | Coaching, calibration, observation hours x loaded rate |
| Tools and licenses | Incremental license cost attributable to the program, for the benefit period |
| Program management and evaluation | Hours x rate |
| Overhead | Only if material and allocable |

### 6.4 Worked example (illustrative, all numbers invented for teaching)

**Program:** Discovery questioning skill, with an AI call-review tool used for scoring and feedback. 8 weeks. Primary outcome: Stage 2 to Closed Won conversion.

**Design:** Staggered rollout. Wave 1 (program group): 3 teams, 24 AEs, 3 managers. Wave 2 (comparison): 2 teams, 16 AEs, start after the measurement window. Teams matched on segment and baseline conversion. Parallel trends check passed on 4 prior quarters.

**Step 1. Costs (program group only, fully loaded)**

| Item | Calculation | Cost |
|---|---|---|
| Design and development | 120 hrs x $90 | $10,800 |
| AI call-review licenses, 12 months | 24 seats x $50 x 12 | $14,400 |
| Rep time | 24 AEs x 14 hrs x $75 | $25,200 |
| Manager time | 3 managers x 24 hrs x $110 | $7,920 |
| Program management and evaluation | 60 hrs x $90 | $5,400 |
| **Total** | | **$63,720** |

**Step 2. Behavior evidence (the chain)**

| Link | Program group | Comparison group |
|---|---|---|
| Workflow coverage (AI review opened on eligible calls) | 78% by week 8 | n/a |
| Live discovery rubric, mean | 1.9 to 2.9 | 2.0 to 2.1 |
| Behavior change rate | 17 of 24 AEs (71%) | 2 of 16 AEs (13%) |

**Step 3. Isolate the outcome**

| | Before (prior quarter) | After (quarter following program) | Change |
|---|---|---|---|
| Program group conversion | 22% | 27% | +5 pts |
| Comparison group conversion | 21% | 23% | +2 pts |
| **Difference-in-differences** | | | **+3 pts** |

**Step 4. Convert to money, conservatively**

- Program group works about 720 Stage 2 opportunities per year (24 AEs x 30).
- Quarter 1 after program: 180 opportunities x 3 pts = 5.4 incremental wins.
- Quarters 2 to 4: assume the lift decays to half (persistence haircut): 540 x 1.5 pts = 8.1 incremental wins.
- First-year incremental wins: 13.5.
- Incremental bookings: 13.5 x $28,000 average ACV = $378,000.
- Profit contribution at 75% gross margin: **$283,500.**

**Step 5. Calculate**

```
BCR = 283,500 / 63,720 = 4.45
ROI = (283,500 - 63,720) / 63,720 x 100 = 345%
```

**Step 6. Sensitivity and honesty**

| Scenario | Incremental wins | Benefit | ROI |
|---|---|---|---|
| Lift ends after Q1 (no persistence) | 5.4 | $113,400 | 78% |
| Base case (half persistence) | 13.5 | $283,500 | 345% |
| Break-even | 3.03 | $63,720 | 0% |

Break-even needs about 3 incremental wins in a year: $63,720 / ($28,000 x 0.75).

**Statistical caveat (state it in the readout):** With roughly 180 opportunities per quarter in the program group, a 3-point difference-in-differences is well inside the noise for a single quarter. The outcome result is directional. The case rests on the full chain: coverage rose, live behavior scores rose in the program group and not in the comparison, and the outcome moved in the predicted direction. Report ROI as a range (78% to 345%) with the break-even, and commit to re-reading at two quarters.

**Intangibles (reported, not monetized):** Managers report shorter coaching prep using AI-flagged clips. Two AEs volunteered to run teach-backs for wave 2.

### 6.5 When you have no comparison group

Use the participant-estimate method as a floor:

1. Ask each participant and their manager: "Of the improvement in [metric], what percent was caused by this program?" and "How confident are you in that estimate (0 to 100%)?"
2. Adjusted attribution = estimated % x confidence %.
3. Use the lower of the participant and manager figures.
4. Label the result "estimate-based, not experimental."

Pair it with the success case method: survey the cohort, interview the 3 to 5 most successful and 3 to 5 least successful learners, and document what the successful ones did differently and what blocked the others. Success cases explain the number and give you the next program's fixes.

---

## 7. Collection Cadence

| Cadence | What to collect | Owner | Time cost |
|---|---|---|---|
| Per session | Attendance, pre-work, 3-item pulse | Enablement | 1 min per learner |
| Weekly | AI tool usage, workflow coverage, coaching log completion, practice reps, live rubric scores (sample) | Enablement plus managers | 15 to 30 min per manager |
| Biweekly | Behavior change rate, self-assessment accuracy, confidence shift | Enablement | 1 hr |
| Monthly | Stage conversion, cycle length, pipeline per rep, scorer calibration check | RevOps | 2 hrs |
| Quarterly | Win rate, deal size, difference-in-differences, ROI, success case interviews | RevOps plus Enablement | 1 to 2 days |

**Sampling rule for live scoring:** Score 2 artifacts per rep per week during the program, chosen at random from eligible calls, not chosen by the rep. Rep-chosen samples measure their best day.

---

## 8. Dashboard Design (Layout Spec)

One page. Four labeled rows, top to bottom in chain order. Never blend rows.

```
+--------------------------------------------------------------------------------+
| HEADER: Program name | Week N of M | Cohort size | Comparison group size        |
|         Primary outcome + decision date | Status: On track / Watch / Intervene  |
+--------------------------------------------------------------------------------+
| ROW 1  ADOPTION (leading)                                                      |
|  [Attendance trend]  [Pre-work trend]  [WAU / eligible]  [Workflow coverage]   |
+--------------------------------------------------------------------------------+
| ROW 2  LEARNING + PRACTICE (leading)                                           |
|  [Knowledge gain]  [Calibration accuracy]  [Practice reps vs plan]  [Confidence]|
+--------------------------------------------------------------------------------+
| ROW 3  BEHAVIOR (leading for outcome)                                          |
|  [Live rubric score, program vs comparison, weekly line]                       |
|  [Behavior change rate]  [Coaching delivered to standard]  [Self-assess gap]   |
+--------------------------------------------------------------------------------+
| ROW 4  OUTCOME (lagging)                                                       |
|  [Primary outcome, program vs comparison, with pre-period, control limits]     |
|  [Guardrail: deal size or cycle length]  [Confounder log: last 3 entries]      |
+--------------------------------------------------------------------------------+
| SIDE PANEL: Alerts fired this week (rule, metric, owner, action due)           |
+--------------------------------------------------------------------------------+
```

**Tile spec:** Each tile shows current value, baseline, target, and a sparkline of the last 8 periods. Status color only when a pre-set rule fires, not when the number "looks low."

**Alert rules:** Use the rule-of-thumb stall thresholds from `enablement-momentum` during the first 8 weeks. Once you have 8+ periods of data, switch to the standard control-chart run rules in `metric-health-dashboard`.

**Guardrail tile:** Every outcome push needs a guardrail. If the program targets conversion, guard average deal size and cycle length. If it targets activity volume, guard reply rate and meeting quality.

**Rep-level views** go to managers only, not to the cohort. Public rep-level rankings during a program damage the safety that Practice and Feedback depend on.

---

## 9. Executive Reporting Template

One page, four blocks. Fill every bracket. If a bracket cannot be filled, write "not yet measurable" and the date it will be.

```
PROGRAM: [Name]            PERIOD: [dates]          SPONSOR: [name]
DECISION REQUESTED: [Continue / Expand to wave 2 / Change / Stop]

1. HEADLINE (one sentence)
   [Target behavior] moved from [baseline] to [current] in the program group
   vs [comparison change] in the comparison group. [Outcome] moved [direction,
   range] vs comparison. Read is [directional / confirmed].

2. THE CHAIN
   | Link       | Metric                 | Program  | Comparison | Status |
   | Adoption   | [workflow coverage]    | [x]      | n/a        | [ ]    |
   | Capability | [practice rubric]      | [x]      | n/a        | [ ]    |
   | Behavior   | [live rubric score]    | [x to y] | [x to y]   | [ ]    |
   | Outcome    | [primary outcome]      | [x to y] | [x to y]   | [ ]    |

3. MONEY
   Costs (fully loaded): $[ ]
   Benefits (isolated, margin-adjusted, first year): $[low] to $[high]
   ROI: [low]% to [high]%      Break-even: [n incremental wins / units]
   Method: [difference-in-differences / participant estimate]
   Intangibles: [list, no dollar values]

4. WHAT WE LEARNED AND WHAT CHANGES
   Lowest failing LOPAFT rung found: [step], fixed by [action]
   What we stopped or cut: [item]
   Confounders: [list]
   Next read date: [date]
```

**Rules for the readout:**
- Lead with behavior and outcome, not completions.
- Always show the comparison group. A number with no comparison invites "the market did that."
- Report a range, not a point estimate, when the sample is small.
- Name what you cut or reversed. A program that never stops anything reads as theater.

---

## 10. Common Mistakes and Fixes

| Mistake | Why it fails | Fix |
|---|---|---|
| Logins and completions as the success metric | Proves access, not behavior or outcome | Report the full chain in separate rows |
| No baseline captured before launch | No way to show movement | Run `enablement-assess` and pull 3 to 6 periods of outcome history before kickoff |
| Measuring outcomes on deals already in flight | Pre-program work contaminates the result | Use deals created after program start |
| Rep-selected call samples | Measures best day, not typical day | Random sample of eligible calls |
| Uncalibrated rubric | Scores reflect the scorer, not the rep | Calibrate on 5 shared artifacts before scoring; re-check monthly |
| AI score trusted without spot-checks | Model errors scale silently | Managers score a random 10% of AI-scored artifacts each month; track agreement |
| Moving the goalposts | Any result can be called success | Pre-register metric, threshold, window, decision rule |
| Claiming bookings as ROI | Overstates value | Convert to profit contribution with gross margin |
| Reporting a single-quarter win rate change as proof | Usually within noise | Report as directional; use behavior chain; re-read next quarter |
| Blending metrics into one health score | Adoption hides behavior failure | Keep rows separate |
| Leaderboards during Practice | Kills safety, invites gaming (a measure that becomes a target stops measuring) | Rep-level detail to managers only |

---

## 11. Pre-Launch Measurement Checklist

- [ ] Target behavior written as an observable action, with a 4-level rubric
- [ ] Scorers calibrated on shared artifacts
- [ ] Primary outcome named, with 3 to 6 periods of baseline
- [ ] Guardrail metric named
- [ ] Comparison design chosen and documented (groups, window)
- [ ] Parallel trends checked
- [ ] Power reviewed with `ab-test-evaluator`; outcome expectations set as a range
- [ ] Data source and owner assigned for every metric
- [ ] Collection cadence on calendars
- [ ] Dashboard built with four separate rows
- [ ] Alert thresholds written down
- [ ] Confounder log started
- [ ] Cost tracking started (hours by role)
- [ ] Readout dates set and shared with sponsor

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). LOPAFT framework by Jonathan Kvarfordt. Licensed CC BY 4.0.*
