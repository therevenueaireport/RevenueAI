---
name: <kebab-case-name>
layer: 2
type: domain
description: <One sentence. The KNOWLEDGE this node owns. Not what to do with it — what it is.>
trigger: <When workflows or core skills need this context. e.g. "Any workflow involving ICP, audience, or fit qualification.">
linked_from: []   # auto-fill via tooling: which workflows depend on this domain
scope: individual              # individual | org   (only relevant in org-admin / org-member mode)
steward: <name or handle>      # REQUIRED in org-admin mode; ignored in individual mode
review_cadence: quarterly      # weekly | monthly | quarterly (org mode)
last_reviewed: YYYY-MM-DD      # org mode — when the steward last did a pass
---

# <Domain name>

> **Domain nodes hold knowledge, not behavior.** This file is the canonical source of truth for one slice of the user's world. Workflows traverse here when they need this context. Multiple workflows can share this node — that's the point.

---

## What this node owns
*One paragraph. What is the scope of knowledge here? Be exclusive — name the edges. "This node covers X and Y. It does NOT cover Z (see [[skills/domains/z]])."*

## Core definitions
*Term-by-term. Each term gets one tight line. No essays.*

- **<term>:** <one-line definition>
- **<term>:** <one-line definition>

## Current state
*Snapshot of how this domain looks for the user RIGHT NOW. Updated as it changes.*

- *State item 1.*
- *State item 2.*

## Working assumptions
*What the user currently believes about this domain. Marked as assumptions so they can be challenged.*

- *Assumption 1 — last validated YYYY-MM-DD.*
- *Assumption 2 — last validated YYYY-MM-DD.*

## Proof / evidence
*Sources, data points, customer quotes, research links. Whatever supports the claims above.*

- *[Source name](url) — what it proves.*

## Anti-patterns
*What this domain is NOT. What looks like a fit but isn't.*

- *Pattern that looks right but is wrong, with why.*

---

## Related domains (graph edges)
- [[skills/domains/<adjacent-domain>]] — *how it relates*
- [[skills/domains/<adjacent-domain>]] — *how it relates*

## Workflows that consume this node
*Auto-discoverable via grep, but listed here for the agent's convenience.*
- [[skills/workflows/<workflow>]]
- [[skills/workflows/<workflow>]]

---

## Curation rules
- Update this file when the underlying truth changes, not when a workflow "needs an update".
- If a workflow disagrees with this node, the workflow is wrong — fix the workflow or change this node, do not duplicate.
- Date every assumption. Stale assumptions are the #1 source of agent drift.
