---
name: prioritize-revenue-ai-use-cases
description: "A ranked list of AI use cases for your revenue team, scored on value you can measure and effort you actually have. Use when: Planning a quarter or half with more AI ideas than capacity. When the loudest stakeholder's idea keeps jumping the queue."
---

# Prioritize AI Use Cases

> From the [Revenue AI Report skill library](https://www.therevenueaireport.com/skills). Level: Intermediate · Task: Plan · Setup: About 45 minutes · For: Executive and Founder, Revenue Operations, GTM Engineering, Sales Leader

**Outcome:** A ranked list of AI use cases for your revenue team, scored on value you can measure and effort you actually have.

## When to use
- Planning a quarter or half with more AI ideas than capacity.
- When the loudest stakeholder's idea keeps jumping the queue.

## Inputs you need
- Your list of candidate AI use cases
- Rough value and effort guesses for each
- Your team's real capacity this quarter

## Quick prompt
Paste into Claude, ChatGPT, or any assistant. Replace the [bracketed] parts.

```text
You are a pragmatic operations advisor. Candidate AI use cases: [paste list]. My team's real capacity this quarter: [paste]. Rank them. For each: the measurable outcome if it works, the honest effort including data cleanup and behavior change, the data dependency, and the risk if it fails. Then give me the top two to start and the one that sounds exciting but should wait, with reasons. Favor use cases where the result is countable within one quarter.
```

## Process
1. List every candidate. Include the boring ones.
2. Score value as a measurable outcome, not a story.
3. Score effort honestly: data cleanup and behavior change dominate most AI projects.
4. Pick two. Fund them properly. Park the rest in writing.
5. Revisit the parked list only when one of the two ships or dies.

## Decision rules
- If the result cannot be counted within one quarter, it goes behind one that can.
- A use case depending on data you do not have starts with a data project, whether anyone likes it or not.
- Two active use cases maximum per team. Three means none are funded.

## Output
- Ranked list with value, effort, data dependency, and risk per use case.
- The two to start and the one to defer, with reasons.

## Quality checks
- Value is stated as a measurable outcome.
- Effort includes cleanup and adoption, not just setup.
- The deferred list is written down.

## Limitations
- Scores are structured judgment, not precision. The ranking matters more than the numbers.
- Political reality sometimes forces a different pick. If so, make the trade-off explicit.

## Worked example
**Input:** Candidates: call summarization, AI outbound sequencing, forecast roll-up automation, support-ticket tagging. Capacity: one RevOps person half-time for a quarter.

**Output:** Start: call summarization (countable time saved, data already exists) and forecast roll-up automation (removes weekly manual work, success visible in four weeks). Defer: AI outbound sequencing, because deliverability risk and data cleanup exceed one half-time person's capacity, and a failure there damages the domain, not just the quarter.

## Review checklist
- [ ] Two picks maximum?
- [ ] Deferred list written down?
- [ ] Each pick countable within a quarter?

## Go deeper
- Full skill page: https://www.therevenueaireport.com/skills/prioritize-revenue-ai-use-cases
- Framework: [proof-gap](https://www.therevenueaireport.com/frameworks/proof-gap)
- Research: [proof-gap](https://www.therevenueaireport.com/research/proof-gap)
- Research: [rollback](https://www.therevenueaireport.com/research/rollback)
- Playbooks that roll this out:
  - [Put an answer layer on the warehouse you already paid for (L4)](https://www.therevenueaireport.com/playbooks/answer-layer-on-warehouse-l4) (L4 Orchestrated)
  - [Make conversation data do work (L3)](https://www.therevenueaireport.com/playbooks/conversation-data-to-work-l3) (L3 Integrated)
  - [Score your ICP on stack density (L4)](https://www.therevenueaireport.com/playbooks/score-icp-on-stack-density-l4) (L4 Orchestrated)

---

*Version 1.0.0 · Last reviewed 2026-09-04 · Source: [The Revenue AI Report](https://www.therevenueaireport.com)*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
