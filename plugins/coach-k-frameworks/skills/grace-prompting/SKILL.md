---
name: grace-prompting
description: >
  Build, fix, and QA prompts with GRACE by Jonathan Kvarfordt (Coach K): Goal/Role, Rules,
  Advanced context, Clear instructions, Examples. Includes his companion methods: SCRIBE for
  conversational and brainstorm prompts with a self-critique pass, MIC (Mission, Instructions,
  Context) for beginners, the Three Keys of prompting, Skeleton of Thought, and the Rule of 90.
  Use when someone says "write me a prompt", "fix this prompt", "my AI output is generic",
  "the AI keeps getting it wrong", "make this repeatable", "turn this into a team prompt",
  "prompt template", "GRACE prompt", "SCRIBE", "MIC prompt", "skeleton of thought", "rule of 90",
  or wants a revenue prompt (account research, call prep, follow-up email, battlecard, QBR, coaching
  plan) that produces the same quality output every time. Picks the right framework, builds the
  prompt, runs a QA checklist, and shows before/after.
---

# GRACE Prompting

> **GRACE by Jonathan Kvarfordt (Coach K)**, with his companion methods SCRIBE, MIC, the Three Keys, Skeleton of Thought, and the Rule of 90. Published in the [Revenue AI Report open skill library](https://www.therevenueaireport.com/skills).

**Outcome:** A prompt that produces the output you meant, in the format you need, every time you run it. Plus a clear read on which framework fits the job.

**The core idea:** most weak AI output is a context problem, not a model problem. People talk to AI as if it should read their minds. A world-class expert handed "make me an onboarding plan" with no context produces something mediocre. Not because they lack skill, but because they lack the brief. GRACE is the brief.

---

## Pick the framework first

| Situation | Use | Why |
|---|---|---|
| You need the **same output, same format, every run** (team prompt, template, recurring report, prompt library entry) | **GRACE** | Five parts lock role, constraints, context, steps, and format so output is repeatable. |
| You are **thinking with the AI**: brainstorming, strategy, a draft you will iterate on | **SCRIBE** | Conversational structure with an open brainstorm phase and a self-critique phase. |
| You or your team are **new to prompting**, or the task is small | **MIC** | Three parts. Fast to teach, hard to get wrong. |
| Output is **long or structured** (plan, brief, deck outline, report) | Add **Skeleton of Thought** to any of the above | Give the outline, not a finished example. |
| Output came back **close but not right** | **Rule of 90** | Edit the last 10 percent yourself, then fix the prompt, not the model. |

Rule of thumb: if more than one person will run it, or you will run it more than three times, build it in GRACE.

---

## GRACE: the five parts

| Letter | Part | What goes in it | Weak version | Strong version |
|---|---|---|---|---|
| **G** | Goal / Role | Who the AI is, and what the output is for | "Help me with an email." | "You are a senior enterprise AE. Goal: a follow-up email that earns a second meeting with a CFO." |
| **R** | Rules | Hard constraints. Must, never, length, tone, what to do when information is missing | (none) | "Never invent numbers. Under 120 words. If the budget is unknown, ask one question instead of guessing." |
| **A** | Advanced context | Everything an expert would need: audience, situation, data, history, what good looks like, what failed before | "It's for a prospect." | Call notes, the buyer's stated priority, the product's two relevant capabilities, the objection raised. |
| **C** | Clear instructions | Numbered steps in the order the work should happen | "Write it." | "1. Restate the buyer's priority in their words. 2. Tie one capability to it. 3. Propose one next step with a date." |
| **E** | Examples | The output format and, where useful, a good and a bad example | (none) | An outline of the email, plus one example of a generic opener to avoid. |

### Writing each part well

- **Goal / Role.** "You are" beats "act as". One frames identity and experience; the other frames a performance. State the business purpose of the output, not just the task.
- **Rules.** Words have power: "rule" and "law" do not read the same. Use firm verbs (MUST, NEVER) for the few constraints that truly matter, so they stand out. Always include a missing-information rule ("if X is missing, ask; do not guess").
- **Advanced context.** This is where most quality lives. Structured context beats a pile of text: label it with headings. Paste the real material (notes, data, definitions) instead of describing it.
- **Clear instructions.** Steps, not paragraphs. If order matters, number it. If the AI should ask questions first, say so as step 1.
- **Examples.** Give theory and an example. Humans learn from both; so does the model. Show a good example and, when the failure mode is predictable, a bad one labelled as bad.

---

## The companion methods

### The Three Keys of prompting

| Key | What it means | Apply it |
|---|---|---|
| 1. Structure and format | Markdown headings, hierarchy, labelled sections | Treat each prompt like a short book: title, table of contents, chapters. |
| 2. Words have power | Word choice changes behavior | "You are" vs "act as". "Rule" vs "law". "Must" vs "try to". |
| 3. Examples | Theory plus worked examples, good and bad | Show the output shape. Label the bad example as bad. |

### Skeleton of Thought

Give the AI the **outline** of the output, not a finished sample to copy. A full example invites cloning; a skeleton invites thinking.

> "I give it the skeleton, it fills in the muscles." (Jonathan Kvarfordt)

| Instead of | Give |
|---|---|
| A complete past account plan to imitate | `## Situation` / `## Three priorities (each: evidence, owner, date)` / `## Risks` / `## Next 30 days` |
| A finished email to rewrite | `Line 1: their priority in their words. Line 2: one proof point. Line 3: one ask with a date.` |

### SCRIBE (conversational prompts)

Use SCRIBE when the goal is better thinking, not a fixed format. Its defining moves, in order:

| Phase | What you do |
|---|---|
| Set the scene | Role, situation, and what a great outcome would be. Conversational, not a spec. |
| Brainstorm openly | Ask for many options with no filtering. Quantity first. |
| Self-critique | Turn the model on its own work: "Stop playing nice. Tell me where this fails." |
| Refine | Keep the survivors, fix the named weaknesses, converge on one. |

The self-critique phase is the point. Models default to agreeing with you; SCRIBE builds the disagreement in.

### MIC (beginner prompts)

| Part | Question | Example |
|---|---|---|
| **M**ission | What do I want? | "Write three subject lines for a renewal reminder." |
| **I**nstructions | How should it be done? | "Under 8 words each. No urgency gimmicks." |
| **C**ontext | What does it need to know? | "Customer has used the product 11 months; usage is up; renewal in 30 days." |

MIC is the on-ramp. When a MIC prompt keeps needing fixes, upgrade it to GRACE.

### The Rule of 90

Two halves, both by Jonathan Kvarfordt:

1. **Any AI output is about 90 percent there. The last 10 percent is you.** Blank page, edit page, final page. Do not skip the edit page.
2. **If it is not working, about 90 percent of the time the problem is the prompt, not the tool.** Before blaming the model, check what context you failed to give.

"AI is the best self-reflection exercise I've ever had." (Jonathan Kvarfordt)

---

## Builder process

1. **Classify the job.** Repeatable output (GRACE), thinking partner (SCRIBE), quick or beginner (MIC).
2. **Write the Goal first.** One line: who the AI is and what the output is for in business terms.
3. **List the Rules.** Three to seven. Must include a missing-information rule and a no-invention rule for any facts or numbers.
4. **Load the Advanced context.** Paste real material under labelled headings. Ask: what would a new expert hire need to know to do this well?
5. **Write Clear instructions** as numbered steps in working order.
6. **Add Examples** as a skeleton of the output. Add a labelled bad example if there is a known failure mode.
7. **Run it three times** on real inputs. Grade with the QA checklist below.
8. **Apply the Rule of 90.** Edit the output's last 10 percent. Then move every edit you made back into the prompt as a rule, context, or example so you do not make it twice.
9. **Version and store it.** Name, owner, date, last-tested model.

Templates for all three frameworks: [references/templates.md](references/templates.md).
Worked before/after rebuilds for revenue tasks: [references/examples.md](references/examples.md).

---

## Prompt QA checklist

Score each line Yes / No. Rule of thumb: ship at 10 or more Yes; rebuild under 8.

| # | Check |
|---|---|
| 1 | The role is specific ("senior CS manager for mid-market SaaS"), not generic ("helpful assistant"). |
| 2 | The goal states the business purpose of the output. |
| 3 | There is an explicit rule for missing information (ask, or mark as unknown). |
| 4 | There is an explicit no-invention rule for facts, names, and numbers. |
| 5 | Length and format are stated. |
| 6 | Context is pasted, not described ("here are the notes" beats "use the notes"). |
| 7 | Context is labelled with headings. |
| 8 | Instructions are numbered and in working order. |
| 9 | The output has a skeleton or format example. |
| 10 | Firm words (MUST, NEVER) are reserved for the few rules that matter. |
| 11 | Three test runs on real inputs produce output of the same shape and quality. |
| 12 | Every edit from the Rule of 90 pass has been folded back into the prompt. |

## Decision rules

- If two runs on the same input differ in structure, the prompt lacks a skeleton. Add one.
- If the output invents facts, the Rules lack a no-invention line or the Context lacks the facts. Fix both.
- If the output is generic, the Advanced context is thin. Add the material an expert would ask for.
- If the output ignores a rule, move that rule higher, make it firmer, and cut weaker rules competing for attention.
- If you edit more than about 10 percent of every output, the prompt is not done.

## Common mistakes

| Mistake | Fix |
|---|---|
| Prompting like a search query | Write a brief. Full sentences, real context. |
| A finished example the AI copies word for word | Replace with a skeleton. |
| Twenty rules all in capitals | Keep three to seven; capitalize only the critical ones. |
| Shipping the first output | Apply the Rule of 90. Edit, then fold the edit back in. |
| Using GRACE for open brainstorming | Use SCRIBE. GRACE converges; brainstorming should diverge first. |

## Related

- GRACE-based prompts in the [Revenue AI Report prompt library](https://www.therevenueaireport.com/prompts/competitive-research-battlecard-creation)
- [backwards-diagnostic](../backwards-diagnostic/SKILL.md) to decide which revenue problem a prompt should serve
- [find-move-close](../find-move-close/SKILL.md) to find the steps worth prompting

---

*GRACE, SCRIBE, MIC, the Three Keys of prompting, Skeleton of Thought, and the Rule of 90 by Jonathan Kvarfordt (Coach K). Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next framework before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
