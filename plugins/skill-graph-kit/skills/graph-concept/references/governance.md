# Governance
**The operating manual for `mode: org-admin` and `mode: org-member`. Skip this file in `individual` mode.**

---

## The split (org-level vs individual-level)

The four node types are the same in every mode. What changes is **who owns each one** when more than one human shares the kit.

| Node type | Where it lives | Why |
|---|---|---|
| **CORE** | Org workspace, canonical, admin-edited | A company has one canonical way to qualify, research, write. If two sellers qualify two different ways, you have folklore, not qualification. |
| **WORKFLOWS** | Org workspace, canonical, with a per-workflow `personal_fork_allowed` policy | Plays cross people (AE, SE, legal, finance, CS). Canonical lives at org level with a named owner; members can fork only when the workflow explicitly allows. |
| **DOMAINS** | Org workspace, each with a single Domain Steward | ICP, positioning, pricing, brand voice, proof library, competitive intel, objection bank, product truth. Exactly one version of each, edit rights restricted to the steward, read rights universal. |
| **CONTEXT** | Individual workspace | Per-account, per-week, per-person overlays. Account notes, deal context, weekly priorities, voice tweaks. Nobody else needs them; nobody else can maintain them. |
| **knowledge/** | Individual workspace | Projects, people, decisions, references are the user's working state, not the company's. |
| **memory/** | Individual workspace | Daily logs are individual. Patterns the user promotes to their own MEMORY.md stay individual. |
| **SOUL.md, AGENTS.md** | Org workspace | The company's voice and operating rules. |
| **USER.md, IDENTITY.md** | Individual workspace | Who the individual is. |

---

## The four governance questions

When a piece of knowledge or behavior shows up, ask in order:

1. **Would two people writing this independently produce conflicting versions?** → Org-level with a steward. (ICP, pricing, positioning, close-play — all org.)
2. **Does it change per account, per week, or per person?** → Individual. (Account notes, deal context, weekly priorities — all individual.)
3. **Is it canonical knowledge about the company, the buyer, or the market?** → Org.
4. **Is it canonical knowledge about how I work — my voice, my cadence, my projects?** → Individual.

If you can't answer in five seconds, you have ambiguity that will cause drift. Decide before adding.

---

## The Domain Steward role

Every domain at org level has exactly one named human owner.

**What a steward owns:**
- The single canonical version of that domain's content.
- Edit rights (no one else can change the file without a PR through them).
- Quarterly review cadence — they're responsible for spotting staleness.
- Conflict resolution — when a workflow disagrees with their domain, they decide which gives.

**What a steward does NOT own:**
- The workflows that consume the domain (those are owned by whoever named the workflow).
- The decision to retire the domain (that's a graph-grow operation with broader approval).

**How a steward is named:**
The domain file's frontmatter has a `steward:` field. The value is the human's name (or handle). graph-validate Check 10 fails any org-level domain without a steward.

**What happens when a steward leaves:**
- Their domains need a new steward before the next quarterly review.
- The kit doesn't auto-reassign — that's a human decision. graph-validate will start failing the next time it runs, which is the prompt to reassign.

---

## Workflow fork policy

Every org-level workflow declares whether members can fork it for personal use.

```yaml
personal_fork_allowed: true   # or false
```

**`true`** — members can copy the workflow into their own `skills/workflows/` and edit the copy. The fork must declare `forks: <org-workflow-name>` in its frontmatter so the lineage stays auditable. Personal forks don't get re-synced automatically — the member owns the divergence.

**`false`** — the workflow is canonical-only. Members invoke it from the org workspace; they cannot make a personal copy. Use this for workflows where divergence would break handoffs (close plays, renewal plays, anything multi-person).

**Default if missing:** the kit treats missing `personal_fork_allowed:` as `false` (safe default — opt-in to fork rights).

---

## The org-admin's responsibilities

When `mode: org-admin` is set, the kit holds the admin to these:

1. **Every domain has a steward.** Validator Check 10 enforces.
2. **Every workflow declares its fork policy.** Validator Check 11 enforces.
3. **Members get read-only access to the org workspace.** This is a deployment choice (file permissions, branch protection in your version-control host, etc.) — the kit doesn't enforce it technically, but documents the expectation.
4. **The admin runs `graph-evolve` weekly across the org's signal logs** — see below.

## The org-member's responsibilities

When `mode: org-member` is set:

1. **Personal forks declare lineage.** Validator Check 12 fails any workflow in your `workflows/` without a `forks:` field if it shares a name with an org workflow.
2. **Context, knowledge, memory stay in your workspace.** Don't write into the org workspace even if you have access — that's an org-admin operation through graph-grow with admin approval.
3. **Surface drift to the steward.** When you notice your fork diverging meaningfully from the canonical, ping the steward. They decide whether the canonical needs to update, or whether your fork is a personal preference.

---

## Signals + evolve in org mode

The graph-evolve loop becomes more powerful with multiple humans:

- Members' signal logs stay in their individual workspace (privacy).
- The org admin can request aggregated signal data weekly (a thin export — node fire counts, trigger misses, manual patterns, no payload contents).
- The admin runs graph-evolve against the aggregated signals to surface org-wide proposals: "trigger drift on `close-play` across 8 members," "everyone's forking `pipeline-build` and adding the same step — promote to canonical."

The exact aggregation mechanism is deployment-specific. The expected line format is the signals schema in the `graph-evolve` skill; the admin scripts the collection.

---

## What this prevents

Without governance, multi-user deployments fail predictably:

| Failure | Without governance | With governance |
|---|---|---|
| Three ICPs | Marketing, sales, CS each have a doc; they disagree; the agent averages | One `domains/icp.md` with a steward; everyone reads the same source |
| Close play breakage | Every AE forks the close play, handoffs collapse | `personal_fork_allowed: false` keeps the play canonical |
| Stale domains | Nobody owns positioning; it hasn't been updated since the rebrand | Steward field forces named ownership; quarterly review is on someone's calendar |
| Anonymous restructuring | Anyone moves files; nobody knows why | graph-grow requires approval; logs to GRAPH_CHANGES.md with a human's name |

---

## When to start using org mode

Two humans is enough. If two people on your team are running this kit independently, you already have two ICPs.

Start by spinning up an admin instance: one machine or one shared repo, `mode: org-admin`, the people doing the consensus work as stewards. Other team members switch their personal kit to `mode: org-member` and point at the admin instance. They keep their context, knowledge, memory — but they read core, workflows, and domains from the canonical source.

---

## When NOT to use org mode

- You're solo. Don't simulate a team. Stay individual.
- You're two people but one of you doesn't use the kit much. Stay individual on the active person's instance; share specific files manually.
- You're an enterprise without an admin willing to own stewardship. Don't deploy org mode without naming the humans first; you'll get the worst of both worlds.

---

## Related files
- `MODE.md` (in each workspace) — the mode selector and per-mode loading rules.
- "When to start using org mode" above — how the admin sets up the org instance.
- The steward-charter template in the `init-workspace` skill — the doc each steward fills out per domain they own.
- The `graph-concept` skill itself — the conceptual explainer (includes the org/individual section).
