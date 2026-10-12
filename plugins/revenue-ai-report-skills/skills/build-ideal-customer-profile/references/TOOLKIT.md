# ICP Toolkit: Data Pull, Trait Scoring, Profile Template, and Worked Example

**Use this file when:**
- You are about to pull win and loss data and want to know exactly which fields, from which systems, for which period.
- You have a draft profile from an AI assistant and need to check whether each trait has earned its place.
- You need to turn the profile into a two-minute scoring rule reps will actually run.
- Sales and marketing are about to argue about the target buyer and you want the argument to happen over evidence.

The SKILL.md holds the process and the decision rules. This file holds the instruments. Run them in the order below.

---

## 1. The Sequence

| Step | What you do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1 | Define "best customer" in writing | Best-customer definition | 15 min |
| 2 | Pull the two lists from the same period | Win list (about 20), loss and stall list (about 10) | 1-2 hours |
| 3 | Fill the trait capture sheet per account | One row per account | 2-3 min per account |
| 4 | Run the trait separation table | Each trait: win share vs loss share | 30 min |
| 5 | Sort traits into inclusion, caution, disqualifier, or noise | Trait verdicts | 30 min |
| 6 | Write the one-page profile | Filled template (Section 5) | 45 min |
| 7 | Build the 5-8 check scoring rule | Scorecard (Section 6) | 30 min |
| 8 | Test against five open pipeline deals | Test log | 30 min |
| 9 | Review with one sales manager and one marketer | Signed-off profile and owned open questions | 30 min |

**The same-period rule:** wins and losses must come from the same time window and the same team. Comparing this year's wins to last year's losses measures a market shift, not a profile.

---

## 2. Step 1: Define "Best Customer" Before You Pull Anything

The skill says best means bought fast, pays full price, renews, and expands. Make that concrete before anyone builds the list, or the list becomes the biggest logos and the loudest champions.

| Criterion | How to measure | Rule-of-thumb bar for "best" |
|---|---|---|
| Bought fast | Days from first meeting to signature | Faster than your median cycle |
| Full price | Discount off list at signature | At or below your standard discount band |
| Renews | Renewal outcome at first renewal | Renewed without a rescue motion |
| Expands | Net change in contract value since first purchase | Any expansion, or seats growing |
| Low cost to serve | Support load and escalations | Not in the top quarter of support load |

**Decision rule:** an account needs at least three of the five to count as "best." A big logo that took a year, a deep discount, and constant escalations is a reference, not a pattern.

**If you have fewer than 20 accounts that qualify:** use what you have and say so in the open-questions list. Do not pad the list with "good enough" accounts. Padding makes the wins look like the average customer, which erases the signal.

---

## 3. Step 2: Data Checklist

Pull these per account. Most come from your CRM. Mark any field you could not fill as "unknown," never as a guess.

| Field | Source system (category) | How far back | Why it matters |
|---|---|---|---|
| Industry (your own categories, not a data vendor's code) | CRM account record, enrichment tool | 18-24 months of closed deals | Vendor industry codes are often too broad to separate wins |
| Employee count at time of purchase | CRM, enrichment tool | Same | Size today is not size when they bought |
| Region | CRM | Same | Shows coverage bias as much as fit |
| Buying trigger | Opportunity notes, call recorder, ask the rep | Same | Usually the strongest trait and the least recorded |
| Champion title and economic buyer title | Opportunity contact roles, call recorder | Same | Defines the buying group |
| Number of people involved | Contact roles, meeting attendee lists | Same | Signals buying-group size and complexity |
| Source (inbound, outbound, partner, referral) | CRM campaign or lead source | Same | Wins can cluster by source, not by fit |
| Cycle length | Opportunity created and closed dates | Same | Input to "best" |
| Discount | Quote or order records | Same | Input to "best" |
| Loss or stall reason (stated and actual) | Closed-lost reason field, rep interview | Same | Stated reasons are often polite fictions |
| Current tools that relate to your product | Enrichment or technographic tool, discovery notes | Current | Optional; treat as a hypothesis, detection is uneven |
| Renewal and expansion outcome | Billing or CS system | All available | Input to "best" |

**Rep interview questions for losses (5 minutes per deal):**
1. What was happening at the account that started this deal?
2. Who would have signed, and did you ever speak with them?
3. What was the last thing the buyer did before it went quiet or was lost?
4. If the closed-lost reason were not allowed to be "price" or "timing," what would it be?
5. Knowing what you know now, should we have qualified this out? At what point?

---

## 4. Steps 3-5: Trait Capture and Separation

### Trait capture sheet (one row per account)

| Account | Win/Loss | Industry | Size band | Region | Trigger | Champion role | Buyer role | # in group | Source | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Customer 01 | W | Logistics | 200-500 | NA | New revenue leader | Head of RevOps | CRO | 4 | Inbound | |

Keep categories coarse. Five size bands and six to eight industries is enough. Fine categories with 30 accounts give you groups of one.

### Trait separation table

For each candidate trait, count how often it appears in each list, then compare shares.

| Trait | Wins with trait | Win share | Losses with trait | Loss share | Gap (win share minus loss share) | Verdict |
|---|---|---|---|---|---|---|
| [trait] | [n] of 20 | [%] | [n] of 10 | [%] | [points] | Include / Caution / Disqualify / Noise |

### Verdict rules (rule of thumb, adjust with more data)

| Pattern | Verdict | Goes where |
|---|---|---|
| Trait appears in wins more than losses and the gap is large (about 30 points or more) | Include | Inclusion rule |
| Trait appears in wins more than losses but the gap is small, or rests on fewer than 5 accounts | Caution (positive) | "Signals to look for," not a must-have |
| Trait appears in losses much more than wins, and no won deal had it | Disqualify | Disqualifier list |
| Trait appears in losses much more than wins, but at least one won deal had it | Caution flag | Per the SKILL.md rule: demote, do not disqualify |
| Trait appears at similar rates in both | Noise | Leave it out, even if everyone believes it |
| Trait could not be filled for most accounts | Unknown | Open-questions list |

**The SKILL.md rule restated as a check:** a trait enters the profile only if its win share beats its loss share. A trait that is common in wins and equally common in losses describes your customer base, not your best customers.

### Two segments, not one

If the separation table shows two groups that each win well but share few traits (for example, mid-size firms in one industry and smaller firms in another), stop and build two short profiles with separate scorecards. Signs you have two segments:

| Signal | Meaning |
|---|---|
| Wins split into two clusters on size or industry with few accounts between | Two segments |
| Different triggers dominate in each cluster | Two segments with different entry points |
| Different champion roles in each cluster | Two segments that need different outreach |
| One cluster wins slightly more but the other is larger | Keep both. Score separately. Do not force one profile |

---

## 5. The One-Page Profile Template

```
IDEAL CUSTOMER PROFILE: [Segment name]
Version: [1.0]   Date: [YYYY-MM-DD]   Owner: [name/role]   Next review: [date, 1-2 quarters out]
Data basis: [n] wins and [n] losses/stalls from [period], [team or region]
Best-customer definition used: [3 of 5 criteria from Section 2]

1. FIRMOGRAPHICS (what the data shows)
   Size:       [band]                       Evidence: [x of 20 wins vs y of 10 losses]
   Industry:   [list]                       Evidence:
   Region:     [list or "no pattern"]       Evidence:
   Other:      [e.g., runs a CRM with a dedicated admin]  Evidence:

2. BUYING TRIGGER (what starts the deal)
   Primary:    [event, e.g., new revenue leader in seat under 6 months]   Evidence:
   Secondary:  [event]                                                     Evidence:
   How a rep spots it: [where the signal shows up before first contact]

3. BUYING GROUP
   Champion:          [role]
   Economic buyer:    [role]
   Typical group size:[range]
   Roles that appear in losses but not wins: [e.g., procurement-led with no exec sponsor]

4. WIN CONDITIONS (what is true in deals we win)
   - [condition] Evidence:
   - [condition] Evidence:

5. WHY DEALS DIE (top two, actual not stated)
   - [reason] Evidence:
   - [reason] Evidence:

6. DISQUALIFIERS (walk away early; none of these appeared in a win)
   - [disqualifier] Check at: [stage]
   - [disqualifier] Check at:

7. CAUTION FLAGS (appeared mostly in losses, but at least one win had it)
   - [flag] What to do if present: [e.g., require exec sponsor meeting before proposal]

8. INFERRED, NOT SHOWN (the AI's or our hypotheses, kept separate)
   - [inference] How we would test it:

9. OPEN QUESTIONS (owner and due date on each)
   - [question] Owner: [ ] Due: [ ]
```

---

## 6. The Two-Minute Scoring Rule

Five to eight yes/no checks. Each check must be answerable from the account record, a quick search, or the first call. If a rep needs a data analyst to answer it, cut it.

### Scorecard template

| # | Check | Type | Yes = | Where the rep finds it |
|---|---|---|---|---|
| 1 | [Size in band] | Inclusion | +1 | Account record |
| 2 | [Industry in list] | Inclusion | +1 | Account record |
| 3 | [Trigger present] | Inclusion | +2 | News, social profile changes, first call |
| 4 | [Champion role reachable] | Inclusion | +1 | Contact search |
| 5 | [Caution flag] | Caution | -1 | First call |
| 6 | [Disqualifier] | Disqualifier | Stop | First call |

**Weighting rule:** give the trigger double weight only if the separation table shows it is the strongest trait. Do not weight by opinion.

### Thresholds (rule of thumb, recalibrate after one quarter)

| Score | Action |
|---|---|
| Any disqualifier | Do not pursue. Log the reason so the disqualifier can be audited later |
| Top third of possible score | Pursue now. Full outreach and senior rep time |
| Middle third | Pursue if capacity allows, or nurture until a trigger appears |
| Bottom third | Do not prioritize. Marketing nurture only |

---

## 7. Step 8: The Five-Deal Pipeline Test

Run the scorecard on five open deals before adoption: pick two the team believes are strong, two they believe are weak, and one nobody is sure about.

| Deal | Team's gut call | Scorecard result | Match? | If no, what explains it |
|---|---|---|---|---|
| Deal A | Strong | | | |

**Reading the test:**

| Result | Meaning | Action |
|---|---|---|
| Scorecard agrees on 4-5 of 5 | Profile is usable | Adopt, review in one quarter |
| Scorecard disagrees on strong deals | A check is too strict, or the team is attached to accounts outside the profile | Inspect the specific check. Do not loosen the profile just to match gut calls |
| Scorecard rates a weak deal as strong | A missing trait, often the trigger or the buyer role | Add the check if the separation table supports it |
| Reps cannot answer a check without help | Check is too hard | Replace with an observable proxy or cut it |

Then run the safety check from the SKILL.md: score your 20 wins with the final scorecard. Any win that would have hit a disqualifier means that disqualifier becomes a caution flag.

---

## 8. Red Flags and What Each Means

| Red flag | What it usually means | What to do |
|---|---|---|
| The profile reads like your marketing website | The AI used general market wisdom, not your lists | Ask it to cite the account rows behind each trait |
| Every trait has 100 percent of wins | The win list was cherry-picked, or the trait is a tautology ("has budget") | Rebuild the list against the best-customer definition |
| No disqualifiers, only inclusion rules | The team does not want to walk away from anything | Push for at least two, tested against past wins |
| The top trait is "inbound" | Source, not fit. Your outbound may never have reached good accounts | Report source separately. Do not make it a profile trait |
| Losses are all "price" or "timing" | Closed-lost reasons are polite fictions | Run the rep interview questions in Section 3 |
| One region dominates wins | Coverage bias. That is where your reps are | Note it as an open question, not a trait |
| Profile is identical to last year's | Either the market is stable or nobody re-pulled the data | Check the period on the data basis line |
| Sales and marketing each bring a different profile | Each is describing its own data: marketing's leads, sales' wins | Use closed-won and closed-lost only as the shared source |

---

## 9. Worked Example: Acme

*Fictional and illustrative. All numbers below are made up for the example.*

**Company:** Acme, a 400-person B2B software company selling a revenue forecasting product. Win rates vary sharply by region and nobody can explain why. Marketing targets "mid-market tech." Sales says the best deals are "anyone with a new CRO."

**Step 1, best-customer definition:** at least three of: closed faster than the 75-day median, discount at or below 15 percent, renewed without rescue, expanded seats. 22 customers qualified from the last 18 months; the team used the 20 with the most complete records.

**Step 2, losses and stalls:** 10 deals from the same 18 months, reached at least the demo stage, then lost or stalled over 60 days.

**Step 4, separation table (excerpt):**

| Trait | Wins | Win share | Losses | Loss share | Gap | Verdict |
|---|---|---|---|---|---|---|
| 200-1,500 employees | 16 of 20 | 80% | 4 of 10 | 40% | 40 | Include |
| SaaS or logistics | 13 of 20 | 65% | 3 of 10 | 30% | 35 | Include |
| New revenue leader under 6 months | 12 of 20 | 60% | 2 of 10 | 20% | 40 | Include, double weight |
| Missed forecast last two quarters | 8 of 20 | 40% | 2 of 10 | 20% | 20 | Caution (positive): signal to look for |
| Dedicated RevOps person on staff | 17 of 20 | 85% | 5 of 10 | 50% | 35 | Include |
| Inbound source | 11 of 20 | 55% | 5 of 10 | 50% | 5 | Noise |
| 5,000+ employees | 0 of 20 | 0% | 5 of 10 | 50% | -50 | Candidate disqualifier |
| Procurement ran the evaluation | 1 of 20 | 5% | 6 of 10 | 60% | -55 | Caution flag (one win had it) |
| No exec sponsor met by demo stage | 0 of 20 | 0% | 7 of 10 | 70% | -70 | Disqualifier |

**Reasoning the team recorded:**
- "Inbound" felt important to marketing but appears at the same rate in losses. It stays out of the profile and goes in the source report.
- "Procurement ran the evaluation" looked like a disqualifier, but one of the 20 wins had it. Per the decision rule it becomes a caution flag: when present, require a meeting with the economic buyer before proposal.
- 5,000+ employees: no wins, but the team has only made a few attempts at that size. It is a disqualifier for this version and an open question for the next.
- The region gap that started the project disappeared once size was controlled for: the weaker region simply had more large enterprises in its patch.

**Profile (condensed):**

```
ICP: Mid-size revenue teams with new leadership
Data basis: 20 wins, 10 losses/stalls, last 18 months, all regions
Firmographics: 200-1,500 employees; SaaS or logistics; dedicated RevOps person
Trigger: new revenue leader in seat under 6 months (primary); missed forecast (secondary)
Buying group: champion is head of RevOps; economic buyer is CRO; 3-5 people
Win conditions: exec sponsor met before demo; RevOps owns the evaluation
Why deals die: no exec sponsor; procurement-led evaluation with no business owner
Disqualifiers: no exec sponsor reachable by demo stage; 5,000+ employees (this version)
Caution flags: procurement running the evaluation -> require economic buyer meeting before proposal
Inferred, not shown: forecast tool already in place lowers win odds (only 3 data points)
Open questions: do wins hold at 1,500-5,000? (Owner: RevOps lead, next quarter)
               Is the logistics pattern real or one champion's network? (Owner: PMM)
```

**Scorecard:** size in band (+1), SaaS or logistics (+1), new revenue leader under 6 months (+2), dedicated RevOps (+1), missed forecast signal (+1), procurement-led (-1), no exec sponsor by demo (stop). Max 6. Pursue now at 4+, nurture at 2-3, deprioritize at 0-1.

**Five-deal test:** the scorecard matched the team's gut on four of five. The miss was a 3,000-person account sales loved. It scored 2 because size was out of band. The team kept the profile and logged the account as a live test of the open 1,500-5,000 question rather than bending the rule.

**Safety check:** all 20 wins scored 3 or higher, and none hit a disqualifier.

---

## 10. AI Assist

### Split the work

| Task | AI assistant | Human |
|---|---|---|
| Define "best customer" | Suggest criteria | Decide and write it down |
| Pull the lists | Clean and normalize categories | Choose which accounts qualify; run rep interviews |
| Separation table | Count, compute shares and gaps | Check counts against the sheet |
| Verdicts | Propose verdicts using Section 4 rules | Override where they know the context (coverage bias, one-off deals) |
| Write the profile | Draft from the template | Edit, cut anything not traced to evidence |
| Scorecard | Propose checks | Confirm a rep can answer each in two minutes |
| Pipeline test | Score the five deals | Judge the mismatches |

### Follow-up prompts to use after the Quick prompt

1. "For every trait in the profile, list the exact customer and deal rows that support it, with counts for wins and for losses. Remove any trait you cannot support from the rows."
2. "Build a table of every trait you considered, with win share, loss share, and the gap. Mark any trait that rests on fewer than 5 accounts."
3. "Check each disqualifier against the win list. If any won account had that trait, name it and convert the disqualifier to a caution flag."
4. "Do the wins look like one group or two? If two, write a short profile and scorecard for each."
5. "Turn the profile into 5 to 8 yes/no checks a rep can answer from the account record or the first call. For each check, say where the rep finds the answer."
6. "Score these five open deals with the scorecard and explain each score: [paste deals]."
7. "List what you inferred rather than read from the data, and how I could test each inference."

### Errors this job invites, and how to catch them

| AI error | How to spot it | Fix |
|---|---|---|
| Generic traits that are not in your data ("values innovation," "growth-minded") | Trait has no row count | Prompt 1 |
| Miscounting shares | Counts do not match your capture sheet | Recount by hand on the top three traits |
| Treating size or industry as causal when it is a proxy for the trigger | Trait and trigger always co-occur | Ask which trait explains wins when the other is absent |
| Overconfident language on thin data | No sample sizes anywhere in the draft | Require "[n] of [N]" next to every claim |
| Disqualifiers that would have killed real wins | Fails the safety check | Prompt 3 |
| Merging two segments into a vague average | Size band is very wide, industry list is long | Prompt 4 |

---

## 11. Common Mistakes

| Mistake | How to spot it | Fix |
|---|---|---|
| Best customers = biggest logos | Win list is mostly your largest contracts | Apply the Section 2 definition |
| Losses from a different period | Dates do not overlap | Re-pull from the same window |
| Too many traits | Profile runs past one page | Keep only traits with a large gap |
| No disqualifiers | Profile only says who to chase | Require at least two, safety-checked |
| Scorecard nobody uses | Reps cannot answer checks quickly | Run the five-deal test with a rep, not an analyst |
| Treating the profile as permanent | No review date on the page | Set a review one to two quarters out |
| Profile never changes behavior | Territories, outreach, and lead routing ignore it | Name one decision the profile will change before you publish it |

---

## 12. The 5-Minute Version

For when you need a first answer today.

1. List the 10 customers your best manager would clone tomorrow, and 5 deals that died after a demo.
2. Paste both into the Quick prompt.
3. Run follow-up prompt 1 and delete any trait without row support.
4. Run follow-up prompt 3 on the disqualifiers.
5. Write three lines: who to pursue, what starts the deal, who to walk away from. Mark it "draft" with today's date.

## 13. The Deep Version

For a new segment launch, territory redesign, or when the profile will set quota.

| Addition | What it adds |
|---|---|
| Expand to the last 200 closed opportunities, won and lost | Enough data to check win rate by score band, not just averages |
| Win rate by score band | A profile can separate averages and still be useless in the middle. Win rate should rise band by band |
| Add retention and expansion data from your CS system | Tests "stay and expand," not just "buy" |
| Technographic signals (treated as hypotheses) | What they already run can predict what they buy next. Detection is uneven, so never assert absence to a buyer |
| Separate profiles per segment with their own scorecards | Avoids the vague average |
| Push score and tier to the account record with contributing signals visible | Reps can explain the score on a call |
| Redraw territories or set quota by tier | The step where the profile starts to cost someone something, so it needs the revenue leader's sign-off |
| Quarterly recalibration: predicted vs actual conversion by tier | Stops the profile turning into folklore |

**Name the ambition level before you automate it.** Scoring accounts with AI inside today's territories is an Optimize change; redrawing territories, quota, and routing around the score is an Amplify change, with higher readiness demands and a named executive owner ([OAR, a framework from The Revenue AI Report](https://www.therevenueaireport.com/frameworks/oar)). Say which one you are doing so the result is judged against the right bar.

---
*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
