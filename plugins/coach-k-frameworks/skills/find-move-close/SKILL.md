---
name: find-move-close
description: >
  Map any revenue process into Find, Move, Close with the Find-Move-Close spine by Jonathan
  Kvarfordt (Coach K). Break each phase into a short task list, overlay People, Process, and
  Results on every task, then mark which steps can be AI-powered and at what OAR level
  (Optimize, Amplify, Reinvent). Use when someone says "map our sales process", "where can AI help
  in our funnel", "AI-power our process", "workflow map", "which steps should we automate",
  "process audit", "where does work get stuck", "map the customer journey", "map our renewal
  process", or needs a clear picture of a sales, marketing, CS, partner, or hiring process before
  choosing tools. Produces a one-page map with tasks, owners, results, friction, and an AI plan
  per step.
---

# Find, Move, Close

> **Find-Move-Close by Jonathan Kvarfordt (Coach K).** Published in the [Revenue AI Report open skill library](https://www.therevenueaireport.com/skills).

**Outcome:** One map of a process in three phases, every task tagged with who does it, how, and what result it produces, and a marked plan for where AI fits and how far.

**The core idea:** every revenue process has the same spine. You **find** the opportunity, you **move** it forward, you **close** it. Break each phase into a short task list, overlay People, Process, and Results, then ask of each step: where can I AI-power this?

---

## The spine applied to different processes

| Process | Find | Move | Close |
|---|---|---|---|
| New business sales | Identify and engage target accounts | Discovery, evaluation, business case | Proposal, negotiation, signature |
| Marketing | Find the audience and the signal | Nurture and educate | Convert to a sales conversation |
| Customer success | Find risk and expansion signals | Run the success or expansion play | Renew or expand |
| Partnerships | Find partners and shared customers | Build the joint plan | Close joint deals |
| Recruiting | Source candidates | Interview and assess | Offer and accept |

Rule of thumb: five to eight tasks per phase. Fewer and you have hidden steps. More and you are mapping clicks.

---

## The overlay: People, Process, Results

For every task, answer three questions.

| Lens | Question | Example (task: "Research the account") |
|---|---|---|
| **People** | Who does it today, and what skill does it take? | AE, 45 minutes, research skill varies widely |
| **Process** | How does it happen, with what tools and data, and where does it stall? | Manual web search plus CRM; no standard brief |
| **Results** | What output does it produce, and which metric does it move? | A brief; affects meeting conversion |

A task with no clear Result is a candidate to cut before anyone automates it.

---

## The AI marking

After the overlay, mark each task with one AI level. OAR by Jonathan Kvarfordt is published at [therevenueaireport.com/frameworks/oar](https://www.therevenueaireport.com/frameworks/oar).

| Mark | Meaning | Test |
|---|---|---|
| **H** (Human) | Keep human-led | The value is judgment, trust, or relationship. |
| **O** (Optimize) | AI improves this task inside the current process | Same steps, less time or better quality. |
| **A** (Amplify) | AI changes the workflow, ownership, or decision quality | The step works differently, not just faster. |
| **R** (Reinvent) | The step should not exist in its current form | Would you design it this way today? |
| **Fix first** | Process is broken; redesign before any AI | Rework, unclear owner, missing data. |

Two rules for marking:
- **Fix first beats every other mark.** If you speed up a broken process, you get more bad output faster.
- **Mark at most three tasks for action now.** The rest go on the backlog.

---

## Process

1. **Name the process and its outcome metric.** For example, "new business sales, measured by new ARR".
2. **Write the three phase definitions** for this process. One line each: where it starts and ends.
3. **List five to eight tasks per phase**, in order, as verbs ("Qualify the inbound lead", not "Lead qualification").
4. **Overlay People, Process, Results** on every task.
5. **Mark friction:** where work waits, gets redone, or drops between owners. Note the time or cost where you can.
6. **Mark each task** H, O, A, R, or Fix first.
7. **Pick up to three** tasks for action now, favoring high friction and a clear Result. Write the next step and owner for each.
8. **Check the map with the people who do the work.** The map is wrong until they agree with it.

Worksheet and a full worked example: [references/worksheet.md](references/worksheet.md).

---

## Quick prompt

```text
You are a revenue process designer. Use Find-Move-Close by Jonathan Kvarfordt (Coach K) to map this process.

Process and outcome metric: [e.g. mid-market new business, new ARR]
How it works today: [paste notes, stage definitions, or a description]
Team and tools: [roles, CRM, other tools]

Steps:
1. Define Find, Move, and Close for this process in one line each.
2. List 5 to 8 tasks per phase, as verbs, in order.
3. For every task give: People (who, skill needed), Process (how, tools, data, where it stalls), Results (output, metric it moves).
4. Mark friction points. Do not invent time or cost figures; mark them "to measure" if I did not give them.
5. Mark each task H (keep human), O (Optimize), A (Amplify), R (Reinvent), or Fix first. One line of reasoning each.
6. Recommend at most 3 tasks to act on now, with next step and owner.

Output: one table per phase (Task | People | Process | Results | Friction | Mark), then the top 3.
```

## Decision rules

- **No outcome metric, no map.** A map without a metric cannot tell you which step matters.
- **Verbs, not nouns.** Each task is something a person does.
- **Fix first before AI.** Any task with rework, an unclear owner, or missing data gets redesigned before it gets a tool.
- **Human where trust is the product.** Tasks whose value is judgment or relationship stay H, with AI preparing the human, not replacing them.
- **Three now, the rest later.** Spreading AI across every step at once is how pilots fail.

## Quality checks

- Each phase has a one-line start and end.
- Five to eight tasks per phase.
- Every task has People, Process, and Results filled in.
- Every friction point is located; numbers are measured or marked "to measure".
- Every task carries one mark with a reason.
- No more than three tasks selected for action now.
- Reviewed with the people who do the work.

## Related

- [backwards-diagnostic](../backwards-diagnostic/SKILL.md) to choose which process to map
- [scale-ai-transformation](../scale-ai-transformation/SKILL.md): this map is the friction map in SCALE's Chart step
- [ai-tool-five-tests](../ai-tool-five-tests/SKILL.md) before buying a tool for a marked step
- [grace-prompting](../grace-prompting/SKILL.md) to build prompts for O-marked steps

---

*Find-Move-Close by Jonathan Kvarfordt (Coach K). Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next framework before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
