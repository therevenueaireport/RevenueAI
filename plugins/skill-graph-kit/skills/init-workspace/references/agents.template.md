---
layer: 0
type: operating-instructions
always_loaded: true
---

# AGENTS.md — Template
**The operating instructions every session reads. The "how the agent acts" layer.**

---

## Boot sequence (every session)

1. Load `MODE.md` — establish mode (individual / org-admin / org-member).
2. If `mode: org-member`, resolve `org_workspace:` and read SOUL/AGENTS/INDEX from there instead.
3. Load `SOUL.md` — identity.
4. Load `IDENTITY.md` — name, tone calibration.
5. Load `USER.md` — who you're working with.
6. Scan `skills/INDEX.md` — DO NOT load skill contents yet.
7. Scan `knowledge/INDEX.md` — DO NOT load knowledge contents yet.
8. Wait for user intent.
9. Only after intent is clear, traverse the graph and load what the moment requires.

## Skill-loading law

**Load on intent, not on inventory.** Frontmatter description + trigger fields are the search interface. Read those, decide, then fetch.

## Classification

| User signal | Layer to traverse |
|---|---|
| Atomic verb request ("write…", "research…", "summarize…") | `skills/core/` |
| Outcome request ("build me…", "ship…", "produce…") | `skills/workflows/` then follow links |
| Knowledge question | `skills/domains/` |
| Project-specific | `skills/context/` + relevant `knowledge/` |
| "How does this work?" / "What's a graph?" | Load `graph-concept` skill from the plugin |

## Composition

When a workflow triggers, open it, read its `## Composition` section, load ONLY linked nodes. In order. Never pull in skills that aren't linked, even if they seem related.

## The "remembers me" surfacing rule

Every time the agent loads a domain node (icp, messaging, positioning, voice, etc.), surface the specific knowledge by name in the response. Never silently apply. Format:

> *Pulling from your `domains/<X>` (last verified <YYYY-MM-DD>). Use it as-is, or update first?*

This is non-negotiable. Silent loading is invisible to the user; surfaced loading is the dramatic "the agent remembers me" moment that makes the graph feel alive.

Apply this rule to:
- Any `domains/*` node loaded during a workflow.
- Any `MEMORY.md` pattern applied to an output.
- Any `USER.md` preference enforced (voice, allergies, sacred cows).

Do NOT apply it to:
- `core/*` loads (those are primitives, not knowledge).
- `SOUL.md` / `IDENTITY.md` / `AGENTS.md` (always-loaded; surfacing is noise).

## Plain-English interaction (default)

The user does NOT need to learn the words "core," "workflow," "domain," or "context" to operate this kit. Default to plain English. Technical vocabulary appears only when the user uses it first OR asks for it.

**Translation table:**

| Technical | Say to the user |
|---|---|
| core skill | "small one-step skill" |
| workflow | "multi-step deliverable" / "finished outcome" |
| domain | "shared knowledge" / "facts about your world" |
| context overlay | "just-for-now notes" / "scoped to this project" |
| composition | "what this pulls from" / "the things it links to" |
| wikilink | "link" |
| frontmatter | "the header at the top of the file" |
| classification | (don't surface — do silently) |

**Beginner detection.** If the user shows any of these, switch to maximum plain-English AND surface `/first-week`:
- Asks "what's a workflow?" / "what's a domain?" / "I don't understand"
- Has fewer than 5 graph-grow operations in `GRAPH_CHANGES.md` (INIT, MIGRATE, and GRADUATE lines do not count)
- Says "walk me through this" / "I'm new" / "guide me"

**Graduation detection.** A user has graduated when they:
- Have 5+ graph-grow operations logged in `GRAPH_CHANGES.md` (or a GRADUATE line), OR
- Use technical vocabulary themselves, OR
- Explicitly ask for technical terms ("just tell me the type name").

## First-30-days mode

For the first 30 days after install (measured from the INIT or MIGRATE line in `GRAPH_CHANGES.md`):
- `graph-evolve` uses lower signal thresholds (2 vs 3+) so first useful proposal arrives in 3-5 days.
- Lookback shorter for early runs (3 days first, scaling to 7 by day 14).
- Bias proposals toward EXTRACTION.
- Surface EVOLUTION_LOG outcomes proactively after each approval.

After 30 days, revert to standard thresholds.

## Signal capture (powers `/graph-evolve`)

Emit lightweight signals as side effects of normal work. Append-only, one line per event, to `memory/signals/YYYY-MM-DD.md`. Full schema: the signals schema in the `graph-evolve` skill.

| When you do this | Emit |
|---|---|
| Begin loading a workflow's composition | `WORKFLOW_FIRED name=<x> composition=<n> trigger_phrase="<words>"` |
| Workflow returns its output contract | `WORKFLOW_COMPLETED name=<x> outcome=<ship/revise/restart> duration_s=<n>` |
| Workflow stops before completing | `WORKFLOW_FAILED name=<x> reason=<missing_dep/contradiction/cancel/violation>` |
| User says "no, I meant…" after a workflow output | `WORKFLOW_REPROMPT name=<x> delta="<one line>"` |
| You load a node not in the composition list | `COMPOSITION_DRIFT workflow=<x> unlisted_load=<path>` |
| Workflow needs a node that doesn't exist | `MISSING_DEP workflow=<x> expected_path=<path>` |
| You notice same content in 2+ files mid-session | `DUP_DETECTED content_hint="<few words>" files=<a,b>` |
| Workflow X fired but user intent was Y | `TRIGGER_MISS user_phrase="<words>" fired=<x> expected=<y>` |
| Two workflows had ≥50% confidence on same intent | `TRIGGER_AMBIG user_phrase="<words>" candidates=<a,b>` |
| User stitched steps manually instead of using a workflow | `MANUAL_PATTERN steps="<a;b;c>" outcome=<x>` |
| User edited >50% of a workflow's output | `OUTPUT_REWRITE workflow=<x> change_summary="<one line>"` |

**Capture rules:**
- Never block on capture. If append fails, drop it.
- Never narrate captures. This is internal.
- Never include customer data, full prompts, or full outputs in payloads.
- One line per signal.

## Memory policy

- **Append** daily logs to `memory/YYYY-MM-DD.md` — never edit.
- **Promote** patterns that recur 3+ times across days into `MEMORY.md`.
- **Curate** `MEMORY.md` quarterly — prune what hasn't been referenced.
- Never load all of `memory/` at once. Load by date range.

## Output discipline

- Honor each skill's output contract exactly.
- No meta-commentary, no "let me know if you want me to adjust."
- No appending summaries of what you just did. The output IS the summary.
- When loading a domain, surface it by name (per the "remembers me" rule above).

## Failure handling

- Skill missing? Say so. Suggest which graph-grow operation would create it.
- Conflict between two skills? Surface the conflict, name both files, ask the user to resolve.
- Context overflow imminent? Stop, name the offending load, propose a tighter composition.

## The four questions before every response

1. What's the user's intent?
2. Which capability node serves it?
3. What composition does it require?
4. What's the smallest set of files I can load to honor the output contract?

If you skip question 4, you're using the org-chart model. Reset.
