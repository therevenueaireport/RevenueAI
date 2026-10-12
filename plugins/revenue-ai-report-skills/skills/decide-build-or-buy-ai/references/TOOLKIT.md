# Build or Buy Toolkit: Three-Year Cost Model, Belief Test, and Kill Criteria

**Use this file when:**
- A build-versus-buy decision for one AI capability carries a price above pilot size.
- A vendor renewal and an engineering estimate land in the same quarter and someone has to choose.
- Finance or the board will ask why you built, or why you paid, and you need the numbers behind it.
- The routing call from `decide-build-buy-or-connect` came back as a close contest between build and buy.

This file holds the instruments. The SKILL.md holds the logic. This skill does the **money and conviction work** on two options already on the table. It assumes connecting existing systems was checked and ruled out. If nobody has checked, run `decide-build-buy-or-connect` first. It takes about fifteen minutes and often ends the debate before a cost model is needed.

---

## 1. How this toolkit fits with decide-build-buy-or-connect

| Question | decide-build-buy-or-connect | This skill |
|---|---|---|
| Which path and which layer? | Answers it | Takes it as input |
| Is connect enough? | Tests it first | Assumes no |
| Three-year true cost, both sides | Rough first-year view | Full model with ranges |
| Opportunity cost of engineering | Notes whether time is confirmed | Names what does not ship |
| What must be true for each side to win | No | Belief test |
| What ends the decision later | Flip condition | Kill criteria with dates |

**Typical sequence:** routing call (other skill) says "buy the platform, build the intelligence layer," or "build vs buy is close." This skill then prices the two finalists, tests the beliefs, and writes the kill criteria. Copy the routing record's layer table into Section 3 below so the two records stay linked.

---

## 2. The decision sequence

| Step | What you do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1 | Define the capability as a workflow outcome | Outcome statement with a metric | 10 min |
| 2 | Gather quotes, estimates, and capacity | Input sheet | 15 min, plus waiting on engineering |
| 3 | Price buy over three years | Buy worksheet | 10 min |
| 4 | Price build over three years | Build worksheet | 15 min |
| 5 | Name the opportunity cost | What does not ship, and when | 5 min |
| 6 | Score core versus commodity | Core score | 5 min |
| 7 | Write the beliefs each side needs | Belief test | 10 min |
| 8 | Decide, record the load-bearing assumption, write kill criteria | Decision record | 10 min |

---

## 3. Step 1: The outcome statement

A feature list invites a vendor comparison. An outcome statement invites a cost-per-result comparison.

```
OUTCOME STATEMENT

Workflow served:       [e.g. reps answering pricing, security, and competitor questions]
Outcome:               [e.g. repeat questions answered without a human, with a cited source]
Metric and baseline:   [e.g. median time to answer: 4 hours today, from team chat timestamps]
Target in 6 months:    [e.g. under 10 minutes for the top 20 questions]
Revenue metric served: [Cost, revenue, margin, risk, or retention, and which one]
Layer table:           [Pasted from the decide-build-buy-or-connect record, if one exists]
```

**Rule:** if you cannot name the revenue metric served, stop. Neither side wins a decision that cannot be measured, and the spend will later fail a Proof Gap review ([the Proof Gap, a framework from The Revenue AI Report](https://www.therevenueaireport.com/frameworks/proof-gap): AI spend divided by verified AI-influenced pipeline).

---

## 4. Step 2: Inputs to collect

| Input | Source | Check before using |
|---|---|---|
| Vendor quote, all years | Vendor proposal | Includes escalators, usage tiers, overage rates, minimum term |
| Implementation fees | Vendor proposal | One-time or recurring |
| Exit terms | Contract draft | Data export format, notice period, fees on early exit |
| Build estimate | Engineering lead, in writing | Covers first working version and production hardening |
| Loaded engineer cost per week | Finance | One number used on every line |
| Engineering roadmap, next two quarters | Product or engineering plan | What the same people would otherwise ship |
| Model and hosting usage estimate | Engineering, from a prototype or comparable workflow | Stated as a monthly range |
| Admin and reviewer hours | The team that will own it | Per week, both sides |
| Security and legal review effort | Security, legal | Applies to both sides, often different sizes |

**Rule:** a build estimate written by the requester and not by engineering is a guess. Mark it "unconfirmed" and widen its range.

---

## 5. Step 3: The buy worksheet (three years)

| Line | Year 1 | Year 2 | Year 3 | Notes |
|---|---|---|---|---|
| License or platform fee | | | | Include escalators as quoted |
| Usage above included tier | | | | Use your volume, not the vendor's example |
| Implementation services | | | | Usually year 1 only |
| Internal integration work | | | | Engineer weeks x loaded cost |
| Admin and configuration hours | | | | Hours x loaded hourly cost |
| Reviewer or extra seats | | | | People who check output but do not use the core tool |
| Security and legal review | | | | Initial plus renewal reviews |
| **Subtotal** | | | | |
| Exit reserve (contingent) | | | | Overlap months, migration, export rework, retraining |

**Exit reserve rule (rule of thumb):** if you cannot price leaving, the buy side is not complete. "Exit is affordable" is a decision rule in the SKILL.md, and this line is where you prove it.

---

## 6. Step 4: The build worksheet (three years)

| Line | Year 1 | Year 2 | Year 3 | Notes |
|---|---|---|---|---|
| Initial build to production | | | | Engineer weeks x loaded cost |
| Model API usage | | | | Monthly range x 12 |
| Hosting, storage, runtime | | | | Vector store, compute, logging |
| Ongoing maintenance | | | | Fraction of an engineer, every year after launch |
| Model and provider changes | | | | Migrations, prompt rewrites, retesting |
| Evaluation set upkeep and runs | | | | Building, running, and fixing the eval set |
| Monitoring, cost ceilings, on-call | | | | Who is paged when it breaks |
| Security and legal review | | | | Often larger for build |
| Admin and content upkeep | | | | Same people work as buy, usually |
| Documentation and handover | | | | So the next owner can change it |
| **Subtotal** | | | | |
| Key-person reserve (contingent) | | | | Cost to rebuild knowledge if the builder leaves |

### Maintenance and churn prompts

| Ask engineering | Why |
|---|---|
| How many model version changes do you expect to absorb in three years, and what does each cost to retest? | Providers update models on their own schedule. Quality can move without a code change |
| What fraction of an engineer keeps this running after launch? | Maintenance is the line most often entered as zero |
| What breaks when an upstream field or API changes, and who notices? | Silent failures are a build risk |
| Who owns the eval set, and how often will it run? | An eval set built once and never run is the same as none |

---

## 7. Step 5: Opportunity cost of engineering

Opportunity cost is not a percentage. It is the specific thing that does not ship.

```
OPPORTUNITY COST

Engineers and weeks this build takes:   [e.g. 2 engineers, 10 weeks]
What they would otherwise ship:         [Named roadmap item(s)]
Delay to that item:                     [e.g. one quarter]
Value of that item, if stated:          [From the roadmap or business case; else "not stated"]
Who agreed this trade:                  [Name of the roadmap owner]
```

| If | Then |
|---|---|
| The displaced item has a stated revenue value | Add the delay cost to the build side as a line |
| It has no stated value | Write the item and delay in words. Do not invent a number |
| Nobody will name the displaced item | Capacity is not real. Treat the build estimate as unconfirmed |
| The roadmap owner has not agreed | The decision is not ready |

---

## 8. Step 6: Core versus commodity score

Score each line 0, 1, or 2. Rule of thumb: 7 to 10 is core and tilts to build, 4 to 6 is mixed and usually means buy the platform and build the layer that is yours, 0 to 3 is commodity and tilts to buy.

| Question | 0 | 1 | 2 |
|---|---|---|---|
| Does a buyer choose you partly because of this capability? | No | Indirectly | Yes, it shows up in win reasons |
| Does it depend on data only you hold? | No | Partly | Entirely |
| Would a competitor running the same vendor get the same result? | Yes | Mostly | No |
| Does your workflow differ from what vendors serve? | No | Somewhat | Substantially, no vendor fits |
| Will you change it faster than a vendor would ship changes? | No | Sometimes | Often, weekly or monthly |

**Mixed scores are the common case.** The retrieval engine is commodity. The corpus it reads is yours. That split is the buy-and-thread quadrant of [BUILD, BUY, THREAD, a framework from The Revenue AI Report](https://www.therevenueaireport.com/frameworks/build-buy-thread), applied in `decide-build-buy-or-connect`: buy the engine, build and own the corpus.

---

## 9. Step 7: The belief test

Write what you would have to believe for each side to win. Then mark each belief as evidenced, plausible, or hoped.

| For build to win, we must believe | Status | Evidence |
|---|---|---|
| The capability is core, or no vendor fits the workflow | | |
| Engineering capacity is confirmed and the displaced work can wait | | |
| Maintenance will stay at or under [N] engineer weeks per year | | |
| We will keep a named owner for three years | | |

| For buy to win, we must believe | Status | Evidence |
|---|---|---|
| The vendor's roadmap matches ours for the next two years | | |
| Exit is affordable at the priced exit reserve | | |
| Price escalators stay within the quoted cap | | |
| Our own layer (data, language, plays) stays portable | | |

| Read | Meaning |
|---|---|
| One side has all beliefs evidenced or plausible | Choose it |
| Both sides have a "hoped" belief | The decision rests on that belief. Test it before signing or staffing |
| Build's case rests on cost savings alone | Build loses. Saving money is not a build reason |

---

## 10. Decision table

| If | Then |
|---|---|
| Core score 7+ and capacity is confirmed | Build. Write kill criteria for maintenance hours and quality |
| Core score 7+ and capacity is not confirmed | Buy as a bridge with a short term, revisit when capacity is confirmed |
| Core score 0-3 | Buy, unless no vendor fits the workflow |
| Core score 4-6 | Buy the platform, build the layer that is yours, cost both parts |
| Build total is lower but rests on zero maintenance | Re-price maintenance. The comparison is not valid yet |
| Buy total is lower but exit cannot be priced | Get exit terms before signing |
| Ranges overlap heavily | Decide on core score and beliefs, not on the midpoint |
| Renewal is due before the build would be ready | Renew for the shortest term with a performance out |

---

## 11. Red flags

| Red flag | What it usually means |
|---|---|
| Build maintenance line is blank | The build total is understated by a large margin |
| Only year 1 of the quote is known | Escalators and usage tiers are hiding in years 2 and 3 |
| "Our engineers can do it in a sprint" | Prototype time quoted as production time |
| Vendor cannot describe data export | Exit is not affordable, whatever the price |
| Business case cites time saved, not a revenue metric | The spend will fail a Proof Gap review later |
| Single-number totals with no range | False precision on three-year AI pricing |
| The builder is also the only reviewer | Key-person risk is not priced |

---

## 12. Kill criteria for the decision itself

Every decision gets an expiry test. Pick two or three.

| Side chosen | Kill criterion (examples) | Checked by | When |
|---|---|---|---|
| Buy | Outcome metric has not moved toward target after two measurement cycles | Owner | Each cycle |
| Buy | Renewal price exceeds quote plus agreed cap | Finance | 90 days before renewal |
| Buy | Vendor drops or delays a roadmap item the decision relied on | Owner | Quarterly |
| Build | Maintenance exceeds [N] engineer weeks per quarter for two quarters | Engineering lead | Quarterly |
| Build | Eval pass rate falls below [N] percent for two consecutive weekly runs | Owner | Weekly |
| Build | Named owner leaves and no second person can change it within a month | Engineering lead | On departure |

---

## 13. The output: decision record template

```
BUILD OR BUY DECISION RECORD

Capability and outcome:     [Outcome statement, metric, baseline, target]
Linked routing record:      [decide-build-buy-or-connect record, or "not run"]
Date / Owner / Reviewer:    [ ] / [ ] / [ ]

Three-year cost (ranges):
  Buy:    [low] to [high]   Expected [ ]   Exit reserve [ ]
  Build:  [low] to [high]   Expected [ ]   Key-person reserve [ ]
Opportunity cost:           [Item displaced, delay, value if stated]
Core score:                 [0-10] Reading: [core / mixed / commodity]

Beliefs required:
  Build: [list, each marked evidenced / plausible / hoped]
  Buy:   [list, each marked evidenced / plausible / hoped]

Recommendation:             [Build / Buy / Buy platform and build our layer]
Load-bearing assumption:    [The one belief that, if false, reverses the call]
How we will test it:        [Test, owner, date]
Kill criteria:              [2-3, each with owner and check date]
Contract terms required:    [Term length, performance out, export, price cap] (buy only)
Unknowns:                   [Inputs not supplied]
```

---

## 14. Worked example: Acme (illustrative)

Acme is a fictional 400-person B2B software company. All figures are illustrative, and the loaded engineer cost of $4k per week and admin cost of $75 per hour are assumptions Acme's finance team supplied.

**Context.** The routing call from `decide-build-buy-or-connect` placed "answer reps' repeat questions with cited sources" as buy-and-thread: buy a retrieval engine, build and own the corpus. Connect failed because the current AI assistant seats cannot enforce a freshness filter on sources. Two finalists remain: an add-on from the enablement platform vendor (renewal due this quarter), or a GTM engineering build on a model API.

**Outcome statement.** Repeat questions on pricing exceptions, security, and competitors answered with a cited, current source. Baseline: median 4 hours to answer, from team chat timestamps. Target: under 10 minutes for the top 20 questions. Revenue metric served: sales cycle time on deals that raise security questions.

**Buy worksheet (three years).**

| Line | Total | Basis |
|---|---|---|
| Add-on fee | $193k | $60k, then 7 percent uplift in years 2 and 3, as quoted |
| Implementation services | $15k | Quoted, year 1 |
| Integration | $12k | 3 engineer weeks |
| Admin hours | $43k | 4 hours a week, 48 weeks, 3 years |
| **Subtotal** | **about $263k** | Range $240k to $310k |
| Exit reserve | $27k | Two overlap months plus 3 engineer weeks to re-point sources |

**Build worksheet (three years).**

| Line | Total | Basis |
|---|---|---|
| Initial build | $80k | 2 engineers x 10 weeks, confirmed in writing |
| Model usage | $54k | $1.5k a month midpoint from a prototype |
| Hosting and runtime | $18k | $500 a month |
| Maintenance | $132k | About a quarter of an engineer after launch |
| Model changes | $24k | Two migrations at 3 weeks each |
| Security review | $8k | 2 weeks |
| Admin hours | $43k | Same as buy |
| **Subtotal** | **about $359k** | Range $300k to $450k |
| Key-person reserve | Not priced | One engineer knows the system. Flagged |

**Opportunity cost.** The two engineers would otherwise ship the quoting-tool integration, delayed one quarter. No revenue value was stated for that item, so it is recorded in words, not as a number.

**Core score: 5 (mixed).** Buyers do not choose Acme for its internal answer engine (0). The data is entirely Acme's (2). A competitor with the same vendor gets a different result only because of the corpus (1). Acme's workflow is standard (0). Acme changes pricing and security answers monthly (2). Reading: the engine is commodity, the corpus is Acme's.

**Belief test.** Build needs maintenance at a quarter of an engineer or less: hoped, no history. Buy needs the vendor to filter out sources past their review date, not just label them: plausible, shown in a demo on vendor data, not tested on Acme's. Buy also needs corpus metadata to be exportable: evidenced, in the contract draft.

**Recommendation.** Buy the add-on and build the corpus as an Acme-owned asset (source registry, owners, review dates). The build is about $96k more expected cost, its key-person risk is unpriced, and the only "hoped" belief sits on the build side.

**Load-bearing assumption.** The vendor enforces a hard freshness filter on Acme's own documents. **Test:** before signature, backdate one pricing document past its review date and confirm it disappears from answers. Owner: enablement lead, within two weeks.

**Kill criteria.** (1) Median time to answer is not under 30 minutes after two monthly cycles. (2) Renewal price exceeds year-3 quote. (3) The freshness test fails at any quarterly recheck. **Terms required:** one-year initial term with a performance out tied to criterion 1, corpus metadata export, escalator cap at 7 percent.

---

## 15. AI assist

### Split the work

| Task | AI assistant | Human |
|---|---|---|
| Lay out both worksheets with every line | Draft | Fills every number from a named source |
| Compute totals and ranges | Compute | Checks the arithmetic on two lines by hand |
| Generate maintenance and churn questions for engineering | Draft | Gets answers from engineering in writing |
| Score core versus commodity | Propose with reasons | Decides, using real win reasons |
| Write the belief test | Draft beliefs | Marks evidenced, plausible, or hoped |
| Write kill criteria | Propose | Assigns owners and dates |

### Follow-up prompts after the Quick prompt

```text
Lay out a three-year cost table for each side using only the numbers I gave you. For every line I did not supply, write "missing" and the person who should supply it. Do not estimate vendor prices or engineering time.
```

```text
Show low, expected, and high totals for both sides. State which single line drives most of the difference between low and high on each side.
```

```text
List what we must believe for build to win and for buy to win. For each belief, tell me what evidence in my inputs supports it, or say "none given".
```

```text
Name the one assumption that, if false, reverses your recommendation. Give me a test I can run in two weeks to check it, and two kill criteria with a measurable threshold and a check date.
```

### Check the AI's output for these errors

| Error this job invites | How to spot it |
|---|---|
| Maintenance priced at zero or "minimal" | Build year 2 and year 3 lower than year 1 by almost the full build cost |
| Invented pricing | A vendor figure or escalator you did not supply |
| Escalators ignored | Year 2 and year 3 license equal to year 1 when the quote says otherwise |
| Opportunity cost as a made-up percentage | A dollar figure for displaced work with no source |
| Core claimed without evidence | "This is strategic" with no win-reason or data line behind it |
| False precision | One total to the dollar, no range |
| Savings as the build reason | Recommendation to build cites only lower cost |

---

## 16. Common mistakes and how to spot them

| Mistake | How to spot it | Fix |
|---|---|---|
| Comparing a year-1 build to a year-1 license | Only one column per side | Use the three-year worksheets |
| Skipping connect | No linked routing record | Run `decide-build-buy-or-connect` first |
| Treating the corpus as part of the vendor | Corpus cost and ownership absent from buy | Price your own layer on both sides |
| Ignoring exit | No exit reserve line | Get export terms and price overlap months |
| No kill criteria | Decision record ends at the recommendation | Add two criteria with owners and dates |
| Letting the requester size the build | Estimate not signed by engineering | Mark unconfirmed and widen the range |

---

## 17. The 5-minute version

1. Write the outcome and the revenue metric it serves.
2. Multiply the quote by three years with escalators. Add implementation.
3. Take engineering's estimate, then add a maintenance line for every year after launch. If no one will estimate maintenance, build is not ready to compare.
4. Name what the engineers would not ship.
5. Ask: is this the reason buyers choose us? If no, lean buy.
6. Write the recommendation, the one assumption it rests on, and one kill criterion with a date.

## The deep version (high-stakes or multi-year contracts)

- Get the routing record from `decide-build-buy-or-connect`, including the layer table and connect test.
- Have engineering and finance each sign their inputs. Build ranges from a working prototype, not a guess.
- Run the load-bearing assumption test before signature, on your data, not the vendor's.
- Negotiate the terms in the decision record into the contract: short initial term, performance out, export, price cap.
- Put kill criteria on the quarterly review and include the capability in the Proof Gap calculation from its first full quarter in production.

---
*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
