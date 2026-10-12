---
type: project
status: active   # active / paused / closed
started: YYYY-MM-DD
last_touched: YYYY-MM-DD
linked_overlays: []   # context overlays scoped to this project
---

# <Project name>

## What this project is
*One paragraph. Goal, stakeholders, success criteria.*

## Current state
- **Phase:** *e.g. discovery, build, launch, sunset*
- **Open questions:** *list them — these are what the agent should ping you about*
- **Blockers:** *list them*

## Key facts the agent must not forget
- *fact 1*
- *fact 2*

## Decisions made on this project
*Link to entries in `knowledge/decisions/` rather than restating.*
- [[knowledge/decisions/YYYY-MM-DD-decision-name]]

## People involved
*Pointers, not contents.*
- [[knowledge/people/<slug>]]

## Related domains
*Which domain nodes this project most heavily depends on.*
- [[skills/domains/<domain>]]

---

## Curation rules
- Update `last_touched` whenever you reference this project.
- When status flips to "closed", move this file to `knowledge/projects/_closed/`.
- If this project starts producing skills that look like patterns, surface them via `/graph-grow` for promotion to workflows or domains.
