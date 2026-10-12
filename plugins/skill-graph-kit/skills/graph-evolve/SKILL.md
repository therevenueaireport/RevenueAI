---
name: graph-evolve
description: Read session signals, detect structural patterns in how the user actually works, and propose ranked improvements to the skill graph. Use whenever the user says "evolve the graph," "what should I improve," "audit my usage," "what is the kit telling me," OR on a weekly cadence (recommended Friday). First-30-days mode lowers signal thresholds so new users see useful proposals in 3-5 days, not 14. Every proposal cites evidence; nothing executes without user approval (approved proposals run through graph-grow).
---

# graph-evolve

The auto-improvement loop. Reads how the user actually uses the kit (from signal logs in `memory/signals/`), detects six pattern types, surfaces ranked proposals for structural improvements. The user approves; graph-grow executes. EVOLUTION_LOG.md measures whether each change helped.

## How to run

### Step 1 — Detect mode and age

Read `MODE.md`. Check `GRAPH_CHANGES.md` for the earliest entry date (the INIT or MIGRATE line).
- If the kit is less than 30 days old → use **first-30-days mode** (see below).
- Otherwise → use standard thresholds.

### Step 2 — Read four sources

1. `memory/signals/*.md` for the lookback window (default 7 days; 3 days first run in first-30-days mode).
2. `GRAPH_CHANGES.md` for the lookback window.
3. `EVOLUTION_LOG.md` — to weight pattern detectors based on which past proposals helped THIS user.
4. The current graph state (`skills/INDEX.md` + skill files).

### Step 3 — Run the six pattern detectors

For each detector that fires above threshold, produce one or more proposals with evidence.

**Detector 1 — Fusion (workflows that should merge)**
Two workflows whose composition lists overlap ≥ 70%, both fired in the window, often within the same session.
→ Propose MERGE.
Evidence: both composition lists, overlap %, co-occurrence count.

**Detector 2 — Extraction (knowledge that became a domain)**
The same content (≥ 5 lines, paraphrased OK) appears in 3+ skill files, OR was edited in 3+ files within the window.
→ Propose EXTRACT into a new domain node; replace inline copies with wikilinks.
Evidence: the duplicated content, the files, edit timestamps.

**Detector 3 — Split (workflows that are too heavy)**
Workflow with composition ≥ 7 nodes, OR fires successfully < 50% of the time (`WORKFLOW_FAILED` > `WORKFLOW_COMPLETED`).
→ Propose SPLIT into two named outcomes.
Evidence: composition count, fire/fail ratio, the two distinct sub-outcomes observed.

**Detector 4 — Retirement (nodes not earning their keep)**
Skill that has not fired in 90+ days (30+ in first-30-days mode is too aggressive — skip this detector early), OR context overlay past its `expires:` date.
→ Propose RETIRE to `_retired/`.
Evidence: last `WORKFLOW_FIRED` date, current trigger field.

**Detector 5 — Promotion (patterns that should become nodes)**
The user has manually done the same multi-step sequence 3+ times in the window (2+ in first-30-days mode) without it being a named workflow.
→ Propose ADD a new workflow that names this outcome.
Evidence: the sessions, the steps the user took each time.

**Detector 6 — Trigger drift (workflows the user invokes with wrong words)**
User language frequently triggers the wrong workflow (`TRIGGER_MISS` entries pointing to same target), OR user re-prompts after a workflow runs (`WORKFLOW_REPROMPT`).
→ Propose an UPDATE (content edit) to the trigger field of the target workflow so it matches actual user language.
Evidence: actual phrasing, intended workflow, fired workflow.

### Step 4 — Surface ranked proposals

Output ranked by evidence strength. Use plain English unless the user has graduated (a GRADUATE line, or 5+ graph-grow operations, in GRAPH_CHANGES.md). For beginners: "I noticed you keep writing emails by hand instead of using your email workflow — want me to update the trigger to match how you ask?" NOT "TRIGGER_DRIFT detected: workflow X fires on phrase Y, expected workflow Z."

### Step 5 — Surface outcomes from past approved proposals (first-30-days mode)

After every approved proposal, immediately read EVOLUTION_LOG.md and surface a one-line outcome from a recent approval that has been measured, for example: "The buyer-persona extraction you approved two weeks ago took duplicate-content signals for that topic from 4 days in 14 to zero. Marked HELPED." Quote the real numbers from the log. If nothing has been measured yet, say so in one line. Builds trust in the loop fast.

### Step 6 — Apply approved proposals

For each "approve," invoke `/graph-grow` with the proposed operation (or its UPDATE path for trigger drift). Update `EVOLUTION_LOG.md` with the decision. Schedule the 14-day outcome measurement (see `references/scheduling.md`).

## First-30-days mode

When the kit is less than 30 days old:
- Signal threshold: minimum **2** occurrences to fire a pattern (vs 3+ normally).
- Lookback: **3 days** for first run, scaling +2 days per week until reaching 7 by day 14.
- Proposal bias: weight EXTRACTION proposals first (most common early-stage cleanup).
- Skip Detector 4 (RETIREMENT) until day 30 — too aggressive early.
- Proactive outcome surfacing after every approved proposal.
- Plain-English report by default (assume beginner status).

After 30 days, revert automatically to standard thresholds.

## Output contract

```
## graph-evolve report — YYYY-MM-DD (last N days)

### Graph state
- Nodes: N (core: N, workflows: N, domains: N, context: N)
- Net change since last evolve: +N / -N
- Validate: PASS / FAIL
- Mode: <first-30-days | standard>

### Proposals (ranked by evidence strength)

#### Proposal 1 — <FUSION | EXTRACTION | SPLIT | RETIREMENT | PROMOTION | TRIGGER_DRIFT>
**Operation:** <graph-grow operation>
**Target:** <file path(s)>
**Evidence:**
  - <bullet 1 — concrete signal data>
  - <bullet 2>
**Why this matters:** <one sentence>
**Risk if approved:** <one sentence>
**Risk if rejected:** <one sentence>

#### Proposal 2 — ...

### Things looking healthy (no action)
- <pattern> — <evidence>

### How to approve
Reply: "1: approve", "2: reject", "3: defer". Approved proposals run through /graph-grow.
```

## Quality bar

- Every proposal cites ≥ 3 concrete signal entries (≥ 2 in first-30-days mode). No hunches.
- Every proposal names what gets better AND what could go wrong.
- Report includes "things looking healthy" — beginners need to see the graph isn't all problems.
- Use plain English for beginners; technical terms only after graduation.
- Ranked proposals. Top one is the highest-leverage change.
- After every approval, surface a one-line outcome from a recent past proposal (first-30-days mode).

## Failure modes to avoid

- Auto-executing any proposal (user is still the architect).
- Generating proposals from < 2 signal events (noise, not pattern).
- Reporting only problems (demoralizing; user stops running).
- Recommending SPLIT and MERGE on the same workflow in the same run (pick one).
- Proposing changes that contradict `override_note:` frontmatter on a file.

## References

- `references/signals-schema.md` — the 11 signal types and what each means.
- `references/evolution-log-format.md` — how to write decisions and measured outcomes.
- `references/scheduling.md` — weekly run, cron nudge, and pre-commit hook.
- `references/signal-log.template.md` — the header for each daily signal file.

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt (Coach K). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
