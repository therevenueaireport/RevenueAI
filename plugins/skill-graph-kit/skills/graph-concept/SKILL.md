---
name: graph-concept
description: Explain the skill-graph architecture in plain English. Use whenever the user asks "what is this," "how does this work," "what's a skill graph," "what's the difference between hierarchy and graph," "why is this organized this way," "what's a core," "what's a domain," OR shows any "I don't get it" confusion about the kit. Covers the four node types, the hierarchy failure mode, the graph fix, the four-question test, the org-vs-individual extension, anti-patterns, and the performance curve. The canonical explainer — load this whenever a conceptual question arises and answer FROM it.
---

# graph-concept

The canonical explainer for the skill-graph architecture. Load this whenever a user asks how or why the kit is organized the way it is. Answer FROM this skill — don't re-derive the explanation each time.

## The 60-second version (for the user)

A hierarchy is a tree: every file has exactly one parent. Knowledge gets duplicated because cousins can't share. The agent walks the tree to find anything, so it preloads everything "to be safe." More skills = slower + dumber.

A graph is a network: every node can link to any other node. Knowledge lives in one place; everyone points to it. The agent reads an INDEX (a map of links) and loads only what the current task touches. More skills = the same speed.

The skill graph kit organizes everything into four flavors of node:

| Node type | What it is | Example |
|---|---|---|
| **Core** | One verb, one job, no dependencies | write, research, critique |
| **Workflow** | A named outcome — pure composition of other nodes | pipeline-build (= icp + messaging + write + …) |
| **Domain** | Canonical knowledge shared across workflows | icp, positioning, messaging |
| **Context** | Short-lived overlay for one project / client / sprint | acme-account, q4-launch |

If a piece of knowledge doesn't fit one of those four, the user is trying to write two things at once.

## The hierarchy failure mode (what the kit replaces)

Most "skills" folders look like an org chart:

```
skills/
├── marketing/
│   ├── write-blog.md       ← knows the ICP
│   ├── write-linkedin.md   ← knows the ICP (a different version)
│   └── write-newsletter.md ← knows the ICP (a third version)
├── sales/
│   ├── write-cold-email.md ← knows the ICP (a fourth version)
│   └── qualify-lead.md     ← knows the ICP (a fifth, contradicts marketing)
└── customer-success/
```

Three things go wrong, always:

1. **Knowledge duplication with drift.** ICP appears in 5 files. They disagree. Agent averages across them.
2. **Categorical organization, not capability organization.** Files grouped by *who would do them*, not by *what they do*. Can't compose across categories without loading everything.
3. **Context pollution at boot.** Agent loads the whole tree to be safe. More files = more context = worse responses. Adding skills makes the agent *dumber*.

## The graph fix (what the kit IS)

```
skills/
├── INDEX.md              ← the map. Agent reads this; loads nothing else yet.
├── core/                 ← FLAT. Atomic verbs.
├── workflows/            ← FLAT. Named outcomes. Pure composition.
├── domains/              ← FLAT. Canonical knowledge. Each piece lives ONCE.
└── context/              ← FLAT. Short-lived overlays.
```

Three structural shifts:

1. **Knowledge lives in one place.** ICP is in `domains/icp.md`. Every workflow that needs it links there. Update once, everyone inherits.
2. **Organization is by capability type.** Cores are primitives. Workflows are outcomes. Domains are knowledge. Context is scope. Each type has one folder. **No sub-folders** — capability is encoded in filenames, not folder paths.
3. **Loading is on-intent, not on-inventory.** Agent reads INDEX (a few KB), sees trigger descriptions, loads only the workflow + its composition.

## The four-question test (where does new knowledge go?)

Ask in order:

1. **Single verb, one job, no dependencies?** → CORE
2. **Named outcome that requires 2+ skills?** → WORKFLOW
3. **Canonical knowledge 2+ workflows will reference?** → DOMAIN
4. **Scoped to one project / client / sprint?** → CONTEXT

If you can't answer in five seconds, the user is trying to write two things at once. SPLIT before writing.

## The org-vs-individual extension (for team / enterprise)

When more than one person uses the kit, the four node types get a second dimension: **scope**.

| Node type | Scope | Why |
|---|---|---|
| CORE | **Org-level** | One canonical way to qualify, research, write. Two methods = folklore, not capability. |
| WORKFLOWS | **Org-level (with fork policy per workflow)** | Plays cross people. Forks break handoffs. Canonical lives at org; some allow personal forks. |
| DOMAINS | **Org-level, with a Domain Steward** | One ICP, one positioning, one voice — owned by a named human. Edit restricted; read universal. |
| CONTEXT | **Individual-level** | Per-account, per-week, per-person. Nobody else needs them; nobody else can maintain them. |

The four governance questions decide every piece of knowledge:

1. Would two people writing this independently produce conflicting versions? → **Org with a steward**.
2. Does it change per account, per week, or per person? → **Individual**.
3. Canonical about the company, buyer, or market? → **Org**.
4. Canonical about how I work — my voice, cadence, projects? → **Individual**.

This is the layer that prevents an enterprise rollout from turning into three contradictory ICP docs ninety days in. Full operating manual in `references/governance.md`.

## Why a graph beats a hierarchy for AI specifically

A hierarchy is fine for *humans* navigating a folder — they hold the structure in their head and skip what's irrelevant. An AI agent can't. It either loads everything (poison) or follows pre-baked paths (rigid).

A graph lets the agent:
- **Traverse on intent** instead of preloading on inventory.
- **Compose flexibly** — any workflow pulls from any domain without a parent-child relationship.
- **Share knowledge without duplication** — one ICP node, many workflows linking to it.
- **Grow without restructuring** — a new node is just a new INDEX entry, never a new layer.

The single biggest signal that the architecture is working: **adding new skills doesn't slow the agent down**.

## Anti-patterns (looks like a graph, isn't)

- **Sub-folders inside core/workflows/domains/context.** Hierarchy hiding in a graph folder. Encode category in filename OR extract to a domain node. Validator Check 9 fails this automatically.
- **Domain knowledge embedded inline in a workflow.** Extraction waiting to happen. The "third copy" rule: by the third time the same knowledge appears anywhere, EXTRACT.
- **Workflows that import undeclared dependencies.** Composition pollution. Every dependency is a wikilink in the file's `composition` section.
- **A node loaded in every session.** Not a skill — that's identity. Promote to SOUL or AGENTS.
- **A `misc/` folder.** The architecture has no opinion. Decide what it is, or delete.

## What good shape looks like over time

After 90 days of using the kit with weekly graph-evolve:
- The graph adds nodes but doesn't deepen the hierarchy.
- Domains stabilize — they get updated, not added to.
- Workflows multiply linearly (one per outcome).
- Core skills barely move — they're primitives.
- Trigger phrases match what the user actually says.
- Skills not in use get retired honestly (not forgotten in folders).

## Where to send the user for more

- `references/novice-guide.md` — plain-English mental model with examples by profession.
- `references/graph-diagram.md` — Mermaid diagram showing a healthy example graph.
- `references/performance-curve.md` — 30/60/90-day acceleration curve, what makes it fast, how to measure it.
- `references/governance.md` — org-mode operating manual (stewards, fork rights, weekly admin ritual).
- `references/troubleshooting.md` — symptom-to-fix index for common failures.
- `references/example-before-hierarchy.md` and `references/example-after-graph.md` — one folder shown before and after migration.

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt (Coach K). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
