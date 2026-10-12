# Build, Buy, or Connect Toolkit: Sourcing Record, Quadrant Test, and Flip Conditions

**Use this file when:**
- A capability request has landed and nobody has yet agreed which of the three paths it belongs on.
- A vendor is pitching a tool that mostly moves data between systems you already own.
- Two teams are sourcing the same capability and you need one record that settles it.
- You are auditing the whole stack and want every capability labelled build, buy, thread, or connect.

This file holds the instruments. The SKILL.md holds the logic. The sourcing grid is BUILD, BUY, THREAD ([BUILD, BUY, THREAD, a framework from The Revenue AI Report](https://www.therevenueaireport.com/frameworks/build-buy-thread)), extended here with a fourth path, connect. This skill makes the **routing call**: which path, which layer, what would change it. When the answer is a genuine build-versus-buy contest with money above pilot size, hand the shortlist to `decide-build-or-buy-ai` for the three-year cost model.

---

## 1. How this toolkit fits with decide-build-or-buy-ai

| Question | Use this skill | Use decide-build-or-buy-ai |
|---|---|---|
| Which path does this capability belong on at all? | Yes | No |
| Is connecting what we already own enough? | Yes, always checked first | Assumes connect was ruled out |
| Which layer of the capability is ours to build? | Yes, quadrant test | Takes the answer as input |
| Is it buyer-facing or internal? | Yes | Takes the answer as input |
| What does each side cost over three years? | Rough order of magnitude only | Yes, full model |
| What do we have to believe for build or buy to win? | No | Yes |
| What would flip the call later? | Yes, observable flip condition | Yes, kill criteria for the decision |

**Handoff rule:** run this skill first. If it lands on connect, or on buy for pure infrastructure, you are usually done. If it lands on build or buy-and-thread, and the spend is above pilot size or the engineering ask is above about four weeks (rule of thumb), run `decide-build-or-buy-ai` on the top two options before signing or staffing.

---

## 2. The sourcing sequence

| Step | What you do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1 | Write the capability as a job, not a product | Job card | 10 min |
| 2 | Inventory what current systems already do toward the job | Coverage table | 15 min |
| 3 | Split the job into layers | Layer list | 10 min |
| 4 | Place each layer on the two axes | Quadrant per layer | 10 min |
| 5 | Run the connect test | Connect pass or fail | 5 min |
| 6 | Cost the three options on four lines | Option sheet | 15 min |
| 7 | Write the call, second-best, flip condition, owner, date | Sourcing record | 10 min |
| 8 | Review with one person who did the work | Signed record | 10 min |

---

## 3. Step 1: The capability job card

A product name is not a capability. "We need a research agent" hides three different jobs. Write the job in the form: **who** needs **what outcome** by **when**, triggered by **what event**.

```
CAPABILITY JOB CARD

Job statement:        [Who] needs [outcome] within [time] when [trigger event]
                      e.g. "AEs need a one-page account brief within 10 minutes
                      of a first meeting being booked"
Current workaround:   [What people do today, and how long it takes]
Who sees the output:  [Buyer / internal team / both]
Volume:               [How often the job runs per week or month]
Accuracy bar:         [What an unacceptable error looks like, in one sentence]
Requested by:         [Team and named person]
Other teams sourcing: [Any parallel request, tool trial, or contract for the same job]
Engineering offered:  [Weeks, and whether it is confirmed in writing: yes / no]
```

**Rule:** if the job statement needs the word "and" to join two outcomes, it is two capabilities. Run two records.

---

## 4. Step 2: What to pull before you decide

| Data | System category | How far back | Why it matters |
|---|---|---|---|
| Current contracts with any overlapping feature | Finance or procurement records | Current terms | You may already own it |
| Feature lists and release notes of tools you run | Vendor admin consoles, release notes | Last 12 months | Platforms ship overlapping features often |
| Fields and objects that hold the needed data | CRM, marketing automation, warehouse | Current schema | Data in place means connect is live |
| Existing automations touching the job | Automation tool, CRM workflow rules | All active | Avoid building a second path |
| Unused or low-use seats | SSO app list, license admin | Last 90 days | Paid-for capacity is the cheapest option |
| Engineering commitments | Roadmap, sprint plan | Next two quarters | Build cannot borrow time already promised |
| Past attempts at this job | Project tracker, team chat search | Last 24 months | A failed build or rollout is evidence |
| AI workflows already in production | AI workflow register, if one exists | Current | Maintenance load you already carry |

---

## 5. Steps 3 and 4: Split into layers, then place each layer

Most capabilities are not one thing. Split them into layers and source each one separately. A common split:

| Layer | Example for an account brief | Usual quadrant |
|---|---|---|
| Data storage and movement | CRM, warehouse, sync between them | Infrastructure |
| Model and runtime | Model API, agent runtime, vector store | Internal infrastructure |
| Workflow surface | Where the user triggers and reads the output | Buyer-facing or internal infrastructure |
| Judgment and language | What to look for, how to say it, what good looks like | Intelligence |
| Evidence and memory | Your win notes, reply corpus, reversal history | Internal intelligence |

### The two-axis placement

| | Infrastructure | Intelligence |
|---|---|---|
| **Buyer-facing** | **Buy.** CRM, marketing automation, phone, video, storage. | **Buy and thread.** Buy the platform, thread your language, plays, and evidence into it. |
| **Internal** | **Buy.** Compute, model APIs, vector stores, agent runtimes. Rent the utilities. | **Build.** ICP model, enablement corpus, reply corpus, your Reversal Ledger ([a framework from The Revenue AI Report](https://www.therevenueaireport.com/frameworks/reversal-ledger)), customer voice model. |

### Placement questions

| Question | If yes | If no |
|---|---|---|
| Does a buyer, prospect, or customer see or receive the output? | Buyer-facing | Internal |
| Would a competitor running the same vendor get the same output? | Infrastructure, or intelligence you have not threaded yet | Intelligence |
| Does the layer encode something only your data or people know? | Intelligence | Infrastructure |
| Could you swap vendors for this layer in a quarter without changing the outcome? | Infrastructure | Intelligence, or a lock-in risk |
| Is the layer the reason a buyer picks you over a competitor? | Candidate for build or thread | Buy or connect |

**Threading defined:** building your own motion into a platform you bought. Prompts, plays, ICP criteria, approved language, evidence, and examples, stored as assets you own and can move. If the threads live only inside the vendor's settings with no export, you have customized, not threaded.

---

## 6. Step 5: The connect test

Connect is the default when the data already exists in systems you own. Score each line. Connect passes at 4 or 5 (rule of thumb).

| Check | Pass when |
|---|---|
| Data exists | Every input the job needs sits in a system you already run |
| Access exists | Those systems expose the data through an API, native sync, or export you are licensed for |
| Logic is configuration | The rules can be written as conditions, mappings, or a prompt, not new code |
| Owner exists | A named team already administers the systems involved |
| Volume fits | Current API limits and automation run quotas cover the job's volume |

| Score | Read |
|---|---|
| 5 | Connect. Do not take a vendor meeting until the connected version has run for a month |
| 4 | Connect, with the failing line as the first risk in the record |
| 3 | Connect is the second-best. Compare against buy |
| 0-2 | Connect is not viable. Choose between build and buy |

---

## 7. Step 6: The option sheet

Cost all three options on the same four lines. If you do not have a number, write "unknown, need [source]". Never estimate a vendor price you were not given.

| Line | Build | Buy | Connect |
|---|---|---|---|
| **Money** (first year) | Engineer weeks x loaded cost, plus model and hosting usage | Quote, plus implementation, plus seats for reviewers | Added usage, connector or automation tier, admin hours |
| **Time to first value** | Weeks to a working version real users touch | Weeks from signature to first live use | Weeks to a configured flow in production |
| **Maintenance** (per year) | Named owner hours, model version changes, prompt and eval upkeep, on-call | Admin hours, renewal work, vendor change management | Owner hours to fix broken syncs, schema changes, quota changes |
| **Failure mode** | Owner leaves and nobody can change it | Vendor changes roadmap, price, or data terms | A field rename or API change silently breaks the flow |

### Maintenance checklist (cost every line that applies)

| Item | Build | Buy | Connect |
|---|---|---|---|
| Model or provider version changes | Yes | Vendor's problem, your retest | Yes if a model step is in the flow |
| Eval set upkeep and weekly runs | Yes | Your acceptance tests | Yes if a model step is in the flow |
| Schema and field changes upstream | Yes | Integration upkeep | Yes, the main cost |
| Access reviews and key rotation | Yes | Seat and role admin | Connector credentials |
| Cost ceiling and alerting | Yes | Contract usage tiers | Run quotas |
| Documentation for the next owner | Yes | Configuration notes | Flow diagram and field map |

**Rule of thumb:** if maintenance for any option is listed as zero, the sheet is wrong. Every option has an owner and a failure mode.

---

## 8. Decision table

| If | Then |
|---|---|
| Connect test scores 4 or 5 | Connect. Buy is usually second-best |
| Layer is buyer-facing or internal infrastructure | Buy. Do not build it |
| Layer is buyer-facing intelligence | Buy the platform and thread it. Write down which threads you own |
| Layer is internal intelligence and the data is yours alone | Build. Keep it small and portable |
| Build is favored but engineering time is not confirmed in writing | Do not build. Choose the best non-build option and set the flip condition to "engineering confirmed" |
| Two teams are sourcing the same job | One record, one owner. The team with the data owns the call |
| A vendor tool is mostly sync between systems you own | Run the connect test before the second meeting |
| Build and buy are close and the spend is above pilot size | Hand off to `decide-build-or-buy-ai` |
| A platform you run just shipped an overlapping feature | Re-run this record before renewal or further build |

---

## 9. Red flags and what each one means

| Red flag | What it usually means |
|---|---|
| The request names a product, not a job | The decision was made before the analysis. Rewrite the job card |
| "We'll build it, it's just a few prompts" | Maintenance and evals are not costed. Expect drift within a quarter |
| The vendor demo uses only your CRM and email data | It is a connector with a price tag. Run the connect test |
| No one can say who maintains it after launch | The failure mode is already live. Name an owner or do not proceed |
| Threads live only in the vendor's settings | You are customizing, not threading. Your edge leaves with the contract |
| Build case rests on "it's cheaper" | Saving money is not a build reason. Check what it is the difference for |
| Engineering estimate came from the requester, not engineering | Treat it as unconfirmed. Do not build against it |
| Same capability in two budget lines | Duplicate sourcing. Consolidate before either renews |

---

## 10. Flip condition library

A flip condition must be something someone can see on a date. Pick one, adapt it, and put it on a calendar.

| Current call | Flip to | Observable condition (examples) |
|---|---|---|
| Connect | Buy | Manual exceptions exceed [N] per week for two weeks running |
| Connect | Build | The logic needs per-account judgment more than [N] times per week |
| Buy | Connect | A platform you already run ships the same feature and passes your acceptance test |
| Buy | Build | The vendor cannot accept your threads in an exportable form by renewal |
| Buy and thread | Buy only | Threaded and unthreaded output score the same on your eval set |
| Build | Buy | The named owner leaves, or maintenance exceeds [N] hours per month for a quarter |
| Build | Connect | Two upstream platforms add native support for the job |

---

## 11. The output: sourcing record template

```
SOURCING RECORD

Capability (job):        [From the job card]
Date / Reviewer:         [Date] / [Person who did the work]
Requested by:            [Team, person]
Other teams affected:    [Teams, and any duplicate sourcing found]

Layers and placement:
  Layer               | Buyer-facing or internal | Infra or intelligence | Path
  [Layer 1]           |                          |                       | [Buy/Thread/Build/Connect]
  [Layer 2]           |                          |                       |

Connect test score:      [0-5] Failing lines: [list]

Option sheet:
                         | Build        | Buy          | Connect
  Money (yr 1)           |              |              |
  Time to first value    |              |              |
  Maintenance (per yr)   |              |              |
  Failure mode           |              |              |

Recommendation:          [Path] because [one sentence tied to a decision rule]
Second-best:             [Path] because [one sentence]
Flip condition:          [Observable condition] Checked by [owner] on [date]
Threads we own:          [Assets we keep if the vendor changes, if any]
Unknowns:                [Prices or estimates not supplied, and who will get them]
Handoff:                 [None / decide-build-or-buy-ai on options X and Y]
Next action:             [Action] Owner: [name/role] Due: [date]
```

---

## 12. Worked example: Acme (illustrative)

Acme is a fictional 400-person B2B software company. All numbers are illustrative.

**Situation.** Marketing is trialing a vendor's "account research agent." RevOps wants to build the same thing on a model API. Sales enablement points out the call recorder Acme already pays for has a pre-meeting brief feature nobody turned on.

**Job card.** AEs need a one-page account brief within 10 minutes of a first meeting being booked. Current workaround: 30 to 45 minutes of manual research, done for about half of meetings. Output seen by: internal only. Volume: about 120 first meetings a month. Engineering offered: three weeks, not confirmed in writing.

**Coverage inventory.** CRM holds firmographics and history. An enrichment tool already syncs technographics nightly. The call recorder holds prior conversations and has a brief feature. The company already licenses an AI assistant for every AE.

**Layer split and placement.**

| Layer | Placement | Path | Reasoning |
|---|---|---|---|
| Data (CRM, enrichment, call history) | Internal infrastructure | Connect | All of it already exists in owned systems |
| Model and runtime | Internal infrastructure | Buy (already owned) | Covered by current assistant and call recorder licenses |
| Brief surface (where AEs read it) | Internal infrastructure | Connect | Delivered into the CRM meeting record |
| What to look for, how to frame it | Internal intelligence | Build (small) | Encodes Acme's ICP criteria and its top three discovery angles |

**Connect test.** Data exists: pass. Access exists: pass. Logic is configuration: pass, the brief is a template plus a prompt. Owner exists: pass, RevOps. Volume fits: partial, the automation tool tier caps runs below 120 a month. Score: 4.

**Option sheet (abridged).**

| Line | Build | Buy (marketing's trial vendor) | Connect |
|---|---|---|---|
| Money yr 1 | 3 engineer weeks plus model usage | Unknown, quote not yet supplied | Automation tier upgrade, about 2 admin days |
| Time to value | 6+ weeks (engineering unconfirmed) | 4 weeks after signature | 2 weeks |
| Maintenance | Owner on-call, evals, model changes | Seat admin, renewal | Field map upkeep, about 2 hours a month |
| Failure mode | RevOps engineer moves teams | Vendor's brief is generic, same as competitors' | A CRM field rename breaks the brief silently |

**Call.** Connect the call recorder's brief feature, CRM, and enrichment data, and build only the small intelligence layer: a versioned brief template and prompt holding Acme's ICP criteria. Second-best: buy, if the connected brief fails the AE acceptance test. Flip condition: if more than 20 percent of briefs in a two-week sample are rated "not usable" by AEs, re-open buy and request a quote. Marketing's trial is closed and the duplicate budget line removed.

**Why not build.** Engineering time was not confirmed in writing, and every infrastructure layer already exists. **Why not buy.** The vendor's agent would read the same CRM and enrichment data Acme owns, and its framing would be the same for every customer. No handoff to `decide-build-or-buy-ai` was needed because connect won outright.

---

## 13. AI assist

### Split the work

| Task | AI assistant | Human |
|---|---|---|
| Turn a request into a job card | Draft | Confirms trigger, volume, accuracy bar |
| Split into layers and propose placement | Draft | Decides buyer-facing vs internal and what is truly yours |
| Read release notes and feature lists for overlap | Summarize | Verifies in the admin console |
| Fill the option sheet | Structure only | Supplies every number and its source |
| Write flip conditions | Propose | Makes each one observable and assigns it |
| Make the call | Recommend | Decides and signs |

### Follow-up prompts after the Quick prompt

```text
Split this capability into layers (data, model and runtime, workflow surface, judgment and language, evidence). For each layer state: buyer-facing or internal, infrastructure or intelligence, and the path. Show your reasoning in one line per layer.
```

```text
Run a connect test on my current systems: does the data exist, is it accessible, is the logic configuration or code, is there an owner, does volume fit. Score each pass or fail and cite which of my inputs supports it.
```

```text
List every number in your option sheet. For each, mark it "from my input" or "your estimate". Delete every estimate of vendor pricing and replace it with "unknown, need quote".
```

```text
Rewrite the flip condition so a named person could check it on a date with a system we already run. If it cannot be observed, say so.
```

### Check the AI's output for these errors

| Error this job invites | How to spot it |
|---|---|
| Invented vendor pricing | Any dollar figure for buy you did not supply |
| Assumed engineering capacity | Build time stated without your confirmed weeks |
| Zero maintenance on one option | A blank or "minimal" on any maintenance line |
| Buy recommended for internal intelligence | Your ICP model or corpus placed in "buy" |
| Connect skipped | No connect test result before build or buy is compared |
| Unobservable flip condition | Words like "if needs change" or "if it stops working" |

---

## 14. Common mistakes and how to spot them

| Mistake | How to spot it | Fix |
|---|---|---|
| The old binary | The record has two columns, build and buy | Add connect and thread before comparing |
| Building infrastructure | A build line includes storage, runtime, or a vector store | Buy the utility, build only the intelligence on top |
| Buying intelligence | A vendor's default plays and language go live unedited | Thread your own and keep them exportable |
| One call for a layered capability | One path for the whole job | Split into layers and source each |
| Deciding on the demo | Recommendation cites vendor claims, not your coverage table | Re-run step 2 |
| Flip condition on nobody's calendar | Condition exists, no owner or date | Assign before sharing the record |

---

## 15. The 5-minute version

1. Write the job in one sentence: who, what outcome, by when, on what trigger.
2. Ask: does the data already sit in systems we own? If yes, the default is connect.
3. Ask: is this infrastructure or intelligence, buyer-facing or internal? Place it on the grid.
4. Ask: is engineering time confirmed in writing? If no, build is off the table.
5. Write the call, the second-best, and one observable flip condition with an owner.

## The deep version (high-stakes or stack-wide)

- Run the record for every capability in the stack, not one. Produce a stack map labelled build, buy, thread, or connect per layer.
- Pull 90 days of seat usage and kill duplicate sourcing before any new decision.
- For each buy-and-thread layer, list the threads and confirm each can be exported.
- For every build or close build-versus-buy call, run `decide-build-or-buy-ai` for the three-year cost and the beliefs each side requires.
- Put every flip condition on a quarterly review, and re-run the map whenever a platform you run ships an overlapping feature.

---
*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
