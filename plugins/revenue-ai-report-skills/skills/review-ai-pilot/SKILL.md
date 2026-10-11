---
name: review-ai-pilot
description: "A go, fix, or stop call on an AI pilot based on the criteria you set before it started. Use when: At the end of any pilot period. When a pilot is being extended a second time without a decision."
---

# Review an AI Pilot

> From the [Revenue AI Report skill library](https://www.therevenueaireport.com/skills). Level: Intermediate · Task: Evaluate AI · Setup: About 45 minutes · For: Executive and Founder, Revenue Operations, Sales Leader, GTM Engineering

**Outcome:** A go, fix, or stop call on an AI pilot based on the criteria you set before it started.

## When to use
- At the end of any pilot period.
- When a pilot is being extended a second time without a decision.

## Inputs you need
- The success criteria set before the pilot started
- Pilot results: usage, output, quality, cost
- What the vendor or internal team promised

## Quick prompt
Paste into Claude, ChatGPT, or any assistant. Replace the [bracketed] parts.

```text
You are reviewing an AI pilot with no stake in the outcome. Criteria set before the pilot: [paste]. Results: [paste usage, output, quality, cost]. What was promised: [paste]. Give me a go, fix, or stop call. Judge results against the original criteria, not against criteria invented after the fact. Where results are ambiguous, say what would resolve them and how long that takes. If the pilot never had real criteria, say that first and stop the review until they exist.
```

## Process
1. Find the criteria written before the pilot. No criteria means the pilot already failed its purpose.
2. Score results against those criteria only.
3. Make the call: go, fix, or stop. Fix gets one defined change and one deadline.
4. Write down the call and the reasoning where the next reviewer can find it.
5. If stop: record what was learned and what it cost. That record is the value.

## Decision rules
- Criteria written after results arrive do not count.
- A second extension without a decision is a stop, announced late.
- Fix gets one change and one deadline. Two fixes means stop.

## Output
- Go, fix, or stop with the reasoning tied to original criteria.
- Ambiguities and what would resolve them.
- A written record either way.

## Quality checks
- Judgment uses pre-pilot criteria.
- The call is one word: go, fix, or stop.
- The reasoning is written down.

## Limitations
- Pilot groups are often your most enthusiastic users. Results may not survive contact with the full team.
- The AI cannot weigh strategic value that was never stated as a criterion.

## Worked example
**Input:** Criteria: 30 percent faster first drafts, complaint rate under 2 percent, adopted by 80 percent of the team by day 45. Results at day 60: drafts 35 percent faster, complaints 1.1 percent, adoption 41 percent.

**Output:** Call: fix. Two of three criteria passed, but 41 percent adoption at day 60 means the tool fits some workflows and not others. One change: identify the two workflows where the 41 percent cluster and restrict the rollout to them. Deadline: 30 days, then a go or stop on the narrowed scope. Do not extend twice.

## Review checklist
- [ ] Pre-pilot criteria in hand?
- [ ] One-word call made?
- [ ] Record written for the next reviewer?

## Go deeper
- Full skill page: https://www.therevenueaireport.com/skills/review-ai-pilot
- Related article: [ai-sdr-kill-criteria-before-you-sign](https://www.therevenueaireport.com/blog/ai-sdr-kill-criteria-before-you-sign)
- Framework: [reversal-ledger](https://www.therevenueaireport.com/frameworks/reversal-ledger)
- Research: [rollback](https://www.therevenueaireport.com/research/rollback)
- Research: [named-reversals](https://www.therevenueaireport.com/research/named-reversals)
- Playbooks that roll this out:
  - [Make conversation data do work (L3)](https://www.therevenueaireport.com/playbooks/conversation-data-to-work-l3) (L3 Integrated)
  - [Turn dormant seats into one shipped workflow (L2)](https://www.therevenueaireport.com/playbooks/dormant-seats-workflow-l2) (L2 Assisted)
  - [Borrow the engineering harness for revenue (L3)](https://www.therevenueaireport.com/playbooks/engineering-harness-for-revenue-l3) (L3 Integrated)

---

*Version 1.0.0 · Last reviewed 2026-09-04 · Source: [The Revenue AI Report](https://www.therevenueaireport.com) · License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
