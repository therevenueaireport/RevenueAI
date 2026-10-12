---
name: data-claims-auditor
description: >
  Systematic teardown and validation of third-party data claims, vendor stats, market sizing
  reports, competitor assertions, analyst projections, and any externally sourced number used
  to drive decisions. Triggers on: "can we trust this number," "is this real," "does this
  hold up," "audit this claim," "what's the source," "this seems too good," "tear this apart,"
  "stress test this report," "validate this data," "how did they get this number," "market
  size," "TAM," "benchmark," "case study results," "they're claiming," "according to
  [analyst/vendor/report]," or any evaluation of external data for decisions, content, or
  competitive intelligence. Also trigger when writing content that cites external data —
  audit before publication to protect credibility.
---

# Data Claims Auditor

> Every number has a source. Every source has a methodology. Every methodology has assumptions. This skill follows the chain back and tells you what's solid, what's shaky, and what's marketing dressed as research.

---

## Purpose

Revenue leaders operate in an ecosystem flooded with data claims: vendor case studies claiming 3x pipeline lift, analyst reports projecting $65B TAMs, competitor decks asserting market leadership, industry benchmarks establishing "best practice" thresholds. All of these claims are presented with confidence. Most deserve less confidence than they carry.

The cost of trusting a bad number:
- **Strategic decisions** built on inflated market sizing
- **Content credibility** damaged by citing a study that doesn't hold up
- **Competitive responses** based on exaggerated competitor claims
- **Investment narratives** anchored to analyst projections with weak methodology

This skill systematically audits data claims to determine how much weight they should carry in the user's decisions and content.

---

## The Audit Protocol

Work through these layers in order. Each layer is a filter — if a claim fails at an early layer, flag it immediately without completing the full audit. Not every claim needs the full protocol; match depth to stakes.

### Layer 1: Source Credibility

Who produced this number, and what are their incentives?

**Source tier classification:**

| Tier | Source Type | Default Trust | Incentive Risk |
|---|---|---|---|
| **Tier 1** | Peer-reviewed research, government statistics agencies, central bank data | High | Low — reputation-dependent, methodology transparent |
| **Tier 2** | Established analyst firms, major consultancies, reputable academic working papers | Moderate-High | Moderate — methodology usually sound but often funded by vendors; read the fine print on sponsorship |
| **Tier 3** | Industry associations, well-established trade publications, large-scale surveys with disclosed methodology | Moderate | Moderate — member/advertiser incentives may bias framing |
| **Tier 4** | Vendor-produced "research," case studies, proprietary benchmarks, startup-funded surveys | Low-Moderate | High — the producer has a financial interest in the conclusion. This is marketing, not research. Treat accordingly |
| **Tier 5** | Blog posts citing unnamed sources, social media claims, "according to experts" without attribution, press release statistics | Low | Very high — no accountability, no methodology, no verification path |

**The incentive question**: Would the source benefit financially or reputationally from this number being large (or small, or trending in a particular direction)? If yes, apply extra scrutiny to methodology.

### Layer 2: Methodology Examination

How was the number produced? This is where most claims break down.

**Questions to ask:**

- **Sample**: How large? How selected? Representative of what population? Self-selected survey respondents are not the same as randomly sampled data.
- **Definition**: How is the key term defined? "AI adoption" can mean anything from "we have a chatbot" to "AI drives core revenue decisions." Definition differences can create 10x swings in reported numbers.
- **Time window**: What period does the data cover? A carefully chosen start/end date can dramatically change a trend line.
- **Methodology disclosed?**: If the full methodology isn't published, the number can't be independently verified. Treat undisclosed methodology as a yellow flag.
- **Replication**: Has anyone else produced a similar number independently? Convergence from independent sources is the strongest signal of validity.

**Common methodology red flags:**

- "Survey of 200 decision-makers" — Self-selected? Paid panel? How were they recruited? 200 is small for generalizable claims.
- "According to our proprietary data" — Can't verify, can't replicate. Trust is entirely on the brand.
- "Market expected to grow from $X to $Y by [year]" — What's the growth model? What assumptions drive it? CAGR from what base year? TAM vs SAM vs SOM?
- "Customers saw a 3x improvement" — In what metric? Over what baseline? With what controls? Cherry-picked top performers?
- "Industry benchmark" — Benchmark of whom? What companies are in the sample? Weighted how?

### Layer 3: Statistical Validity

Apply the core statistical-reasoning lenses to the specific claim.

- **Sample size vs. claim precision**: A claim like "35% of enterprises have adopted AI agents" implies a sample large enough to estimate a population proportion within a reasonable margin. For a 95% CI of ±3%, you need ~1,000 respondents. Many industry surveys have 200-400. The margin of error is wider than the headlines suggest.
- **Effect size plausibility**: Does the claimed effect size make sense in the domain? "3x pipeline" is an extraordinary claim in B2B SaaS. Extraordinary claims require extraordinary evidence. A single case study doesn't meet that bar.
- **Base rate context**: How does this number compare to known base rates? If the industry average conversion rate is 2-3% and a vendor claims their tool drives 12%, the claim needs rigorous controls to be credible.
- **Survivorship bias check**: Are failures included in the sample? Vendor case studies almost never include customers who churned or saw no improvement. The reported average is the average of winners, not the average of all users.

### Layer 4: Contextual Fit

Even if the number is methodologically sound, does it apply to the user's context?

- **Population match**: The study measured enterprise companies with 5,000+ employees. If the user's market is mid-market (200-2,000), the number may not transfer. 
- **Time relevance**: The study was conducted in 2022. The market has shifted substantially. Is the number still applicable?
- **Geographic/industry scope**: Global averages may not reflect the specific market and region the user operates in (e.g., North American B2B SaaS).
- **Definitional alignment**: The report defines "AI adoption" as "any AI tool in use." The user may mean "AI integrated into core GTM workflows." These are different populations.

---

## Audit Output

### Quick Assessment (conversational)

For low-stakes claims or rapid evaluation:

**Pattern**: "That [number/claim] comes from [source tier]. [Key concern — methodology, sample, incentive]. I'd weight it at [high/moderate/low confidence]. [One sentence on what it's useful for vs. what it's not]."

### Full Audit (structured)

For claims driving decisions or being published in the user's content:

```
## Claim Under Audit
[Exact claim as stated, with source attribution]

## Source Assessment
- Source: [Who produced it]
- Tier: [1-5]
- Incentive risk: [Low / Moderate / High]
- Methodology disclosed: [Yes / Partially / No]

## Methodology Review
- Sample: [Size, selection method, representativeness]
- Definitions: [How key terms are defined — and whether those match the user's context]
- Time window: [Period covered]
- Key methodological concern: [The single biggest weakness]

## Statistical Validity
- Effect size plausibility: [Plausible / Stretch / Extraordinary]
- Sample adequacy: [Adequate / Marginal / Insufficient for claimed precision]
- Base rate context: [How the claim compares to known baselines]

## Contextual Fit
- Applicability to the user's context: [Direct / Partial / Low]
- Key gap: [What doesn't transfer]

## Verdict
- Trust level: [High / Moderate / Low / Do Not Cite]
- Usable for: [What this number can legitimately support]
- Not usable for: [What this number should NOT be used to claim]
- Better alternative: [If available — a more credible source for the same question]
```

### Content QA Mode

When the user is publishing content that cites a data claim:

**Pattern**: "Before we publish — that [statistic] from [source]. [Quick audit result]. [Recommendation: cite as-is / cite with caveat / replace with better source / remove]."

---

## Claim Type Playbooks

### Market Sizing Claims (TAM/SAM/SOM)

Market sizing is the most systematically inflated category of data claims in B2B. Standard playbook:

1. **Identify the methodology**: Top-down (total market × penetration assumption) or bottom-up (count of potential buyers × average deal size). Top-down is easier to inflate.
2. **Check the definition**: "AI market" and "AI agent market" and "conversational AI market" are different things reported with overlapping numbers. What's included?
3. **Compare across analysts**: If two analyst firms put very different sizes on the "same" market, the definitions differ. The gap IS the insight.
4. **Look at the CAGR**: >30% CAGR sustained over 5+ years is optimistic for any market. The base year matters enormously — a small base inflates percentage growth.
5. **SAM is what matters**: TAM is a vanity metric. SAM (Serviceable Available Market) scoped to the user's actual addressable segment is the number worth tracking.

### Vendor Case Study Claims

Vendor case studies are marketing assets, not research. Standard audit:

1. **Was there a control group?** Almost never. Without a control, you cannot attribute the result to the product.
2. **Cherry-picked customer?** Vendors select their best-performing customers for case studies. This is the top of the distribution, not the average experience.
3. **Metric definition**: "3x pipeline" — from what baseline? Over what period? Compared to what alternative?
4. **Observer effect**: Customers in case studies know they're being measured and get extra attention from the vendor's CS team. This inflates results.
5. **Default verdict**: Treat as directional signal (the product can work) not as expected outcome (this is what you'll get).

### Competitor Performance Claims

When a competitor claims market position, growth, or customer results:

1. **Verify independently**: Can the claim be corroborated by a funding database (for example Crunchbase or PitchBook), public filings, independent peer-review sites (for example G2), or third-party coverage?
2. **Metric gaming**: "Fastest growing" can mean highest percentage growth off a tiny base. "Market leader" can mean most revenue, most customers, most funding, or most employees — whichever tells the best story.
3. **Selection of timeframe**: Competitors choose the window that makes them look best. Compare across multiple timeframes when possible.
4. **The press release test**: If the claim only appears in the company's own press release and nowhere else, treat it as unverified marketing.

---

## Integration

- **statistical-reasoning**: The core framework. Data claims auditor is the specialized application of statistical-reasoning lenses to externally sourced data.
- **bayesian-updater**: Audit results feed into belief updates. A Tier 1 source with strong methodology provides high-weight evidence. A Tier 4 vendor case study provides low-weight evidence. The update magnitude should reflect the audit tier.
- **Content QA**: When the user is writing newsletters, social posts, or reports that cite external data, this skill runs QA before publication. Credibility is built on intellectual rigor — one bad citation undermines it.
- **monte-carlo**: When audited data is used as input for scenario modeling, the confidence level from the audit should inform the variance ranges in the simulation. Low-confidence inputs deserve wider uncertainty bands.
- **Source log**: Track which sources and claim types the user encounters most frequently, and which tend to hold up vs. fall apart. Over time, this builds a source reliability database.

---

*Trust but verify. Then verify the verification methodology.*

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt (Coach K). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
