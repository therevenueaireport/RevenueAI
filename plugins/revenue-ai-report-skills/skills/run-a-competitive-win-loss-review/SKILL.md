---
name: run-a-competitive-win-loss-review
description: "A pattern read across deals against one competitor: why you win, why you lose, and the one change worth making. Use when: You are deciding whether to change pricing, packaging, or positioning against one competitor. Different leaders tell different stories about why you lose to them. Before you fund a competitive programme, so you can measure whether it worked."
---

# Run a Competitive Win and Loss Review

> From the [Revenue AI Report skill library](https://www.therevenueaireport.com/skills). Level: Advanced · Task: Measure Results · Setup: About two hours · For: Revenue Operations, Sales Leader, Marketing, Enablement

**Outcome:** A pattern read across deals against one competitor: why you win, why you lose, and the one change worth making.

## When to use
- You are deciding whether to change pricing, packaging, or positioning against one competitor.
- Different leaders tell different stories about why you lose to them.
- Before you fund a competitive programme, so you can measure whether it worked.

## Inputs you need
- Closed won and closed lost deals against the competitor for the last two quarters
- The stated reason per deal, ideally from the buyer rather than the rep
- Segment fields: size, industry, entry point, deal value

## Quick prompt
Paste into Claude, ChatGPT, or any assistant. Replace the [bracketed] parts.

```text
You are a revenue analyst. Using only the closed deal data I paste below, find the pattern in our results against [COMPETITOR]. Produce: win rate against them overall and by segment, the reasons that appear in three or more losses, the reasons that appear in three or more wins, any segment where the pattern reverses, and what the data cannot answer. Count reasons, do not narrate individual deals. Tell me the sample size for every figure, and say plainly when a sample is too small to support a conclusion.

Deal data:
[paste closed won and closed lost records with reasons]
```

## Process
1. Pull every closed deal against the competitor for a fixed period. Do not cherry-pick.
2. Separate no-decision deals from competitive losses. They are different problems.
3. Code the stated reasons into a small set of themes, then count them.
4. Look for segments where the pattern reverses. That is usually where the decision is.
5. Pick one change, name the owner, and set the measure that says whether it worked.

## Decision rules
- A theme counts as a pattern at three or more deals. Below that it is an anecdote.
- Rep-stated loss reasons are a hypothesis. Buyer-stated reasons are evidence. Label which you have.
- If wins and losses share the same stated reason, the reason is not the cause. Keep digging.
- One change per review. A list of eight changes is a decision not made.

## Output
- Win rate against the competitor, overall and by segment, with sample sizes.
- Counted loss and win reasons, with source labelled.
- One change, one owner, one measure, one date to check it.

## Quality checks
- Every percentage is shown with its sample size.
- No-decision deals are reported separately from competitive losses.
- The review states what the data cannot answer.

## Limitations
- CRM loss reasons record what the rep believed, which is often not what the buyer decided.
- Small samples produce confident nonsense. Say the sample is too small when it is.
- This tells you what already happened. It does not predict a competitor's next move.

## Worked example
**Input:** Pasted: 34 closed deals against one competitor over two quarters, with stated reason, segment, and value.

**Output:** Win rate 38 percent, 34 deals. Under 500 employees it is 52 percent, 21 deals. Over 500 it is 15 percent, 13 deals, and the stated reason in 7 of 11 losses is implementation support. Sample too small to split by industry. One change: named implementation plan in enterprise deals, owner and check date set.

## Review checklist
- [ ] Are buyer-stated and rep-stated reasons kept apart?
- [ ] Is every figure published with its sample size?
- [ ] Is there exactly one change with an owner and a date?

## Go deeper
- Full skill page: https://www.therevenueaireport.com/skills/run-a-competitive-win-loss-review
- Research: [proof-gap](https://www.therevenueaireport.com/research/proof-gap)
- Research: [spend-vs-attribution](https://www.therevenueaireport.com/research/spend-vs-attribution)
- Playbooks that roll this out:
  - [Make conversation data do work (L3)](https://www.therevenueaireport.com/playbooks/conversation-data-to-work-l3) (L3 Integrated)
  - [Put an answer layer on the warehouse you already paid for (L4)](https://www.therevenueaireport.com/playbooks/answer-layer-on-warehouse-l4) (L4 Orchestrated)
  - [Point retrieval at the revenue corpus (L4)](https://www.therevenueaireport.com/playbooks/point-retrieval-at-revenue-corpus-l4) (L4 Orchestrated)

---

*Version 1.0.0 · Last reviewed 2026-09-22 · Source: [The Revenue AI Report](https://www.therevenueaireport.com) · License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
