# Example AFTER — Skill Graph

The same operator's folder, reconstructed by running `/migrate-folder`. Same capabilities, fewer files, zero duplication, clear triggers.

```
workspace/
  SOUL.md                              ← 35 lines: who the agent is, voice
                                         rules, iron laws. NOTHING else.
  AGENTS.md                            ← 60 lines: boot sequence, routing,
                                         output discipline
  USER.md                              ← 50 lines: identity, mission this
                                         quarter, working preferences, project
                                         POINTERS (not project content)
  IDENTITY.md                          ← 25 lines: name, tone calibration
  MEMORY.md                            ← curated patterns, decisions, stop-
                                         doing list
  memory/
    2026-05-20.md                      ← daily log, append-only
    2026-05-21.md
    2026-05-22.md
  knowledge/
    INDEX.md                           ← graph entry for projects, people,
                                         decisions, reference material
    projects/
      acme-engagement.md               ← the old `onboarding-runbook.md`,
                                         moved out of skills/ because it
                                         was project state, not capability
    decisions/
      2026-04-12-no-paid-acquisition.md
  skills/
    INDEX.md                           ← the graph entry. Every node listed
                                         with one-line trigger description.

    core/                              ← atomic primitives. One verb each.
      research.md
      write.md
      synthesize.md
      critique.md

    workflows/                         ← named outcomes. Pure composition.
      pipeline-build.md                ← was: build-sequence.md
                                         Now: links to [[icp]], [[messaging]],
                                         [[channel-strategy]], [[write]]
      content-engine.md                ← was: 3 separate "write-X" files
                                         Now: ONE workflow that handles post,
                                         newsletter, repurpose
      competitor-teardown.md           ← new — emerged when the migrator
                                         noticed three workflows referenced
                                         the same teardown pattern

    domains/                           ← canonical knowledge. Each one
                                         exists EXACTLY once.
      icp.md                           ← the ICP. Singular. Every workflow
                                         links here. Update once, everyone
                                         inherits.
      positioning.md                   ← category, differentiator, POV
      messaging.md                     ← voice, angles, hooks, banned phrases
      channel-strategy.md              ← which channels, what cadence

    context/                           ← short-lived overlays
      (empty — no active client overlays right now)
```

## What changed

| Before | After |
|---|---|
| 800-line INSTRUCTIONS.md | SOUL (35), AGENTS (60), USER (50), IDENTITY (25) — total 170 lines, separated by purpose |
| ICP duplicated in 4 files with drift | `domains/icp.md` — singular, canonical |
| Voice rules in 3 contradicting files | `domains/messaging.md` — single source of truth |
| Old client runbook auto-loaded every session | Moved to `knowledge/projects/` — loaded only when that client is in scope |
| `misc/` folder | Removed. `summarize-meeting.md` was actually a `core/synthesize` invocation; `check-grammar.md` was a `core/critique` invocation. Both deleted. |
| `copy-of-` file | Deleted. |
| `old-experiment-do-not-use.md` | Deleted. |
| `seo-research.md` (never triggered) | Folded into `core/research` with depth=deep flag. |
| Files arranged by role | Files arranged by capability type |

## What the agent does now

- Loads ~40 KB of identity + operating rules at session start (down from ~600 KB).
- Reads `skills/INDEX.md` (5 KB) to know what's available, but loads no skill content yet.
- When the user says "build me a pipeline for mid-market SaaS RevOps leaders," the agent:
  1. Sees the verb "build" + outcome "pipeline" → routes to `workflows/pipeline-build`
  2. Opens that file → sees composition list
  3. Loads ONLY: `domains/icp`, `domains/messaging`, `domains/channel-strategy`, `core/write`, `core/synthesize`
  4. Returns the output contract exactly: sequence + copy pack + metrics plan
- ICP definition stays consistent across pipeline work and content work, because both pull from the same node.
- Adding a new workflow doesn't slow anything down — it's just a new node, not a new layer.

## The mental shift in one image

**Before:** every session, the agent walked into a hoarder's basement, took inventory of everything, and tried to find the right tool.

**After:** every session, the agent walks into a workshop with one pegboard. Tools hang labeled. It picks up only what the job calls for. The rest stays on the wall.
