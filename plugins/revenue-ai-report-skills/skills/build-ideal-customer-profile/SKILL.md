---
name: build-ideal-customer-profile
description: "A one-page profile of the accounts most likely to buy, expand, and stay, built from your own win data. Use when: You are planning a new segment, territory, or campaign and need a shared definition of a good account. Win rates differ widely by segment and nobody can say why. Marketing and sales disagree about who the target buyer is."
---

# Build an Ideal Customer Profile

> From the [Revenue AI Report skill library](https://www.therevenueaireport.com/skills). Level: Start Here · Task: Plan · Setup: About 30 minutes · For: Marketing, Sales Leader, Revenue Operations, Executive and Founder

**Outcome:** A one-page profile of the accounts most likely to buy, expand, and stay, built from your own win data.

## When to use
- You are planning a new segment, territory, or campaign and need a shared definition of a good account.
- Win rates differ widely by segment and nobody can say why.
- Marketing and sales disagree about who the target buyer is.

## Inputs you need
- A list of your 20 best customers and why they bought
- A list of 10 deals you lost or that stalled
- Basic firmographics: industry, employee count, region

## Quick prompt
Paste into any AI assistant. Replace the [bracketed] parts.

```text
You are a B2B go-to-market analyst. Using the customer and deal lists I paste below, draft a one-page ideal customer profile. Include: the firmographics that show up in wins, the buying trigger that starts most deals, the roles in the buying group, the two most common reasons deals die, and three disqualifiers we should apply early. Separate what the data shows from what you are inferring. End with five questions I should answer before treating this profile as final.

Best customers:
[paste list]

Lost or stalled deals:
[paste list]
```

## Process
1. List your best customers. Best means they bought fast, pay full price, renew, and expand. Not the biggest logos.
2. List lost and stalled deals from the same period.
3. Ask the AI to find the traits that separate the two lists: industry, size, trigger event, buying role.
4. Turn the traits into inclusion rules (must have) and disqualifiers (walk away early).
5. Test the profile against five open pipeline deals before you adopt it.

## Decision rules
- A trait only enters the profile if it appears in wins more than in losses.
- If two segments win at similar rates, keep both and score them separately. Do not force one profile.
- If a disqualifier would have killed a deal you actually won, demote it to a caution flag.

## Output
- One page: firmographics, trigger, buying group, win conditions, disqualifiers.
- A scoring rule of five to eight checks a rep can run in two minutes.
- An open-questions list of what the data could not answer.

## Quality checks
- Every claim traces to the pasted lists, not to general market wisdom.
- The profile names who to avoid, not only who to pursue.
- A rep can apply the scoring rule without help.

## Limitations
- The AI sees only what you paste. Thin or biased input gives a confident, wrong profile.
- Past wins describe the market you already reached, not segments you have never tried.

## Worked example
**Input:** Best customers: 12 of 20 are 200 to 2,000 person SaaS or logistics firms; most bought within 90 days of a new CRO or a forecast miss. Losses: 7 of 10 were 5,000+ person enterprises stuck in security review.

**Output:** Profile: 200 to 2,000 employees, SaaS or logistics, new revenue leader in seat under 6 months. Disqualifier: enterprise security review with no executive sponsor. Open question: do wins hold at 2,000 to 5,000 employees, which the sample does not cover.

## Review checklist
- [ ] Did a manager read the final profile and agree it matches reality?
- [ ] Are the disqualifiers safe, meaning they would not have lost past wins?
- [ ] Is the open-questions list assigned to someone?

## Toolkit
Load `references/TOOLKIT.md` for the win/loss data checklist, the trait separation table with verdict rules, the two-minute scoring rule, and a fully worked example.

## Go deeper
- Full skill page: https://www.therevenueaireport.com/skills/build-ideal-customer-profile
- Framework: [oar](https://www.therevenueaireport.com/frameworks/oar)
- Research: [proof-gap](https://www.therevenueaireport.com/research/proof-gap)
- Research: [four-answers](https://www.therevenueaireport.com/research/four-answers)
- Playbooks that roll this out:
  - [Score your ICP on stack density (L4)](https://www.therevenueaireport.com/playbooks/score-icp-on-stack-density-l4) (L4 Orchestrated)
  - [Put an answer layer on the warehouse you already paid for (L4)](https://www.therevenueaireport.com/playbooks/answer-layer-on-warehouse-l4) (L4 Orchestrated)
  - [Make conversation data do work (L3)](https://www.therevenueaireport.com/playbooks/conversation-data-to-work-l3) (L3 Integrated)

---

*Version 1.0.0 · Last reviewed 2026-09-04 · Source: [The Revenue AI Report](https://www.therevenueaireport.com) · License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
