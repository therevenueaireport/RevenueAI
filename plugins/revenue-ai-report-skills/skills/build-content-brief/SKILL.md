---
name: build-content-brief
description: "A brief that tells a writer exactly what to produce: the question being answered, the evidence, and the bar for quality. Use when: Commissioning any article, guide, or report. When content volume is up and pipeline from content is flat."
---

# Build a Content Brief

> From the [Revenue AI Report skill library](https://www.therevenueaireport.com/skills). Level: Start Here · Task: Build Campaigns · Setup: About 20 minutes · For: Marketing, Enablement

**Outcome:** A brief that tells a writer exactly what to produce: the question being answered, the evidence, and the bar for quality.

## When to use
- Commissioning any article, guide, or report.
- When content volume is up and pipeline from content is flat.

## Inputs you need
- The buyer question the piece must answer
- The audience and where they will read it
- Any internal data, expert, or point of view you can contribute

## Quick prompt
Paste into any AI assistant. Replace the [bracketed] parts.

```text
You are an editorial director. Build a content brief for a piece answering this buyer question: [QUESTION]. Audience: [paste]. What we can contribute: [data, experts, point of view]. The brief must include: the working headline, the direct answer in the first 100 words, three supporting sections with the evidence each needs, what would make this piece worth citing, and what would make it generic filler we should not publish. Be specific. If we have no evidence or expert for this question, say the piece should not be written yet.
```

## Process
1. Start from a real buyer question, not a keyword.
2. List the evidence you can bring. If the answer is none, stop.
3. Generate the brief and cut anything a competitor's first page already says.
4. Add the quality bar: what would make someone cite or forward this.
5. Review the draft against the brief before editing prose.

## Decision rules
- No original evidence, data, or expert means no piece. Publish less.
- If the answer fits in one paragraph, write one paragraph. Do not pad to length.
- If the draft fails the brief, fix the draft, not the brief.

## Output
- Brief: question, answer, sections with required evidence, citation-worthy bar, kill criteria.

## Quality checks
- The piece answers the question in the first 100 words.
- Each section names its evidence.
- Kill criteria are written before writing starts.

## Limitations
- The AI cannot supply your evidence. A brief without evidence produces competent filler.
- Buyers and answer engines both discount generic content. Volume is not the goal.

## Worked example
**Input:** Question: how do I set kill criteria for an AI SDR pilot? Audience: VPs of Sales at mid-market SaaS. We have: three customer post-mortems and a kill-criteria framework.

**Output:** Headline: The five numbers that decide whether your AI SDR lives or dies. Answer first: kill it if cost per qualified meeting, meeting-to-opportunity rate, and complaint rate miss threshold by day 60. Sections: the five numbers with post-mortem evidence, setting thresholds before signing, the exit conversation. Kill criteria for the piece: if it reads like a vendor blog, it does not ship.

## Review checklist
- [ ] Real buyer question?
- [ ] Evidence named per section?
- [ ] Kill criteria written down?

## Toolkit
Load `references/TOOLKIT.md` for the four-part buyer question test, the evidence gate with strength grades, the first-page cut-list check, and a draft review scorecard against the brief.

## Go deeper
- Full skill page: https://www.therevenueaireport.com/skills/build-content-brief
- Related article: [ai-sdr-kill-criteria-before-you-sign](https://www.therevenueaireport.com/blog/ai-sdr-kill-criteria-before-you-sign)
- Research: [ai-slop-backlash](https://www.therevenueaireport.com/research/ai-slop-backlash)
- Playbooks that roll this out:
  - [Make conversation data do work (L3)](https://www.therevenueaireport.com/playbooks/conversation-data-to-work-l3) (L3 Integrated)
  - [Lifecycle content engine with a brand gate (L3)](https://www.therevenueaireport.com/playbooks/lifecycle-content-engine-brand-gate-l3) (L3 Integrated)
  - [AI outlines from an approved brief (L1)](https://www.therevenueaireport.com/playbooks/marketing-brief-to-outline-l1) (L1 Starter)

---

*Version 1.0.0 · Last reviewed 2026-09-04 · Source: [The Revenue AI Report](https://www.therevenueaireport.com) · License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
