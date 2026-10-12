---
name: scale-ai-transformation
description: >
  Run an AI transformation with SCALE by Jonathan Kvarfordt (Coach K): Set strategic outcomes,
  Chart friction and foundation, Align capabilities and readiness, Launch with control, Evolve and
  expand. Outcome first, tool last; foundation before features; pilot before rollout. One
  deliverable and one gate per step. Use when someone says "AI strategy", "AI transformation",
  "AI roadmap", "where do we start with AI", "what AI should we buy", "our AI pilots go nowhere",
  "board wants an AI plan", "operationalize AI", "scale AI across the team", "SCALE framework",
  "AI operating plan", or has an AI budget with no measured result behind it. Produces an outcome
  charter, friction and foundation map, capability and readiness map, controlled pilot with kill
  criteria and graduation date, and a scaling blueprint with governance.
---

# SCALE AI Transformation

> **SCALE by Jonathan Kvarfordt (Coach K).** Published at [therevenueaireport.com/frameworks/scale](https://www.therevenueaireport.com/frameworks/scale) and in the [Revenue AI Report open skill library](https://www.therevenueaireport.com/skills).

**Outcome:** Five deliverables, in order, ending in a measured pilot and a scale or kill decision. Not a deck.

**The core idea:** most AI programs start at the wrong end. They start with the tech. SCALE starts with the business number the company already committed to, works backwards to where the work gets stuck, and only then picks a capability.

> "Coach, what AI should I buy? It's a great question. It's the wrong time to ask it." (Jonathan Kvarfordt)

**Throughlines:** outcome first, tool last. Foundation before features. Pilot before rollout. Kill criteria are a feature, not a failure. AI scales whatever system you have, good or bad.

---

## The five steps

| Step | Name | Question | Deliverable | Gate to pass |
|---|---|---|---|---|
| **S** | Set strategic outcomes | What is the number? | **Outcome charter** | Is there a specific delta with a date and an owner? |
| **C** | Chart friction and foundation | Where does work get stuck, and is the data ready? | **Friction and foundation map** | Is each bottleneck costed in time or money, and is the data foundation rated? |
| **A** | Align capabilities and readiness | What capability fits each friction point, and are we ready? | **Capability and readiness map**, plus a sourcing decision | Is the data ready for the capability picked, and is build, buy, or connect decided? |
| **L** | Launch with control | How do we test small? | **Controlled pilot** with success criteria, kill criteria, owners, graduation date | Are success metrics, kill criteria, and guardrails written and signed before day one? |
| **E** | Evolve and expand | Scale, kill, or govern? | **Scaling blueprint** and governance structure | Is the result measured against the pre-AI baseline, and is there a named governance owner? |

On the public site the steps are shortened to Strategic Outcomes, Chart Friction, Align Capabilities, Launch with Control, Evolve and Expand. Same method.

**Cadence:** one week per step is the published working default, so about five weeks to a controlled pilot. Larger organizations stretch Chart, because workflow mapping is the slowest step.

---

## S: Set strategic outcomes

Start with the end in mind. Name a business outcome with a hard number and a timeframe: reduce cost, grow revenue, decrease risk, or increase raving fans. Then name the two to four driver metrics (leading and lagging) that produce it.

| Do | Don't |
|---|---|
| "New ARR from $10M to $13M this fiscal year; win rate is the lever" | "Use AI to be more efficient" |
| One or two outcomes the business already committed to | A portfolio of disconnected use cases |
| Current value and target for each driver | Drivers with no baseline |

**Trap:** confusing a surface metric ("we need more pipeline") with the outcome under it. Engine for this step: [backwards-diagnostic](../backwards-diagnostic/SKILL.md).

## C: Chart friction and foundation

Map where the work actually gets stuck, on two layers.

| Layer | What to map | How |
|---|---|---|
| **Human friction** | Cognitive load, capacity, admin tax, handoffs, rework | Workflow map of the process behind the lever ([find-move-close](../find-move-close/SKILL.md)); five whys on each bottleneck |
| **Data foundation** | Where the data lives, who owns it, how it flows | Rate each source on completeness, accuracy, accessibility, timeliness |

Red flags: siloed data, manual entry, conflicting sources. Classify each gap before choosing any instrument: skills, systems, strategy, or product. A skills gap does not get fixed by a systems purchase.

This step feels like going backwards. It is the most important one. "AI only scales bad things" when the foundation is wrong.

## A: Align capabilities and readiness

Now, and only now, match AI capabilities to the specific friction points from C. Never the reverse.

| For each friction point | Decide |
|---|---|
| Capability that fits | What the AI must do (for example: summarize, draft, classify, predict, retrieve, take an action) |
| Readiness | Data, process, and people ready? If not, what has to happen first |
| OAR level | Optimize, Amplify, or Reinvent ([OAR](https://www.therevenueaireport.com/frameworks/oar)) |
| Sourcing | Build, buy, or connect, decided on core-focus cost, upkeep, and time to value |
| Shortlist | If buying, vendors scored on features, fit, security, and scale |

"Now anybody can build it. The question isn't can you. It's should you?" (Jonathan Kvarfordt)

## L: Launch with control

A pilot, not a rollout.

| Control | Rule of thumb |
|---|---|
| Team | One to three champions to start, one small team |
| Scope | One high-value use case, time-boxed |
| Success criteria | Three to five metrics, with baselines |
| Kill criteria | The explicit signal that ends or pivots the pilot |
| Guardrails | What the AI may and may not do, data it may touch, human review points |
| Owners | One accountable owner, one decider |
| Graduation date | Fixed at the start; scale or retire on that date |
| Feedback loop | Weekly check against criteria |

Killing a pilot is not "the idea was bad". It is a decision you made on purpose, in advance. Keep the learning; the initiative does not have to die with the pilot.

## E: Evolve and expand

Measure against the pre-AI baseline. Scale what worked, kill what did not. Expand from the champions outward, documenting what you did, why, and the outcome so the next team buys in. Stand up governance (a named owner or center of excellence) so successful pilots do not fragment into sprawl.

---

## Process

1. Run S and get the outcome charter signed by the business owner.
2. Run C with the people who do the work. Cost each bottleneck. Rate each data source.
3. Run A only against the top friction points. Decide sourcing and OAR level.
4. Run L with written controls signed before day one.
5. On the graduation date, run E: scale, fix, or kill, against the baseline.
6. Loop: the next outcome or the next friction point starts at S or C.

Deliverable templates for every step: [references/step-templates.md](references/step-templates.md).
Full worked example: [references/worked-example.md](references/worked-example.md).

---

## Quick prompt

```text
You are an AI transformation lead. Use SCALE by Jonathan Kvarfordt (Coach K): Set strategic outcomes, Chart friction and foundation, Align capabilities and readiness, Launch with control, Evolve and expand. Outcome first, tool last.

Business outcome we committed to: [number, date, owner]
Driver metrics and current values: [paste]
Process behind the lever, as it runs today: [paste]
Data sources and their state: [paste]
Tools under consideration (if any): [paste]

Steps:
1. S: Write the outcome charter. If the outcome is not a number with a date, stop and ask.
2. C: Map human friction and the data foundation. Rate each data source on completeness, accuracy, accessibility, timeliness. Classify each gap as skills, systems, strategy, or product. Do not invent costs; mark "to measure".
3. A: For the top 3 friction points only, match a capability, rate readiness, set an OAR level, and recommend build, buy, or connect. Ignore any tool I listed that does not match a friction point.
4. L: Design one pilot: team, scope, 3 to 5 success metrics with baselines, kill criteria, guardrails, owner, graduation date.
5. E: Write what evidence on the graduation date would mean scale, fix, or kill, and who owns governance.

Output: one section per step, each ending with its deliverable and its gate question answered yes or no.
```

## Decision rules

- **Always start at S. Never start at A.** A tool chosen before the outcome is a demo looking for a problem.
- **No gate, no next step.** Each deliverable is the entry ticket to the next.
- **Fix the foundation first.** If a data source fails on accuracy or accessibility, the capability that depends on it waits.
- **Three use cases max.** Each with a large benefit on the back end. Spread wider and it fails.
- **Top-down with champions.** Transformation comes from rethinking the process for the whole team, driven from the center, proven through a few champions.
- **The graduation date does not move.**

## Anti-patterns

| Anti-pattern | What it looks like | Fix |
|---|---|---|
| Starting with the tool | Licenses bought before an outcome was written | Back to S |
| Automating a broken process | Faster broken work | Back to C; redesign first |
| Pilot with no controls | A demo that cannot scale because nothing was baselined | Write L controls before day one |
| Adoption theater | Logins reported as transformation | Measure the outcome metric, not usage |
| Buying because a peer said so | No framework, wasted time and money | Run A against charted friction |
| No governance | Every team buys its own version of the same thing | Name a governance owner in E |
| Reinvent language, Optimize work | Board told "transformation" for a task speed-up | Label the OAR level honestly |

## Quality checks

- Outcome charter has a delta, a date, and an owner.
- Every bottleneck is costed or marked "to measure"; every data source is rated.
- Every capability maps to a charted friction point.
- Pilot controls signed before day one, including kill criteria and graduation date.
- Final decision compares against the pre-AI baseline.
- Governance owner named.

## Related

- [Turn an AI Ambition Into an Operating Plan](../../../revenue-ai-report-skills/skills/turn-ai-ambition-into-an-operating-plan/SKILL.md): the step-by-step operating-plan job built on SCALE
- [Set AI Pilot Kill Criteria](../../../revenue-ai-report-skills/skills/set-ai-pilot-kill-criteria/SKILL.md) for the L step
- [Review an AI Pilot](../../../revenue-ai-report-skills/skills/review-ai-pilot/SKILL.md) for the E step
- [Decide Whether to Build, Buy, or Connect](../../../revenue-ai-report-skills/skills/decide-build-buy-or-connect/SKILL.md) for the A step
- [ai-tool-five-tests](../ai-tool-five-tests/SKILL.md) to gate any tool on the A shortlist
- Framework pages: [SCALE](https://www.therevenueaireport.com/frameworks/scale) · [OAR](https://www.therevenueaireport.com/frameworks/oar)

---

*SCALE by Jonathan Kvarfordt (Coach K). Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next framework before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
