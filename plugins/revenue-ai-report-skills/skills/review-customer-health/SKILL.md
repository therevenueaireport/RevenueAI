---
name: review-customer-health
description: "A practical read on one account's renewal risk using the signals you actually have. Use when: 90 to 120 days before any renewal. When a champion leaves or usage drops. When your health-score tool and your gut disagree."
---

# Review Customer Health

> From the [Revenue AI Report skill library](https://www.therevenueaireport.com/skills). Level: Start Here · Task: Keep Customers · Setup: About 15 minutes per account · For: Customer Success, Sales Leader

**Outcome:** A practical read on one account's renewal risk using the signals you actually have.

## When to use
- 90 to 120 days before any renewal.
- When a champion leaves or usage drops.
- When your health-score tool and your gut disagree.

## Inputs you need
- Usage or engagement signals you track
- Recent interactions and support history summarized
- Renewal date and contract size

## Quick prompt
Paste into Claude, ChatGPT, or any assistant. Replace the [bracketed] parts.

```text
You are a customer success leader reviewing one account. Here is what we track: [paste usage, engagement, support, and relationship notes]. Renewal is [DATE] at [AMOUNT]. Give me: a health read of green, yellow, or red with the reason; the two strongest risk signals and the two strongest healthy signals; what we do not know that we should; and the next three actions with dates. Do not average the signals into a score. Judge them.
```

## Process
1. Gather the signals you have. Name the ones you do not.
2. Run the read. Weigh relationship signals against usage signals.
3. Confirm the read with anyone who talked to the account recently.
4. Book the next action with the customer, not just internally.
5. Log what you predicted so you can check accuracy at renewal.

## Decision rules
- A champion departure drops any account to yellow until the new relationship exists.
- Usage up but executive contact dead for a quarter is yellow, not green.
- A red account with renewal inside 90 days gets an executive sponsor this week.

## Output
- Green, yellow, or red with reasons.
- Top risk and health signals.
- Three dated actions, one of them customer-facing.

## Quality checks
- Signals are judged, not averaged into a fake score.
- Unknowns are listed explicitly.
- At least one action involves the customer directly.

## Limitations
- It cannot see signals you do not track, like internal champion politics.
- Health reads decay. A read older than 30 days is history, not current state.

## Worked example
**Input:** Renewal in 100 days at $180k. Usage steady. Champion changed jobs last month. One open support escalation. No executive contact since kickoff.

**Output:** Read: yellow leaning red. Risks: champion gone, no executive relationship, open escalation. Healthy: usage steady, team adoption broad. Unknown: who owns the renewal decision now. Actions: CSM maps the new decision-maker by Friday, executive sponsor intro within two weeks, escalate the support ticket to resolution before any renewal talk.

## Review checklist
- [ ] Was the champion question asked explicitly?
- [ ] Is at least one action customer-facing?
- [ ] Did you log the prediction?

## Go deeper
- Full skill page: https://www.therevenueaireport.com/skills/review-customer-health
- Research: [trust](https://www.therevenueaireport.com/research/trust)
- Playbooks that roll this out:
  - [Customer health scoring with AI signals (L4)](https://www.therevenueaireport.com/playbooks/cs-health-scoring) (L4 Orchestrated)
  - [AI first-draft renewal briefs (L1)](https://www.therevenueaireport.com/playbooks/cs-renewal-brief-drafts-l1) (L1 Starter)
  - [Support deflection with an audit lane (L5)](https://www.therevenueaireport.com/playbooks/support-deflection-audit-lane-l5) (L5 Autonomous)

---

*Version 1.0.0 · Last reviewed 2026-09-04 · Source: [The Revenue AI Report](https://www.therevenueaireport.com) · License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
