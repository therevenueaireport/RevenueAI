---
name: <kebab-case-name>
layer: 2
type: context
description: <One sentence. The SCOPE this overlay applies to. e.g. "Active overlay for Project X — overrides defaults while this project is in flight.">
trigger: <When to load this overlay. e.g. "Any task that mentions Project X, client X, or sprint X.">
expires: <YYYY-MM-DD or 'on-completion'>   # context overlays should be short-lived
overrides: []                              # list any default skills this overlay overrides
---

# <Overlay name>

> **Context overlays are temporary.** They override defaults for a specific scope (a project, a client, a sprint, a single campaign). When the scope ends, the overlay is deleted — not archived.

---

## Scope
*Exactly what this overlay applies to. Be narrow.*

## What this overlay changes

| Default behavior | Overridden behavior | Why |
|---|---|---|
| *e.g. Default voice from USER.md* | *More formal, third-person* | *Client requested* |
| *e.g. ICP from domains/icp.md* | *Narrower segment — enterprise only* | *Project scope* |

## What stays the same
*Default skills, domains, and behaviors that this overlay does NOT touch. Important — overlays should change as little as possible.*

## Active timeline
- **Start:** YYYY-MM-DD
- **Expected end:** YYYY-MM-DD
- **Decommission task:** delete this file when scope ends

## Specific context for this scope

*Project-specific facts, contacts, decisions, links. Whatever the agent needs to know while this overlay is active.*

---

## Curation rules
- If an overlay outlives its scope, the user has a project management problem, not a skill problem. Delete on schedule.
- If two overlays start to overlap, one of them is really a domain node — promote it.
- Never let an overlay reach more than 100 lines. If it does, it's becoming a project knowledge node — move it to `knowledge/projects/`.
