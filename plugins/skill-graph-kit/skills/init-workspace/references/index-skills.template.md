---
layer: 2
type: skill-graph-index
load_policy: scan-only
---

# skills/INDEX.md

The agent reads this map and decides which nodes to load. Never preload.

## Core (atomic primitives)
- [[skills/core/research]]: gather sourced evidence to answer one focused question → brief
- [[skills/core/write]]: turn one angle into prose in a set voice and length → draft
- [[skills/core/synthesize]]: compress many sources into one point of view → synthesis
- [[skills/core/critique]]: judge an artifact against named criteria → redline + verdict

## Workflows (named outcomes)
- (none yet; add via /graph-grow)

## Domains (deep knowledge)
- (none yet; add via /graph-grow)

## Context overlays
- (none yet; add via /graph-grow)

---

## Line format
Every entry is a dash, then a double-bracket link to `skills/<folder>/<file-name>` (folder is core, workflows, domains, or context; no `.md`), then a colon and a one-line trigger description. Copy the shape of the core lines above. The bash validator matches that link shape, so keep it. Replace the "(none yet)" line in a section when you add that section's first entry.

## Rules
1. Every skill in the folder must be listed here with its trigger description.
2. Workflows declare their dependencies via wikilinks in their own file, not here.
3. Never duplicate domain content inside a workflow. Link instead.
4. If two skills feel like they should be merged, merge them.
5. Skills loaded every session don't belong here. Promote to SOUL.md or AGENTS.md.
