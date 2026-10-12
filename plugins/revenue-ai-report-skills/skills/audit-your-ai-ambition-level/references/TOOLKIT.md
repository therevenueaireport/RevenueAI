# AI Ambition Audit Toolkit: Inventory, Evidence Grades, Level Tests, and the Verdict

**Use this file when:**
- You are about to run the audit and need the inventory sheet, the level tests, and the evidence grades in one place.
- Leadership calls the program "transformation" and you need a classification that survives a finance review.
- You are splitting next year's AI budget and need to know which spend is evidenced and which is hope.
- A board asks what the AI spend bought and you need the table, the split, and the gap list by Friday.

The SKILL.md holds the logic. This file holds the instruments. Run them in the order below. The three levels come from OAR (Optimize, Amplify, Reinvent), a framework from The Revenue AI Report: [therevenueaireport.com/frameworks/oar](https://www.therevenueaireport.com/frameworks/oar). OAR is meant to be applied after the outcome, metric driver, and operating constraint are known; this audit applies it backward to work already running.

---

## 1. The Audit Sequence

| Step | What you do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1 | Build the inventory of every AI initiative | Inventory sheet (Section 2) | 15-30 min, longer if nobody owns the list |
| 2 | Grade the evidence behind each result | Evidence grade A-D per initiative | 2-3 min per initiative |
| 3 | Run the four level tests on the measured result | Measured level per initiative | 2-5 min per initiative |
| 4 | Compare claimed level to measured level | Gap list | 10 min |
| 5 | Split spend by measured level | Spend table | 10 min |
| 6 | Write what the next level would require | Next-level evidence line per initiative | 15 min |
| 7 | Write the verdict and actions with owners and dates | One-page verdict (Section 6) | 20 min |
| 8 | Review with one person who did the work, then finance | Signed-off audit | 30 min |

**The order matters.** Grade the evidence before you classify. If you classify first, you will grade the evidence to fit the label.

---

## 2. Step 1: The Inventory Sheet

One row per initiative. An "initiative" is anything with AI in it that costs money or a named person's time: seats, platforms, agents, internal builds, services contracts, a pilot with a budget line.

| Field | What to write | Example entry |
|---|---|---|
| Initiative | Plain name, not the vendor name | Call summaries into CRM |
| Owner | One named person | RevOps manager |
| Function | Sales, marketing, CS, RevOps, finance, partner | Sales |
| Start date | Month it went live in production | Feb 2026 |
| Annual spend | License + services + internal build hours at loaded cost | 60,000 |
| Claimed level | What the deck, the kickoff, or the budget request said | Optimize |
| Intended change | The number it was supposed to move, with a baseline | Cut admin time per rep from 45 to 20 min/day |
| Measured result | What actually moved, with the number | 18 min/day saved per rep |
| Source of the figure | System and report name | CRM activity timestamps, Q2 vs Q4 prior |
| Business driver reached? | Did the change reach pipeline, win rate, deal size, cycle, retention, or cost line? | No. Time saved not redeployed |
| Evidence grade | A / B / C / D (Section 3) | B |

### Where to find initiatives nobody listed

| Source category | What to pull | How far back |
|---|---|---|
| Finance / accounts payable | Every software and services line with "AI" in the description or a vendor known to sell AI features | 12 months |
| Expense reports and corporate cards | Individual assistant seats bought outside procurement | 6 months |
| Identity and single-sign-on logs | Apps connected in the last year | 12 months |
| CRM and marketing automation app lists | Installed AI add-ons and connected agents | Current |
| Team chat channels | Channels or bots named after AI pilots | 6 months |
| Budget requests and board decks | Anything pitched with AI as the reason | 4 quarters |

**Rule of thumb:** if the finance pull finds more than two initiatives the revenue team did not list, stop and fix the inventory before classifying anything. An incomplete inventory makes the spend split meaningless.

---

## 3. Step 2: Evidence Grades

Grade the measured result, not the initiative.

| Grade | Label | Descriptor | Can it be classified? |
|---|---|---|---|
| **A** | System data, finance-reconciled | Figure comes from a system of record (CRM, billing, CS platform, ledger) and finance has seen and accepted it | Yes |
| **B** | System data, not reconciled | Figure comes from a system of record but nobody outside the owning team has checked it | Yes, flagged for finance review |
| **C** | Self-reported | Survey, owner estimate, vendor dashboard, or "the team says" | Provisional only. Label "provisional" |
| **D** | None or anecdote | No figure, one story, a screenshot, or a demo | No. Label "unmeasured" |

### Tests that drop a grade

| Finding | Effect |
|---|---|
| Baseline was estimated, not measured before the AI went live | Drop one grade |
| Figure comes only from the vendor's own dashboard | Cap at C |
| Time saved is reported but nobody can show where the time went | Result counts as capacity only. It cannot support Amplify or Reinvent |
| Less than one full quarter in production | Cap at C. Too early to read |
| The figure changed when you asked a second person for it | Cap at C until reconciled |
| Pipeline is counted as "AI-influenced" with no test of whether it would have happened anyway | Cap at C |

---

## 4. Step 3: The Four Level Tests

Apply in order to the **measured result**. Stop at the first "no."

| Test | Question | If yes | If no |
|---|---|---|---|
| T0. Measured? | Is the evidence grade A, B, or C? | Go to T1 | Unmeasured. Stop |
| T1. Optimize | Did a task inside the current process get cheaper, faster, or better, with the steps and owners unchanged? | At least Optimize. Go to T2 | Unmeasured or no effect. Stop |
| T2. Amplify | Did the workflow, decision quality, team boundary, or ownership change, so the economics moved because the system changed and not because one person did the same task faster? | At least Amplify. Go to T3 | Optimize. Stop |
| T3. Reinvent | Did the business start earning differently (new revenue model, pricing structure, channel, product, or operating model built from the outcome backward)? | Candidate Reinvent. Go to T4 | Amplify. Stop |
| T4. Repeated | Has the T3 change held across at least two independent instances or one full quarter? | Reinvent | Amplify (provisional) |

### Level descriptors and the evidence each needs

| Level | What it looks like in a revenue team | Evidence that proves it | Evidence that does not |
|---|---|---|---|
| **Optimize** | Faster call notes, quicker routing, better sequence copy, cheaper research | Time or cost per unit, before and after, from system data | "Reps love it," adoption rate, logins |
| **Amplify** | Forecast process redesigned around a model; CS coverage reassigned by risk score; one team now owns a step another team used to own | A changed process map plus movement in a business driver (win rate, cycle, retention, forecast error) over at least one quarter | Output volume up with the same workflow; a single good quarter |
| **Reinvent** | A new way to price, package, sell, or serve that did not exist before; a revenue line that depends on the new model | Revenue or margin that the old model could not produce, repeated, reconciled by finance | A pilot, a demo, one deal, a press release |

### Tie-breaker rules (rule of thumb)

| Situation | Classify as | Why |
|---|---|---|
| Large savings, same process | Optimize | Size does not change the level (SKILL.md decision rule) |
| More output, same people, same workflow | Optimize | Volume alone is a faster task, not a changed system |
| More output because work was restructured (roles or handoffs changed) | Amplify | The system changed |
| Changed workflow, no business driver moved yet | Optimize, with Amplify as the next-level target | The change is real; the economics are not yet shown |
| One deal, one customer, one pilot of a new model | Amplify (provisional) | One instance is not a repeatable model |
| Measured result is lower than claimed but real | The measured level. Never round up | Claimed level goes in its own column |
| Measured result is higher than claimed | The measured level | Under-claims are gaps too. Report them |

---

## 5. Steps 4-6: Gap List, Spend Split, Next-Level Requirements

### Gap types

| Gap type | Pattern | What it usually means | Action |
|---|---|---|---|
| **Inflation** | Claimed level above measured level | The pitch outran the result | Relabel. Set a measurement date for the claimed level |
| **Blind spend** | Claimed any level, measured "unmeasured" | Money is going out with no read | Owner + measurement date within 30 days, or pause at renewal |
| **Stalled capacity** | Optimize, time saved, no driver moved | Saved hours were not redeployed | Name where the hours should go and measure that |
| **Under-claim** | Measured level above claimed | Good work nobody is talking about | Promote it. It is the best case for the next budget |
| **Single instance** | Candidate Reinvent with one instance | Promising, unproven | Name the second instance and its date |

### Spend split template

| Measured level | Initiatives | Annual spend | Share of spend |
|---|---|---|---|
| Optimize | | | |
| Amplify | | | |
| Amplify (provisional) | | | |
| Reinvent | | | |
| Unmeasured | | | |
| **Total** | | | 100% |

Show the claimed split beside it. The distance between the two columns is the headline.

### Next-level evidence line

For every initiative write one sentence: "To move from [current] to [next], we need [specific number] from [system] by [date], owned by [name]."

| From | To | Typical evidence required |
|---|---|---|
| Unmeasured | Optimize | A before-and-after time or cost figure from system data, with a baseline measured before go-live |
| Optimize | Amplify | A redesigned process (who decides, who owns, what step disappears) plus one business driver moving for a full quarter |
| Amplify | Reinvent | Revenue or margin produced by a model the old business could not run, repeated across at least two instances, reconciled by finance |

---

## 6. Step 7: The Output Template (ready to fill)

```
AI AMBITION AUDIT: [Company], [Quarter]
Prepared by: [name]   Reviewed by (did the work): [name]   Finance review: [name, date]

1. VERDICT (3 sentences max)
   [Where the program actually sits, what share of spend is evidenced, the single biggest gap.]

2. CLASSIFICATION TABLE
   | Initiative | Owner | Spend | Claimed | Measured | Evidence (number + source) | Grade |
   |---|---|---|---|---|---|---|

3. SPEND SPLIT
   | Level | Claimed spend | Claimed % | Measured spend | Measured % |
   |---|---|---|---|---|

4. GAP LIST
   | Initiative | Gap type | Claimed vs measured | What would close it | Owner | Date |
   |---|---|---|---|---|---|

5. NEXT-LEVEL REQUIREMENTS
   - [Initiative]: To move from [X] to [Y], we need [number] from [system] by [date], owned by [name].

6. ACTIONS (max 5, each with owner and date)
   - [Action] | [Owner] | [Date]

7. WHAT THIS AUDIT CANNOT TELL YOU
   [Figures not reconciled, initiatives under one quarter old, anything taken on trust.]
```

---

## 7. Worked Example: Acme

*Illustrative only. Acme is a fictional 400-person B2B software company with a 60-person sales team and a 20-person CS team. All figures are invented for the example.*

### Inventory and evidence

| # | Initiative | Spend | Claimed | Measured result and source | Grade |
|---|---|---|---|---|---|
| 1 | Call summaries into CRM | 60,000 | Optimize | 18 min/rep/day saved; CRM activity timestamps, two quarters before vs after | B |
| 2 | Outbound agent | 180,000 | Reinvent | Meetings booked shown in vendor dashboard; no tie to pipeline in CRM | D for pipeline |
| 3 | Forecast assistant | 90,000 | Amplify | Commit forecast error down from 14% to 9% across three quarters; manager roll-up call removed; CRM snapshots vs closed-won, checked by finance | A |
| 4 | Marketing content drafting | 40,000 | Amplify | Published assets doubled per quarter, same headcount, same workflow; no change in content-sourced pipeline | B |
| 5 | Renewal risk scoring | 70,000 | Optimize | CSM coverage reassigned by risk tier instead of account size; at-risk cohort renewal rate up from 78% to 85% over two quarters; CS platform + billing | A |
| 6 | AI-assisted usage pricing pilot | 30,000 | Reinvent | Three deals structured on usage pricing, all in one segment, one quarter | B |
| 7 | Website chat for inbound | 45,000 | Amplify | Owner says "lead quality is up"; no figure | D |

### Level tests, with the reasoning

| # | T0 | T1 | T2 | T3 | T4 | Measured | Reasoning |
|---|---|---|---|---|---|---|---|
| 1 | Yes | Yes | No | | | Optimize | Same steps, same owners. Time saved, but nobody can show where the 18 minutes went |
| 2 | No | | | | | Unmeasured | Meetings in a vendor dashboard are not pipeline. Claim of Reinvent has no figure behind it |
| 3 | Yes | Yes | Yes | No | | Amplify | Decision process changed (roll-up call removed, model-led commit) and a driver moved for three quarters |
| 4 | Yes | Yes | No | | | Optimize | Doubled output with the same workflow is a faster task. Volume is not a system change |
| 5 | Yes | Yes | Yes | No | | Amplify | Coverage model changed (team boundary) and retention moved. Claimed Optimize: an under-claim |
| 6 | Yes | Yes | Yes | Yes | No | Amplify (provisional) | New pricing structure is a Reinvent candidate, but three deals in one segment in one quarter is one instance class |
| 7 | No | | | | | Unmeasured | No figure. "Quality is up" is not evidence |

### Spend split

| Level | Claimed spend | Claimed % | Measured spend | Measured % |
|---|---|---|---|---|
| Optimize | 130,000 | 25.2% | 100,000 | 19.4% |
| Amplify | 175,000 | 34.0% | 160,000 | 31.1% |
| Amplify (provisional) | 0 | 0% | 30,000 | 5.8% |
| Reinvent | 210,000 | 40.8% | 0 | 0% |
| Unmeasured | 0 | 0% | 225,000 | 43.7% |
| **Total** | **515,000** | **100%** | **515,000** | **100%** |

### Gap list

| Initiative | Gap type | Claimed vs measured | What would close it | Owner | Date |
|---|---|---|---|---|---|
| Outbound agent | Blind spend | Reinvent vs unmeasured | Opportunities created from agent-booked meetings, tracked by CRM source field, compared with a holdout territory | Head of sales development | 30 days |
| Website chat | Blind spend | Amplify vs unmeasured | Conversion from chat lead to qualified opportunity vs form lead, one quarter | Demand gen lead | 30 days |
| Content drafting | Inflation | Amplify vs Optimize | Show content-sourced pipeline moved, or relabel and cut spend to match | Content lead | Next quarter |
| Pricing pilot | Single instance | Reinvent vs Amplify (provisional) | Usage pricing in a second segment, with margin per deal from finance | Pricing lead | Two quarters |
| Renewal risk | Under-claim | Optimize vs Amplify | None needed. Present it as the program's best evidenced result | CS VP | Board deck |
| Call summaries | Stalled capacity | Optimize vs Optimize | Name where saved time goes (more first meetings per rep) and measure it | Sales ops | Next quarter |

### Verdict (as written for the CFO)

> Acme's AI program is an Optimize-and-Amplify program that is described as Reinvent. 41 percent of spend was pitched as Reinvent; none of it measures at that level. 44 percent of spend has no measured result, and most of that is one outbound agent. The two best results (forecast and renewal risk) are both Amplify and together cost less than the outbound agent.

**Actions:** measurement plan for the outbound agent and chat within 30 days or pause at renewal (Head of sales development, Demand gen lead); relabel content drafting as Optimize (Content lead, this week); fund a second pricing segment before calling it Reinvent (Pricing lead, two quarters).

---

## 8. Decision Table and Red Flags

| If you see | It means | Do this |
|---|---|---|
| More than a third of spend unmeasured (rule of thumb) | The program is being run on belief | Lead the verdict with it. No new initiatives until each unmeasured one has a measurement date |
| Every initiative claimed at Amplify or Reinvent | Labels were set to win budget | Classify from scratch on measured results only. Do not adjust the claims |
| Zero Optimize initiatives | Either nothing basic is evidenced, or Optimize work was relabelled | Check items 1-2 in the inventory. Most real programs start here |
| A Reinvent claim owned by the vendor's success manager | The vendor wrote the label | Re-run T3 using only your system data |
| Time-saved figures with no redeployment plan | Capacity that will quietly disappear | Treat as Optimize, and add a "where does the time go" action |
| Results only from the first month | Novelty effect | Cap at C. Re-read after a full quarter |
| Finance has never seen the figures | The audit is a draft | Do not present to the board until finance has reviewed |
| Spend per initiative unknown | Cannot split spend | Use list price times seats as a floor and say so |

### Optional cross-check: the Proof Gap

For initiatives that claim pipeline impact, the Proof Gap (a framework from The Revenue AI Report, [therevenueaireport.com/frameworks/proof-gap](https://www.therevenueaireport.com/frameworks/proof-gap)) divides AI spend by verified, incremental AI-influenced pipeline in the same quarter. The Report's thresholds: under 1.0x is defensible, 1.0x to 4.0x is a watch, above 4.0x on a rolling four-quarter basis triggers a review. Do not apply it to initiatives with under one full quarter in production.

---

## 9. AI Assist: Splitting the Work

| Task | AI assistant | Human |
|---|---|---|
| Normalize a messy initiative list into the inventory sheet | Yes | Confirm nothing was dropped |
| Grade evidence | Drafts a grade per row | Owns the final grade. Checks each source exists |
| Run the level tests | Drafts the T0-T4 path with reasoning | Challenges every Amplify and Reinvent |
| Compute the spend split | Yes | Re-add the totals by hand |
| Write the verdict | Drafts | Rewrites in your voice, removes anything a CFO would query |
| Decide actions and owners | Suggests | Decides. Owners must agree before the doc goes out |

### Follow-up prompts after the Quick prompt

1. "Before classifying, grade the evidence for each initiative A to D: A is system data reconciled by finance, B is system data not reconciled, C is self-reported or vendor dashboard, D is none. Anything graded D is unmeasured. Show the grade table first."
2. "For each initiative, run these tests in order and stop at the first no: measured, same-process improvement, changed workflow or ownership with a business driver moved, new way of earning, repeated across two instances. Show the path for each."
3. "List every place where you inferred a number I did not give you. If there are none, say so."
4. "Recompute the spend split for claimed and measured levels. Show the arithmetic and confirm both columns sum to the total."
5. "For each initiative, write one sentence: to move from the current level to the next, we need [number] from [system] by [date]. Use only systems I named."
6. "Now argue the opposite: take the two initiatives you rated highest and make the strongest case that they are one level lower."

### Errors this job invites, and how to check

| AI error | How to spot it | Fix |
|---|---|---|
| Classifies on the description, not the result | Reasoning quotes the intended change, not the measured figure | Ask "which number supports this level?" |
| Fills a missing number with a plausible one | A figure appears that is not in your input | Run follow-up prompt 3. Delete anything invented |
| Rounds unmeasured up to the claimed level | Fewer unmeasured items than you expected | Count rows with no figure in your input; compare |
| Treats volume as Amplify | "Output doubled" rated Amplify with no process change named | Ask what step, owner, or decision changed |
| Spend split does not sum | Percentages total 98 or 103 | Re-add by hand |
| Generous on vendor dashboard figures | Grade B or A on a vendor screen | Cap vendor-only figures at C |

---

## 10. Common Mistakes

| Mistake | How to spot it | Fix |
|---|---|---|
| Auditing only the initiatives the CRO remembers | Finance pull finds extra spend | Run the Section 2 source pull first |
| Grading evidence after classifying | Grades suspiciously match labels | Grade first, in a separate pass |
| Treating Optimize as failure | Owners argue for higher labels | Restate the decision rule: a cheap Optimize win beats an unmeasured ambition |
| Counting adoption as a result | "85% weekly active" in the evidence column | Adoption is an input. Ask what changed downstream |
| Ignoring under-claims | Gap list contains only inflation | Check every row where measured is above claimed |
| One audit, never repeated | Next budget cycle starts from the deck again | Re-run quarterly with the same sheet |
| Presenting before finance review | Board questions a number you cannot source | Finance signs off first, always |

---

## 11. The 5-Minute Version

For a hallway question or a pre-read with no time.

1. List initiatives and spend (from memory if you must; say so).
2. For each, answer one question: "What number moved, and which system says so?" No answer: unmeasured.
3. Of those with a number: same process faster = Optimize; changed how decisions or ownership work and a business number moved = Amplify; new way of earning, repeated = Reinvent.
4. Write one line: "[X]% of spend is unmeasured; the biggest gap is [initiative]."
5. Label the whole thing "draft, not reconciled."

## 12. The Deep Version

For board submissions, annual budget allocation, or a contract renewal over a material threshold.

| Addition | What it adds |
|---|---|
| Full finance AP and card pull (Section 2) | Complete inventory, including shadow seats |
| Loaded internal cost per initiative (build and admin hours) | True spend, not just license |
| Holdout or before-after comparison for every pipeline claim | Incrementality, not correlation |
| Second reviewer grades evidence independently, then compare | Removes owner bias |
| Proof Gap on pipeline-claiming initiatives, rolling four quarters | One finance-grade ratio per initiative |
| Interview each owner: "What would make you stop this?" | Exit criteria for every initiative |
| Repeat the audit next quarter and show movement | Turns a one-off into a management system |

---
*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
