---
name: diagnose-a-stalled-ai-rollout
description: "A named reason your team is not using the tool, tied to one rung of the adoption ladder, with the specific fix for that rung. Use when: Usage dropped after launch week and nobody can say why. A leader is about to fund another training event to fix an adoption problem. You need a defensible answer for the CRO or CEO on why the rollout is not working."
---

# Diagnose Why an AI Rollout Did Not Stick

> From the [Revenue AI Report skill library](https://www.therevenueaireport.com/skills). Level: Intermediate · Task: Coach Teams · Setup: About 45 minutes · For: Enablement, Sales Leader, Revenue Operations, Executive and Founder

**Outcome:** A named reason your team is not using the tool, tied to one rung of the adoption ladder, with the specific fix for that rung.

## When to use
- Usage dropped after launch week and nobody can say why.
- A leader is about to fund another training event to fix an adoption problem.
- You need a defensible answer for the CRO or CEO on why the rollout is not working.

## Inputs you need
- What was rolled out, to whom, and on what date
- What training, examples, and practice time people actually received
- Current usage numbers, even rough ones
- Two or three quotes from people who stopped using it

## Quick prompt
Paste into any AI assistant. Replace the [bracketed] parts.

```text
You are an enablement diagnostician. Using the rollout details I paste below, work through six adoption rungs in order: Learn, Observe, Practice, Apply, Feedback, Teach. For each rung, state whether the deliverable existed, cite the evidence I gave you, and mark it pass, partial, or missing. Then name the single lowest failing rung as the root cause, explain why the rungs above it cannot be fixed first, and give me a two-week fix for that rung with an owner and a measurable check. Separate what my evidence shows from what you are inferring.

Rollout details:
[paste]
```

## Process
1. Collect the inputs above. Thin input produces a confident, wrong answer.
2. Learn: Someone explains it. First exposure to the content. Training deck, SOP, or launch email.
3. Observe: Watch what good looks like and what bad looks like. Without both, a person cannot tell where they stand. Examples library, recorded calls, pass and fail samples.
4. Practice: A safe place to try, fail, and try again. No stakes, no judgment, no live customer. Sandbox, role play, dry runs.
5. Apply: Real work, real deals, real risk. The first live rep.
6. Feedback: An honest read on the work, measured against a standard. Not how did it go. A measurement.
7. Teach: Teach it to someone else. This is the rung that locks it in. If a person can teach it, they understand it.
8. Write the verdict and the next action with an owner and a date.
9. Have one person who did the work review the output before you share it.

## Decision rules
- Fix the lowest failing rung first. A higher rung cannot hold when the one under it is missing.
- Practice means reps with no customer on the line. A live deal is not practice.
- Feedback means measurement against a written standard, not a check-in conversation.
- If people cannot teach it to a new hire, treat the skill as fragile even when usage looks fine.

## Output
- A six-row card: rung, evidence, pass or partial or missing.
- One named root-cause rung with the reasoning.
- A two-week fix with an owner, a deliverable, and a measurable check.

## Quality checks
- Every rung verdict cites evidence you supplied, not general advice.
- The fix targets one rung, not all six.
- The measurable check can be read from a system you already have.

## Limitations
- The ladder explains adoption, not whether the tool is any good. A bad tool fails every rung.
- Usage data without quotes tends to produce a confident but shallow read.

## Worked example
**Input:** Rolled out an AI call-summary tool to 40 reps on July 8 with one 60-minute session. No sandbox. No example library. Usage fell from 62 percent in week one to 11 percent by week five. Two reps said they did not know what a good summary looked like.

**Output:** Root cause: Observe. Nobody saw a good and a bad summary, so Practice and Feedback had no standard to work against. Fix: publish six annotated examples, three pass and three fail, and score ten summaries per manager against them for two weeks.

## Review checklist
- [ ] Did a manager who ran the rollout agree with the rung verdicts?
- [ ] Is the fix small enough to finish in two weeks?
- [ ] Is there a date to re-check usage?

## Toolkit
Load `references/TOOLKIT.md` for the tool-versus-adoption check, a rung-by-rung interview bank with quote coding, scoring descriptors for each rung, and a two-week fix library with measurable checks.

## Go deeper
- Full skill page: https://www.therevenueaireport.com/skills/diagnose-a-stalled-ai-rollout
- Related article: [enablement-in-the-age-of-agents](https://www.therevenueaireport.com/blog/enablement-in-the-age-of-agents)
- Research: [adoption-curve](https://www.therevenueaireport.com/research/adoption-curve)
- Research: [what-works](https://www.therevenueaireport.com/research/what-works)
- Playbooks that roll this out:
  - [Make conversation data do work (L3)](https://www.therevenueaireport.com/playbooks/conversation-data-to-work-l3) (L3 Integrated)
  - [Turn dormant seats into one shipped workflow (L2)](https://www.therevenueaireport.com/playbooks/dormant-seats-workflow-l2) (L2 Assisted)
  - [The 30-day first workflow (L2)](https://www.therevenueaireport.com/playbooks/first-workflow-30-day-l2) (L2 Assisted)

---

*Version 1.0.0 · Last reviewed 2026-09-04 · Source: [The Revenue AI Report](https://www.therevenueaireport.com) · License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
