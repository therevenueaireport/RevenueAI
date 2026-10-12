---
name: graph-report
description: Show the user their actual speed and quality gains from using the skill graph, computed from their own signal data. Use whenever the user says "how am I doing," "is this actually working," "show me the data," "graph report," "performance report," "are we getting faster," OR on a monthly cadence. Reads memory/signals/*.md and EVOLUTION_LOG.md, produces a numeric report comparing recent weeks to baseline. Honest — surfaces regressions too, not just wins.
---

# graph-report

Read the user's own signal data and produce a numeric report of how the graph is performing for them. This is the skill that turns the kit's 30/60/90-day curve from a description into evidence the user can see.

## How to run

### Step 1 — Confirm signal data exists

Read `memory/signals/` directory. Count signal files and total signals.

- If fewer than 3 days of signal data → report "I need at least 3 days of signal data to produce a useful comparison. You have N days. Come back after a few more sessions." Stop.
- If 3-14 days → produce a "first-look" report (limited windows, no trend lines).
- If 14+ days → produce a full report with week-over-week comparison.

### Step 2 — Compute the metrics

For each metric below, compute current-window value AND baseline (first week of usage).

**Speed metrics:**
- Average `WORKFLOW_COMPLETED.duration_s` per workflow (lower = faster)
- Workflows fired per session
- Average composition size (smaller = leaner)

**Quality metrics:**
- `WORKFLOW_REPROMPT` count per workflow (lower = agent gets it right first time)
- `OUTPUT_REWRITE` count (lower = user edits less)
- `WORKFLOW_FAILED` count (lower = fewer broken executions)
- `TRIGGER_MISS` count (lower = trigger phrases match user language)

**Consistency metrics:**
- `DUP_DETECTED` count (lower = less knowledge drift)
- Number of `EXTRACTION` operations approved in EVOLUTION_LOG (higher early = healthy cleanup)

**Architecture health:**
- Active node count (core / workflows / domains / context)
- Nodes fired in last 30 days vs total nodes (engagement ratio)
- Retired nodes in last 30 days

### Step 3 — Compute deltas vs baseline

For each metric, compute: `(current - baseline) / baseline * 100` → percent change.

Use plain language. Beginners see "38% faster" not "WORKFLOW_COMPLETED.duration_s decreased 38%."

### Step 4 — Read EVOLUTION_LOG for impact attribution

For every APPROVED proposal in EVOLUTION_LOG.md from the last 30 days:
- Pull the "Net assessment" (HELPED / NEUTRAL / HURT)
- Pull the "Outcome" line
- Surface a one-line summary

### Step 5 — Surface honestly

Include regressions, not just wins. If something got slower or worse, name it. Trust comes from honesty.

## Output contract

```
## Skill graph report — YYYY-MM-DD

**Days of data:** N | **Mode:** <individual|org-admin|org-member>
**Compared to:** your first 7 days as baseline

### Speed
- Average workflow response: <X seconds> (<Δ% vs baseline>)
- Workflows per session: <N> (<Δ% vs baseline>)
- Avg composition size: <N nodes> (<Δ% vs baseline>)

### Quality
- Workflows that got it right first time: <X%> (<Δ% vs baseline>)
- Output rewrites by you: <N/week> (<Δ% vs baseline>)
- Failed workflow runs: <N/week> (<Δ% vs baseline>)

### Consistency
- Duplicate-knowledge events: <N/week> (<Δ% vs baseline>)
- Extractions you've approved: <N total>

### Architecture
- Active nodes: core <N> | workflows <N> | domains <N> | context <N>
- Nodes that fired in last 30 days: <N of N> (<X%>)
- Nodes retired in last 30 days: <N>

### What graph-evolve learned and you approved
- <YYYY-MM-DD>: <operation> — outcome: <HELPED|NEUTRAL|HURT>
- <YYYY-MM-DD>: <operation> — outcome: <HELPED|NEUTRAL|HURT>
- ...

### Headline
<one sentence summarizing the story the data tells>

### What I'd do next
<one specific action the user should take, based on the data>
```

## Quality bar

- Every number is real, pulled from the user's own files. Never fabricate baselines.
- Regressions surfaced as honestly as wins.
- The "Headline" is one sentence — the story the data tells in plain English.
- The "What I'd do next" is one specific action, not three options.
- If a metric has no data (e.g. zero TRIGGER_MISS — never fired wrong workflow), say so. Don't pad with zeros.

## Failure modes to avoid

- Computing percentages off baselines of 1 or 2 events (noise, not signal). If baseline is < 5, say "not enough data yet for this metric."
- Cherry-picking only positive metrics. Show the full picture.
- Comparing to the expected curve in the graph-concept skill's performance guide. Compare to THIS user's actual baseline.
- Burying the headline. Lead with the story; details follow.

## When to run

- Day 14: first useful report
- Monthly thereafter
- After any major graph-grow operation, to measure impact
- Whenever the user asks "is this actually working"

## Notes for the agent

This is the "felt difference made measurable" skill. The graph-concept skill's performance guide describes the expected curve; this skill shows whether THIS user is on it. If they're not, the report tells them why (usually: not running graph-evolve weekly).

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt. License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
