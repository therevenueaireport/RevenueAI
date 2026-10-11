# ASSESS Methods: Baseline Instruments, Rubrics, and Placement

**Use this file when:**
- You are about to design a program and need to know where each learner actually starts, skill by skill.
- You are rolling out an AI tool (call review, research assistant, drafting agent) and need to know if the team, the data, and the managers are ready.
- A program is underperforming and you suspect it was built for a learner who does not exist.
- You need a baseline that `enablement-measure` can track against later.

This file holds the instruments. The SKILL.md holds the logic. Run them in the order below.

---

## 1. The Assessment Sequence

| Step | What you do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1 | Define the skill as observable behaviors | Skill definition card | 1-2 hours, once per skill |
| 2 | Build or adapt the rubric | 4-level rubric | 2-3 hours, once per skill |
| 3 | Calibrate the raters | Agreement check on 3-5 shared samples | 60-90 min |
| 4 | Run the learner baseline survey | Self-report per learner | 10-15 min per learner |
| 5 | Run the manager observation checklist | Manager read per learner | 10 min per learner |
| 6 | Score real calls or artifacts | Observed score per learner | 15-20 min per sample |
| 7 | Triangulate and place each learner | Four Levels placement + starting LOPAFT step | 5 min per learner |
| 8 | Segment the cohort | Segment map and routing | 1 hour |
| 9 | Write the baseline report | Report (template in Section 11) | 2 hours |

**The triangulation rule:** never place a learner from one source. Use at least two of: self-report, manager observation, scored artifact. When sources disagree, the scored artifact wins on performance and the self-report wins on awareness.

---

## 2. Step 1: The Skill Definition Card

You cannot assess "discovery" or "AI adoption." You can assess behaviors. If a behavior cannot be seen in a recording, a document, or a system log, it does not go on the card.

```
SKILL DEFINITION CARD

Skill name:            [e.g., Confirming the buying process before proposing]
Role(s):               [AE / SDR / CSM / Manager]
Why it matters:        [The business outcome it drives, in one sentence]
Where it shows up:     [Call stage, document, CRM field, AI tool log]

Observable behaviors (3-6 max):
  B1: [Verb + object + condition. e.g., "Asks how the last similar purchase was approved"]
  B2:
  B3:

What "not done" looks like:     [The most common failure, described as behavior]
What "done well" looks like:    [Description, plus link to an example recording or artifact]
Evidence source:                [Call recording / email / CRM / tool usage log]
Prerequisite skills:            [What must already be at Level 3+ for this to be learnable]
```

**Decision rule:** if a skill needs more than six behaviors to describe, it is two skills. Split it and assess each separately. This matches the one-skill-at-a-time principle in `enablement-coach`.

---

## 3. Step 2: The Skill Rubric, Mapped to the Four Levels

### Why a single performance score cannot place a learner

The Four Levels describe two things at once: **performance** (can they do it?) and **awareness** (do they know where they stand?). A rubric that only scores performance cannot tell Level 1 from Level 2, because both fail to execute. And it struggles to tell Level 3 from Level 4, because both can execute when the conditions are easy.

So every rubric in this system scores three dimensions:

| Dimension | Question | Source |
|---|---|---|
| **Performance** | Does the behavior happen, and how well? | Scored artifact or observation |
| **Awareness** | Does the learner accurately know whether they did it? | Self-assessment compared to observed score |
| **Consistency under load** | Does it hold on hard calls, under time pressure, without a script? | 3+ samples, including at least one hard one |

### Generic level descriptors (adapt per skill)

| Level | Performance | Awareness | Consistency under load |
|---|---|---|---|
| **1. Unconscious Incompetence** | Behavior absent or wrong | Does not see the gap. Self-rates high or says "I already do that" | N/A |
| **2. Conscious Incompetence** | Behavior absent, attempted, or partial | Sees the gap. Self-rates low or accurately. Can describe what good looks like but not produce it | N/A |
| **3. Conscious Competence** | Behavior present and correct when deliberate | Accurate. Can explain what they did and why | Holds on easy samples, slips on hard ones or under pressure |
| **4. Unconscious Competence** | Behavior present, adapted to context, fluent | Accurate, often under-describes how they do it ("I just do it") | Holds across all samples, including hard ones |

**Placement rule:** place on the lowest dimension that is not met. A rep who executes well on easy calls but collapses on a complex multi-threaded call is Level 3, not Level 4, regardless of the average score.

### Behavior scoring scale (per behavior, per sample)

| Score | Label | Descriptor |
|---|---|---|
| 0 | Absent | Behavior did not occur when the situation called for it |
| 1 | Attempted | Behavior occurred but was incomplete, mistimed, or abandoned |
| 2 | Executed | Behavior occurred correctly, followed the model |
| 3 | Adapted | Behavior occurred correctly and was adjusted to this buyer or situation |
| N/A | Not applicable | The situation never called for it. Do not score as 0 |

### Worked rubric A: Confirming the buying process before proposing (AE)

| Behavior | 0 Absent | 1 Attempted | 2 Executed | 3 Adapted |
|---|---|---|---|---|
| B1. Asks how a similar purchase was approved | Never asks | Asks "what's your process?" and accepts a vague answer | Asks about a specific past purchase and gets named steps | Probes the gaps ("who could stop it?") using what was said earlier on the call |
| B2. Identifies approvers by name or role | No approvers named | Names the champion only | Names economic buyer and at least one other approver | Maps approvers and their likely objections |
| B3. Confirms timeline against the process | No timeline | Accepts buyer's date without checking | Walks the date backward through the named steps | Surfaces a conflict and agrees a revised plan |
| B4. Proposes only after B1-B3 | Proposal sent first | Proposal sent with partial process known | Proposal sent after process confirmed | Proposal structured around the process |
| B5. Records process in CRM | Nothing recorded | Free-text note | Required fields complete | Fields complete and next step dated |

Level mapping for this rubric (rule of thumb, adjust once you have data):

| Pattern across 3+ calls | Level |
|---|---|
| Mostly 0s, self-rates "I always do this" | 1 |
| Mostly 0-1s, self-rates low, can name what is missing | 2 |
| Mostly 2s on standard calls, drops to 0-1 on complex or late-stage calls | 3 |
| 2-3s on every sampled call including the hardest one | 4 |

### Worked rubric B: Judging AI-generated output (any revenue role)

For AI-tool rollouts, the skill to assess is rarely "uses the tool." It is judging what the tool produces. This rubric scores a rep reviewing an AI call summary or AI-drafted email before it is sent or saved.

| Behavior | 0 Absent | 1 Attempted | 2 Executed | 3 Adapted |
|---|---|---|---|---|
| B1. Checks claims against source (call, CRM, buyer email) | Sends as-is | Skims, no correction | Catches and fixes factual errors | Catches subtle errors (wrong stakeholder, misattributed objection) |
| B2. Checks fit for this buyer and stage | Generic output sent | Edits tone only | Edits content to match buyer context | Rewrites the core point around a buyer-specific insight |
| B3. Decides whether to act at all | Acts on every suggestion | Occasionally skips | Skips low-value suggestions with a reason | Explains the decision to a peer or manager unprompted |
| B4. Gives the tool better input next time | Same prompt or settings every time | Changes input randomly | Adds missing context deliberately | Has a reusable input pattern others could copy |

**Test design for B1:** seed three practice outputs with one known error each (a wrong number, an invented commitment, a misnamed stakeholder). The score is how many the learner finds. This is a performance test, not a self-report, and it separates Level 1 from Level 2 quickly: Level 1 learners do not look for errors at all.

---

## 4. Step 3: Rater Calibration (Before Any Scoring)

Uncalibrated scoring produces numbers that measure the rater, not the rep.

**Calibration session (60-90 minutes, all raters together):**

| Minutes | Activity |
|---|---|
| 0-10 | Review the skill definition card and rubric line by line |
| 10-30 | Everyone scores Sample 1 independently. No discussion |
| 30-45 | Reveal scores. For every behavior where raters differ by 2+ points, each rater cites the moment that drove their score |
| 45-55 | Rewrite any descriptor that caused the disagreement |
| 55-80 | Score Samples 2 and 3 independently. Reveal and compare |
| 80-90 | Record agreement rate. Decide go or recalibrate |

**Pass threshold (rule of thumb):** raters land within one point of each other on at least 80 percent of behavior scores. If not, rewrite descriptors and run one more sample. For formal reliability, compute Cohen's kappa for two raters; for practical enablement work, percent agreement within one point is usually enough.

**If an AI tool will do the scoring:** treat the model as a rater. Score a set of calls by hand and by model and compare per behavior. The Revenue AI Report's call-scorecard playbook uses fifty calls and rewrites or drops any rubric line below 70 percent human-model agreement. Publish the agreement rate. A score nobody trusts poisons the whole program.

---

## 5. Step 4: The Learner Baseline Survey

10-15 minutes. Confidential to enablement (not shared with the learner's manager as individual raw answers). Say so in the invitation, and mean it. Individual placements are shared; raw self-ratings are not.

### Section A: Self-placement on the Four Levels (one item per skill)

Use plain language. Do not show the level names; they invite gaming.

> **A1. Which statement best describes you and [skill]? Pick one.**
> a) I'm not sure what this involves or why it would matter for my deals.
> b) I know this matters, and I know I'm not doing it as well as I could.
> c) I can do this when I focus on it, but it takes effort and I sometimes skip it.
> d) I do this without thinking about it, even on hard calls.

(a = Level 1, b = Level 2, c = Level 3, d = Level 4. Self-placement only. Never use it alone.)

### Section B: Behavioral frequency (one item per behavior on the skill card)

Frequency questions are harder to inflate than agreement questions, because they ask about events, not identity.

> **B1-Bn. In your last 10 [calls / deals / drafts], how many times did you [behavior]?**
> Scale: 0 / 1-2 / 3-5 / 6-8 / 9-10 / Not sure

"Not sure" is a useful answer. A high rate of "Not sure" on a skill is a Level 1 signal.

### Section C: Self-efficacy (confidence to perform)

Adapted from Bandura's approach to self-efficacy scales: ask about confidence to perform specific tasks, at graded difficulty, on a 0-10 scale.

> **C1. How confident are you that you could [behavior] on a standard first call?** 0 (cannot do) to 10 (certain)
> **C2. ...on a call with three stakeholders who disagree?** 0-10
> **C3. ...on a call where the buyer pushes for pricing in the first ten minutes?** 0-10

The drop from C1 to C3 is informative. A flat high score across difficulty is either Level 4 or overconfidence. Check against observed performance.

### Section D: Knowledge check (3-5 items, scored, not self-rated)

Scenario-based, one correct answer, plausible distractors. Example for rubric A:

> **D1. A champion says "we'll have budget approved by the end of the month." What is the best next question?**
> a) "Great, should I send the proposal now?"
> b) "Who signs off on budget, and when did they last approve something like this?" (correct)
> c) "What's your budget range?"
> d) "Can we get a meeting with procurement?"

### Section E: Relevance and motivation (Knowles: adults learn what they see as relevant to a real problem)

> **E1. How much would getting better at [skill] change your results this quarter?** 1 (not at all) to 5 (a lot)
> **E2. What gets in the way of doing [skill] more often?** (open text)
> **E3. If you could watch one person do this well, who would it be?** (open text)

E3 doubles as a peer-model nomination for the Observe step and the Teach step.

### Section F: AI-tool items (add for any AI rollout)

> **F1. In the last two weeks, how often did you use [tool] for real work?** Never / Once / Weekly / Several times a week / Daily
> **F2. When you use [tool], how often do you change its output before using it?** Never / Rarely / Sometimes / Usually / Always
> **F3. How much do you trust [tool]'s output on [task]?** 1 (not at all) to 5 (completely)
> **F4. What would make [tool] more useful for your job?** (open text)

**Read F2 and F3 together:** high trust plus "never change it" is the riskiest profile in an AI rollout. It indicates unexamined action, a Level 1 pattern on Rubric B.

Always compare F1 to the tool's usage logs. Self-reported usage of new tools tends to run higher than logged usage.

---

## 6. Step 5: The Manager Observation Checklist

10 minutes per rep. The manager completes it from recent direct observation, not memory of the rep in general. If the manager has not observed this skill in the last 30 days, they mark "No recent observation" and that rep gets an artifact sample instead.

```
MANAGER OBSERVATION CHECKLIST
Rep: ______  Skill: ______  Manager: ______  Date: ______
Evidence used (tick all): [ ] Live call  [ ] Recording  [ ] CRM record  [ ] Document  [ ] AI tool log
Date of most recent observation of this skill: ______   [ ] No recent observation

For each behavior on the skill card:
                                  Not seen  Seen once  Seen often  Seen always  Can't tell
B1 ____________________________     [ ]       [ ]        [ ]         [ ]          [ ]
B2 ____________________________     [ ]       [ ]        [ ]         [ ]          [ ]
B3 ____________________________     [ ]       [ ]        [ ]         [ ]          [ ]

Awareness signals (tick if observed):
[ ] Rep raised this skill as something to work on without prompting
[ ] Rep can accurately describe what went well/badly on a call for this skill
[ ] Rep dismisses feedback on this skill ("I already do that")
[ ] Rep asks to see examples of others doing it

Load signals:
[ ] Behavior holds on hard calls (multi-stakeholder, late stage, hostile buyer)
[ ] Behavior only appears when rep knows they are being observed
[ ] Behavior drops at end of quarter or under volume pressure

Manager's level estimate: [ ]1  [ ]2  [ ]3  [ ]4
One specific moment that supports the estimate (call, date, timestamp):
______________________________________________
```

**Decision rule:** a manager estimate without a cited moment is recorded but weighted as low confidence. "One specific moment" is the cheapest bias check available.

---

## 7. Step 6: Call and Artifact Scoring Method

### Sampling

| Rule | Why |
|---|---|
| Score 3 samples per learner minimum, 5 if the skill is high stakes | One sample cannot show consistency under load |
| Select samples by rule, not by preference (e.g., the last 3 first calls, or randomly from the last 30 days) | Managers pick favorites and recent memories |
| Include at least one hard sample (complex deal, late stage, multi-stakeholder) | Separates Level 3 from Level 4 |
| Use only samples where the situation called for the skill | Otherwise you score N/A as 0 and invent a gap |
| Use samples from before the program announcement | People change behavior when they know they are being assessed (observer effect) |

### Scoring procedure

1. Rater reads the skill card and rubric before every scoring session, not once.
2. Score each behavior independently, citing a timestamp or quote for every score of 0, 1, or 3.
3. Score blind to the rep's tenure, quota attainment, and self-assessment where possible.
4. For each learner, record per behavior: the median score across samples, and the lowest score on any hard sample.
5. Second-score 1 in 5 samples with a different rater. If agreement drifts below threshold, recalibrate.

### Aggregation into an observed level

| Median across samples | Lowest on hard sample | Observed performance level |
|---|---|---|
| 0-0.9 | any | 1 or 2 (use awareness to split) |
| 1.0-1.9 | any | 2 |
| 2.0+ | 0-1 | 3 |
| 2.0+ | 2-3 | 4 candidate (confirm with manager load signals) |

### AI-assisted scoring

If a call-review or conversation-intelligence tool scores calls, use it to widen coverage, not to replace the calibration step. The model applies a rubric consistently, including the parts of the rubric that are wrong. Validate the rubric with humans first, then let the model scale it.

---

## 8. Step 7: Triangulate and Place Each Learner at a Starting LOPAFT Step

### Triangulation table

| Self-report | Observed | Manager | Placement | Note |
|---|---|---|---|---|
| High | Low | Low | **Level 1** | Does not see the gap. Classic unconscious incompetence |
| Low | Low | Low | **Level 2** | Sees the gap. Ready to learn |
| Low | Medium | Medium | **Level 2-3** | Under-confident. Often responds well to Practice with Feedback |
| Medium | Medium, drops on hard samples | Medium | **Level 3** | Effortful, inconsistent under load |
| High | High, holds on hard samples | High | **Level 4** | Candidate peer model and teacher |
| Low | High | High | **Level 3-4, low self-efficacy** | Competent but doubts it. Ask them to Teach; it builds confidence |
| Any | No data | Any | **Unplaced** | Get an artifact sample before assigning a track |

### Placement into the starting LOPAFT step

This table extends the step-to-level mapping in `lopaft-framework`. The principle from the LOPAFT diagnostic applies: **start at the lowest step that is not yet in place.** A higher step cannot hold when the one under it is missing.

| Learner profile | Starting step | Why | First deliverable |
|---|---|---|---|
| Level 1 | **L, Learn** | The gap is not felt yet. Learn must surface it without shame and activate the WHY | Short session showing the cost of the gap in their own deals or data |
| Level 2, cannot describe what good looks like | **O, Observe** | They know they are missing something but have no reference point | Annotated good and bad examples (recordings, artifacts) |
| Level 2, can describe good but cannot produce it | **P, Practice** | They have the benchmark. They need safe reps | Role-play or sandbox reps with no customer on the line |
| Level 3, consistent in practice, not yet on live deals | **A, Apply** | Practice has not transferred to real work | A named set of live deals where the skill is used, with an owner |
| Level 3, used on live deals but inconsistent or drifting | **F, Feedback** | They are applying without knowing if they are moving toward good | Scored samples against the rubric, on a spaced schedule |
| Level 4 | **T, Teach** | Teaching deepens encoding and gives the cohort a model | Lead a peer session, contribute examples to the Observe library |

**Important:** the starting step is where the learner enters the cycle, not a step they skip forever. A Level 3 learner who starts at Feedback still benefits from an Observe library; they just do not need a Learn session first. LOPAFT is a spiral: once a learner reaches Level 4 on one skill, they re-enter at Learn on the next layer of complexity.

### Placement for an AI-tool rollout

| Profile (from survey F-items, logs, and Rubric B) | Starting step |
|---|---|
| Never logged in, does not see the need | L: show the specific task the tool removes from their week |
| Logged in once and abandoned | O: they did not know what good output or good use looks like |
| Occasional user, sends output unedited | O then P: show good vs. bad outputs, then run error-spotting drills |
| Regular user, edits output, inconsistent quality | F: score their reviewed outputs against Rubric B |
| Daily user with reusable input patterns | T: package their patterns for others |

---

## 9. Readiness Assessment for an AI-Tool Rollout

Learner readiness is one of four. A rollout fails if any of the four is not ready, and the fix for each is different. Score every item 0 (no), 1 (partial), 2 (yes).

### Dimension 1: Data readiness

| # | Item | 0 / 1 / 2 |
|---|---|---|
| D1 | The data the tool reads (calls, CRM, knowledge base) exists for most of the target workflow | |
| D2 | That data is accurate enough that a rep would trust a summary built from it | |
| D3 | Recording and data-use consent meets the rules in every region you sell into, with approved disclosure wording | |
| D4 | Access permissions are set so the tool sees what it needs and nothing it should not | |
| D5 | Source content (playbooks, battlecards, pricing) is current; stale content is archived before indexing | |

### Dimension 2: Workflow readiness

| # | Item | 0 / 1 / 2 |
|---|---|---|
| W1 | One named workflow is the target, not "use AI more" | |
| W2 | The exact point where the tool enters that workflow is documented | |
| W3 | Something is removed from the rep's work, not only added | |
| W4 | A written standard exists for what good tool output and good use look like | |
| W5 | Usage can be measured from a system you already have (logs, CRM fields) | |

### Dimension 3: Manager readiness

| # | Item | 0 / 1 / 2 |
|---|---|---|
| M1 | Managers use the tool themselves on real work | |
| M2 | Managers can tell good output from bad (test them with Rubric B) | |
| M3 | A coaching cadence exists that can absorb the new skill | |
| M4 | Managers can explain why the tool matters for the team's number | |
| M5 | Managers have agreed how tool data will and will not be used in coaching (see `enablement-coach`) | |

### Dimension 4: Learner readiness

| # | Item | 0 / 1 / 2 |
|---|---|---|
| L1 | Baseline survey complete, including F-items | |
| L2 | Prerequisite skills are at Level 3+ (the tool amplifies a skill; it does not supply one) | |
| L3 | Learners see relevance (Section E averages 3+ of 5) | |
| L4 | Learners have protected time for Practice before Apply | |
| L5 | Skeptics have been heard, and their objections are logged with a response | |

### Readiness decision rules

| Result | Decision |
|---|---|
| All four dimensions 7+ of 10 | Launch |
| Any dimension 4-6 | Launch only the parts that dimension does not block; fix it in parallel with a named owner and date |
| Any dimension 0-3 | Do not launch to the full cohort. Fix the lowest dimension first, or run a small pilot with learners who clear it |
| Data below 4 | Do not train people on a tool whose output they cannot trust. Training will be blamed for a data problem |
| Manager below 4 | Run `enablement-coach` before learner training. Learners will not keep a habit their manager does not reinforce |

This reflects the transfer-of-training model of Baldwin and Ford: whether training transfers to the job depends on learner characteristics, training design, and the work environment. Data, workflow, and manager readiness are the work environment.

---

## 10. Segmenting the Cohort

### Segment by level per skill, not by tenure or title

Tenure predicts level poorly for new skills, and especially for AI-tool skills, where newer reps sometimes lead. Segment on the placement from Section 8.

| Segment | Placement | Track | Group size (rule of thumb) |
|---|---|---|---|
| Unaware | Level 1 | Learn-first track: gap surfacing, WHY, cost of the gap | Any size; works in groups |
| Aware | Level 2 | Observe and Practice track: example library, safe reps | Small groups of 4-6 for practice |
| Effortful | Level 3 | Apply and Feedback track: live deals, scored samples, spaced review | Individual coaching with the manager |
| Fluent | Level 4 | Teach track: peer models, example contributors, practice partners | 1-2 per group of Level 2s |

### Mixed-level cohorts

Most cohorts are mixed, and splitting them fully is often impractical. Use the mix instead of fighting it.

| Situation | Rule |
|---|---|
| Mostly Level 2 with a few Level 4s | Run one track; assign Level 4s as Observe models and Practice partners |
| Bimodal (cluster at 1, cluster at 3) | Two tracks. One curriculum cannot serve both without overwhelming one group and boring the other |
| One or two far outliers below | Route to individual pre-work before joining the cohort |
| One or two far outliers above | Exempt from Learn, assign to Teach, and give them a harder skill in parallel |
| Wide spread with no clusters | Shared Learn and Observe; individual Practice targets; this is where Vygotsky's zone of proximal development matters: set each person's practice just beyond what they can do alone |

### Segment by attitude for AI rollouts (secondary axis)

| Attitude | Signal | Handling |
|---|---|---|
| Skeptic | Low F3 trust, low F1 usage, objections in E2 | Show proof on their own deals; recruit one skeptic to test and report honestly |
| Curious | Medium trust, occasional usage | Standard track |
| Over-truster | High F3 trust, F2 "never changes output" | Rubric B error-spotting drills first |
| Power user | Daily usage, reusable patterns | Teach track; harvest their prompts and patterns for the Observe library |

---

## 11. Handling Self-Assessment Bias

Self-assessment is necessary (it is the only window on awareness) and unreliable as a performance measure. Name the biases and design around them.

| Bias | What it looks like | Design fix |
|---|---|---|
| **Dunning-Kruger effect** (Kruger and Dunning): people with low skill in a domain tend to overestimate their performance, because the skill to perform and the skill to judge performance overlap | Level 1 reps self-rate high | Never place from self-report alone. Treat a high self-rating with low observed performance as a Level 1 signal, not noise |
| **Social desirability bias** | Everyone says they do the thing leadership talks about | Confidential surveys. Ask frequency ("in your last 10 calls") instead of agreement ("I am good at...") |
| **Reference-group effect** | Rep compares themselves to their team, not to the standard | Show the standard (an example) before asking for a rating |
| **Fear of consequences** | Under-reporting gaps when the survey feels like a performance review | State in writing that raw self-ratings are not shared with managers or used in performance decisions. Then honor it |
| **Response-shift bias** (Howard and colleagues) | After training, learners realize they overrated themselves at baseline, so pre/post self-ratings show little or negative change | Add a retrospective pre-rating at the end ("Knowing what you know now, how would you have rated yourself before?") and rely on observed scores for change |
| **Usage over-claiming** (AI tools) | Self-reported tool use exceeds logged use | Always use logs for usage; use the survey for why |

### The calibration gap

For each learner and skill, compute:

**Calibration gap = self-placement level minus observed level**

| Gap | Meaning | Action |
|---|---|---|
| +2 or more | Over-confident. Likely Level 1 on this skill | Start at Learn with their own recordings as evidence. Lead with curiosity, not correction |
| +1 | Mild over-estimate | Observe step: compare their sample to a strong example side by side |
| 0 | Accurate | Proceed with placement |
| -1 or less | Under-confident | Practice with fast feedback; Teach assignment early to build self-efficacy |

Track the calibration gap over time. Shrinking gaps are a leading indicator that Feedback is working, and `enablement-measure` uses self-assessment accuracy as a behavior-level signal.

---

## 12. Audit Mode Procedure

Use when a program already launched without a baseline.

1. Run the SKILL.md audit checklist and record the score.
2. Pull 3 artifacts per learner from **before** launch (recordings and CRM records persist). Score them with the rubric. This reconstructs a baseline.
3. Pull 3 artifacts per learner from the last 30 days. Score them.
4. Run the survey now, with a retrospective pre-rating item for each skill.
5. Compare the program's assumed entry level (from the design docs or the first session's content) to the reconstructed distribution.
6. Name the mismatch: program pitched too high (Level 1s overwhelmed), too low (Level 3s disengaged), or one-size for a bimodal cohort.
7. Re-segment and re-route. Do not restart the program for everyone.

---

## 13. Output Template: Baseline Report

```
BASELINE REPORT
Program:              [name]
Skill(s) assessed:    [list, with link to skill definition cards]
Cohort:               [n learners, roles, teams]
Assessment window:    [dates]
Methods used:         [survey / manager checklist / n artifacts per learner / AI-assisted scoring]
Rater calibration:    [agreement rate within one point; kappa if computed]

1. HEADLINE
   [One sentence: where the cohort is and what that means for the program.]

2. LEVEL DISTRIBUTION (per skill)
   Skill            L1    L2    L3    L4    Unplaced
   [skill A]        n     n     n     n     n
   [skill B]        n     n     n     n     n

3. PROGRAM FIT
   Assumed entry level:    [what the draft program assumes]
   Actual median level:    [observed]
   Mismatch:               [none / pitched too high / too low / bimodal]

4. STARTING LOPAFT STEP BY SEGMENT
   Segment        n    Starting step    First deliverable           Owner
   Unaware        n    L                [ ]                         [ ]
   Aware          n    O / P            [ ]                         [ ]
   Effortful      n    A / F            [ ]                         [ ]
   Fluent         n    T                [ ]                         [ ]

5. CALIBRATION GAP
   Mean gap:                       [+/- n]
   Learners with gap +2 or more:   [n]  (route to Learn with own evidence)
   Learners with gap -1 or less:   [n]  (route to early Teach)

6. AI-TOOL READINESS (if applicable)
   Data [x/10]   Workflow [x/10]   Manager [x/10]   Learner [x/10]
   Gating dimension:   [lowest]
   Decision:           [launch / partial launch / fix first]
   Fix owner and date: [ ]

7. PEER MODELS AND TEACHERS
   [Names of Level 4 learners and survey E3 nominations, with consent to be used as models]

8. RISKS AND OPEN QUESTIONS
   [Thin data, uncalibrated raters, missing manager observations, consent issues]

9. BASELINE METRICS HANDED TO enablement-measure
   [Per-skill observed scores, calibration gap, usage from logs, related business metric baseline]

10. RE-ASSESSMENT DATE
   [Mid-program re-assessment date and method]
```

---

## 14. Worked Example (Illustrative)

*All names and numbers below are invented for illustration.*

**Context:** A mid-market software company has 24 AEs across 4 managers. Leadership has bought an AI call-review tool and wants to use it to fix a known problem: deals stall after the proposal. Enablement is asked for "AI training."

**Step 1. Skill definition.** Enablement refuses to define the skill as "using the AI tool." The business problem points to Rubric A (confirming the buying process before proposing). The AI skill is Rubric B, reviewing the tool's call summaries before they go into the CRM.

**Step 2-3. Rubric and calibration.** Four managers and the enablement lead score three shared calls. First round: agreement within one point on 60 percent of behavior scores. The disagreement is on B2 ("approvers named"): two managers count the champion as an approver. The descriptor is rewritten to "names the economic buyer and at least one other approver." Second round: 85 percent. Pass.

**Step 4-6. Data collection.** Survey response rate is high after enablement states in writing that raw answers go to enablement only. Each AE gets 3 calls scored from the 30 days before the announcement, one of them a late-stage call.

**Step 7. Placement (Rubric A):**

| Level | n | Notes |
|---|---|---|
| 1 | 7 | Self-placed at c or d; observed medians below 1. Six of the seven have high tenure |
| 2 | 9 | Self-placed at b; can name the gap in E2 |
| 3 | 6 | Medians above 2 on early calls; dropped to 0-1 on late-stage calls |
| 4 | 2 | Held on every sample. Both nominated by peers in E3 |

**Readiness (AI tool):** Data 8, Workflow 5, Manager 4, Learner 7. Workflow is partial because nobody has defined what is removed from the AE's week. Manager is gating: two of four managers have never opened the tool, and when tested with seeded errors, managers caught fewer errors on average than the two Level 4 AEs.

**Decisions:**
1. Run `enablement-coach` with managers for two weeks before learner training. Managers are scored on Rubric B themselves.
2. RevOps removes the manual call-notes field once AI summaries are reviewed, so the tool subtracts work.
3. Level 1 AEs start at Learn: each sees two of their own lost deals where the proposal went out before the process was known. Shown privately, by enablement, not in a group.
4. Level 2 AEs start at Observe: an example library of six annotated clips, three good and three bad, including two from the Level 4 AEs (with consent).
5. Level 3 AEs start at Feedback: scored late-stage calls every two weeks.
6. The two Level 4 AEs join the Teach track and run practice pairs.
7. Re-assessment in week 6 with the same rubric and sampling rule.

**What the report headline said:** "The program as drafted assumed every AE was at Level 2. Seven are at Level 1 and do not see the gap; six already execute on early calls and fail only late. One curriculum would have lost both groups. Manager readiness, not learner readiness, is the gating risk for the AI tool."

---

## 15. Common Mistakes

| Mistake | Why it fails | Fix |
|---|---|---|
| Assessing "the person" instead of the skill | Levels are skill-specific. A Level 4 closer can be Level 1 on AI review | One placement per learner per skill |
| Using a satisfaction or confidence survey as the baseline | Measures feelings, not performance | Survey plus scored artifacts, always |
| Letting managers choose which calls to score | Selection bias toward best or most memorable | Rule-based sampling |
| Scoring without calibrating raters | Scores reflect the rater | Calibration session before any scoring |
| Treating N/A as 0 | Invents gaps where the situation never arose | Score N/A separately |
| Placing from one easy sample | Cannot see consistency under load | 3+ samples including one hard one |
| Sharing raw self-ratings with managers | Next survey is inflated | Share placements, protect raw answers |
| Assessing learners but not the environment | A ready learner in an unready workflow still fails | Run all four readiness dimensions for AI rollouts |
| Treating tenure as level | New skills reset the board | Segment on observed level |
| Baseline once, never again | Cannot route learners as they advance | Schedule a mid-program re-assessment |
| Announcing the assessment before pulling samples | Behavior changes when observed | Pull pre-announcement samples first |

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). LOPAFT framework by Jonathan Kvarfordt. Licensed CC BY 4.0.*
