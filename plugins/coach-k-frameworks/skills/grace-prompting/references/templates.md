# GRACE, SCRIBE and MIC Templates

> Templates for **GRACE by Jonathan Kvarfordt (Coach K)** and his companion methods. Copy, replace the `[bracketed]` parts, delete any line that does not apply. Back to [SKILL.md](../SKILL.md).

---

## 1. GRACE master template

```text
# [Prompt name]

## Goal / Role
You are [specific role with relevant experience, e.g. "a senior customer success manager for mid-market B2B software"].
Your goal is to produce [the output] so that [the business purpose, e.g. "the account team can walk into the renewal call with one clear recommendation"].

## Rules
- You MUST [the most important constraint].
- NEVER invent facts, names, numbers, or quotes. If something is not in the context, write "unknown" or ask.
- If [critical input] is missing, ask me for it before you start.
- Length: [e.g. "under 300 words" or "one page"].
- Tone: [e.g. "plain, direct, no hype"].
- [Optional: what to avoid, e.g. "no generic openers like 'I hope this finds you well'"].

## Advanced context
### Situation
[What is happening and why this output is needed now.]
### Audience
[Who reads the output, what they care about, what they already know.]
### Source material
[Paste the real notes, data, transcript excerpts, definitions.]
### What good looks like
[One or two lines on the standard, or what failed last time.]

## Clear instructions
1. [First step, e.g. "Read the source material and list the three facts that matter most."]
2. [Second step.]
3. [Third step.]
4. Check your draft against the Rules before you answer.

## Examples
### Output skeleton
[Section heading]: [what goes in it]
[Section heading]: [what goes in it]
[Section heading]: [what goes in it]

### Bad example (do not do this)
[One short example of the predictable failure, labelled as bad.]
```

---

## 2. GRACE quick card (one screen)

```text
GOAL/ROLE: You are [role]. Produce [output] so that [purpose].
RULES: MUST [x]. NEVER invent facts or numbers. If [input] is missing, ask. Max [length].
CONTEXT: [paste material under labels]
INSTRUCTIONS: 1. [ ] 2. [ ] 3. [ ]
EXAMPLES: Output skeleton: [heading] / [heading] / [heading]
```

---

## 3. SCRIBE conversational template

Use for strategy, messaging, brainstorming, or any draft you plan to iterate on.

```text
Let's think through something together.

Who you are: [role and perspective].
The situation: [what is going on, in plain conversational language].
What a great outcome would look like: [the result, not the format].

Phase 1, brainstorm: Give me [10] distinct options. Do not filter or rank yet. Make at least [3] of them unconventional.

[Wait for output.]

Phase 2, self-critique: Stop playing nice. For each option, tell me where it fails: the assumption most likely to be wrong, the objection a skeptical [buyer / CFO / rep] would raise, and what it would cost to test.

[Wait for output.]

Phase 3, refine: Keep the [2] strongest. Fix the weaknesses you named. Give me one recommendation and the first step to test it this week.
```

---

## 4. MIC beginner template

```text
MISSION: [What I want, in one sentence.]
INSTRUCTIONS: [How to do it: length, tone, format, anything to avoid.]
CONTEXT: [What it needs to know: who, what, when, why.]
```

---

## 5. Skeleton of Thought blocks

Drop one of these into the Examples part of any GRACE prompt.

**Account brief**
```text
## Company in one line
## What changed recently (each item: fact, source)
## Likely top three priorities (each: evidence, confidence high/medium/low)
## Who matters (role, why, what they care about)
## Our angle (one sentence)
## Questions we still cannot answer
```

**Call follow-up email**
```text
Subject: [their priority, under 8 words]
Line 1: Their priority, in their words.
Line 2: The one thing we discussed that addresses it.
Line 3: One proof point.
Line 4: One next step with a proposed date.
```

**Coaching plan**
```text
## The one skill to build (and the evidence it is the right one)
## What good looks like (observable behavior)
## Practice plan (weekly, with a safe place to fail)
## How we both know it worked (metric, date)
```

**QBR outline**
```text
## Results against the goals they set
## What did not work, and why
## What we learned about their business
## Next quarter: three priorities, owners, dates
## The ask
```

---

## 6. Rule of 90 edit log

Run after every test of a new prompt. Each edit you make should become a prompt change so you never make it twice.

| Edit I made to the output | Why | Prompt change | Part (G/R/A/C/E) |
|---|---|---|---|
| Removed an invented customer count | Not in source | Added "NEVER invent numbers" | R |
| Rewrote the opener | Generic | Added a bad-example opener | E |
| Added the renewal date | Missing context | Pasted contract summary | A |

---

*GRACE, SCRIBE, MIC, and Skeleton of Thought by Jonathan Kvarfordt (Coach K). Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*
