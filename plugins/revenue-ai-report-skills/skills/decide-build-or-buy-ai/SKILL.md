---
name: decide-build-or-buy-ai
description: "A structured build-versus-buy call for one AI capability, with the hidden costs on both sides priced in. Use when: Any AI capability decision with a price tag over a pilot. When a vendor renewal and an engineering estimate land in the same quarter."
---

# Decide Build or Buy for AI

> From the [Revenue AI Report skill library](https://www.therevenueaireport.com/skills). Level: Advanced · Task: Evaluate AI · Setup: About 1 hour · For: Executive and Founder, GTM Engineering, Revenue Operations, Revenue Finance

**Outcome:** A structured build-versus-buy call for one AI capability, with the hidden costs on both sides priced in.

## When to use
- Any AI capability decision with a price tag over a pilot.
- When a vendor renewal and an engineering estimate land in the same quarter.

## Inputs you need
- The capability you need and the workflow it serves
- Vendor quotes for buying
- Your engineering capacity and what else it would not do

## Quick prompt
Paste into Claude, ChatGPT, or any assistant. Replace the [bracketed] parts.

```text
You are an advisor helping me decide build versus buy for one AI capability: [paste]. Vendor quotes: [paste]. Our engineering capacity and competing priorities: [paste]. Walk me through the decision: the true three-year cost of each side including maintenance, model changes, and the opportunity cost of engineering time; what we would need to believe for build to win; what we would need to believe for buy to win; and your recommendation with the assumption it rests on. If the capability is close to our core product advantage, say so early, because that changes the answer.
```

## Process
1. Define the capability as a workflow outcome, not a feature list.
2. Price both sides over three years, including maintenance and model churn on the build side.
3. Price the opportunity cost of engineering time on the build side.
4. Ask whether the capability is core to your product advantage. Core tilts to build; commodity tilts to buy.
5. Make the call and record the assumption it rests on.

## Decision rules
- Build only wins when the capability is core or no vendor fits the workflow. Save money is not a build reason.
- Buy only wins when the vendor's roadmap matches yours and exit is affordable.
- Whichever you pick, write the kill criteria for the decision itself.

## Output
- Three-year true cost on both sides.
- The belief required for build and for buy.
- Recommendation with its load-bearing assumption.

## Quality checks
- Maintenance and model churn are priced into build.
- Opportunity cost of engineering is stated.
- The core-versus-commodity question is answered explicitly.

## Limitations
- Three-year forecasts of AI pricing are soft. Treat totals as ranges.
- The build estimate is only as honest as your engineering capacity number.

## Worked example
**Input:** Capability: forecasting assistant over our CRM. Buy quote: $90k per year. Build estimate: 2 engineers for 4 months, then ongoing maintenance.

**Output:** Three-year buy: roughly $270k plus integration time. Three-year build: roughly 14 engineer-months including maintenance and model updates, plus those engineers not shipping two roadmap items. The capability is not core to your product. Recommendation: buy, with a contract out at renewal and kill criteria if forecast accuracy does not improve within two cycles. Assumption to record: vendor roadmap keeps pace with your CRM changes.

## Review checklist
- [ ] Three-year costs on both sides?
- [ ] Core-versus-commodity answered?
- [ ] Kill criteria for the decision itself?

## Go deeper
- Full skill page: https://www.therevenueaireport.com/skills/decide-build-or-buy-ai
- Framework: [proof-gap](https://www.therevenueaireport.com/frameworks/proof-gap)
- Research: [proof-gap](https://www.therevenueaireport.com/research/proof-gap)
- Playbooks that roll this out:
  - [The agent control plane (L4)](https://www.therevenueaireport.com/playbooks/agent-control-plane-l4) (L4 Orchestrated)
  - [Rebuild coverage around agents, not headcount (L6)](https://www.therevenueaireport.com/playbooks/rebuild-coverage-around-agents-not-headcount-l6) (L6 Rebuilt)
  - [Point retrieval at the revenue corpus (L4)](https://www.therevenueaireport.com/playbooks/point-retrieval-at-revenue-corpus-l4) (L4 Orchestrated)

---

*Version 1.0.0 · Last reviewed 2026-09-04 · Source: [The Revenue AI Report](https://www.therevenueaireport.com)*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
