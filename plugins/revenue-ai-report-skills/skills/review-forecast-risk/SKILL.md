---
name: review-forecast-risk
description: "A deal-by-deal stress test of the commit, with the specific deals that decide whether the number lands. Use when: Before you commit a number upward. The week before the board meeting. Any period where last period's forecast missed by more than ten percent."
---

# Review Forecast Risk

> From the [Revenue AI Report skill library](https://www.therevenueaireport.com/skills). Level: Intermediate · Task: Forecast · Setup: About 30 minutes · For: Sales Leader, Revenue Operations, Executive and Founder

**Outcome:** A deal-by-deal stress test of the commit, with the specific deals that decide whether the number lands.

## When to use
- Before you commit a number upward.
- The week before the board meeting.
- Any period where last period's forecast missed by more than ten percent.

## Inputs you need
- Your commit and best-case lists with amounts and close dates
- One line per deal: why it closes
- Last period's forecast accuracy

## Quick prompt
Paste into Claude, ChatGPT, or any assistant. Replace the [bracketed] parts.

```text
You are a skeptical forecast reviewer. Here is my commit list for this period: [paste deals with amount, close date, and why each closes]. Stress test it. For each deal, name what must be true for it to close on time and what evidence is missing. Rank the five deals that decide the number. Then give me the commit, the honest range, and what you would tell the board. Do not smooth it over. If a why-it-closes reason is really a hope, call it a hope.
```

## Process
1. List the commit deals with the reason each closes.
2. Run the stress test. Read the evidence-missing column first.
3. Send managers to get the missing evidence on the five deciding deals.
4. Set the commit at what survives the stress test, not what the target wants.
5. Record the call so next period's accuracy is measurable.

## Decision rules
- A deal stays in commit only if the buyer has confirmed the process and date in their words.
- If two of the five deciding deals lack evidence, the range, not the commit, goes to the board.
- Missed two periods running? The process changes before the next commit, not just the deals.

## Output
- Per-deal risk note with missing evidence.
- The five deciding deals ranked.
- Commit, honest range, and the board-ready sentence.

## Quality checks
- Every commit deal has buyer-confirmed process and date.
- The range reflects evidence, not optimism.
- The call is recorded for accuracy tracking.

## Limitations
- It reads the notes you give it. It cannot verify that a champion told the truth.
- Point-in-time. A single slip on one deciding deal invalidates the read.

## Worked example
**Input:** Commit $1.4M across 9 deals. Deal A $300k: champion says paper process started. Deal B $220k: waiting on legal since the 12th. Last period: forecast missed by 14%.

**Output:** Commit holds at $1.1M. Range to the board: $0.9M to $1.3M. Deal A lacks proof that procurement has the paper; get the confirmation email or move it to best case. Deal B is a legal queue risk; ask legal for the position in line, in writing.

## Review checklist
- [ ] Is each commit deal buyer-confirmed?
- [ ] Did the deciding deals get evidence requests?
- [ ] Is the range what you would defend in a board meeting?

## Go deeper
- Full skill page: https://www.therevenueaireport.com/skills/review-forecast-risk
- Related article: [pipeline-truth-test-for-ai](https://www.therevenueaireport.com/blog/pipeline-truth-test-for-ai)
- Research: [proof-gap](https://www.therevenueaireport.com/research/proof-gap)
- Playbooks that roll this out:
  - [AI assisted pipeline hygiene checklist (L1)](https://www.therevenueaireport.com/playbooks/revops-pipeline-hygiene-checklist-l1) (L1 Starter)
  - [Make conversation data do work (L3)](https://www.therevenueaireport.com/playbooks/conversation-data-to-work-l3) (L3 Integrated)
  - [Frontline manager operating system (L6)](https://www.therevenueaireport.com/playbooks/enablement-manager-operating-system-l6) (L6 Rebuilt)

---

*Version 1.0.0 · Last reviewed 2026-09-04 · Source: [The Revenue AI Report](https://www.therevenueaireport.com)*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
