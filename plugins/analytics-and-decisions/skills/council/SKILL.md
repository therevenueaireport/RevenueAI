---
name: "council"
description: "Pressure-test a real decision with five independent AI advisors, blind peer review, and a chairman verdict with kill criteria. Run on /council, council this, run the council, war room this. Modes: quick, gtm, with, again, debrief."
---

# Council

One AI answer gives you one perspective and no way to judge it. The council runs a decision through five advisors who think in deliberately conflicting ways, has them review each other blind, and hands everything to a chairman who must commit to a real answer, a first step, and the tripwires that would reverse it.

Built on a published multi-model council method (independent answers, anonymous peer review, chairman synthesis), using sub-agents with different thinking lenses instead of different models.

---

## Commands

Text after the command is the question or the mode.

| Command | What runs | Approx. agent calls |
|---|---|---|
| `/council [question]` | Full council: 5 advisors, 5 lens reviews, chairman | 11 |
| `/council quick [question]` | 5 advisors + chairman, no peer review | 6 |
| `/council gtm [question]` | Full council with the GTM lineup (below) | 11 |
| `/council with [lens, lens, lens] : [question]` | Custom lineup of 3 to 7 lenses | 2n + 1 |
| `/council again [question]` | Re-run against a prior transcript and show what moved | 11 |
| `/council debrief [decision]` | Compare a past verdict to what actually happened | 1 |
| `/council` (nothing after) | Ask: "What decision should the council take?" | 0 |

Phrases like "council this", "run the council", "war room this", and "convene the council" equal `/council`.

Do NOT trigger on "stress test", "pressure test", or "devil's advocate" alone. Those belong to statistical-reasoning and monte-carlo. If the user seems to want a council but used those words, offer it in one line instead of running it.

---

## Gate: is this a council question?

Run the council only when all three hold:
1. There is a real decision or a piece of work to judge (not a fact lookup, not a writing task).
2. Reasonable people could disagree.
3. Being wrong costs real money, time, reputation, or relationships.

If the gate fails, answer directly and say in one line why a council would be overkill. A full council is about 11 agent calls; spend them where they matter.

---

## Step 1: Intake

Extract from the user's message:
- **Decision**: the actual choice, in one sentence
- **Type**: Go/No-Go, A vs B (or more options), open ("what should I do about X"), or artifact review (copy, deck, plan, pricing page)
- **Options**: list them; for open questions, name the 2 to 4 realistic paths
- **Stakes**: what is at risk and roughly how much
- **Reversibility**: one-way door (hard to undo) or two-way door (cheap to undo)
- **Deadline and constraints**: time, budget, people, commitments
- **What would change the user's mind**, if they said it

If two or more of Decision, Options, or Stakes are missing, ask ONE bundled clarifying question (use AskUserQuestion when available), then proceed. Never ask a second round.

---

## Step 2: Context packet

Generic advice comes from thin context. Spend up to 60 seconds and 3 to 5 sources pulling the specifics:

1. Files the user attached or named
2. User memory, when memory tools exist: profile, preferences, and any notes that match the decision
3. A connected folder or cloud drive, only for files the user referenced or that obviously match (for example pricing data for a pricing decision)
4. Prior council transcripts on the same topic
5. A project CLAUDE.md or memory/ folder, if present

Build a **context packet** of 400 words or fewer. Every fact carries its source in brackets, for example `[memory: pricing-notes]` or `[file: q3-pipeline.xlsx]`. No opinions in the packet.

Then write two prompts:
- **Briefed question**: decision, type, options, stakes, reversibility, constraints, context packet. Every advisor except the Outsider gets this.
- **Blind question**: the user's own words plus the options only. No context packet, no names of internal tools, no history. The Outsider gets only this.

---

## Step 3: Convene the advisors (parallel)

### Default lineup

1. **The Contrarian.** Assumes there is a fatal flaw and hunts for it. If it all looks solid, digs deeper. Saves the user from a bad deal by asking what they are avoiding.
2. **The First Principles Thinker.** Asks what problem is actually being solved, strips assumptions, rebuilds from zero. Allowed to say "you are asking the wrong question."
3. **The Expansionist.** Hunts for the upside nobody priced in: the bigger version, the adjacent opportunity, the undervalued asset. Ignores risk; that is the Contrarian's job.
4. **The Outsider.** Zero context about the user or their field. Reacts only to what is in front of them. Catches the curse of knowledge. Always receives the blind question.
5. **The Executor.** Only cares whether it can be done and what happens Monday morning. If there is no clear first step, says so.

Tensions by design: Contrarian vs Expansionist (downside vs upside), First Principles vs Executor (rethink vs ship), Outsider as the honesty check.

### GTM lineup (`/council gtm`)

1. **The CRO.** Does this help make the number this year? Pipeline, coverage, win rate, cycle time.
2. **The CFO.** Unit economics, payback, cash, and the opportunity cost of doing this instead of something else.
3. **The Buyer.** A skeptical economic buyer in the ICP. Would I take the meeting, believe the claim, and pay for it?
4. **The Operator.** RevOps and enablement. Systems, data quality, adoption, who does the work, what breaks at scale.
5. **The Outsider.** Same as default. Always blind.

Tensions: CRO vs CFO (growth vs efficiency), Buyer vs Operator (what sells vs what runs).

### Custom lineup (`/council with ...`)

Accept 3 to 7 lenses. Write a two-sentence thinking style for each. Always keep one downside lens and one blind Outsider; if the user's list has neither, add them and say so.

### Advisor prompt template

```
You are [Advisor Name] on a decision council.

Your thinking style: [description]

The question:
---
[briefed question, or blind question for the Outsider]
---

Lean fully into your angle. Do not hedge or balance; other advisors cover other angles.

Evidence rule: tag every factual claim as [context], [assumption], or [estimate]. Never invent statistics, benchmarks, or quotes. If you need a number you do not have, give a range and tag it [estimate].

Respond in exactly this format, no preamble:

POSITION: [Go / No-Go / Conditional, or the option you back]
CONFIDENCE: [0-100]
ANALYSIS: [150-250 words]
LOAD-BEARING ASSUMPTION: [the one thing that must be true for your position to hold]
WOULD CHANGE MY MIND: [the specific evidence that would flip you]
```

Spawn all advisors at once with the Agent tool so no answer bleeds into another. If sub-agents are unavailable, write each advisor in a separate pass, finishing each before reading the others, and label the report "sequential fallback".

---

## Step 4: Blind peer review (parallel; skipped in quick mode)

1. Shuffle the responses and label them A, B, C, D, E. Keep the mapping private.
2. Spawn one reviewer per advisor. Each reviewer keeps its own lens and sees the OTHER responses only (remove its own, so nobody votes for themselves).

```
You are [Advisor Name], reviewing other members of a decision council through your own lens: [thinking style].

The question:
---
[briefed question]
---

Responses:
[the other responses, labeled by letter]

Answer in this format, under 200 words total:

STRONGEST: [letter] because [reason]
BIGGEST BLIND SPOT: [letter] is missing [what]
EVERYONE MISSED: [the consideration no response raised]
POSITION NOW: [your position and confidence after reading these, and what moved you, or "unchanged"]
```

3. Tally the STRONGEST votes and record every position shift. Shifts show where the council is converging.

---

## Step 5: Chairman verdict

One agent gets the briefed question, all responses with names revealed, all reviews, the vote tally, and the position shifts.

```
You are the Chairman of a decision council. Synthesize into a verdict the user can act on today.

[briefed question]
[named advisor responses]
[peer reviews, vote tally, position shifts]

Use exactly this structure:

## Verdict
One line: [Go / No-Go / Conditional / Option X] | Confidence [0-100] | [One-way or two-way door]

## Where the council agrees
Points reached independently by several advisors. High-confidence signal.

## Where the council clashes
Each real disagreement, both sides, and why reasonable advisors split.

## What peer review surfaced
What only appeared in review, including the EVERYONE MISSED answers.

## Recommendation
A real answer with reasoning. Never "it depends." You may side with a minority of one if their reasoning is strongest; say so and why.

## Kill criteria
2 to 3 tripwires that would reverse this call. Each is a metric or event, a threshold, and a date.

## Do this first
One action, who does it, and by when.

## What would change this verdict
The single piece of evidence that would most change the recommendation.
```

If the verdict hinges on a number, the chairman names the skill to run next when it is available: statistical-reasoning (is the number real), data-claims-auditor (is the source credible), monte-carlo (range of outcomes), bayesian-updater (how much should new evidence move the call).

---

## Step 6: Deliver

**In chat, first and short:** the Verdict line, Do this first, and Kill criteria. The user should be able to act without opening anything.

**Report (HTML), the scannable version:**
1. The question and decision type
2. The chairman verdict, prominent
3. A position map: each advisor's position and confidence before and after peer review, so convergence and holdouts are visible at a glance
4. Vote tally from peer review
5. Collapsible sections for each advisor (collapsed by default) and for the peer reviews
6. Footer: timestamp, mode, lineup, and "sequential fallback" if it applied

Before building it, load the artifact-design skill if available. Clean briefing-document style, readable in light and dark mode. Write report copy plainly: no jargon, no filler, no em-dashes.

Delivery: if the Artifact tool is available, publish the report (private by default, shareable later). Otherwise save `council-report-YYYY-MM-DD-[slug].html` to the outputs folder, or the connected folder if one exists, and send it.

**Transcript (markdown), the record:** `council-transcript-YYYY-MM-DD-[slug].md`, saved next to the report. Include the raw question, briefed question, blind question, context sources, every advisor response, the letter mapping, every review, the tally and shifts, and the full chairman verdict.

**Decision log line:** end the chat reply with one line the user can keep:
`[date] | [decision] | [verdict] | conf [n] | kill: [tripwires] | review by [date]`
Offer once to save it to memory. Do not save it unless the user says yes.

---

## `/council again`

Needs the prior transcript: ask the user to attach it or find it in the connected folder. Run the full council with the new facts, then add a section **What changed since last council**: which positions moved, which assumptions were confirmed or broken, and whether the verdict flipped.

## `/council debrief`

Inputs: the transcript or decision log line, plus what actually happened. Output, under 250 words:
- Was the verdict right, partly right, or wrong?
- Which advisor called it best, and which load-bearing assumption broke?
- Calibration: stated confidence compared with the outcome
- One adjustment for future councils (for example "the Buyer lens was missing" or "kill criteria fired late")

Offer once to save the adjustment to memory or the user's decision log. Do not save it unless the user says yes.

---

## Example verdict (GTM mode)

**Question:** Should we launch a paid community at $49/month or keep it free and sell a $2,500 cohort course?

**Verdict:** Option B (free community + cohort) | Confidence 70 | Two-way door

**Kill criteria:** fewer than 25 paid cohort seats from the first 500 community members by Dec 15; community weekly active rate below 20% by week 6.

**Do this first:** You post the cohort waitlist to the existing list this Friday with a 48-hour early-bird, before building anything.

---

## Non-negotiables

- Advisors run in parallel. Always.
- Peer review is anonymized, and reviewers never see their own response.
- The Outsider always gets the blind question.
- The chairman may overrule the majority, with reasons.
- No invented numbers anywhere in the chain.
- Do not council trivia. Use the gate.

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt (Coach K). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
