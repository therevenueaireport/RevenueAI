---
name: review-ai-governance
description: "A practical check of who can buy AI, what data it can touch, and whether anyone would know if a tool went wrong. Use when: When AI tools are spreading faster than any policy. After a customer complaint or a data scare involving an AI tool. Before the board asks what your AI governance looks like."
---

# Review AI Governance

> From the [Revenue AI Report skill library](https://www.therevenueaireport.com/skills). Level: Advanced · Task: Govern AI · Setup: About 1 hour · For: Executive and Founder, Revenue Operations, Revenue Finance

**Outcome:** A practical check of who can buy AI, what data it can touch, and whether anyone would know if a tool went wrong.

## When to use
- When AI tools are spreading faster than any policy.
- After a customer complaint or a data scare involving an AI tool.
- Before the board asks what your AI governance looks like.

## Inputs you need
- A list of AI tools currently in use, sanctioned or not
- Your current approval process, if any
- Any data-handling rules that already exist

## Quick prompt
Paste into any AI assistant. Replace the [bracketed] parts.

```text
You are a governance advisor for a revenue organization. AI tools in use: [paste list, including unsanctioned ones]. Current approval process: [paste or say none]. Data rules: [paste or say none]. Assess our governance: the three biggest exposure points, the minimum policy we need (buying approval, data access, customer-facing output review, kill process), and how to find the tools we do not know about. Keep it proportionate for a company our size: [SIZE]. Do not hand me an enterprise compliance program.
```

## Process
1. Inventory what is in use, including expensed and free tools.
2. Name the exposure points: data in, output out, money spent.
3. Write the minimum policy: approval, data access, output review, kill process.
4. Assign one owner. Governance without an owner is a document.
5. Review quarterly. Tools change faster than annual policies.

## Decision rules
- Any tool touching customer data goes through review, no exceptions for free tiers.
- Customer-facing AI output needs a named human reviewer until it has earned trust with logs.
- A tool nobody will own gets shut off.

## Output
- The three biggest exposures, named.
- Minimum viable policy in four parts.
- A method for finding unknown tools.

## Quality checks
- The policy fits your company size.
- One owner is named.
- The inventory method finds unsanctioned tools, not just licensed ones.

## Limitations
- Policy does not equal behavior. Budget for the conversation, not just the document.
- This is operational governance, not legal advice. Regulated industries need counsel.

## Worked example
**Input:** 14 AI tools in use across sales and marketing, 5 expensed individually. No approval process. Reps paste CRM notes into free chat tools.

**Output:** Exposures: customer data flowing into free tools with no data terms, unreviewed customer-facing output, and spend nobody owns. Minimum policy: all tools touching customer data approved by the RevOps lead; a provided, approved assistant so reps stop using free ones; human review on outbound AI content; a kill process any leader can trigger. Find unknown tools quarterly via expense reports and a two-question team survey.

## Review checklist
- [ ] Owner named?
- [ ] Free-tier tools covered by the policy?
- [ ] Quarterly review scheduled?

## Toolkit
Load `references/TOOLKIT.md` for the four-source inventory method with an amnesty survey, a 0-3 exposure scoring sheet, a fill-ready one-page policy with a tested kill process, and a worked example sized for a mid-market company.

## Go deeper
- Full skill page: https://www.therevenueaireport.com/skills/review-ai-governance
- Related article: [ai-sdr-kill-criteria-before-you-sign](https://www.therevenueaireport.com/blog/ai-sdr-kill-criteria-before-you-sign)
- Research: [trust](https://www.therevenueaireport.com/research/trust)
- Research: [rollback](https://www.therevenueaireport.com/research/rollback)
- Playbooks that roll this out:
  - [Get shadow AI into the light (L3)](https://www.therevenueaireport.com/playbooks/get-shadow-ai-into-the-light-l3) (L3 Integrated)
  - [The agent control plane (L4)](https://www.therevenueaireport.com/playbooks/agent-control-plane-l4) (L4 Orchestrated)
  - [Company operating policy rebuilt for agents (L6)](https://www.therevenueaireport.com/playbooks/agent-operating-policy-rebuild-l6) (L6 Rebuilt)

---

*Version 1.0.0 · Last reviewed 2026-09-04 · Source: [The Revenue AI Report](https://www.therevenueaireport.com) · License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
