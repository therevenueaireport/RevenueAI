# Competitive Win and Loss Review: Toolkit

**Use this file when:**
- You have a decision on the table (price, packaging, positioning, enablement spend) against one named competitor and need evidence, not opinion.
- Two leaders tell two different stories about why you lose, and you need a counted answer both will accept.
- You are about to fund a competitive programme and need a baseline to measure it against later.
- A previous review produced a list of ten fixes and nothing changed.

The SKILL.md holds the logic. This file holds the instruments: the data pull, the coding scheme, the scoring sheets, the template, and a worked example.

---

## 1. The Review Sequence

| Step | What you do | Output | Time (rule of thumb) |
|---|---|---|---|
| 0 | Write the decision this review will inform | One-sentence decision statement | 10 min |
| 1 | Pull every closed deal against the competitor for a fixed period | Deal table, no exclusions | 30-45 min |
| 2 | Split outcomes: won, competitive loss, no decision, lost to another rival | Outcome-coded table | 15 min |
| 3 | Code stated reasons into 6-8 themes, label each reason's source | Coded reason table | 30-45 min |
| 4 | Count, then cut by segment; look for reversals | Win rate grid with sample sizes | 20-30 min |
| 5 | Test the top themes against the shared-reason rule | Cause vs. noise read | 15 min |
| 6 | Pick one change, owner, measure, check date | Decision record | 15 min |

**The decision-first rule:** if you cannot write Step 0, stop. A review without a decision to inform becomes a report nobody acts on.

---

## 2. Data Checklist: What to Pull

| Field | Source system category | Lookback | Why it matters |
|---|---|---|---|
| Deal ID, close date, stage reached | CRM opportunity records | Two full quarters minimum; four if under 30 deals | Fixed period prevents cherry-picking |
| Outcome (won / lost / no decision / closed other) | CRM | Same | No-decision must be separable |
| Competitor present (primary, secondary) | CRM competitor field, call recorder mentions | Same | CRM field alone undercounts presence |
| Stated loss or win reason (rep) | CRM close reason and notes | Same | Hypothesis layer |
| Buyer-stated reason | Exit interviews, survey replies, buyer emails | Same | Evidence layer |
| Company size band | CRM account or enrichment data | Current | Most common reversal axis |
| Industry | CRM account | Current | Second common reversal axis |
| Entry point (inbound, outbound, partner, expansion) | CRM lead source | At deal creation | Often hides a reversal |
| Deal value band | CRM amount | At close | Enterprise vs. mid-market split |
| Stage at loss | CRM stage history | Full history | Early losses and late losses differ in cause |
| Sales cycle length | CRM created and close dates | Full history | Long cycles often signal a different buyer |
| Product or package quoted | Quote or CPQ records | At close | Needed if the decision is about packaging |
| Rep and team | CRM owner | At close | Checks whether one team drives the pattern |

**Presence check:** before counting, search call transcripts and notes for the competitor's name across all closed deals in the period. If transcript mentions exceed CRM-tagged deals by a wide margin, your competitor field is undercounting and your sample is biased toward deals where reps bothered to tag. Say so in the output.

---

## 3. Outcome Coding

| Code | Definition | Counts in competitive win rate? |
|---|---|---|
| W | Closed won, competitor was evaluated | Yes, numerator and denominator |
| L-C | Closed lost, buyer chose this competitor | Yes, denominator |
| L-O | Closed lost, buyer chose a different competitor | No. Report separately |
| ND | No decision: buyer stayed with status quo, deferred, or went dark | No. Report separately |
| L-B | Lost to build-in-house | No. Report separately |
| X | Disqualified by you before a buyer decision | No. Exclude, but count how many |

**Win rate against the competitor = W / (W + L-C).** Show the no-decision count next to it every time. A rising win rate with a rising no-decision count is not progress.

---

## 4. Reason Coding Scheme

Start with this theme list. Merge or rename to fit, but keep it at 6-8 themes. More than eight and every theme stays below the three-deal threshold.

| Theme | Includes | Common false positive |
|---|---|---|
| Price / commercial terms | List price, discount, payment terms, contract length | Often a polite cover for weak value proof |
| Product capability gap | Missing feature, integration, scale limit | Rep-stated version is often a positioning gap |
| Implementation and support | Time to value, onboarding plan, services, support model | Usually under-coded because reps do not hear it |
| Relationship and access | Champion strength, executive access, incumbent relationship | Overused by reps for any late-stage loss |
| Proof and risk | References, case evidence, security review, vendor viability | Often coded as "price" by reps |
| Process and timing | Missed a procurement window, late entry, budget cycle | Frequently a no-decision, not a competitive loss |
| Strategic fit | Platform consolidation, existing stack, buyer's standard | Real, but rarely changeable by sales |
| Other / unclear | Reason absent or too vague to code | Report the count; a high count is a finding |

### Source labels (apply to every reason)

| Label | Meaning | Weight |
|---|---|---|
| B | Buyer stated it, in an interview, survey, or written message | Evidence |
| R | Rep stated it in CRM or notes | Hypothesis |
| R+T | Rep stated it and a transcript quote supports it | Strong hypothesis |
| M | Manager or leader recalled it after the fact | Weakest. Flag it |

**Rule:** one primary theme per deal, plus up to one secondary. Count primaries for the pattern. Secondaries go in a separate column so they do not inflate a theme.

### Coding consistency check

If two people code, both code the same 8-10 deals independently first. Where they disagree on primary theme on more than two of ten (rule of thumb), rewrite the theme definitions before coding the rest.

---

## 5. Analysis Sheets

### 5a. Win rate grid (fill one row per segment cut)

| Segment | W | L-C | Win rate | n (W + L-C) | ND | Support level |
|---|---|---|---|---|---|---|
| All | | | | | | |
| Size band A | | | | | | |
| Size band B | | | | | | |
| Entry: inbound | | | | | | |
| Entry: outbound | | | | | | |
| Value band A | | | | | | |
| Value band B | | | | | | |

### 5b. Sample size support level (rule of thumb)

| n in the cell | Label | What you may say |
|---|---|---|
| Under 8 | Too small | "Sample too small to support a conclusion." Report the count only, no percentage |
| 8-14 | Directional | "Suggests." Do not change price or packaging on this alone |
| 15-29 | Usable | "Indicates." Enough for an enablement or positioning change |
| 30+ | Solid | Enough to support a pricing or packaging decision, if sources are buyer-stated |

A gap between two segments counts as a reversal (rule of thumb) when both cells are at least Directional and the win rates differ by enough that flipping two or three deals in either cell would not close the gap. Do the flip test by hand and write the result down.

### 5c. Reason count sheet

| Theme | Loss count (primary) | Of which B | Win count (primary) | Of which B | Shared? | Status |
|---|---|---|---|---|---|---|
| | | | | | | Pattern / Anecdote / Not a cause |

- **Pattern:** 3+ deals as primary.
- **Anecdote:** under 3. List it, do not act on it.
- **Not a cause:** the same theme appears 3+ times in both wins and losses. Keep digging (see Section 6).

---

## 6. Decision Table

| If you see | It probably means | Do this |
|---|---|---|
| Same theme high in wins and losses | The theme is a topic every buyer raises, not a decider | Look one level down: which sub-reason differs between wins and losses? |
| One segment wins, another loses badly | The decision lives in the losing segment | Scope the change to that segment only |
| Price is the top loss reason, rep-stated only | Hypothesis, often a cover reason | Get 5+ buyer interviews before touching price |
| Price is the top loss reason, buyer-stated, and you lose at every stage | Real commercial gap | Model a packaging change before a discount change |
| Most losses happen late (final stage) | You are a strong second choice | Look at proof, risk, and executive access |
| Most losses happen early | You are being screened out | Look at positioning, entry point, and first-call messaging |
| "Other / unclear" is the largest theme | Your loss-reason capture is broken | The one change is the capture process. Fix it first |
| No-decision count exceeds competitive losses | The competitor is not your main problem | Run a no-decision review instead; say so |
| One team or rep drives most losses | A coaching issue, not a market issue | Route to the manager, exclude from market conclusions |
| Win rate is fine, but presence is rising | They are entering more deals earlier | Watch entry point, not win rate |

### Red flags in the data

| Red flag | What it means |
|---|---|
| Every loss has a reason, all in the same week | Reasons were back-filled for the review. Treat as M source |
| No buyer-stated reasons at all | Your output is a hypothesis list. Label the whole review that way |
| Competitor field blank on most lost deals | Presence undercounted; win rate likely overstated |
| Deal count jumps when you widen the period by one quarter | Your period was cherry-picked, deliberately or not |
| Leaders disagree with the result before seeing it | Agree the method and theme list with them before you count |

---

## 7. Output Template

```
COMPETITIVE WIN AND LOSS REVIEW

Competitor:            [name]
Period:                [start date] to [end date], fixed before pulling data
Decision this informs: [e.g., "Whether to change enterprise packaging against this competitor"]
Prepared by / date:    [name, date]

1. HEADLINE (3 lines max)
   [Win rate X% (n=..). The pattern reverses in [segment]. One change: [change].]

2. OUTCOMES
   Won: [n]   Lost to competitor: [n]   Lost to other: [n]   No decision: [n]   Disqualified: [n]
   Win rate vs. competitor: [W/(W+L-C)] (n=[..])

3. WIN RATE BY SEGMENT
   [Paste grid 5a. Every percentage with n and support label.]

4. LOSS REASONS (counted, primary theme only)
   [Theme], [count] of [losses], source: [B count] buyer / [R count] rep, [Pattern/Anecdote]
   
5. WIN REASONS (counted, primary theme only)
   [Theme], [count] of [wins], source: [..], [Pattern/Anecdote]

6. REVERSALS
   [Segment] where the pattern flips, with n on both sides and flip-test result.

7. WHAT THE DATA CANNOT ANSWER
   - [e.g., Industry split: no cell above 8 deals]
   - [e.g., Buyer-side reason for 70% of losses: rep-stated only]

8. THE ONE CHANGE
   Change:       [specific, scoped to a segment if a reversal drove it]
   Owner:        [one named role or person]
   Measure:      [the number that will say it worked]
   Baseline:     [today's value, with n]
   Check date:   [date]
   Kill rule:    [what result at the check date means stop or reverse]

9. PARKED (not acted on this cycle)
   [Other findings, each one line, each with why it is parked]
```

---

## 8. Worked Example (illustrative)

**Company:** Acme, a 400-person B2B software company. **Competitor:** "Rival X." **Decision:** whether to cut enterprise list price, which the enterprise sales leader has asked for.

**Step 1-2. Pull and code outcomes.** Two quarters, every opportunity where Rival X appears in the competitor field or in a call transcript. Transcript search adds 6 deals the CRM field missed.

| Outcome | Count |
|---|---|
| W | 15 |
| L-C | 19 |
| L-O | 4 |
| ND | 12 |
| X | 3 |

Win rate vs. Rival X: 15 / 34 = 44 percent (n=34). No-decision count: 12, reported alongside.

**Step 3. Code reasons.** 9 of 19 losses have buyer-stated reasons from exit calls; 10 are rep-stated only.

**Step 4. Segment cut.**

| Segment | W | L-C | Win rate | n | Support |
|---|---|---|---|---|---|
| Under 500 employees | 11 | 8 | 58% | 19 | Usable |
| 500+ employees | 4 | 11 | 27% | 15 | Usable |
| Inbound | 9 | 7 | 56% | 16 | Usable |
| Outbound | 6 | 12 | 33% | 18 | Usable |

Flip test on size: moving three 500+ losses to wins gives 7 of 15, 47 percent, still below 58 percent. The gap survives. This is a reversal.

**Step 5. Reason counts, 500+ losses only (n=11).**

| Theme | Losses | Of which B | Wins (500+, n=4) | Status |
|---|---|---|---|---|
| Price | 5 | 1 | 3 | Not a cause (shared) |
| Implementation and support | 4 | 4 | 0 | Pattern, buyer-stated |
| Proof and risk | 2 | 1 | 0 | Anecdote |

**Reasoning.** Price appears in losses and in wins, mostly rep-stated. Enterprise buyers who chose Acme also raised price and bought anyway. Price is a topic, not the decider. Implementation appears in 4 losses, all buyer-stated, and in zero wins. Stage history shows all 4 lost in the final stage, after the buyer asked who would run onboarding. That points to a missing named implementation plan, not a price gap.

**What the data cannot answer.** Industry split (no cell above 6). Why outbound underperforms: plausibly overlaps with size, since outbound skews enterprise; cannot separate with this n.

**The one change.**

| Field | Entry |
|---|---|
| Change | Every 500+ deal with Rival X present gets a named implementation lead and a written onboarding plan before the final-stage meeting |
| Owner | Head of customer success |
| Measure | Win rate vs. Rival X in 500+ deals |
| Baseline | 27% (n=15) |
| Check date | End of the next two quarters, when n will reach about 15 new deals |
| Kill rule | If win rate is unchanged and buyer-stated implementation losses persist, revisit; if implementation stops appearing but losses continue, the next review looks at proof |
| Parked | Price cut (not supported), outbound messaging (confounded with size) |

---

## 9. AI Assist

### Split the work

| Task | AI assistant | Human |
|---|---|---|
| Normalize messy CRM exports into one table | Yes | Spot-check 10 rows |
| First-pass reason coding into themes | Yes, with your theme definitions pasted in | Review every Pattern-level theme; re-code the "Other" bucket |
| Counting and win rates by segment | Yes | Recompute the headline number by hand once |
| Flip test | Yes, ask explicitly | Confirm the logic |
| Deciding the one change | No | Yes. The AI does not know your capacity, politics, or cost |
| Labelling buyer vs. rep source | Only if the source is in the data | You know where each reason came from |

### Follow-up prompts (use after the Quick prompt)

1. "Re-code each deal's reason using only these themes and definitions: [paste Section 4 table]. Give one primary and at most one secondary theme per deal, and show the deal ID next to each coding so I can audit it."
2. "For every theme that appears in three or more losses, tell me how many wins share it. Mark any theme shared by three or more wins as 'not a cause' and suggest what sub-reason might distinguish wins from losses, quoting the deal text."
3. "Run a flip test on every segment gap: how many deals would need to change outcome to close the gap? Report the segments where the gap survives flipping three deals."
4. "List every conclusion in your analysis whose cell has fewer than 8 deals. Rewrite each as 'sample too small'."
5. "What questions does this data not answer? List them, and for each, the data I would need to collect."

### Check the AI's output for these errors

| Error this job invites | How to catch it |
|---|---|
| Percentages without sample sizes | Search the output for every "%" and confirm an n sits next to it |
| No-decision deals folded into losses | Recompute W/(W+L-C) yourself from the outcome counts |
| Narrating individual deals instead of counting | If the output quotes a single deal as "the reason," send prompt 2 again |
| Inventing a theme the data does not support | Ask for the deal IDs behind each theme count; check three |
| Treating rep-stated reasons as fact | Ask: "Which of these counts are buyer-stated?" If it cannot say, you did not give it source labels |
| Recommending many changes | Ask it to rank and return one, with the reason the others are parked |
| Confident segment claims on tiny cells | Prompt 4 |

---

## 10. Common Mistakes

| Mistake | How to spot it | Fix |
|---|---|---|
| Choosing the period after seeing the data | The period starts or ends at an odd date | Fix the period in Step 0, before the pull |
| Only including deals tagged in the competitor field | Transcript search finds more deals | Union both sources |
| Counting no-decision as a loss | Win rate looks worse than leaders expect | Separate ND and report it beside the rate |
| Twenty themes | Nothing reaches three | Collapse to 6-8 |
| Acting on rep-stated price objections | Price change proposed with no buyer interviews | Get buyer-stated evidence first |
| A list of changes with no owner | Output ends in "recommendations" | Force one change, one owner, one date |
| No baseline for the change | Next review cannot tell if it worked | Record baseline with n in the decision record |

---

## 11. Two Versions

### 5-minute version
1. Pull last two quarters of closed deals against the competitor. Count W, L-C, ND.
2. Compute win rate with n. Cut once, by size band.
3. Count the top loss reason in the weaker segment. Check whether wins share it.
4. Write: one finding, the sample size, and whether it is buyer- or rep-stated. If n is under 8 anywhere, say the review cannot support a decision yet.

### Deep version (pricing or packaging at stake)
- Extend to four quarters if fewer than 30 competitive deals.
- Run 8-12 buyer interviews split between wins and losses, by someone other than the deal's rep, using the same five questions: what triggered the search, who else was considered, what decided it, what nearly changed the decision, what the losing vendor could have done.
- Double-code reasons with two coders and reconcile.
- Run the flip test on every reversal.
- Pre-register the measure, baseline, check date, and kill rule with the executive sponsor before the change ships.
- Repeat the review on the same period length at the check date and compare like for like.

---
*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
