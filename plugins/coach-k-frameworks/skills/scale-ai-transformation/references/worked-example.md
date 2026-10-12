# SCALE Worked Example: Acme Software

> A full five-week run of **SCALE by Jonathan Kvarfordt (Coach K)**. Acme is fictional and every number is illustrative. Back to [SKILL.md](../SKILL.md).

**Starting point:** Acme Software (mid-market B2B, 60 AEs) has an AI budget, three unconnected pilots that started from vendor demos, and a board asking what AI has returned. The CRO's first question: "Which AI deal coach should we buy?"

---

## Week 1. S: Set strategic outcomes

| Field | Answer |
|---|---|
| Outcome | Grow new ARR from $30M to $36M this fiscal year |
| Owner | CRO |
| Drivers | Qualified opps 1,200/yr · Avg deal $125K · Win rate 20% · Cycle 110 days |
| Lever | Win rate (largest gap to Acme's own best year; controllable by sales leadership) |
| Target | Win rate 20% to 24% on new-business deals by the end of Q3 |
| Surface metric parked | "More pipeline": opp volume is near plan; adding more at a 20% win rate adds cost |

**Gate passed:** delta, date, owner. Signed by CRO.

The three existing pilots were checked against this charter. One (an AI deal coach) touched win rate. Two (an outbound email tool and a slide generator) did not and were paused.

---

## Week 2. C: Chart friction and foundation

Mapped with six AEs, two managers, and RevOps, using Find-Move-Close on the new-business process.

### Human friction

| Step | Friction | Cost | Root cause (five whys, short) | Gap type |
|---|---|---|---|---|
| Discovery | Business problem not documented on most opps | To measure | No standard; managers do not inspect it | Skills and systems |
| Deal review | Managers spend reviews collecting facts, not coaching | About 3 hours a week per manager | CRM fields empty; facts live in reps' heads | Systems |
| Business case | Skipped on most deals | Lost deals cite "no decision" | Template is a 12-tab spreadsheet nobody uses | Strategy and systems |
| CRM entry | Reps update after the week ends | About 30 min a day per rep | Manual entry; no capture from calls | Systems |

### Data foundation

| Source | Completeness | Accuracy | Accessibility | Timeliness | Red flags |
|---|---|---|---|---|---|
| CRM opportunity fields | 1 | 2 | 3 | 1 | Manual entry |
| Call recordings | 3 | 3 | 1 | 3 | Siloed in the recorder, not linked to CRM |
| Win/loss reasons | 1 | 1 | 3 | 2 | Free text, conflicting picklist |

**Top three friction points:** deal review without facts; skipped business cases; call data siloed from CRM.

**Gate passed:** each bottleneck costed or marked to measure; each source rated. The step felt like going backwards. It changed the plan: the deal coach the CRO wanted depends on CRM fields that were mostly empty.

---

## Week 3. A: Align capabilities and readiness

| Friction point | Capability | OAR | Data ready? | Process ready? | People ready? | First | Sourcing |
|---|---|---|---|---|---|---|---|
| Call data siloed from CRM | Summarize calls and write fields to CRM | Optimize | Yes (recordings complete) | Needs field definitions | Yes | Define 6 discovery fields | Connect: recorder already owned; turn on CRM sync |
| Deal review without facts | Pre-read per deal from CRM and call data | Amplify | Not until fields fill | Needs new review format | Managers need training | Field capture running for 4 weeks | Buy: deal coach, shortlist of 2 |
| Skipped business cases | Draft business case from discovery fields | Amplify | Not until fields fill | Needs a one-page template | AEs need practice | One-page template | Build: GRACE prompt in the existing assistant |

Sequencing decision: connect call capture first, because the other two depend on its data.

**Gate passed:** capability matched to data readiness; sourcing decided. Both shortlisted deal coaches were gated with the Five Tests; one scored at pilot level, one was passed.

---

## Week 4. L: Launch with control

| Control | Setting |
|---|---|
| Use case | AI deal-review pre-read plus AI-drafted business case on new-business deals over $100K |
| Champions | 2 managers and their 12 AEs |
| Control group | The other managers' teams, same segment |
| Time box | One quarter |
| Success criteria | Win rate on piloted deals vs control · Discovery fields complete on most piloted opps · Business case attached before proposal on most piloted deals · Manager review time spent coaching, by manager self-report and observed sample |
| Kill criteria | AE use of the pre-read stalls after week 4 · Any customer data sent outside approved systems · Business cases contain invented figures in spot checks |
| Guardrails | AI drafts, AE owns and edits every business case; no AI output goes to a buyer unreviewed |
| Owner | Sales operations lead |
| Decider | CRO |
| Graduation date | Last business day of Q3, fixed today |

**Gate passed:** controls written and signed by the CRO before day one.

---

## Week 5 onward. E: Evolve and expand

At the graduation date (illustrative result):

| Criterion | Baseline | Pilot | Control | Met? |
|---|---|---|---|---|
| Win rate, deals over $100K | 19% | 24% | 20% | Yes |
| Discovery fields complete | Low | Most opps | Low | Yes |
| Business case before proposal | Rare | Most deals | Rare | Yes |
| Kill criteria triggered | | None | | |

**Decision: Scale.** Wave 1: four more managers next quarter, each with a champion AE from the pilot. Wave 2: the remaining teams the quarter after.

**Buy-in story:** what we did (connected call data, then pre-reads and business cases), why (win rate was the lever; deals stalled after proposal), outcome (pilot win rate above control).

**Governance:** sales operations lead owns the deal-review stack; no team buys a separate deal coach or call recorder; quarterly review. Next friction point (win/loss data quality) re-enters at C.

---

## What SCALE changed at Acme

| Before | After |
|---|---|
| Three pilots chosen from demos | One pilot chosen from the outcome |
| "Which deal coach should we buy?" asked in week 0 | Answered in week 3, after the data foundation was fixed |
| Two tools that moved nothing the board cared about | Paused in week 1 |
| No baseline | A control group and a fixed graduation date |

---

*SCALE by Jonathan Kvarfordt (Coach K). Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*
