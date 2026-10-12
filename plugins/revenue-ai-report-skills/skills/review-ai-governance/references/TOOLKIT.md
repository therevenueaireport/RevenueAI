# Review AI Governance: Toolkit

**Use this file when:**
- AI tools are spreading across sales, marketing, and CS faster than anyone can list them.
- A customer complaint, a data scare, or a surprise invoice just made governance urgent.
- The board, a large customer's security review, or an auditor is about to ask what your AI governance looks like.
- You need a policy people will follow, not one legal will file.

The SKILL.md holds the logic. This file holds the instruments: inventory method, exposure scoring, the four-part minimum policy, a kill process, and a worked example. This is operational governance, not legal advice. Regulated industries need counsel on top of it.

---

## 1. The sequence, with time boxes

| Step (from SKILL.md) | What you actually do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1. Inventory | Run the four-source sweep in Section 2 | Tool register | 2-3 weeks elapsed, 3-4 hours of work |
| 2. Name exposures | Score every register row on data in, output out, money spent | Top three exposures | 1 hour |
| 3. Write minimum policy | Fill the four-part template in Section 5 | One-page policy | 2 hours |
| 4. Assign one owner | Name a person, not a committee, with the authority to say no | Owner line on the policy | 1 conversation |
| 5. Review quarterly | Re-run the sweep, update the register, kill something if warranted | Quarterly review note | 1-2 hours per quarter |

**The amnesty rule:** inventory before enforcement. If the first thing people hear is a ban, usage goes dark and you lose the visibility you were trying to buy.

---

## 2. Inventory: finding the tools you do not know about

No single source finds everything. Use all four and reconcile.

| Source | What to pull | How far back | Finds | Misses |
|---|---|---|---|---|
| Expense and corporate card data | Every line with an AI vendor, "AI," "assistant," "agent," "notes," "transcribe" in the merchant or memo | 12 months | Paid individual and team tools | Free tiers, tools paid by personal card and never expensed |
| Single sign-on and identity app list | All connected apps, plus "sign in with" grants on work accounts | Current | Sanctioned tools and OAuth grants | Anything used with a personal login |
| Browser extension and CRM app marketplace list | Installed extensions on managed devices; apps connected to your CRM, email, calendar | Current | Note-takers, writing assistants, enrichment add-ons with data access | Unmanaged devices |
| Amnesty survey | Three questions (below), anonymous, sent by the revenue leader, not by IT or legal | Point in time | Free tools, personal accounts, actual use cases | People who do not respond |

**Amnesty survey (three questions only):**
1. Which AI tools do you use for work, including free ones and personal accounts?
2. What do you use each one for? (One line.)
3. Are you paying for any of them yourself?

**Announcement wording that works:** "Nobody gets in trouble. We want to buy the good ones properly and make them easier to use than what you have now." Wording that kills response: "compliance," "audit," "unauthorized."

**Response-rate threshold (rule of thumb):** below half of the revenue team, the inventory is not trustworthy. Re-send from the most senior revenue leader personally.

### The tool register

One row per tool or workflow. No blank owner column.

| Field | What to record |
|---|---|
| Tool / workflow | Category and purpose (e.g., "meeting note-taker," "AI assistant, personal account") |
| Users | Team and count |
| Sanctioned? | Yes / No / Tolerated |
| Tier | Free / individual paid / business or enterprise |
| Data in | None / internal only / customer business data / personal data / regulated data |
| Output out | Internal only / customer-facing with human review / customer-facing without review / writes to a system of record |
| Money | Monthly spend, who pays, on what card |
| Data terms | Trains on your data? Retention? Data processing agreement signed? Unknown counts as "No" |
| Logs | Can you see what was sent and returned? Y/N |
| Owner | Named person. If nobody will own it, mark for shut-off |

---

## 3. Exposure scoring sheet

Score each register row on three axes. 0-3 per axis.

| Axis | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Data in** | No company data | Internal, non-sensitive | Customer business data (CRM notes, deal terms, call transcripts) | Personal or regulated data (contact PII, health, payment, NDA material) |
| **Output out** | Internal draft only, discarded | Internal use, informs decisions | Customer-facing, named human reviews before send | Customer-facing without review, or writes to CRM or billing automatically |
| **Money spent** | Free, sanctioned | Small, owned, on a company contract | Unowned spend on individual cards | Usage-priced with no cap, or agents that can loop |

**Multipliers (rule of thumb):** add 2 if data terms are unknown or the tool is a consumer tier; add 1 if there are no logs; add 1 if there is no owner.

| Total | Rating | Action |
|---|---|---|
| 0-3 | Low | Register it. No action beyond the quarterly sweep |
| 4-6 | Medium | Move to sanctioned tier or sanctioned alternative within one quarter |
| 7-9 | High | Fix within 30 days: contract terms, review step, or replace |
| 10+ | Critical | Stop the data flow now; replace with a sanctioned path the same week |

Your "three biggest exposures" are the three highest totals, grouped where several rows share the same root cause (for example, eight people pasting CRM notes into personal accounts is one exposure, not eight).

---

## 4. Decision table

| If | Then | Why |
|---|---|---|
| A tool touches customer data, any tier | It goes through review. No free-tier exception | SKILL.md rule. Free tiers are where the data terms are worst |
| Customer-facing output has no named reviewer | Assign one now, or switch the output to internal-only | Unreviewed output is the fastest route to a complaint |
| A tool has no owner after you ask twice | Shut it off | SKILL.md rule. An unowned tool is an unmanaged risk |
| People use personal accounts because the approved path is slower | Fix the approved path before enforcing anything | People route around governance that is slower than the shadow path |
| Survey shows one use case dominates (e.g., summarizing calls) | Sanction one tool for it, plus one general assistant | Two supported tools beat eight tolerated ones |
| A usage-priced agent has no spend cap | Add a monthly cap with alert before the cap and automatic pause at the cap | A retry loop can burn a quarter's budget in a weekend |
| Output has earned trust (logs show low error rate over a sustained period) | Move from review-every-item to sampled review | SKILL.md rule: reviewer until trust is earned with logs |
| You are in a regulated industry | Bring counsel in before writing the data access section | This is operational governance, not legal advice |
| The policy is more than one page | Cut it. Move detail to an appendix nobody needs to memorize | A policy people cannot recite does not change behavior |
| Spot check: people cannot name the never-items | Re-communicate; the policy has not landed | Policy does not equal behavior |

### Red flags

| Red flag | What it means |
|---|---|
| Inventory came only from the licensed-software list | You found the tools you already knew about |
| Tool register has "unknown" in data terms | Treat as the worst case until proven otherwise |
| Governance owner is a committee | Nobody can say no quickly; tools keep spreading |
| A kill switch exists but has never been tested | It is not a kill switch |
| The same exposure appears in two consecutive quarterly reviews | The owner lacks authority or time |
| Shadow spend grows after sanctioned tools launch | The sanctioned path is slower or worse than the shadow one |

---

## 5. Minimum viable policy: the one-page template

Four parts, matching the SKILL.md. Fill, cut anything that does not apply, keep to one page.

```
AI USE POLICY: [Company]       Owner: [name, title]       Version: [date]
Next review: [date, one quarter out]

1. BUYING APPROVAL
   Any AI tool or AI feature that touches company or customer data needs approval
   from [owner] before use, including free tiers and trials.
   Approval checks: business-tier contract, training on our data OFF, retention set,
   data processing agreement signed, named owner, monthly cap if usage-priced.
   Approved tools: [list]. Request a new one: [form / channel]. Answer within [5] business days.

2. DATA ACCESS
   Always fine:   [e.g., drafting internal content; summarizing public material]
   Ask first:     [e.g., anything customer-facing; anything with a compliance claim]
   Never:         [e.g., customer personal data in unapproved tools; unreleased pricing;
                   material under NDA; health or payment data]
   Approved tools only for: CRM notes, call transcripts, deal terms, contract text.

3. CUSTOMER-FACING OUTPUT REVIEW
   Any AI output a customer or prospect will see has a named human reviewer before it
   goes out, until logs show it has earned sampled review.
   Reviewer by output type: [outbound email: sending rep; proposals: deal owner; support
   replies: team lead]. Moving to sampled review requires [owner] sign-off and log evidence.

4. KILL PROCESS
   Any revenue leader can pause any AI tool or workflow immediately, without approval.
   Pause triggers: customer complaint about AI output; data sent where it should not go;
   spend cap hit; output error found in a customer-facing artifact.
   After a pause: owner reviews within [2] business days: fix, restart, or retire.
```

**Make the policy pass PROOF.** Two of the five checks in [PROOF, a framework from The Revenue AI Report](https://www.therevenueaireport.com/frameworks/proof) are governance in one line each: Owner has a name, and Failure mode is clear. Every row in the tool register should pass both before it is approved.

### Kill process detail

| Trigger | Who can pull it | First action | Within 2 business days |
|---|---|---|---|
| Customer complaint about AI output | Any leader | Pause the workflow; notify owner | Owner reviews logs, finds root cause, decides fix or retire |
| Data sent to an unapproved tool | Anyone who sees it; owner acts | Revoke access, rotate any keys | Assess what was sent; counsel if personal or regulated data |
| Spend cap hit | Automatic | Automatic pause, owner paged | Owner explains spike before restart |
| Error found in output already sent | Reviewer or leader | Pause; correct with the customer | Owner adds the case to a test set before restart |

---

**Record every kill.** When a tool is retired, log the reason with the codes from [the Reversal Ledger, a framework from The Revenue AI Report](https://www.therevenueaireport.com/frameworks/reversal-ledger): DATA, HALLUCINATION, DIAGNOSTIC, ECONOMICS, INTEGRATION, ADOPTION. Add the sunk spend. After a few quarters the log shows which kind of failure your company keeps buying.

## 6. Proportionality: what to do at your size

Do not hand a 200-person company an enterprise compliance program.

| Company size | Owner | Inventory cadence | Policy form | Logging |
|---|---|---|---|---|
| Up to ~150 | Revenue operations lead or COO | Quarterly survey + expense scan | One page | Tool-native logs where available |
| ~150-500 | Named RevOps or ops leader with CFO sponsorship | Quarterly, all four sources | One page + approved-tool list | Required for any customer-facing workflow |
| ~500-1,000 | Named owner plus security and legal partners | Quarterly, plus continuous app-list monitoring | One page + short standards appendix | Central logging and spend caps for all AI calls touching customer data |

**Size is one input; maturity is the other.** On [the L1 to L6 AI Maturity Ladder, a framework from The Revenue AI Report](https://www.therevenueaireport.com/frameworks/ai-maturity-ladder), getting shadow tools into the light is L3 work and central logging with spend caps per workflow is L4 work. Once more than a couple of AI workflows touch customers or revenue data, central logging stops being optional, whatever your headcount.

---

## 7. Worked example

**Situation (illustrative):** Acme, a fictional 400-person B2B software company. The CFO noticed AI charges on six different cards. A prospect asked in a security questionnaire how AI is governed.

**Inventory result (four-source sweep):**

| # | Tool / workflow | Users | Tier | Data in | Output out | Money | Owner |
|---|---|---|---|---|---|---|---|
| 1 | AI assistant, personal accounts | ~40 reps | Free/individual | CRM notes, deal terms | Outbound emails | Personal cards | None |
| 2 | Meeting note-taker | 22 | Individual paid | Call audio with customers | Notes into CRM | 5 cards | None |
| 3 | AI SDR pilot | Marketing | Business | Contact PII | Emails sent without review | Usage-priced, no cap | Marketing ops |
| 4 | AI writing assistant, sanctioned | Marketing | Business | Internal | Blog drafts, reviewed | Company contract | Content lead |
| 5 | Enrichment add-on in CRM | RevOps | Business | Contact data | Writes to CRM | Company contract | RevOps |

**Scoring:**

| # | Data in | Output out | Money | Multipliers | Total | Rating |
|---|---|---|---|---|---|---|
| 1 | 2 | 2 | 2 | +2 consumer tier, +1 no logs, +1 no owner | 10 | Critical |
| 2 | 3 | 3 | 2 | +2 terms unknown, +1 no owner | 11 | Critical |
| 3 | 3 | 3 | 3 | none | 9 | High |
| 4 | 1 | 1 | 1 | none | 3 | Low |
| 5 | 2 | 3 | 1 | none | 6 | Medium |

**Reasoning:** row 2 scored highest because customer call audio (which may include personal and confidential detail) is flowing into tools with unknown terms, and the output writes to the CRM. Row 1 is the widest exposure by headcount. Row 3 has an owner and a contract, but it sends to prospects with no reviewer and no spend cap, so it is one bad loop away from both a brand and a budget incident.

**Three biggest exposures:**
1. Customer data (call audio, CRM notes) flowing into tools with no data terms. Rows 1 and 2.
2. Customer-facing AI output with no named reviewer. Rows 1 and 3.
3. AI spend with no owner and no cap. Rows 1, 2, 3.

**Minimum policy decisions:**

| Part | Decision |
|---|---|
| Buying approval | RevOps lead approves; CFO sponsor. Free tiers included |
| Data access | Buy one business-tier AI assistant and one note-taker, with training off and signed data terms. Personal-account use for CRM notes stops 30 days after the approved tools are live |
| Output review | Sending rep reviews every AI-drafted email. AI SDR pilot moves to review-before-send until logs show a low error rate over a sustained period |
| Kill process | Any revenue leader can pause. AI SDR gets a monthly cap with alert and automatic pause |
| Unknown-tool method | Quarterly: expense scan, app-list pull, three-question amnesty survey |

**Owner:** RevOps lead, named on the policy, with CFO sponsorship and authority to deny purchases.

**What happened next (the part that matters):** the approved note-taker was set up to log in with one click from the work calendar. Personal-account use dropped because the approved path was faster, not because of the policy.

---

## 8. AI assist: who does what

| Task | AI | Human |
|---|---|---|
| Normalize expense lines into a tool list | Yes | Check vendor matches |
| Draft survey and announcement | Yes | Sender must be the revenue leader |
| Score exposures | Draft | Decide, especially "data in" |
| Read vendor data terms | Summarize | Verify the actual contract clause; counsel for regulated data |
| Draft the one-page policy | Yes | Cut to fit your size; name the owner |
| Decide what to shut off | No | Yes |

### Follow-up prompts after the Quick prompt

1. **Register build:** "Turn this expense export and survey output into one table: tool category, users, tier, data in, output out, monthly spend, owner. Merge duplicates. Mark any field you cannot determine as UNKNOWN, do not guess."
2. **Scoring:** "Score each row 0-3 on data in, output out, and money spent using this rubric [paste Section 3]. Show your reason for each score in one line."
3. **Root-cause grouping:** "Group the high-scoring rows by root cause. Give me the three exposures, each with the rows it covers."
4. **Proportionality check:** "We are [SIZE] people with [N] in revenue roles and no dedicated security team. Remove anything from this policy that would need more than one owner and a few hours a month to run."
5. **Behavior check:** "List the three never-items in this policy. Then write a ten-person spot-check: how to ask people whether they can recite them."
6. **Kill test:** "Write a test plan for the kill process: one tabletop scenario per trigger, who does what, and how we know it worked."

### Errors this job invites

| Error | How to spot it | Check |
|---|---|---|
| Enterprise program for a mid-size company | Committees, multi-tier risk classes, a 15-page policy | Prompt 4; one page, one owner |
| Assumed vendor terms | "This tool does not train on your data" with no contract reference | Verify on the actual agreement or admin settings |
| Legal advice dressed as operations | Statements about what a regulation requires | Mark for counsel; do not rely on it |
| Inventory limited to licensed tools | No free tiers or personal accounts in the list | Confirm all four sources were used |
| Owner = "the AI council" | No single name | Push back: one person |

---

## 9. Common mistakes

| Mistake | How to spot it | Fix |
|---|---|---|
| Leading with a ban | Survey response drops; shadow spend rises | Amnesty first, enforcement after a faster sanctioned path exists |
| Policy without an owner | Requests sit unanswered | Name one person with authority to say no |
| Approved path slower than the shadow one | Extra logins, extra clicks, personal cards still in use | Single sign-on, pre-built prompts, one-click access |
| Reviewing once a year | New tools appear in the register every quarter | Quarterly review on the calendar now |
| Treating policy as done | Nobody can name the never-items | Spot-check ten people; re-communicate |
| Free tiers exempted "because they cost nothing" | Customer data in consumer tools | No free-tier exception for customer data |

---

## 10. The 5-minute version

1. Ask finance for a list of AI-related card charges in the last 12 months. (1 min to ask)
2. Ask three managers: "Which AI tools does your team use, including free ones?" (3 min)
3. Name the single tool that touches customer data with no contract. (1 min)

Action: put that one tool behind review or replace it this month. Name an owner today.

## 11. The deep version

For a board review, a security questionnaire from a major customer, or after an incident.

| Add | How |
|---|---|
| Full four-source inventory | All sources in Section 2, reconciled into one register |
| Contract review | Data terms, retention, training opt-out, subprocessors for every tool scored 7+ |
| Central logging | Route customer-facing AI calls through one logged path; prove it by reconstructing one past output from logs |
| Spend caps | Monthly cap per workflow, alert before the cap, automatic pause at the cap, tested |
| Test sets | A small set of known-good cases per customer-facing workflow, run on every change and on a schedule |
| Tabletop | Run the kill process on one scenario per trigger with the owner and two leaders |
| Board one-pager | Register summary, top three exposures and their status, owner, next review date |

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
