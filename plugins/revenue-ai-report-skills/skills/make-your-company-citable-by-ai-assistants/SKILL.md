---
name: make-your-company-citable-by-ai-assistants
description: "A checked list of what an AI assistant can and cannot answer about you, and the fixes that make it cite you instead of a competitor. Use when: Buyers arrive already shortlisted and you were not on the list. An assistant answers questions about your category without naming you. Your pricing or security answers live only in a sales conversation."
---

# Make Your Company Citable by AI Assistants

> From the [Revenue AI Report skill library](https://www.therevenueaireport.com/skills). Level: Intermediate · Task: Build Campaigns · Setup: About an hour · For: Marketing, Executive and Founder, Revenue Operations, GTM Engineering

**Outcome:** A checked list of what an AI assistant can and cannot answer about you, and the fixes that make it cite you instead of a competitor.

## When to use
- Buyers arrive already shortlisted and you were not on the list.
- An assistant answers questions about your category without naming you.
- Your pricing or security answers live only in a sales conversation.

## Inputs you need
- The ten questions a buyer asks before shortlisting you
- The public pages that answer them, if any
- Your pricing, security, and integration pages
- Answers an assistant currently returns when asked about you

## Quick prompt
Paste into Claude, ChatGPT, or any assistant. Replace the [bracketed] parts.

```text
You are an answer-engine analyst. Using the buyer questions and pages I paste below, check each question five ways: is it answerable from public pages, is the answer grounded in evidence a machine can verify, is the page easy for a machine to read, is a named human attached, and can the claim be traced back to a source. Score each question pass or fail per check, cite the page you used, and give me the fix list ordered by how many buyer questions each fix unlocks.

Buyer questions and pages:
[paste]
```

## Process
1. Collect the inputs above. Thin input produces a confident, wrong answer.
2. Answerable: The buyer's question is answered in the first paragraph, not buried under setup. Agents lift the answer, not the introduction.
3. Grounded in evidence: Every claim carries a named benchmark, a date, and a source link. Adjectives do not survive a machine read.
4. Easy for a machine to read: Plain HTML with transcripts. Not trapped in a PDF, a gated form, or a page that only renders after interaction.
5. Named human attached: A real expert on every claim. Answer engines attribute to people. Faceless team bylines get skipped.
6. Trail back to the source: An agent can walk from the claim to its source without a dead end. A broken citation chain disqualifies the page.
7. Write the verdict and the next action with an owner and a date.
8. Have one person who did the work review the output before you share it.

## Decision rules
- If the answer is not on a public page, an assistant cannot cite it. Sales decks do not count.
- A claim with no verifiable source is a marketing line, not an answer.
- Attach a named human to any answer that involves judgment.
- Fix the questions buyers ask before shortlisting first, not the ones they ask after.

## Output
- A question-by-check grid with the page used as evidence.
- A fix list ordered by buyer questions unlocked.
- The questions you should not answer publicly, and why.

## Quality checks
- Every pass cites a live public URL.
- No fix invents a number, a customer, or a result.
- The list separates a missing page from a badly written one.

## Limitations
- Assistant answers vary by model and by day. Treat one sample as a signal, not a measurement.
- Publishing an answer does not force a citation. It removes the reason not to cite you.

## Worked example
**Input:** Ten buyer questions including pricing model, security posture, CRM integrations, and implementation time. Public pages: product, about, contact. No pricing or security page.

**Output:** Six of ten questions fail the answerable check. One page, a plain-language pricing model page with a named owner, unlocks four of them. Security posture needs a source that can be verified, not a claim.

## Review checklist
- [ ] Did someone re-ask the assistant two weeks after publishing?
- [ ] Does every new page name a human?
- [ ] Are the claims ones you could defend to a customer?

## Go deeper
- Full skill page: https://www.therevenueaireport.com/skills/make-your-company-citable-by-ai-assistants
- Related article: [buyers-shortlist-with-ai](https://www.therevenueaireport.com/blog/buyers-shortlist-with-ai)
- Research: [who-publishes-the-receipts](https://www.therevenueaireport.com/research/who-publishes-the-receipts)
- Research: [citation-decay](https://www.therevenueaireport.com/research/citation-decay)
- Playbooks that roll this out:
  - [Evidence first content operation (L6)](https://www.therevenueaireport.com/playbooks/marketing-evidence-first-content-rebuild-l6) (L6 Rebuilt)
  - [Put an answer layer on the warehouse you already paid for (L4)](https://www.therevenueaireport.com/playbooks/answer-layer-on-warehouse-l4) (L4 Orchestrated)
  - [Make conversation data do work (L3)](https://www.therevenueaireport.com/playbooks/conversation-data-to-work-l3) (L3 Integrated)

---

*Version 1.0.0 · Last reviewed 2026-09-04 · Source: [The Revenue AI Report](https://www.therevenueaireport.com)*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
