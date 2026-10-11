---
name: check-crm-readiness-for-ai
description: "A blunt assessment of whether your CRM data can support the AI tool you are about to connect to it. Use when: Before connecting any AI tool to the CRM. When an AI tool's output looks wrong and you suspect the data."
---

# Check CRM Readiness for AI

> From the [Revenue AI Report skill library](https://www.therevenueaireport.com/skills). Level: Intermediate · Task: Evaluate AI · Setup: About 1 hour · For: Revenue Operations, GTM Engineering, Sales Leader

**Outcome:** A blunt assessment of whether your CRM data can support the AI tool you are about to connect to it.

## When to use
- Before connecting any AI tool to the CRM.
- When an AI tool's output looks wrong and you suspect the data.

## Inputs you need
- What the AI tool needs to read and write
- A sample of your CRM records or field-fill rates
- Who owns data quality today

## Quick prompt
Paste into Claude, ChatGPT, or any assistant. Replace the [bracketed] parts.

```text
You are a RevOps analyst assessing whether our CRM can support an AI tool. The tool needs to: [paste read and write requirements]. Here is our data reality: [paste field-fill rates, duplicates, record samples or an honest description]. Assess readiness: which requirements our data can support today, which it cannot, the cleanup work needed with rough effort, and the risks of connecting the tool before cleanup. If the honest answer is that we do not know our fill rates, the first deliverable is a one-week audit plan.
```

## Process
1. List exactly what the tool reads and writes.
2. Measure fill rates on those fields. Do not guess.
3. Match requirements to reality and name the gaps.
4. Estimate cleanup in weeks, with an owner.
5. Decide: connect now, connect after cleanup, or narrow the tool's scope.

## Decision rules
- A field under 60 percent filled cannot feed a feature. The feature waits or narrows.
- The tool never writes to records without a human-reviewable log, whatever the vendor defaults say.
- If nobody owns data quality, name an owner before the tool connects.

## Output
- Requirement-by-requirement readiness verdict.
- Cleanup list with rough effort and owner.
- Connect, wait, or narrow recommendation.

## Quality checks
- Fill rates are measured, not estimated.
- Write access is treated as the highest risk.
- The recommendation is one of three explicit options.

## Limitations
- Fill rates do not capture wrong-but-filled data. Spot-check accuracy on the fields that matter most.
- Readiness decays. Recheck before each new tool, not once ever.

## Worked example
**Input:** Tool drafts outreach from account fields and writes activities back. Fill rates: industry 88 percent, employee count 34 percent, last-touch notes inconsistent. 12 percent duplicate accounts.

**Output:** Verdict: narrow. Drafting can run on industry and website fields only; personalization by company size stays off until employee-count fill reaches 60 percent, estimated four weeks of enrichment work. Write-back allowed with a reviewable log. Duplicates must be merged before connect, roughly one week. Owner: RevOps lead.

## Review checklist
- [ ] Fill rates measured on the actual required fields?
- [ ] Write access constrained?
- [ ] Cleanup has an owner and an estimate?

## Go deeper
- Full skill page: https://www.therevenueaireport.com/skills/check-crm-readiness-for-ai
- Related article: [ai-sdr-kill-criteria-before-you-sign](https://www.therevenueaireport.com/blog/ai-sdr-kill-criteria-before-you-sign)
- Research: [rollback](https://www.therevenueaireport.com/research/rollback)
- Playbooks that roll this out:
  - [Make conversation data do work (L3)](https://www.therevenueaireport.com/playbooks/conversation-data-to-work-l3) (L3 Integrated)
  - [Autonomous pipeline generation with a human audit lane (L5)](https://www.therevenueaireport.com/playbooks/autonomous-pipeline-agent-with-audit-l5) (L5 Autonomous)
  - [Momentum.io call-to-CRM autofill (L3)](https://www.therevenueaireport.com/playbooks/momentum-call-crm-autofill-l3) (L3 Integrated)

---

*Version 1.0.0 · Last reviewed 2026-09-04 · Source: [The Revenue AI Report](https://www.therevenueaireport.com)*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
