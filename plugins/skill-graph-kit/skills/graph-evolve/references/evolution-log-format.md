# EVOLUTION_LOG.md
**The record of what graph-evolve proposed, what got approved, and whether it helped.**

Append-only. Newest entries at the top. Each entry has three parts: PROPOSAL, DECISION, OUTCOME.

---

## Entry format

```
## YYYY-MM-DD — Proposal #N

**Type:** FUSION | EXTRACTION | SPLIT | RETIREMENT | PROMOTION | TRIGGER_DRIFT
**Target:** <file path(s)>
**Evidence:** <one paragraph — the signals that drove the proposal>
**Proposed operation:** <graph-grow operation>

**Decision:** APPROVED | REJECTED | DEFERRED (date deferred to)
**Approved by:** <user>
**Operation executed:** <YYYY-MM-DD HH:MM, or "n/a">

**Outcome (measured 14 days later):**
- Did the targeted signal type decrease? Y/N
- Did any new signals appear that suggest the change made things worse? Y/N
- Net assessment: HELPED / NEUTRAL / HURT
- If HURT: what to do next (reverse, refine, accept)
```

---

## Why this file exists

graph-evolve will degrade fast if its proposals aren't measured. Without an outcome check, the loop becomes "agent proposes, user approves, nobody knows if it worked." With outcome checks, the loop compounds:

- Patterns that produced helpful proposals get weighted higher next time.
- Patterns that produced bad proposals get questioned.
- The user gets honest data on whether the kit is actually getting better.

It is the standard experiment loop applied to structure: hypothesis → change → measure → keep or discard → accumulate.

---

## Example entries (delete once you have real ones)

```
## 2026-06-05 — Proposal #3

**Type:** EXTRACTION
**Target:** skills/workflows/pipeline-build.md, skills/workflows/content-engine.md, skills/workflows/competitor-teardown.md
**Evidence:** All three workflows independently restated the buyer-persona definition over the last 14 days. DUP_DETECTED fired 4 times for `buyer-persona` content_hint. Each restatement had subtle drift (Enterprise vs Mid-market, contradictory titles).
**Proposed operation:** EXTRACT into a new `skills/domains/buyer-personas.md` node; replace inline content in all three workflows with `[[skills/domains/buyer-personas]]`.

**Decision:** APPROVED
**Approved by:** workspace owner
**Operation executed:** 2026-06-05 14:22

**Outcome (measured 2026-06-19):**
- Did DUP_DETECTED for `buyer-persona` decrease? Y — went from 4/14 days to 0/14 days
- Did any new signals appear? N
- Net assessment: HELPED
- Note: ICP definition drift in workflow outputs dropped noticeably. Keep this pattern.
```

```
## 2026-06-12 — Proposal #4

**Type:** RETIREMENT
**Target:** skills/workflows/old-experiment.md
**Evidence:** WORKFLOW_FIRED count = 0 over 90 days. Last edit 2026-02-14.
**Proposed operation:** RETIRE to `_retired/`.

**Decision:** REJECTED
**Decided by:** workspace owner
**Operation executed:** n/a — kept because Q3 launch will need this

**Outcome (measured 2026-06-26):**
- Workflow fired in Q3 prep on 2026-06-22. Rejection was correct.
- Net assessment: rejection HELPED (kept a node we needed).
- Note: graph-evolve doesn't know about future plans. User judgment correct.
```
