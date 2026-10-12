---
name: ai-tool-five-tests
description: >
  Gate any AI tool, vendor, agent, or internal build with the Five Tests by Jonathan Kvarfordt
  (Coach K): every tool must reduce cost, increase profit, increase revenue, decrease risk, or
  increase raving fans. Point it at one of those or don't bother. Scores each test on evidence,
  checks for harm on the other four, and returns proceed, pilot, or pass. Use when someone says
  "should we buy this AI tool", "evaluate this vendor", "is this tool worth it", "AI tool
  evaluation", "vendor demo looked great", "my buddy said this tool is awesome", "renew or cancel
  this tool", "tool sprawl", "justify this AI spend", or brings a demo, quote, or pitch deck. Hands
  off to pilot kill criteria, pilot review, AI SDR evaluation, and build/buy/connect skills.
---

# The Five Tests for Any AI Tool

> **The Five Tests by Jonathan Kvarfordt (Coach K).** Published in the [Revenue AI Report open skill library](https://www.therevenueaireport.com/skills).

**Outcome:** A one-page gate decision on a tool: which of the five things it does, how strong the evidence is, what it might break, and whether to proceed, pilot, or pass.

**The core idea:** a tool earns a place only if it does at least one of five things. Reduce cost. Increase profit. Increase revenue. Decrease risk. Increase raving fans. Point it at one of those or don't bother. The common failure is buying on a demo or a friend's recommendation with no framework, then wasting the time and the money.

---

## The five tests

| # | Test | The question | Evidence that counts | Evidence that does not |
|---|---|---|---|---|
| 1 | **Reduce cost** | Which cost line goes down, by how much, and when? | A named budget line, current spend, and a realistic reduction; hours saved that convert to a cost you actually stop paying | "Saves reps time" with no plan for the time |
| 2 | **Increase profit** | Does margin improve after the tool's full cost? | Unit economics before and after, including license, usage, implementation, and upkeep | Revenue lift with costs left out |
| 3 | **Increase revenue** | Which revenue driver moves (opportunities, deal size, win rate, cycle, retention, expansion)? | A baseline for that driver and a measurable target | Activity counts: emails sent, meetings booked without conversion |
| 4 | **Decrease risk** | Which risk goes down: compliance, data, forecast, churn, key-person? | The specific risk, how it is measured, and the current exposure | "More visibility" with no decision attached |
| 5 | **Increase raving fans** | Do customers (or employees) get a better experience they would tell others about? | Customer or user feedback, retention, response time, NPS or CSAT movement | Internal enthusiasm for the demo |

### Scoring

Score each test on the evidence in hand, not on the vendor's promise.

| Score | Meaning |
|---|---|
| **-1** | The tool works against this test (adds cost without offset, adds data or brand risk, worsens the customer experience) |
| **0** | No effect, or no evidence |
| **1** | Plausible, vendor claim only |
| **2** | Evidence from a comparable team, a reference call, or a small internal test |
| **3** | Measured in your own environment against a baseline |

### The gate

Rules of thumb, not laws. Adjust to your risk appetite and write down why.

| Result | Decision |
|---|---|
| One test at **3** and no test at **-1** | **Proceed** to a controlled rollout. |
| Best test at **2**, no test at **-1** | **Pilot** with written kill criteria. |
| Best test at **1** or below | **Pass**, or go back for evidence. A demo is not evidence. |
| Any test at **-1** | Resolve the harm first. A risk at -1 blocks proceed regardless of other scores. |
| Scores spread at 1 across four or five tests | **Pass.** A tool that does a little of everything usually does nothing measurable. Pick the primary test. |

---

## Process

1. **Name the primary test.** Which one of the five is this tool for? If the sponsor cannot pick, stop.
2. **Tie it to a number.** Which metric, what baseline, what target, by when. Use [backwards-diagnostic](../backwards-diagnostic/SKILL.md) if the link is unclear.
3. **Price the full cost.** License, usage or credits, implementation, integration, upkeep, and the time of the people running it.
4. **Score all five tests** with evidence. Write the evidence in one line per test.
5. **Run the harm check.** For every test, ask what could go backwards: data exposure, brand risk from automated outreach, customer frustration, cost creep.
6. **Apply the gate.** Proceed, pilot, or pass.
7. **Hand off:** pilot goes to kill criteria; build questions go to build/buy/connect; AI SDR tools get the dedicated evaluation.

Scorecard and a worked example: [references/scorecard.md](references/scorecard.md).

---

## Quick prompt

```text
You are a skeptical revenue finance partner evaluating an AI tool. Use the Five Tests by Jonathan Kvarfordt (Coach K): reduce cost, increase profit, increase revenue, decrease risk, increase raving fans.

Tool and what it claims: [paste]
Full cost (license, usage, implementation, upkeep): [paste or "unknown"]
Our baseline metrics: [paste]
Evidence we have (references, tests, data): [paste]

Steps:
1. Ask me which ONE test is primary if I have not said.
2. For each of the five tests, score -1 to 3: -1 works against it, 0 none, 1 vendor claim only, 2 comparable evidence or small test, 3 measured in our environment vs baseline. One line of evidence per score. Do not raise a score without evidence I gave you.
3. List anything that could make a test go backwards.
4. Apply the gate: one test at 3 and none at -1 = proceed; best at 2 = pilot with kill criteria; best at 1 or below = pass; any -1 = resolve first.
5. List the 3 questions to put to the vendor that would most change the scores.

Output: score table, harm list, decision, vendor questions.
```

## Decision rules

- **One primary test.** If the tool needs all five to justify itself, it justifies none.
- **Evidence, not enthusiasm.** Vendor claims cap at 1. Demos cap at 1.
- **Time saved is not cost reduced** until you say what the time will be used for and how you will see it in a number.
- **Harm blocks.** A -1 on risk or raving fans stops a proceed decision until resolved.
- **Right question, right time.** "What AI tool should I buy?" is a good question asked too early. Run the diagnostic first, then this gate.

## Quality checks

- One primary test named, tied to a baseline metric.
- Full cost priced, or marked unknown and flagged.
- Five scores, each with one line of evidence.
- Harm check done on all five.
- Decision follows the gate, or the deviation is explained.
- Next skill named for the hand-off.

## Hand-offs in this library

| If the decision is | Go to |
|---|---|
| Pilot | [Set AI Pilot Kill Criteria](../../../revenue-ai-report-skills/skills/set-ai-pilot-kill-criteria/SKILL.md) |
| Pilot finished, decide next | [Review an AI Pilot](../../../revenue-ai-report-skills/skills/review-ai-pilot/SKILL.md) |
| The tool is an AI SDR | [Evaluate an AI SDR](../../../revenue-ai-report-skills/skills/evaluate-ai-sdr/SKILL.md) |
| Could we build it or connect what we have? | [Decide Whether to Build, Buy, or Connect](../../../revenue-ai-report-skills/skills/decide-build-buy-or-connect/SKILL.md) |
| Part of a larger AI program | [scale-ai-transformation](../scale-ai-transformation/SKILL.md) |

---

*The Five Tests by Jonathan Kvarfordt (Coach K). Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next framework before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
