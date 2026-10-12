# CRM Readiness Toolkit: Requirement Inventory, Data Audit, Write-Risk Ladder, and the Connect Decision

**Use this file when:**
- An AI tool is about to be connected to your CRM and someone needs to sign off that the data can carry it.
- An AI tool is producing wrong output and you need to know whether the data or the tool is at fault.
- You do not know your fill rates and need a one-week audit plan you can start Monday.
- A vendor's default setting lets the tool write to records and you need a policy before it goes live.

The SKILL.md holds the process and the decision rules. This file holds the instruments.

---

## 1. The Sequence

| Step | What you do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1 | Build the requirement inventory: every field the tool reads and writes | Inventory table | 1-2 hours with the vendor's documentation and a test account |
| 2 | Scope the records the tool will touch | Record scope definition | 30 min |
| 3 | Measure fill rates on those fields, in that scope | Fill-rate table | 1-3 hours |
| 4 | Spot-check accuracy on the fields that matter most | Accuracy sample | 2-3 hours |
| 5 | Check duplicates, freshness, and consistency | Hygiene table | 1-2 hours |
| 6 | Classify write access on the risk ladder | Write policy | 30 min |
| 7 | Give each requirement a verdict | Readiness table | 1 hour |
| 8 | Estimate cleanup in weeks with an owner | Cleanup list | 1 hour |
| 9 | Decide: connect now, connect after cleanup, or narrow | Recommendation | 30 min with the sponsor |

If you cannot complete Step 3 this week, the first deliverable is the one-week audit plan in Section 9 (SKILL.md Quick prompt rule).

---

## 2. Step 1: Requirement Inventory

List exactly what the tool reads and writes (SKILL.md Step 1). Ask the vendor for the field list and verify it in a sandbox or test account; marketing pages are not a field list.

| # | Feature | Object | Field | Read / Write | Required or optional for the feature | Vendor default | Notes |
|---|---|---|---|---|---|---|---|
| R1 | [e.g., outreach drafting] | Account | Industry | Read | Required | | |
| R2 | | Contact | Title | Read | Required | | |
| W1 | [e.g., activity logging] | Activity | Notes, type, date | Write | Required | Writes to live record | |

**Questions to ask the vendor:**
1. Which objects and fields does each feature read? Which does it write, create, or update?
2. Does it overwrite existing values, append, or write only to empty fields?
3. Can writes go to a staging field or a review queue instead of the live field?
4. Is every write logged with before value, after value, time, and the triggering source? Can we export the log?
5. Can we restrict it to a saved list or segment of records?
6. What does the feature do when a required field is empty: skip, guess, or fail visibly?
7. How do we roll back a batch of writes?

Question 6 matters most. A tool that guesses when data is missing produces confident output from empty fields.

---

## 3. Steps 2-3: Record Scope and Fill Rates

### Define the scope first

Measure fill rates only on the records the tool will touch. A field can be 40 percent filled across all accounts and 85 percent filled across the active accounts the tool will actually use, or the reverse.

| Scope question | Example answer |
|---|---|
| Which object? | Accounts |
| Which records? | Owned accounts in the mid-market segment with activity in the last 12 months |
| How many records? | [n] |

### Fill-rate table

| Field | Records in scope | Records filled | Fill rate | Filled with a placeholder ("N/A," "unknown," "-", default picklist value) | Real fill rate |
|---|---|---|---|---|---|

**Real fill rate** excludes placeholders and default values. Default picklist values are the most common hidden gap: a field that defaults to the first option looks 100 percent filled.

### How to measure (any CRM)

| Method | Use when |
|---|---|
| A CRM report grouped by "field is blank / not blank" on the scoped records | Quick, no export needed |
| Export the scoped records to CSV and count blanks and placeholders per column | Need placeholder detection |
| A query in your data warehouse, if the CRM syncs there | Many fields or objects |

Example warehouse query pattern (adapt field and table names):

```sql
SELECT
  COUNT(*) AS records_in_scope,
  SUM(CASE WHEN industry IS NOT NULL AND TRIM(industry) NOT IN ('', 'N/A', 'Unknown', '-') THEN 1 ELSE 0 END) AS industry_real_filled
FROM accounts
WHERE segment = 'Mid-Market' AND last_activity_date >= CURRENT_DATE - INTERVAL '12 months';
```

---

## 4. Step 4: Accuracy Spot-Check

Fill rates do not capture wrong-but-filled data (SKILL.md limitation). Check the fields the tool's most visible output depends on.

| Step | How |
|---|---|
| Pick fields | The 3-5 fields that, if wrong, would embarrass you in front of a buyer or corrupt a forecast |
| Sample | 20-30 random records from the scope (rule of thumb). Random, not the accounts you know well |
| Check against source | Company website or filing for firmographics; the call recording or email thread for deal fields; the contact's current professional profile for titles |
| Record | Correct / wrong / outdated / cannot verify, per field per record |

| Field | Sampled | Correct | Wrong | Outdated | Cannot verify | Accuracy |
|---|---|---|---|---|---|---|

**Accuracy rule of thumb:** for fields that appear in buyer-facing output, treat below about 90 percent accurate as not ready, even if fill rate passes. For internal-only fields, below about 80 percent needs a caution label on the feature.

---

## 5. Step 5: Hygiene Checks

| Check | How to measure | Rule-of-thumb concern level | Why it matters for AI |
|---|---|---|---|
| Duplicate accounts | Match on normalized domain, then normalized name | Above about 5 percent in scope | Tool splits history, double-contacts buyers, merges context wrongly |
| Duplicate contacts | Match on email | Above about 5 percent | Duplicate outreach to the same person |
| Stale records | Last modified or last verified date | Key fields not updated in 12+ months | Tool acts on people who left and companies that changed |
| Inconsistent picklists | Count distinct values on free-text fields that should be picklists | Many spellings of the same value | Tool cannot group or filter reliably |
| Orphaned records | Contacts without accounts, opportunities without contacts | Any meaningful volume | Missing context for the tool |
| Notes quality | Read 20 random activity notes | Mostly empty, "called," or copy-paste | Summaries and drafts built on nothing |
| Ownership | Records with inactive or missing owners | Any | Writes nobody will review |

---

## 6. Step 6: The Write-Risk Ladder

Write access is the highest risk (SKILL.md quality check). The tool never writes to records without a human-reviewable log, whatever the vendor defaults say (SKILL.md decision rule).

| Level | What the tool may do | Risk | Requirements before allowing |
|---|---|---|---|
| 0. Read only | Read fields, produce output for a human | Low | Scope restriction |
| 1. Suggest | Propose values shown to a human, nothing written | Low | Same |
| 2. Write to staging | Writes to a separate staging field or review queue; human confirms into the live field | Medium | Staging fields exist; confirm and correct are one click each |
| 3. Write new records or activities | Creates activities, tasks, or notes; does not overwrite existing values | Medium-high | Write log with source; source stamp on every record; rollback tested |
| 4. Update existing fields | Overwrites live values | High | Everything in level 3, plus before/after values in the log, write only to fields with a named owner, weekly sample audit |
| 5. Autonomous actions | Sends, enrolls, or changes stage without a human | Highest | Everything in level 4, plus volume and spend ceilings, a tested off switch a human can press without a vendor ticket, restriction to a saved record list |

**Rule of thumb:** start one level lower than the vendor proposes. Move up only after a clean audit of a few weeks of logs at the current level. This is the sequencing idea in [SLING, a framework from The Revenue AI Report](https://www.therevenueaireport.com/frameworks/sling): set the foundation, layer the change in, and ground-truth every number before the next step.

---

## 7. Step 7: Readiness Verdict per Requirement

| Condition | Verdict |
|---|---|
| Real fill rate 60 percent or above, accuracy passes, no hygiene blocker | Ready |
| Real fill rate 60 percent or above, accuracy or hygiene issue | Ready with caution: fix named issue or limit the feature |
| Real fill rate under 60 percent | Not ready: the feature waits or narrows (SKILL.md rule) |
| Fill rate unknown | Unknown: audit first |
| Write requirement without a reviewable log | Not ready, regardless of data quality |

### Readiness table template

| Req | Field(s) | Real fill | Accuracy | Hygiene issues | Verdict | What the feature can do today |
|---|---|---|---|---|---|---|

---

## 8. Steps 8-9: Cleanup List and the Decision

### Cleanup effort guide (rule of thumb, varies widely by volume and tooling)

| Cleanup type | Typical effort | Who usually owns |
|---|---|---|
| Merge duplicates in a scoped set | Days to about two weeks | RevOps |
| Fill firmographic fields through enrichment | One to four weeks, including review of matches | RevOps |
| Convert free text to picklists and map values | One to two weeks | RevOps |
| Require fields at stage change going forward | Days to configure; weeks to see effect | RevOps plus sales leadership |
| Fix notes and activity habits | Ongoing; months | Sales managers |
| Create staging fields and a write log | Days to two weeks | GTM engineering or CRM admin |

### Cleanup list template

| Item | Blocks which requirement | Effort (weeks) | Owner | Done when |
|---|---|---|---|---|

**If nobody owns data quality, name an owner before the tool connects** (SKILL.md rule). The owner is a person, not a team.

### The decision

| Pattern across requirements | Recommendation |
|---|---|
| All required fields ready, write policy in place | Connect now |
| Core requirements blocked, cleanup under about a quarter | Connect after cleanup, with a date |
| Some features ready, others blocked | Narrow: turn on only the ready features, add others as fields pass |
| Core requirements blocked, cleanup longer than about a quarter or no owner | Wait. Revisit the tool choice; the data is the project |
| Tool cannot run without writing and has no reviewable log | Do not connect until the log exists |

The recommendation is exactly one of connect, wait, or narrow (SKILL.md quality check). "Connect after cleanup" is "wait" with a date.

---

## 9. The One-Week Audit Plan (When You Do Not Know Your Fill Rates)

| Day | Task | Owner | Output |
|---|---|---|---|
| Monday | Get the field list from the vendor; build the requirement inventory | RevOps | Inventory |
| Tuesday | Define scope; run fill-rate reports, including placeholder detection | RevOps | Fill-rate table |
| Wednesday | Accuracy spot-check on 3-5 key fields, 20-30 records | RevOps plus one rep | Accuracy table |
| Thursday | Duplicates, staleness, picklists, notes sample | RevOps | Hygiene table |
| Friday | Verdicts, cleanup list, recommendation; 30-minute review with sponsor | RevOps lead and sponsor | Readiness report |

---

## 10. Red Flags

| Red flag | What it usually means | What to do |
|---|---|---|
| "Our data is pretty good" with no numbers | Nobody has measured | Run the one-week audit |
| Vendor says the tool "cleans data as it goes" | Writes to live records by default | Check the write level; require a log |
| Fill rate near 100 percent on a field nobody fills | Default value or required-field junk | Check real fill rate |
| Tool output names wrong titles or companies | Stale contacts | Staleness check; restrict to recently verified records |
| AI summaries are vague | Notes are empty | Do not blame the model first; check notes quality |
| No one can say who owns a field | No ownership | Name an owner before connecting |
| Pilot runs on a hand-picked clean segment | Readiness overstated | Measure the scope it will run on in production |

---

## 11. Worked Example: Acme

*Fictional and illustrative. All numbers are made up for the example.*

**Company:** Acme, a 400-person B2B software company. Sales leadership wants an AI tool that drafts outreach from account and contact fields and logs activities back to the CRM. The vendor's default is to write activities and update contact titles it finds.

**Step 1, inventory:**

| Req | Feature | Field | R/W |
|---|---|---|---|
| R1 | Drafting | Account industry | Read |
| R2 | Drafting | Account employee count | Read |
| R3 | Drafting | Contact title | Read |
| R4 | Drafting | Last-touch notes | Read |
| W1 | Logging | New activity records | Write |
| W2 | Enrichment | Contact title | Update existing |

**Step 2, scope:** mid-market accounts owned by active reps with activity in the last 12 months: 3,100 accounts, 14,000 contacts.

**Steps 3-5, data reality:**

| Field | Real fill | Accuracy (25 sampled) | Hygiene |
|---|---|---|---|
| Industry | 88% | 23 of 25 correct | 41 spellings across free-text values |
| Employee count | 34% | 21 of 25 | |
| Contact title | 91% | 19 of 25 (5 outdated, 1 wrong) | Many not updated in 12+ months |
| Last-touch notes | 70% filled | Mostly "called" or "left voicemail" on read of 20 | |
| Duplicates | | | 12% duplicate accounts by domain |

**Reasoning:**
- Industry passes fill and accuracy, but free-text spellings mean the tool cannot group reliably. Caution: map to a picklist (one week).
- Employee count is under 60 percent: personalization by company size waits (SKILL.md rule).
- Contact title is well filled but 76 percent accurate, too low for buyer-facing output. Drafts should not reference title-specific claims until titles are re-verified.
- Notes are filled but empty in substance. Drafts should not cite "last conversation" content.
- 12 percent duplicates means double outreach. Must merge before connect.
- W2 (update existing titles) is level 4 on the ladder with no before/after log offered by default. Not allowed.

**Readiness table:**

| Req | Verdict | Today |
|---|---|---|
| R1 Industry | Ready with caution | Use after picklist mapping |
| R2 Employee count | Not ready | Off until 60 percent real fill |
| R3 Contact title | Ready with caution | Use for routing, not for claims in copy |
| R4 Notes | Not ready in substance | Off |
| W1 Activities | Ready at level 3 with log | Allowed with source stamp and log |
| W2 Title updates | Not ready | Move to level 2: suggest into a staging field |

**Cleanup list:** merge duplicates (one week, RevOps lead); picklist mapping for industry (one week, RevOps lead); enrichment of employee count to 60 percent (about four weeks, RevOps analyst); staging field for suggested titles (one week, CRM admin).

**Recommendation: narrow.** Connect after the duplicate merge (about one week) with drafting on industry and website fields only, activity logging at level 3 with a log, title updates as suggestions only. Revisit employee-count personalization when real fill reaches 60 percent. Data quality owner: RevOps lead.

---

## 12. AI Assist

### Split the work

| Task | AI assistant | Human |
|---|---|---|
| Requirement inventory | Extract fields from vendor documentation | Verify in a test account |
| Fill rates | Count blanks and placeholders in an export; write report or query logic | Run the reports; confirm scope |
| Accuracy | Compare sampled values with source text you provide | Pick the sample; judge "cannot verify" |
| Hygiene | Find duplicate clusters and picklist variants in an export | Approve merges |
| Verdicts and plan | Draft the readiness table and cleanup list | Set owners and dates; make the decision |

### Follow-up prompts to use after the Quick prompt

1. "From this vendor documentation, list every object and field each feature reads, writes, creates, or updates. Mark anything the documentation does not state clearly as 'unconfirmed'."
2. "In this CSV export of [n] records, count for each column: blanks, placeholder values ('N/A', 'unknown', '-', '0'), and the most common value with its share. Flag any column where one value covers most records."
3. "Group these free-text industry values into a clean picklist of no more than [n] options and show the mapping."
4. "Find likely duplicate accounts using normalized domain and name. Show each cluster and which record looks most complete."
5. "Classify each write requirement on this ladder: read only, suggest, write to staging, write new records, update existing, autonomous. State what log and rollback each needs."
6. "Give a verdict per requirement using these rules: under 60 percent real fill is not ready; writes without a reviewable log are not ready. Then recommend exactly one of connect, wait, or narrow."

### Errors this job invites, and how to catch them

| AI error | How to spot it | Fix |
|---|---|---|
| Estimated fill rates presented as measured | No record counts | Require counts and the scope for every rate |
| Counting placeholders as filled | Suspiciously high fill on neglected fields | Prompt 2 |
| Accepting vendor claims about writes | Write level not stated | Prompt 5; verify in a test account |
| Recommending "connect with monitoring" | Not one of the three options | Prompt 6 |
| Treating accuracy as fine because fill is high | No accuracy column | Run the spot-check yourself |

---

## 13. Common Mistakes

| Mistake | How to spot it | Fix |
|---|---|---|
| Measuring the whole database instead of the tool's scope | Fill rates do not match what the tool sees | Scope first |
| Trusting the vendor's default write settings | Tool updates live fields on day one | Start one level lower on the ladder |
| One-time readiness check | Last audit predates the current tool | Recheck before each new tool (SKILL.md limitation) |
| Blaming the model for data problems | Output wrong in the same way the data is wrong | Trace three bad outputs back to their source fields |
| Cleanup with no owner | Cleanup list has team names, not people | Name one person per item |

---

## 14. The 5-Minute Version

1. Write down the five fields the tool most depends on.
2. Run one CRM report showing blank vs filled for each, on active records only.
3. Open ten random records and check the most visible field against a real source.
4. Ask the vendor one question: "Does it write to live records, and is every write logged with before and after values?"
5. Decide connect, wait, or narrow, and name the data owner.

## 15. The Deep Version

For tools that write or act autonomously, or that feed forecasting or compensation.

| Addition | What it adds |
|---|---|
| Accuracy sample of 50+ records per key field | Confidence in buyer-facing output |
| Ground-truth test: run the tool on records you have checked by hand | Measures the tool and the data together |
| Write log reviewed weekly for the first month, with a random sample audit | Catches silent damage, not only visible errors |
| Field-level ownership map | Every written field has a person accountable |
| Required fields at stage change, so new data arrives clean | Stops the decay behind every cleanup |
| Recheck schedule tied to each new AI tool | Readiness stays current |

---
*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
