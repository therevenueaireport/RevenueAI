---
name: backwards-diagnostic
description: >
  Diagnose any revenue problem from the outcome backwards with the Backwards Diagnostic by
  Jonathan Kvarfordt (Coach K): outcome, then the few metrics that drive it, then the one lever
  that is realistically movable, then where the gap is, then whether the gap is skills, fit, value,
  or process. Only then decide whether AI, training, or a process fix is the instrument. Use when
  someone says "we need to hit a bigger number", "why is win rate down", "ramp takes too long",
  "NRR is slipping", "what should we fix first", "where should AI go", "what AI tool should I buy",
  "diagnose our funnel", "root cause", "pick one priority", or brings a goal and a pile of possible
  fixes. Produces a one-page diagnosis with the lever, the gap, its category, the fix, and the
  metric that will prove it. Works for sales, marketing, CS, enablement, and RevOps.
---

# Backwards Diagnostic

> **The Backwards Diagnostic by Jonathan Kvarfordt (Coach K).** Published in the [Revenue AI Report open skill library](https://www.therevenueaireport.com/skills).

**Outcome:** One page that names the business outcome, the lever you will move, the gap holding it back, the category of that gap, and the fix. Written before anyone buys a tool.

**The core idea:** start with the end in mind and work backwards. Most teams start with the tool, or with a long list of problems. The diagnostic forces one outcome, one lever, one gap. "The metrics point the direction." (Jonathan Kvarfordt)

---

## The ladder

| Step | Question | Output | Stop if |
|---|---|---|---|
| 1. Outcome | What business result, by how much, by when? | One number with a date | Nobody can state it as a number |
| 2. Drivers | Which few metrics produce that result? | Two to four driver metrics with current values | You cannot get current values |
| 3. Lever | Of those, which one is realistic to move this period? | One chosen lever with target | The team picks more than one |
| 4. Gap | Where exactly does that lever break down? | The stage, segment, or step where performance drops | The gap is a feeling, not a data point |
| 5. Category | Is the gap skills, fit, value, or process? | One primary category, with evidence | |
| 6. Fix | What instrument fits that category? | The fix, its owner, the metric that proves it | |

### Step 2: standard driver trees

| Outcome | Drivers |
|---|---|
| New revenue | Number of qualified opportunities, average deal size, win rate, sales cycle length (sales velocity = opportunities x deal size x win rate / cycle length) |
| Net revenue retention | Gross retention (churn and contraction), expansion rate, expansion deal size |
| Rep productivity | Ramp time, quota attainment distribution, selling time share |
| Pipeline | Target account coverage, conversion by stage, source mix |
| Cost to serve | Volume per customer, time per interaction, share handled without a human |

### Step 3: choosing the lever

Score each driver. Pick the highest total. Rule of thumb: if two tie, pick the one with the shorter feedback loop.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Distance from benchmark or own best period | At or above | Some gap | Large gap |
| Controllable by this team this period | No | Partly | Yes |
| Speed to see movement | More than two quarters | One to two quarters | Within a quarter |
| Effect on the outcome if it moves | Small | Medium | Large |

### Step 5: the four gap categories

| Category | It looks like | Evidence to check | Typical instrument |
|---|---|---|---|
| **Skills** | People know what to do but cannot do it well | Call reviews, win/loss by rep, spread between top and bottom performers | Coaching, practice, enablement (see LOPAFT) |
| **Fit** | Effort goes to the wrong accounts, buyers, or segments | Win rate and cycle by segment, ICP match of lost deals | ICP, targeting, routing, territory |
| **Value** | Buyers do not see or believe the value | Loss reasons citing price or "no decision", discount depth, weak business cases | Messaging, business case, pricing, proof |
| **Process** | Work stalls between steps, data is missing, handoffs drop | Stage aging, rework, admin time, missing CRM fields | Process redesign, then automation and AI |

**AI belongs mainly in Process, and as a support to the others.** A skills gap does not get fixed by a systems purchase. A fit gap gets worse when you automate outreach to the wrong list.

---

## Process

1. **Write the outcome as a number and a date.** "Grow new ARR from $10M to $14M this fiscal year", not "grow faster".
2. **Pull current values** for each driver. Last four quarters if possible.
3. **Score the drivers** with the lever table. Pick one. Force the choice.
4. **Locate the gap.** Cut the chosen lever by stage, segment, rep, source, or product until the drop shows up in one place.
5. **Classify the gap.** Pick one primary category and write the evidence in one line. Name a secondary only if the evidence is strong.
6. **Choose the instrument** that fits the category. Only now ask where AI helps, and at what level: Optimize, Amplify, or Reinvent ([OAR](https://www.therevenueaireport.com/frameworks/oar)).
7. **Set the proof metric.** The lever itself, measured against the baseline from step 2, on a fixed date.

Worksheet: [references/worksheet.md](references/worksheet.md). Worked examples for win rate, ramp time, and NRR: [references/worked-examples.md](references/worked-examples.md).

---

## Quick prompt

```text
You are a revenue operations analyst who diagnoses from the outcome backwards. Use the Backwards Diagnostic by Jonathan Kvarfordt (Coach K).

Outcome: [number and date]
Current driver metrics (last 4 quarters if available): [paste]
Context: [team size, segments, recent changes]

Steps:
1. Restate the outcome as one number and date. If it is not a number, stop and ask me.
2. List the 2 to 4 drivers and their current values. Mark any value I did not give you as "missing". Do not estimate it.
3. Score each driver on: gap size, controllability, speed, effect (0 to 2 each). Pick one lever.
4. Tell me how to cut that lever to find the gap (by stage, segment, rep, source). If I gave you the cuts, find the gap.
5. Classify the gap as skills, fit, value, or process, with one line of evidence. Say what evidence would change your mind.
6. Recommend the instrument. Only mention AI if the category supports it, and name the OAR level.
7. Name the proof metric, its baseline, and the review date.

Output: one page with headings Outcome, Lever, Gap, Category, Fix, Proof.
```

## Decision rules

- **No number, no diagnosis.** If the outcome is not a number with a date, stop at step 1.
- **One lever.** Three focus areas at most across the whole team; one lever per diagnosis. Boil the ocean and it fails.
- **Data before category.** A category without evidence is an opinion. Go back to step 4.
- **Fix the category, not the symptom.** A process tool for a skills gap, or training for a fit gap, burns the quarter.
- **Never automate a broken process.** If the gap is Process, redesign first. AI scales whatever system you have, good or bad.
- **Surface metric vs real outcome.** "We need more pipeline" is usually a driver, not the outcome. Ask what the pipeline is for.

## Quality checks

- Outcome has a number, a baseline, and a date.
- Every driver has a current value or is marked missing.
- Exactly one lever was chosen, with scores shown.
- The gap is located in a specific stage, segment, or step.
- The category has one line of evidence.
- The fix matches the category.
- The proof metric is the lever itself, with a review date.

## Common mistakes

| Mistake | Fix |
|---|---|
| Starting with "what AI should we buy?" | Right question, wrong time. Run the ladder first. |
| Picking every lever | Force one. Park the rest. |
| Calling everything a skills gap | Check fit and value first. Good reps lose bad-fit deals. |
| Measuring the fix by activity (logins, emails sent) | Measure the lever. |

## Related

- [find-move-close](../find-move-close/SKILL.md) to map the process once the gap is in Process
- [ai-tool-five-tests](../ai-tool-five-tests/SKILL.md) before buying anything to close the gap
- [scale-ai-transformation](../scale-ai-transformation/SKILL.md): the diagnostic is the engine of SCALE's first two steps
- [Measure AI ROI](../../../revenue-ai-report-skills/skills/measure-ai-roi/SKILL.md) to trace the result after the fix

---

*The Backwards Diagnostic by Jonathan Kvarfordt (Coach K). Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next framework before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
