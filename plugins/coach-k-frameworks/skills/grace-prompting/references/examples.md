# GRACE Worked Examples: Before and After

> Revenue prompts rebuilt with **GRACE by Jonathan Kvarfordt (Coach K)** and his companion methods. All companies and people are fictional. Back to [SKILL.md](../SKILL.md).

Each example shows the weak prompt, what was wrong, the rebuilt prompt, and what changed in the output.

---

## Example 1: Account research brief (GRACE + Skeleton of Thought)

### Before
```text
Research Acme Logistics for me.
```

### Diagnosis
| Part | Problem |
|---|---|
| Goal / Role | No role, no purpose. Research for what? |
| Rules | Nothing stops invented facts. |
| Advanced context | No product, no reason for outreach, no stakeholder. |
| Clear instructions | None. |
| Examples | No format, so every run comes back different. |

### After
```text
## Goal / Role
You are a senior enterprise account executive who sells route-planning software to mid-market logistics firms. Your goal is a one-page account brief that lets me open a first conversation with Acme Logistics' VP of Operations with a credible point of view.

## Rules
- NEVER invent facts, numbers, names, or quotes. Every fact needs a source link or the label "unverified".
- If you cannot find something, write "unknown". Do not fill gaps with guesses.
- One page. Plain language. No hype.

## Advanced context
### What we sell
Route-planning software that cuts empty miles and late deliveries.
### Why now
Acme posted three dispatcher job openings this month.
### Who I am meeting
VP of Operations. Owns on-time delivery and fleet cost.

## Clear instructions
1. Find what Acme has said publicly in the last 12 months about operations, growth, or cost.
2. List what changed recently, each with a source.
3. Infer the three most likely operations priorities. Rate confidence high, medium, or low and say why.
4. Write one sentence on how our product connects to the top priority.
5. List the questions you could not answer.

## Examples
## Company in one line
## What changed recently (fact, source)
## Likely top three priorities (evidence, confidence)
## Our angle (one sentence)
## Questions we still cannot answer
```

### What changed
Output arrives in the same five sections every run, every fact carries a source, and "unknown" replaces the guesses that used to appear as facts.

---

## Example 2: Post-call follow-up email (GRACE)

### Before
```text
Write a follow-up email to the CFO I met today. Make it good.
```

### After
```text
## Goal / Role
You are an enterprise account executive. Goal: a follow-up email that earns a 30-minute second meeting with Acme's CFO.

## Rules
- Under 120 words.
- NEVER claim results we did not discuss. Use only the notes below.
- No opener like "I hope this finds you well" or "Great to connect".
- End with one specific ask and a proposed date.

## Advanced context
### Call notes
CFO's priority: reduce cost to serve per customer before next fiscal year.
Concern raised: "Every vendor says they save money. Show me how you'd measure it."
What we showed: the usage report that ties tickets per account to support cost.
Proposed next step: a 30-minute session with their support ops lead to baseline current cost.

## Clear instructions
1. Open with the CFO's priority in their own words.
2. Answer the measurement concern in one sentence.
3. Propose the next step with a date next week.

## Examples
Line 1: their priority in their words.
Line 2: how we would measure it.
Line 3: next step with a date.
Bad opener (do not use): "Thanks so much for your time today, it was great to connect!"
```

### What changed
The email leads with the buyer's priority, answers the stated objection, and asks for one dated step. No invented savings figures.

---

## Example 3: Messaging brainstorm (SCRIBE, not GRACE)

### Before
```text
Give me a new tagline for our product. Use this format: [tagline] - [subhead].
```

### Diagnosis
Brainstorming forced into a fixed format converges too early. The output is ten variations of the same safe line. This job calls for SCRIBE.

### After
```text
Let's think through positioning together.

Who you are: a B2B positioning strategist who has launched products in crowded categories.
The situation: Acme Analytics sells pipeline forecasting to RevOps leaders. Every competitor says "AI-powered accuracy." Buyers no longer believe it.
A great outcome: one line a RevOps leader would repeat to their CRO.

Phase 1, brainstorm: Give me 12 distinct positioning angles. Do not filter. At least 4 should be uncomfortable.

Phase 2, self-critique: Stop playing nice. For each angle, tell me where it fails with a skeptical RevOps leader, and which competitor could claim the same thing.

Phase 3, refine: Keep the 2 strongest. Fix their weaknesses. Recommend one and give me a 5-customer test for it this week.
```

### What changed
The critique phase kills the angles any competitor could also claim. The survivors are specific enough to test.

---

## Example 4: Rep coaching plan (MIC upgraded to GRACE)

### MIC version (good for a first try)
```text
MISSION: Build a 30-day coaching plan for one rep.
INSTRUCTIONS: Focus on one skill. One page.
CONTEXT: Rep is 6 months in. Discovery calls run short and miss the business problem.
```

### Why upgrade
The manager will reuse this for every rep on the team. Two runs gave different structures and one invented a certification program. Repeatable output means GRACE.

### GRACE version
```text
## Goal / Role
You are a frontline sales manager who coaches through observed calls. Goal: a 30-day plan that improves one rep's discovery so that more first calls end with a documented business problem.

## Rules
- One skill only. If the evidence points to more than one, pick the one with the biggest effect and say why.
- NEVER invent programs, courses, or tools we have not listed.
- One page.

## Advanced context
### Rep
Six months in. Average first call: 18 minutes. Manager review of 5 calls: asks about features in the first 5 minutes; rarely asks about cost of the problem.
### Resources we have
Weekly 1:1, call recordings, a peer who is strong at discovery.

## Clear instructions
1. Name the one skill and cite the evidence from the call review.
2. Describe what good looks like as observable behavior on a call.
3. Lay out a weekly practice plan using only the resources listed.
4. Define how rep and manager will both know it worked by day 30.

## Examples
## The one skill (evidence)
## What good looks like
## Weeks 1 to 4
## How we will know (metric, date)
```

---

## Example 5: Applying the Rule of 90

A RevOps lead built a GRACE prompt for a weekly pipeline summary. First three runs:

| Run | What needed editing | Prompt fix |
|---|---|---|
| 1 | Summary listed every deal, not the ones that changed | Instruction: "Only include deals whose stage, amount, or close date changed." |
| 2 | Called a deal "at risk" with no reason | Rule: "Every risk label needs one stated reason from the data." |
| 3 | Fine except the subject line | Example: added a subject-line skeleton. |
| 4 | No edits | Prompt versioned and shared with the team. |

The edits shrank each run because each one became a permanent prompt change. That is the Rule of 90 working as designed: the human owns the last 10 percent, and the prompt keeps learning from it.

---

*GRACE, SCRIBE, MIC, Skeleton of Thought, and the Rule of 90 by Jonathan Kvarfordt (Coach K). Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*
