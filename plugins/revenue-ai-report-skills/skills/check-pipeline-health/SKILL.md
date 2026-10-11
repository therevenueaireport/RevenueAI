---
name: check-pipeline-health
description: "A blunt read on whether your pipeline can support the number, with the three leaks to fix first. Use when: Start of a quarter or half. When the forecast and the pipeline tell different stories. Before committing a number to the board."
---

# Check Pipeline Health

> From the [Revenue AI Report skill library](https://www.therevenueaireport.com/skills). Level: Intermediate · Task: Forecast · Setup: About 45 minutes · For: Sales Leader, Revenue Operations, Executive and Founder

**Outcome:** A blunt read on whether your pipeline can support the number, with the three leaks to fix first.

## When to use
- Start of a quarter or half.
- When the forecast and the pipeline tell different stories.
- Before committing a number to the board.

## Inputs you need
- Pipeline by stage with counts and value
- Historical win rate and average sales cycle by stage
- This period's target and how much is already closed

## Quick prompt
Paste into Claude, ChatGPT, or any assistant. Replace the [bracketed] parts.

```text
You are a revenue operations analyst. Here is my current pipeline by stage: [paste]. Here are my historical win rates and cycle times by stage: [paste]. Target is [NUMBER] with [AMOUNT] already closed. Tell me plainly: does this pipeline support the number? Where are the three biggest leaks (stage where deals die, age past cycle, coverage shortfall)? What should I inspect this week? Use my numbers only. Where you make an assumption, name it.
```

## Process
1. Export pipeline by stage with age in stage.
2. Add your real historical conversion and cycle numbers. Do not use benchmarks.
3. Ask for the read. Demand it use only your numbers.
4. Validate the three leaks with the managers who own those stages.
5. Pick one fix per leak and date it.

## Decision rules
- Coverage below your historical requirement is a pipeline problem, not a closing problem. Say so.
- Deals aged past twice the average cycle count as dead until a buyer action proves otherwise.
- If a stage converts under half the historical rate for two periods, inspect the stage definition, not the reps.

## Output
- A yes or no on whether the pipeline supports the number, with the math shown.
- The three leaks, ranked by dollars at risk.
- An inspection list for this week.

## Quality checks
- All math uses your pasted numbers, not industry ratios.
- Assumptions are listed, not hidden.
- Each leak has an owner and a next step.

## Limitations
- Aggregates hide single-deal risk. A pipeline can look healthy and still miss on one big deal.
- Historical rates break when the market or your motion just changed. Say so if they did.

## Worked example
**Input:** Stage 2: 40 deals, $4.1M, avg age 61 days (cycle avg 38). Historical stage-2-to-close: 18%. Target $2.5M, closed $0.9M.

**Output:** Verdict: no. Stage-2 value at historical conversion yields about $740k, leaving a gap of roughly $860k against the remaining $1.6M. Leak one: stage 2 aging 60 percent past cycle, meaning a slice of the $4.1M is stale. Inspection: every stage-2 deal older than 60 days needs a buyer-verified next step this week.

## Review checklist
- [ ] Did the read use your numbers only?
- [ ] Are stale deals reclassified honestly?
- [ ] Does each leak have an owner and a date?

## Go deeper
- Full skill page: https://www.therevenueaireport.com/skills/check-pipeline-health
- Related article: [pipeline-truth-test-for-ai](https://www.therevenueaireport.com/blog/pipeline-truth-test-for-ai)
- Research: [proof-gap](https://www.therevenueaireport.com/research/proof-gap)
- Playbooks that roll this out:
  - [Make conversation data do work (L3)](https://www.therevenueaireport.com/playbooks/conversation-data-to-work-l3) (L3 Integrated)
  - [Put an answer layer on the warehouse you already paid for (L4)](https://www.therevenueaireport.com/playbooks/answer-layer-on-warehouse-l4) (L4 Orchestrated)
  - [Point retrieval at the revenue corpus (L4)](https://www.therevenueaireport.com/playbooks/point-retrieval-at-revenue-corpus-l4) (L4 Orchestrated)

---

*Version 1.0.0 · Last reviewed 2026-09-04 · Source: [The Revenue AI Report](https://www.therevenueaireport.com) · License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
