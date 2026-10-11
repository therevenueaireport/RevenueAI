---
name: review-sales-deal
description: "A structured read on one open deal: what is proven, what is assumed, and the next action that moves it. Use when: Weekly deal reviews and forecast calls. Any deal that slipped its close date once already. Before discounting to save a deal."
---

# Review a Deal

> From the [Revenue AI Report skill library](https://www.therevenueaireport.com/skills). Level: Start Here · Task: Run Deals · Setup: About 10 minutes per deal · For: Sales Leader, Sales Representative, Revenue Operations

**Outcome:** A structured read on one open deal: what is proven, what is assumed, and the next action that moves it.

## When to use
- Weekly deal reviews and forecast calls.
- Any deal that slipped its close date once already.
- Before discounting to save a deal.

## Inputs you need
- Deal notes or CRM fields: stage, amount, close date, contacts
- Last three interactions summarized
- What the champion and the blocker each said, if known

## Quick prompt
Paste into Claude, ChatGPT, or any assistant. Replace the [bracketed] parts.

```text
You are a deal coach. Here is everything I know about one open deal: [paste notes]. Review it. Split what is proven (the buyer said it or did it) from what is assumed (I believe it but have no evidence). Then tell me: the biggest risk to this deal, whether the close date is justified, and the single next action most likely to move it forward or kill it honestly. If my notes are too thin to judge, list the three facts I need to go get.
```

## Process
1. Paste the notes. Include what the buyer actually said, not your summary of the mood.
2. Read the proven-versus-assumed split first. That is the review.
3. Challenge the close date: what buyer action is it tied to?
4. Agree on one next action with a date and an owner.
5. Update the CRM so the record matches reality.

## Decision rules
- No buyer-verified next step means the deal drops a stage. Hope is not a stage.
- A close date with no tied buyer action moves out a full cycle.
- If the champion has never introduced power, the deal is single-threaded. That is the top risk until fixed.

## Output
- Proven versus assumed list.
- Top risk and close-date verdict.
- One next action, owner, and date.

## Quality checks
- Proven items quote buyer words or actions.
- The next action requires the buyer to do something.
- The CRM record is updated to match.

## Limitations
- The review is only as honest as the notes. Sandbagged or happy-ear notes produce a clean, wrong read.
- The AI cannot see stakeholder politics it was never told about.

## Worked example
**Input:** $120k, stage 3, close 9/30. Champion is a director who likes the product. No meeting with the VP yet. Security review mentioned but not scheduled.

**Output:** Proven: director-level interest, problem confirmed. Assumed: budget, VP support, close date. Top risk: single-threaded with an unscheduled security review. Verdict: 9/30 is not justified. Next action: champion books VP and security scoping call by Friday, or the close date moves out one cycle.

## Review checklist
- [ ] Is anything labeled proven that the buyer never actually said?
- [ ] Does the next action put work on the buyer?
- [ ] Did the CRM change after the review?

## Go deeper
- Full skill page: https://www.therevenueaireport.com/skills/review-sales-deal
- Related article: [pipeline-truth-test-for-ai](https://www.therevenueaireport.com/blog/pipeline-truth-test-for-ai)
- Research: [proof-gap](https://www.therevenueaireport.com/research/proof-gap)
- Research: [four-answers](https://www.therevenueaireport.com/research/four-answers)
- Playbooks that roll this out:
  - [Make conversation data do work (L3)](https://www.therevenueaireport.com/playbooks/conversation-data-to-work-l3) (L3 Integrated)
  - [AI assisted pipeline hygiene checklist (L1)](https://www.therevenueaireport.com/playbooks/revops-pipeline-hygiene-checklist-l1) (L1 Starter)
  - [AI first-draft renewal briefs (L1)](https://www.therevenueaireport.com/playbooks/cs-renewal-brief-drafts-l1) (L1 Starter)

---

*Version 1.0.0 · Last reviewed 2026-09-04 · Source: [The Revenue AI Report](https://www.therevenueaireport.com)*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
