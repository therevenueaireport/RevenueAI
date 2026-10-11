---
name: set-ai-pilot-kill-criteria
description: "Written pass and fail conditions for an AI pilot, agreed before the pilot starts. Use when: Before signing or starting any AI pilot. When a stakeholder wants to just try it and see."
---

# Set AI Pilot Kill Criteria

> From the [Revenue AI Report skill library](https://www.therevenueaireport.com/skills). Level: Start Here · Task: Evaluate AI · Setup: About 30 minutes · For: Executive and Founder, Revenue Operations, Sales Leader, Revenue Finance

**Outcome:** Written pass and fail conditions for an AI pilot, agreed before the pilot starts.

## When to use
- Before signing or starting any AI pilot.
- When a stakeholder wants to just try it and see.

## Inputs you need
- What the tool is supposed to change, in numbers
- The pilot length and cost
- Who decides go or stop at the end

## Quick prompt
Paste into Claude, ChatGPT, or any assistant. Replace the [bracketed] parts.

```text
You are helping me design an AI pilot that can actually fail. Tool and goal: [paste]. Pilot length and cost: [paste]. Decision-maker: [paste]. Write the pilot charter: three to five measurable pass criteria with thresholds, two automatic kill conditions that end the pilot early regardless of other results, the measurement plan (what we count, from where, weekly), and the decision meeting date. Criteria must be measurable with data we actually have. If a proposed criterion cannot be measured, replace it with one that can.
```

## Process
1. State the goal as a number. If nobody can, the pilot should not start.
2. Set pass thresholds and automatic kill conditions.
3. Name the data source for every criterion. No source, no criterion.
4. Get the decision-maker to agree in writing before day one.
5. Book the decision meeting now, for the pilot's end date.

## Decision rules
- A criterion without a data source is deleted, not kept as a stretch.
- Kill conditions override everything. A tool can pass on usage and still die on complaints.
- The decision meeting date is fixed at the start and does not move.

## Output
- Pilot charter: pass criteria, kill conditions, measurement plan, decision date, decider.

## Quality checks
- Every criterion has a threshold and a data source.
- At least two automatic kill conditions exist.
- The decision-maker signed it before day one.

## Limitations
- Charters fail when the decider was never really committed. Get the signature, not a nod.
- Thresholds are judgment calls. Record why you picked each number.

## Worked example
**Input:** AI SDR pilot, 90 days, $30k. Goal: qualified meetings. Decider: VP Sales.

**Output:** Pass: cost per qualified meeting under $400 by day 60; meeting-to-opportunity conversion within 20 percent of human SDR baseline; 80 percent of sequences need no manual repair. Kill: spam complaint rate above 0.5 percent in any week, or any send to a do-not-contact list. Measured weekly from the engagement platform and CRM. Decision meeting: day 90, VP Sales, go or stop only.

## Review checklist
- [ ] Thresholds and sources on every criterion?
- [ ] Kill conditions truly automatic?
- [ ] Decision meeting booked?

## Go deeper
- Full skill page: https://www.therevenueaireport.com/skills/set-ai-pilot-kill-criteria
- Related article: [ai-sdr-kill-criteria-before-you-sign](https://www.therevenueaireport.com/blog/ai-sdr-kill-criteria-before-you-sign)
- Framework: [reversal-ledger](https://www.therevenueaireport.com/frameworks/reversal-ledger)
- Research: [rollback](https://www.therevenueaireport.com/research/rollback)
- Playbooks that roll this out:
  - [Autonomous pipeline generation with a human audit lane (L5)](https://www.therevenueaireport.com/playbooks/autonomous-pipeline-agent-with-audit-l5) (L5 Autonomous)
  - [Make conversation data do work (L3)](https://www.therevenueaireport.com/playbooks/conversation-data-to-work-l3) (L3 Integrated)
  - [Borrow the engineering harness for revenue (L3)](https://www.therevenueaireport.com/playbooks/engineering-harness-for-revenue-l3) (L3 Integrated)

---

*Version 1.0.0 · Last reviewed 2026-09-04 · Source: [The Revenue AI Report](https://www.therevenueaireport.com) · License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
