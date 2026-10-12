# Review Customer Health: Toolkit

**Use this file when:**
- A renewal is 90 to 120 days out and you need a read you would defend in a forecast call.
- A champion just left, usage just dropped, or an escalation just opened.
- Your health-score tool says green and your gut says otherwise (or the reverse).
- You run a CS team and want every CSM reading accounts the same way, and checking their own accuracy.

The SKILL.md holds the logic. This file holds the instruments: signal checklist, signal judgment sheet, the override rules that replace averaging, the health read template, the prediction log, and a worked example.

---

## 1. The sequence, with time boxes

| Step (from SKILL.md) | What you actually do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1. Gather signals; name the missing ones | Pull from the checklist in Section 2. Write "not tracked" where you have nothing | Signal pack + unknowns list | 5 min |
| 2. Run the read | Rate each signal on the judgment sheet (Section 3), then apply override rules (Section 4) | Green / yellow / red with reasons | 5 min |
| 3. Confirm with whoever talked to them recently | One message to the AE, support lead, or exec who last spoke to the customer | Confirmed or revised read | 2-3 min (plus wait) |
| 4. Book the next action with the customer | Send the invite or email, not just an internal task | One customer-facing action on a calendar | 2 min |
| 5. Log the prediction | One row in the prediction log (Section 7) | Logged read with date | 1 min |

**The judge-not-average rule:** a single dead relationship signal can outweigh five healthy usage signals. A composite score hides that. Rate each signal, then let the override rules decide.

---

## 2. Signal checklist: what to pull, from where, how far back

| Category | Signal | Source system category | Lookback |
|---|---|---|---|
| **Relationship** | Champion still in role, still engaged | CRM contacts, professional social network, last email | Current |
| | Executive sponsor contact (theirs and ours) | CRM activity, calendar | 1 quarter |
| | Last meaningful two-way conversation (not a newsletter, not a ticket) | Email, call recorder, CRM | 60 days |
| | Attendance at the last business review | CRM, calendar | Last two reviews |
| | Decision-maker for the renewal identified by name | CRM, account plan | Current |
| **Usage** | Active users on the core workflow vs. licensed | Product analytics, admin console | 90 days, by month |
| | Trend direction (not level) | Product analytics | 90 days vs. prior 90 |
| | Breadth: teams or departments using it | Product analytics | 90 days |
| | Core feature adoption (the feature the value case depends on) | Product analytics | 90 days |
| **Support** | Open escalations or severity-1 tickets | Support desk | Current |
| | Ticket tone and repeat issues | Support desk, call recorder | Last 5-10 tickets or 90 days |
| | Time to resolution trend | Support desk | 90 days |
| **Commercial** | Renewal date, amount, terms (auto-renew, notice period) | Contract, billing | Current |
| | Invoice disputes or late payments | Billing | 12 months |
| | Requests for discounts, seat reductions, or contract changes | CRM, email | 6 months |
| **Business context** | Their company news: layoffs, acquisition, leadership change, new strategy | Public news, their site | 6 months |
| | Value delivered: did they hit the outcome they bought for? | Business review notes, success plan | Since last renewal |

**Write the unknowns down.** Every row you could not fill goes into the "What we do not know" section of the read. Common ones: who owns the renewal decision now, whether the original business case was met, whether a competitor is in the account.

---

## 3. Signal judgment sheet

Rate each signal you have as Healthy, Watch, or Risk. Do not add them up.

| Signal | Healthy | Watch | Risk |
|---|---|---|---|
| Champion | In role, engaged in last 30 days | In role, quiet 30-60 days | Left, changed role, or silent 60+ days |
| Executive contact | Two-way contact this quarter | Last contact one quarter ago | No contact for more than a quarter, or never since kickoff |
| Renewal decision-maker | Named and engaged | Named, not engaged | Unknown |
| Usage trend | Flat or rising on core workflow | Down modestly or flat at a low level | Down sharply, or core workflow unused |
| Usage breadth | Several teams | One team | One or two power users only |
| Support | No open escalation, tone neutral or positive | Open ticket, normal severity, or repeat issue | Open escalation, angry tone, or a stalled fix |
| Commercial | Paid on time, no change requests | Asked about pricing or terms | Discount demand, seat-reduction request, invoice dispute |
| Business context | Stable or growing | Leadership change in another function | Layoffs, acquisition, new leader in the buying function |
| Value delivered | Outcome met and acknowledged by them | Outcome partly met or never measured | Outcome missed, or they say it was missed |

**Thresholds (rule of thumb):** "modestly" and "sharply" depend on your product. Set them once from your own history: look at accounts that churned and see how far usage had fallen 120 days before renewal. Until you have that, treat a drop of a quarter or more in active users over 90 days as sharp.

---

## 4. Override rules: from signals to a read

Apply in order. The first rule that fires sets the read. Red rules come first so a yellow rule never masks a red one.

| # | If | Then the read is | Source |
|---|---|---|---|
| 1 | Open escalation the customer says is blocking, or they have said they are evaluating alternatives | Red | Judgment |
| 2 | Renewal decision-maker unknown and renewal inside 90 days | Red | Judgment |
| 3 | Risk ratings in two or more different categories | Red | Judgment |
| 4 | Champion departed and no new relationship exists yet | Yellow | SKILL.md rule |
| 5 | Usage up but executive contact dead for a quarter | Yellow | SKILL.md rule |
| 6 | Any other Risk rating, or three or more Watch ratings | Yellow | Judgment |
| 7 | No Risk ratings and no more than two Watch | Green | Judgment |

**Leaning:** when a read sits on a boundary (for example, rule 4 fires and there is also an open escalation close to blocking), write "yellow leaning red." The lean tells the forecast which way to move if nothing changes.

**Relationship beats usage.** Usage tells you whether the product is used. Relationship tells you whether anyone with authority will defend the renewal. When they disagree, the relationship signal decides the color and the usage signal decides the save play.

### Action rules by read

| Read | Required actions |
|---|---|
| Green | One customer-facing action to confirm the renewal path (decision-maker, timeline). Re-read in 30 days |
| Yellow | Fix the specific Risk or Watch signal driving the color. One customer-facing action within 2 weeks. Re-read in 2-3 weeks |
| Red, renewal more than 90 days out | Save plan with owner. Executive sponsor engaged within 2 weeks. Re-read weekly |
| Red, renewal inside 90 days | Executive sponsor this week (SKILL.md rule). Save plan with dates. Flag in forecast |

---

## 5. Red flags that the tool score is wrong

| Pattern | What it usually means |
|---|---|
| Tool says green, champion left | The score weighs usage; the renewal depends on people |
| Tool says green, one power user drives most usage | Breadth risk. If that person leaves, usage collapses |
| Tool says red, renewal decision-maker is engaged and positive | Usage is low but valued (seasonal use, executive reporting tool) |
| Health score has not moved in months | It may be stale or built on signals that do not change |
| Score green on accounts that churned last year | The score was never backtested against your own churn |
| Every account is yellow | The thresholds are not discriminating; fix them or ignore the score |

---

## 6. The health read template

```
HEALTH READ: [Account]
Prepared by: [CSM]     Date: [date]     Valid until: [date + 30 days]
Renewal: [date] ([N] days)     Amount: [$]     Terms: [auto-renew? notice period?]

READ: [GREEN | YELLOW | RED]  [leaning ___ if on a boundary]
Rule that set it: [override rule # and one line]

TWO STRONGEST RISK SIGNALS
  1. [signal]: [evidence, date, source]
  2. [signal]: [evidence, date, source]

TWO STRONGEST HEALTHY SIGNALS
  1. [signal]: [evidence, date, source]
  2. [signal]: [evidence, date, source]

WHAT WE DO NOT KNOW (and how we will find out)
  - [unknown] -> [who asks whom, by when]

CONFIRMED WITH: [name, role, date]  Change to read: [none / revised to ___ because ___]

NEXT THREE ACTIONS
  1. [customer-facing action]  Owner: [ ]  Date: [ ]  Booked: [Y/N]
  2. [action]                  Owner: [ ]  Date: [ ]
  3. [action]                  Owner: [ ]  Date: [ ]

PREDICTION LOGGED: [Y]  Predicted outcome: [renew flat / expand / contract / churn]
```

---

## 7. The prediction log

The step most teams skip, and the one that makes the next read better. One row per read.

| Account | Read date | Read | Lean | Predicted outcome | Renewal date | Actual outcome | Right? | What we missed |
|---|---|---|---|---|---|---|---|---|
| [ ] | [ ] | Y | Red | Contract | [ ] | [ ] | [ ] | [ ] |

**Review each quarter:**

| Question | What it tells you |
|---|---|
| Of accounts read green, how many churned or contracted? | Whether your green is too generous |
| Of accounts read red, how many renewed flat? | Whether your red is crying wolf, or your save plays work |
| Which signal was present in most misses? | The signal you are underweighting |
| Which reads were older than 30 days at renewal? | Whether reads are being refreshed |

---

## 8. Worked example

**Situation (illustrative):** Acme, a fictional 400-person B2B software company, sells a workflow platform. Account: a mid-size distributor. Renewal in 100 days at $180k, annual, 60-day notice period.

**Signal pack:**

| Signal | Evidence | Rating |
|---|---|---|
| Champion | Ops director who bought the product changed jobs last month (professional profile, bounced email) | Risk |
| Executive contact | No executive contact since kickoff, 11 months ago | Risk |
| Renewal decision-maker | Unknown | Risk |
| Usage trend | Steady over 90 days, 68 of 80 seats active weekly | Healthy |
| Usage breadth | Four teams use it | Healthy |
| Support | One open escalation, 3 weeks old, integration bug, customer tone frustrated | Watch (borderline Risk) |
| Commercial | Paid on time, no change requests | Healthy |
| Business context | Nothing in news | Healthy |
| Value delivered | Business case never measured after kickoff | Watch |

**Applying the override rules:**
- Rule 1: escalation is frustrating but the customer has not said it blocks them. Does not fire.
- Rule 2: decision-maker unknown, but renewal is 100 days out, not inside 90. Does not fire yet. In 10 days it will.
- Rule 3: all three Risk ratings sit in one category (Relationship); support is Watch. Does not fire, but three Relationship risks is the whole relationship.
- Rule 4: champion departed, no new relationship. Fires. Read is yellow.

**Read: yellow leaning red.** Rule 4 set yellow. The lean is red because rule 2 fires in 10 days unless the decision-maker is found, and one more Risk outside Relationship (the escalation turning blocking) fires rule 3.

**Reasoning that mattered:** an average of these signals would look fine: five healthy, two watch, three risk. The tool score said green (78/100) because it weighs usage heavily. But usage is not who signs. Nobody with authority at the customer currently has a reason to defend this renewal.

**Confirmed with:** the AE who sold the deal. Added: the departed champion had been the one pushing the escalation. Read unchanged; urgency up.

**Next three actions:**
1. CSM emails the champion's replacement and the department head to book a 30-minute review of the escalation and their goals. Customer-facing. By Friday.
2. Support lead commits a resolution date for the escalation before any renewal conversation. Within 1 week.
3. Our VP of Customer Success requests an intro to their operations VP via the AE. Within 2 weeks.

**Prediction logged:** yellow leaning red; predicted outcome: renew flat if decision-maker engaged within 30 days, otherwise contract.

---

## 9. AI assist: who does what

| Task | AI | Human |
|---|---|---|
| Summarize tickets, call notes, emails into signals | Yes | Spot-check the tone calls |
| Rate each signal against Section 3 | Draft | Confirm, especially Relationship |
| Apply override rules | Yes | Check the rule that fired is correct |
| Know internal politics, informal conversations | No | Yes. Step 3 exists for this |
| Write the read and actions | Draft | Book the customer action yourself |
| Log the prediction | Format the row | Own the log |

### Follow-up prompts after the Quick prompt

1. **Signal table:** "Before giving a color, list every signal I provided in a table: category, evidence, date, and a rating of Healthy, Watch, or Risk using these definitions [paste Section 3]. List every category I gave you nothing for as NOT TRACKED."
2. **Override check:** "Apply these override rules in order [paste Section 4]. Tell me which rule fired first and what read it sets. Do not average."
3. **Staleness:** "Which signals are older than 30 days? Which conclusions depend only on them?"
4. **Champion question:** "Is the original champion still in role and engaged? If the material does not say, mark it as the top unknown."
5. **Customer-facing action:** "Rewrite action 1 as an email I can send today to [role] asking for a specific meeting. Under 90 words. No mention of renewal risk."
6. **Prediction:** "State the most likely renewal outcome (expand, flat, contract, churn) and what would change it."

### Errors this job invites

| Error | How to spot it | Check |
|---|---|---|
| Averaging into a score | "Overall health 72/100" | Prompt 2; reject any composite |
| Usage-dominated read | Green despite a Relationship Risk | Rules 4 and 5; relationship sets color |
| Invented tone | "Customer is frustrated" with no quoted ticket text | Ask for the quote |
| Internal-only actions | All three actions are "review," "discuss," "flag" | Prompt 5 |
| Missing unknowns | No "what we do not know" section | Prompt 1 lists untracked categories |

---

## 10. Common mistakes

| Mistake | How to spot it | Fix |
|---|---|---|
| Trusting the tool score without reading signals | Read copied from the dashboard | Rate signals first, then compare to the score |
| Starting at 30 days | Red accounts discovered in the renewal month | Read at 90-120 days; re-read on any trigger |
| Not asking the champion question | Template filled, champion status blank | Make it the first field you fill |
| Actions with no customer in them | Internal meetings only | One action booked with the customer, every read |
| Never checking accuracy | No prediction log | Log every read; review quarterly |
| Treating every red as a crisis | Save plays on accounts already gone | Prioritize by amount and recoverability |

---

## 11. The 5-minute version

1. Champion still there and engaged? (1 min)
2. Executive contact this quarter? (1 min)
3. Usage trend over 90 days: up, flat, down? (1 min)
4. Any open escalation? (1 min)
5. Read: blocking escalation, or unknown decision-maker inside 90 days = red. Otherwise champion gone or no exec contact for a quarter = yellow. Book one customer meeting. (1 min)

## 12. The deep version

For the largest renewals, strategic logos, or accounts where the read is contested.

| Add | How |
|---|---|
| Stakeholder map | Every buying role at the customer: name, stance, last contact, our relationship owner |
| Value audit | The outcome they bought for, the measurement, and whether they agree it was met |
| Usage drill-down | Core workflow usage by team and by month; identify the power users and their tenure |
| Competitive check | Ask the AE and support: any mention of alternatives, any procurement requests for information |
| Commercial scenario | Renew flat, contract, churn: what each means for the forecast and what concession you would or would not make |
| Executive alignment | Our executive sponsor reads the brief and owns one action |
| Backtest your rules | Run the override rules on last year's renewals; adjust thresholds where they missed |

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
