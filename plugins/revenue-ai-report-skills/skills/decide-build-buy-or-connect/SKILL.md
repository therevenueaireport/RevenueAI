---
name: decide-build-buy-or-connect
description: "A sourcing call for one AI capability, with the reasoning written down so the next person can challenge it. Use when: A team wants to build something a vendor already sells. You are being sold a tool that mostly moves data between systems you own. The same capability is being sourced twice by different teams."
---

# Decide Whether to Build, Buy, or Connect a Capability

> From the [Revenue AI Report skill library](https://www.therevenueaireport.com/skills). Level: Advanced · Task: Evaluate AI · Setup: About an hour · For: Revenue Operations, GTM Engineering, Executive and Founder, Revenue Finance

**Outcome:** A sourcing call for one AI capability, with the reasoning written down so the next person can challenge it.

## When to use
- A team wants to build something a vendor already sells.
- You are being sold a tool that mostly moves data between systems you own.
- The same capability is being sourced twice by different teams.

## Inputs you need
- The capability you need, described as a job, not a product
- What your current systems already do toward that job
- Engineering time you can realistically get, in weeks
- Whether the capability touches your buyer or only your team

## Quick prompt
Paste into Claude, ChatGPT, or any assistant. Replace the [bracketed] parts.

```text
You are a go-to-market architect. Using the details I paste below, make a three-way sourcing call for the capability: build it, buy it, or connect existing systems. For each option state the cost, the time to first value, the maintenance burden, and the failure mode. Weigh whether the capability is buyer-facing or internal. Recommend one option, name the second-best, and write the condition that should make me switch. Do not assume engineering capacity I did not give you.

Details:
[paste]
```

## Process
1. Collect the inputs above. Thin input produces a confident, wrong answer.
2. Buyer-facing infrastructure, buy: CRM, marketing automation, phone, video, storage. Nobody wins by building what everyone else already bought.
3. Buyer-facing intelligence, buy and thread: Where most AI-native leverage now lives. The vendor supplies the substrate. You supply the language, the plays, and the evidence.
4. Internal infrastructure, buy: Compute, model APIs, vector stores, agent runtimes. Rent the utilities. Buying infrastructure is not a strategy by itself.
5. Internal intelligence, build: Your ICP model, your enablement corpus, your reply corpus, your reversal ledger, your customer voice model. Only you can build these.
6. Write the verdict and the next action with an owner and a date.
7. Have one person who did the work review the output before you share it.

## Decision rules
- Infrastructure that everybody needs and nobody sees is usually bought.
- Build only where the capability is the difference between you and a competitor.
- Connecting existing systems is the default when the data already exists in them.
- Do not build against engineering time you have not been promised in writing.

## Output
- Three options costed on money, time, maintenance, and failure mode.
- One recommendation with the second-best option named.
- The condition that would flip the decision.

## Quality checks
- Maintenance is costed, not assumed to be zero.
- The recommendation matches the engineering capacity you actually have.
- The flip condition is observable.

## Limitations
- Pricing you did not supply is unknown and must not be estimated.
- The call ages. Re-run it when a platform ships overlapping functionality.

## Worked example
**Input:** Capability: enrich and route inbound leads within two minutes. Current systems hold firmographics and routing rules. Engineering: four weeks, unconfirmed.

**Output:** Recommendation: connect existing systems, because both data sets already sit in tools you own and the routing rules are configuration, not code. Second best: buy. Flip condition: routing logic that needs per-account judgment more than twice a week.

## Review checklist
- [ ] Did engineering confirm the time estimate in writing?
- [ ] Is maintenance owned by a named team?
- [ ] Is the flip condition on someone's review calendar?

## Go deeper
- Full skill page: https://www.therevenueaireport.com/skills/decide-build-buy-or-connect
- Related article: [headless-gtm-stack](https://www.therevenueaireport.com/blog/headless-gtm-stack)
- Research: [what-works](https://www.therevenueaireport.com/research/what-works)
- Research: [spend-vs-attribution](https://www.therevenueaireport.com/research/spend-vs-attribution)
- Playbooks that roll this out:
  - [Score your ICP on stack density (L4)](https://www.therevenueaireport.com/playbooks/score-icp-on-stack-density-l4) (L4 Orchestrated)
  - [Put an answer layer on the warehouse you already paid for (L4)](https://www.therevenueaireport.com/playbooks/answer-layer-on-warehouse-l4) (L4 Orchestrated)
  - [The agent control plane (L4)](https://www.therevenueaireport.com/playbooks/agent-control-plane-l4) (L4 Orchestrated)

---

*Version 1.0.0 · Last reviewed 2026-09-04 · Source: [The Revenue AI Report](https://www.therevenueaireport.com) · License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
