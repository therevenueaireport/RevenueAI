# AI SDR Evaluation Toolkit: Cost per Qualified Meeting, Vendor Questions, and Contract Terms

**Use this file when:**
- A vendor has quoted you an AI SDR or outbound automation tool and you need the real unit cost before the next call.
- An AI SDR contract is coming up for renewal and you need to decide on evidence, not the vendor's dashboard.
- Someone is comparing the vendor's monthly fee to one SDR's salary and calling it the business case.
- You need a pilot design that the vendor cannot grade for itself.

This file holds the instruments. The SKILL.md holds the logic. The unit throughout is **cost per qualified meeting held**: a meeting that happened, with someone who fits your ICP, who has a plausible problem, and who agreed to a next step, as accepted by the AE. Meetings booked and replies are activity, not economics.

---

## 1. The evaluation sequence

| Step | What you do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1 | Measure your baseline cost per qualified meeting | Baseline sheet | 20 min if the data exists |
| 2 | Build the fully loaded monthly cost of the AI SDR | Cost sheet | 15 min |
| 3 | Adjust for meeting quality and held rate | Effective cost per qualified meeting | 10 min |
| 4 | Check market burn: how fast it consumes your addressable list | Runway in months | 5 min |
| 5 | Run the five-risk review | Risk table | 10 min |
| 6 | Take the question bank into the vendor call | Answers, with red flags marked | One call |
| 7 | Mark terms to require and refuse | Negotiation sheet | 10 min |
| 8 | Design the pilot or decide | Decision record | 15 min |

---

## 2. Step 1: Your baseline

If your current cost per qualified meeting is unknown, measure it before you evaluate anyone. A vendor comparison with no baseline is the vendor's comparison.

| Data | System category | How far back |
|---|---|---|
| SDR loaded cost (salary, variable, benefits, taxes) | Finance or payroll | Last full quarter |
| Outbound tool, data, and dialer costs | Finance, vendor invoices | Last full quarter |
| Share of SDR manager time | Org chart, manager estimate | Current |
| Meetings booked and held | CRM activity or meeting objects | Last two quarters |
| Meetings accepted as qualified by AEs | CRM stage or field, AE acceptance | Last two quarters |
| Meeting-to-opportunity rate | CRM opportunity source | Last two to four quarters |
| Pipeline created from SDR meetings | CRM, by source | Last two to four quarters |

```
BASELINE SHEET (monthly)

SDR loaded cost:            [ ] x [number of SDRs] = [ ]
Tools and data:             [ ]
Manager share:              [ ]
Total monthly cost:         [ ]
Meetings held:              [ ]
AE-accepted qualified:      [ ]  ([ ]% of held)
Cost per qualified meeting: [total / qualified]
Meeting-to-opportunity:     [ ]%
Pipeline per qualified mtg: [ ]
```

**Rule:** use the same definition of "qualified" for the baseline and for the AI SDR. If the vendor's definition differs, translate theirs into yours, not the other way round.

---

## 3. Step 2: Fully loaded monthly cost

| Line | What to include | Source | Often missed? |
|---|---|---|---|
| License or platform fee | As quoted, with usage tiers | Quote | No |
| Overage and per-contact charges | At your planned volume | Quote, pricing schedule | Yes |
| Data and enrichment | Contacts and verification at planned volume | Your data tool pricing | Yes |
| Sending domains and inboxes | Secondary domains, mailboxes, renewals | Your IT or vendor | Yes |
| Deliverability monitoring and warming | Tools and hours to watch reputation | IT, RevOps | Yes |
| Human review of messaging and replies | Hours per week x loaded hourly cost | Manager estimate | Yes, the largest |
| Admin and configuration | RevOps hours, CRM integration upkeep | RevOps | Yes |
| AE time on unqualified meetings | Unqualified meetings held x AE hours x loaded cost | Step 3 | Almost always |
| Setup, amortized | One-time integration and onboarding over the term | Quote, RevOps | Sometimes |
| Incident reserve | Domain repair, list cleanup, brand recovery if something goes wrong | Your judgment, stated as a range | Always |

**Rule:** if a line is unknown, write "unknown, need [source]". Never estimate a vendor price you were not given.

---

## 4. Step 3: Quality-adjusted unit cost

Vendor dashboards report meetings booked. Your P&L pays for qualified meetings held.

```
QUALITY ADJUSTMENT

Meetings booked per month (vendor claim or pilot):  [A]
Held rate (no-shows removed):                         [B]%
Qualified rate (AE-accepted, your definition):        [C]%
Qualified meetings held = A x B x C:                  [Q]
Unqualified meetings held = A x B - Q:                [U]
AE cost of unqualified meetings = U x hours x rate:   [E]
Effective cost per qualified meeting = (total + E) / Q
```

| Comparison | Valid? |
|---|---|
| Vendor fee per booked meeting vs your cost per qualified meeting | No |
| Fully loaded cost per qualified meeting vs your baseline on the same definition | Yes |
| Pipeline per qualified meeting, AI vs human, from the same segments | Yes, and the strongest |

---

## 5. Step 4: Market burn check

AI SDRs send at volumes human teams never attempt. Your addressable market is a finite asset, not an infinite top of funnel.

```
Addressable contacts in ICP:           [N]
Planned new contacts per month:        [V]
Months to touch the whole market:      N / V
Contacts already touched in last 12m:  [ ]
```

| Months to touch the whole market (rule of thumb) | Read |
|---|---|
| Under 12 | High burn. Restrict the AI SDR to a segment you can afford to spend |
| 12 to 36 | Workable if suppression and recontact rules are enforced |
| Over 36 | Low burn risk at this volume |

---

## 6. Step 5: The five risks vendors do not volunteer

| Risk | What happens | How to test before signing |
|---|---|---|
| Deliverability contamination | Sender reputation damage spreads from outbound domains to your primary domain and affects normal company email | Ask how sending domains are isolated from your primary domain and who owns them if you leave |
| Market burn | The tool spends your addressable list on low-fit or bad-data contacts you cannot recontact for months | Run Step 4; require suppression rules and per-segment volume caps |
| Message risk | Generated messages make claims, promises, or personalization that are false or off-brand | Ask for 50 sample messages on your accounts; check each for invented facts |
| Meeting quality inflation | Booked meetings look strong while AE-accepted qualified meetings stay low | Ask for meeting-to-opportunity rates across current customers, not a case study |
| Lock-in and data ownership | Sequences, reply data, and domain history stay with the vendor at exit | Ask what you can export, in what format, and what happens to domains |

Also check: consent and opt-out handling for each region you sell into, and who is liable when the tool breaks a rule.

---

## 7. Step 6: The vendor question bank

| Area | Question | Good answer | Red flag answer |
|---|---|---|---|
| Performance | What is the average meeting-to-opportunity rate across current customers in our segment? | A number, its definition, and the sample | Only case studies, or "every customer is different" |
| Performance | How do you count a meeting: booked, held, or qualified? | Held, with a qualification field you control | Booked |
| Performance | Will you pilot on our data, measured in our CRM, with criteria set before start? | Yes, with written criteria | Pilot measured in their dashboard |
| Deliverability | What complaint rate triggers an automatic pause, and what happens next? | A specific threshold, an automatic pause, a named contact | No threshold, or "our AI manages it" |
| Deliverability | Whose domains do we send from, and who owns them at exit? | Ours, isolated from the primary domain | Theirs, shared, or unclear |
| Deliverability | What monitoring do we see, and how often? | Daily reputation and bounce data we can access | A monthly summary |
| Data | Where do contacts come from, and how are they verified? | Named verification step, bounce guarantees | Vague sources |
| Control | Can we approve messaging before it sends, and set claims it may never make? | Yes, with a blocked-claims list | Full autonomy only |
| Control | Can we cap volume per segment and suppress accounts? | Yes, by account and segment | Volume set by the vendor |
| Control | Is every message and reply logged and exportable? | Yes, in a standard format | Viewable only in their interface |
| Commercial | What performance out exists after the pilot? | Exit with notice if agreed metrics are missed | None, or only for "material breach" |
| Commercial | What happens to price at renewal? | A written cap | "Standard market adjustment" |

**Decision rule from the SKILL.md:** if the vendor cannot state complaint-rate thresholds and what happens when they are hit, do not sign.

---

## 8. Step 7: Contract terms

| Require | Refuse |
|---|---|
| Pilot of one cycle before any annual commitment | Annual term with no performance out after the pilot |
| Performance out tied to AE-accepted qualified meetings | Performance measured on booked meetings or replies |
| Automatic pause at a stated complaint threshold | "Best efforts" deliverability language |
| Domains and inboxes owned by you | Sending from vendor-owned or shared domains |
| Full export of messages, replies, and contact history | Data viewable only in the vendor interface |
| Per-segment volume caps and suppression controls you set | Vendor-controlled volume |
| Blocked-claims list and message approval rights | Fully autonomous messaging with no approval option |
| Renewal price cap in writing | Uncapped renewal or auto-renew without notice |

---

## 9. Step 8: Pilot design

| Element | Rule of thumb |
|---|---|
| Segment | One segment you can afford to spend, not your best accounts |
| Control | A comparable segment worked by humans, or held out entirely |
| Duration | Long enough for meetings to become opportunities, usually one full sales stage cycle |
| Success criteria | Written before start: cost per qualified meeting, qualified rate, pipeline per meeting |
| Kill criteria | Complaint rate over threshold, any primary-domain incident, qualified rate below a set floor |
| Measurement | Your CRM, your definitions, AE acceptance |
| Review | Weekly 50-message spot check for invented claims |

Use `set-ai-pilot-kill-criteria` to write the criteria and `review-ai-pilot` to make the go, fix, or stop call at the end.

---

## 10. Decision table

| If | Then |
|---|---|
| Baseline cost per qualified meeting is unknown | Measure it first. Do not evaluate yet |
| Vendor cannot state complaint thresholds and pause behavior | Do not sign |
| Quality-adjusted cost is at or above baseline | Do not sign on economics. Revisit only for coverage you cannot staff |
| Quality-adjusted cost is below baseline only at the vendor's claimed rates | Pilot on a limited segment before any commitment |
| Market burn is under 12 months | Cap volume to one segment or do not proceed |
| Vendor insists on an annual term with no out | Refuse. Walk if necessary |
| Pilot beat baseline on qualified meetings and pipeline, no incidents | Sign with the terms in Section 8 |
| Renewal: pipeline per meeting is falling month over month | Investigate market burn and message quality before renewing |

---

## 11. Red flags in the demo

| Red flag | What it usually means |
|---|---|
| ROI slide compares fee to one SDR's salary | The five hidden cost lines are not in the math |
| Case study metrics are meetings booked | Quality is unmeasured or unflattering |
| "Fully autonomous" offered as the main benefit | You will not control claims, volume, or timing |
| Deliverability answered with "our AI handles it" | No threshold, no pause, no accountability |
| Demo uses only the vendor's sample accounts | Message quality on your market is unknown |
| Pressure to sign before quarter end with a discount | The annual term is the product |

---

## 12. The output: evaluation record

```
AI SDR EVALUATION RECORD

Vendor / quote date:              [Vendor] / [Date]
Term and price as quoted:         [ ]
Baseline cost per qualified mtg:  [ ] (definition: [ ])

Fully loaded monthly cost:        [ ] (lines: license, overage, data, domains, deliverability,
                                   review, admin, setup, incident reserve)
Quality adjustment:               Booked [A] x held [B]% x qualified [C]% = [Q]
AE cost of unqualified meetings:  [E]
Effective cost per qualified mtg: [ ]  vs baseline [ ]
Market burn:                      [ ] months to touch the addressable market

Five risks:                       [Risk, how tested, result]
Questions asked / answers:        [With red flags marked]
Terms required:                   [List]
Terms refused:                    [List]

Decision:                         [Do not sign / Pilot / Sign / Renew / Do not renew]
Pilot design (if any):            [Segment, control, duration, success and kill criteria]
Owner and next action:            [Name/role, action, date]
Unknowns:                         [Inputs not supplied]
```

---

## 13. Worked example: Acme (illustrative)

Acme is a fictional 400-person B2B software company. All figures are illustrative and come from Acme's own inputs.

**Baseline.** Four human SDRs at $8.5k a month loaded ($34k), outbound tools and data at $3k, half of an SDR manager at $7.5k: $44.5k a month. 64 meetings held a month, 70 percent AE-accepted as qualified: 45. **Baseline: about $989 per qualified meeting.**

**Quote.** $4.5k a month, 12-month term, "40 meetings a month," planned volume 6,000 new contacts a month. No performance out.

**Fully loaded monthly cost.**

| Line | Monthly | Basis |
|---|---|---|
| License | $4,500 | Quote |
| Data and enrichment | $1,200 | Acme's data tool price for 6,000 contacts |
| Domains and inboxes | $400 | 10 domains, 30 inboxes |
| Deliverability monitoring | $300 | Monitoring and warming |
| Human review | $3,118 | 8 hours a week of SDR manager time at $90 an hour |
| Admin | $1,300 | 4 hours a week of RevOps at $75 an hour |
| Setup, amortized | $500 | $6k over 12 months |
| **Total** | **$11,318** | Incident reserve noted, not priced |

The invoice is $4.5k. The fully loaded cost is about two and a half times that.

**Quality adjustment.** Vendor's claim: 40 booked. Acme assumes an 80 percent held rate (32 held) and a 40 percent qualified rate, the midpoint of what two reference customers reported. Qualified held: 12.8. Unqualified held: about 19, at one AE hour each at $100: $1,920.

Effective cost per qualified meeting: ($11,318 + $1,920) / 12.8 = **about $1,034**, against a baseline of $989. Even at the vendor's own meeting volume, Acme pays slightly more per qualified meeting than it does today.

**Market burn.** About 30,000 addressable contacts in Acme's ICP. At 6,000 a month the tool touches the whole market in five months. High burn.

**Risks found.** Vendor sends from its own shared domains (contamination and lock-in). Complaint threshold: "managed automatically," no number. Sample messages on ten Acme accounts: two cited a funding round that did not happen.

**Decision.** Do not sign the annual term. Offer a 90-day pilot on one lower-tier segment of 5,000 contacts at no more than 1,500 a month, from Acme-owned domains, with a blocked-claims list and message approval for the first month. **Success:** cost per AE-accepted qualified meeting at least 20 percent below baseline, and pipeline per qualified meeting no worse than half the human baseline. **Kill:** any primary-domain deliverability incident, or a complaint rate above the threshold the vendor must now state in writing. If the vendor will not state a threshold, Acme walks, per the decision rule. Owner: VP Sales Development, response to vendor within a week.

**Reasoning that mattered most.** The economics were roughly even, but market burn and shared domains were the deciding facts. Deliverability damage outlives the contract, so it was weighted above price.

---

## 14. AI assist

### Split the work

| Task | AI assistant | Human |
|---|---|---|
| Build baseline and cost sheets from your numbers | Compute | Supplies every number and its source |
| Quality adjustment and market burn | Compute and show the formula | Supplies held and qualified rates from your CRM or references |
| Draft vendor questions for your situation | Draft | Asks them and records the actual answers |
| Review sample messages for invented claims | First pass, flag suspicious facts | Verifies each flagged fact against the account |
| Mark terms to require and refuse | Draft | Negotiates |

### Follow-up prompts after the Quick prompt

```text
Show the fully loaded monthly cost as a table, one line per cost, with the source of each number. Any line I did not give you a number for, write "unknown, need [source]". Do not estimate vendor pricing.
```

```text
Compute effective cost per qualified meeting at three qualified rates: [low]%, [mid]%, [high]%. Include AE time on unqualified meetings at [hours] hours and [rate] per hour. Compare each to my baseline of [baseline].
```

```text
Here are 20 sample messages the vendor generated for my accounts: [paste]. List every factual claim in each message and mark it "verifiable from public source", "from our data", or "cannot verify". Do not judge tone.
```

```text
Turn your list of risks into contract language I can send: for each, the term I require and the term I refuse.
```

### Check the AI's output for these errors

| Error this job invites | How to spot it |
|---|---|
| Fee compared to salary | The math has no human review, deliverability, or AE time lines |
| Booked meetings used as the unit | Cost per meeting computed from the vendor's claimed volume with no held or qualified rate |
| Invented benchmarks | A "typical" reply, held, or qualified rate you did not supply |
| Deliverability treated as a cost line only | No mention of primary-domain risk or exit ownership of domains |
| Vendor claims stated as fact | Performance numbers repeated without "vendor claim" attached |

---

## 15. Common mistakes and how to spot them

| Mistake | How to spot it | Fix |
|---|---|---|
| Evaluating with no baseline | The record has no baseline line | Measure your current cost first |
| Letting the vendor define "qualified" | Pilot success measured in their dashboard | Use AE acceptance in your CRM |
| Piloting on your best accounts | Pilot segment is tier 1 | Use a segment you can afford to spend |
| Ignoring market burn | No months-to-touch figure | Run Step 4 before agreeing volume |
| Weighting price over deliverability | Decision rests on the fee | Weigh domain and reputation risk heavier |
| Renewing on activity | Renewal case cites sends and replies | Renew only on qualified meetings and pipeline |

---

## 16. The 5-minute version

1. Write your current cost per AE-accepted qualified meeting. If you do not know it, stop and measure it.
2. Take the quote and add data, domains, deliverability, and at least eight review hours a week. That is your real monthly cost.
3. Divide by the vendor's meeting claim times a realistic held and qualified rate, not by booked meetings.
4. Ask one question: what complaint rate triggers an automatic pause? No number, no deal.
5. Refuse an annual term without a performance out after the pilot.

## The deep version (large contracts or renewals)

- Pull two to four quarters of baseline data and compute pipeline per qualified meeting, not just cost.
- Call two reference customers yourself and ask for held, qualified, and meeting-to-opportunity rates.
- Generate 50 sample messages on your own accounts and verify every claim.
- Run a controlled pilot with a held-out segment, your domains, and pre-written success and kill criteria.
- At renewal, compare month-over-month pipeline per qualified meeting and market burn, and renegotiate terms in Section 8 before signing again.
- Count the fully loaded cost in your Proof Gap ([the Proof Gap, a framework from The Revenue AI Report](https://www.therevenueaireport.com/frameworks/proof-gap)) from the first full quarter in production, so the renewal case is AI spend against verified AI-influenced pipeline, not meetings booked.

---
*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
