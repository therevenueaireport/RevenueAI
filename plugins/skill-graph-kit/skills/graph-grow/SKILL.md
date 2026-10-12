---
name: graph-grow
description: Add, split, merge, extract, or retire a skill node in a skill-graph workspace without breaking the graph. Use whenever the user says "add a skill," "I want a new workflow," "split this," "merge these," "extract this knowledge," "retire this skill," OR describes something they wish their agent could do that it can't yet. Defaults to plain-English diagnostic questions; never forces the user to name a "type." Updates INDEX, wikilinks, and frontmatter; logs to GRAPH_CHANGES.md; auto-runs graph-validate before declaring done.
---

# graph-grow

The single entry point for every structural change to the skill graph. ADD, SPLIT, MERGE, EXTRACT, RETIRE — five operations, one workflow. Never edit the graph by hand; always run through this skill.

## Plain-English interaction (default)

NEVER start by asking "is this a core, workflow, domain, or context?" That question requires the user to already understand the graph. Instead, ask diagnostic questions in plain English, infer the classification silently, then surface the proposal for confirmation.

| Technical term | What you say to the user instead |
|---|---|
| core skill | "small one-step skill" |
| workflow | "multi-step deliverable" or "finished outcome" |
| domain | "shared knowledge" or "facts about your world" |
| context overlay | "just-for-now notes" or "scoped to this project" |
| composition | "what this skill pulls from" |
| wikilink | "link" |
| frontmatter | "the header at the top of the file" |

Use the technical words only if the user uses them first or asks for them.

## The five operations

### ADD a new node

1. Ask diagnostic questions, ONE at a time, until classification is clear:
   - "Walk me through what you want this to do — what's the input, what's the output?"
   - "Is this one specific thing in one step, or a finished deliverable with several steps?"
   - "Will multiple other skills need to reference this knowledge?" (only if it sounds like knowledge)
   - "Is this scoped to one project/client/week, or something you'll use repeatedly?"
2. Classify silently using the Type Decision Tree (see `references/type-decision-tree.md`).
3. State the inference in plain English: "Sounds like a multi-step deliverable — I'll set it up as a workflow that pulls from your audience and brand voice. Output will be: [list]. Sound right?"
4. **If mode is org-admin** and type is core/workflow/domain: ask scope in plain English ("Is this something everyone in the org will use, or just you?"). If org-level domain, ask for steward. If org-level workflow, ask for fork policy.
5. **If mode is org-member** and type is workflow that shares a name with an org workflow: set `forks: <org-workflow-name>` automatically and tell the user.
6. Copy the matching template from `references/`, fill in fields, show the user the proposed file.
7. On approval, write the file and add a line to the matching section of `skills/INDEX.md`, in the same shape as the existing lines: a double-bracket link to `skills/<folder>/<file-name>` (no `.md`), a colon, and the one-line trigger. If the section still says "(none yet)", replace that line.
8. Run `/graph-validate` before declaring done.

### SPLIT an existing node

1. State the two single-job descriptions the existing node is mashing together.
2. Propose two filenames. Confirm with user.
3. Move content; update wikilinks across the graph; update INDEX.
4. The original file becomes one of the two splits OR is moved to `_retired/`.
5. Run `/graph-validate`.

### MERGE two nodes

1. State why (overlap, conflicting truth, redundant trigger).
2. Pick the surviving filename. Confirm.
3. Combine content. Resolve contradictions in the open — don't paper over.
4. Update every wikilink that pointed to either file.
5. Delete the loser (move to `_retired/`). Update INDEX.
6. Run `/graph-validate`.

### EXTRACT knowledge from a workflow/core into a domain

1. Quote the knowledge content currently embedded.
2. Propose the new domain file path. Confirm.
3. Write the new domain file. Replace the embedded content with a wikilink.
4. **De-dup pass**: grep for the same knowledge in OTHER files; offer to extract those too.
5. Update INDEX.
6. Run `/graph-validate`.

### RETIRE a node

1. Grep every wikilink to the node. List them.
2. If wikilinks exist, ask: replace with what, or delete the references?
3. Move file to `_retired/` at the workspace root (never hard-delete). `_retired/` sits outside `skills/`, so it never counts as a sub-folder or an orphan.
4. Remove from INDEX. Update or remove every wikilink.
5. Run `/graph-validate`.

## After every operation

Append a one-line entry to `GRAPH_CHANGES.md` at the workspace root:

```
YYYY-MM-DD  <operation>  <target>  —  <one-line rationale>
```

`<operation>` is ADD, SPLIT, MERGE, EXTRACT, RETIRE, or UPDATE. INIT, MIGRATE, and GRADUATE lines are written by other skills and are not graph-grow operations.

## Content edits (UPDATE)

Changing what is inside a node without changing the graph's shape (rewriting a trigger phrase, correcting a definition in a domain, tightening an output contract) is not one of the five structural operations. It is still a change the user approves:

1. Show the before and after of the field or section.
2. On approval, edit the file. In org modes, a change to an org-level domain goes to its steward first.
3. Log it as `UPDATE` in `GRAPH_CHANGES.md`.
4. Run `/graph-validate`.

This is how `/graph-evolve` applies an approved trigger-drift proposal.

## Beginner safety nets

- If `GRAPH_CHANGES.md` shows fewer than 5 graph-grow operations and no GRADUATE line, surface the `/first-week` skill once and offer guided hand-holding.
- If the user says "I have no idea what this is" — walk through the four diagnostic questions one at a time, slow.
- If classification stays ambiguous after diagnostics — propose CONTEXT as the safe default. ("Let's start it as just-for-now scoped to your current work. We can promote it later if it stays useful.")

## Quality bar

- The user is never forced to name a type. Plain-English diagnostics; agent classifies.
- Every ADD ends with INDEX updated AND graph-validate run.
- Every EXTRACT de-duplicates ALL copies, not just the trigger copy.
- Every RETIRE moves to `_retired/`, never hard-deletes — auditability matters.
- Every operation logs to GRAPH_CHANGES.md with a human-readable rationale.

## Failure modes to avoid

- Adding a node without putting it in INDEX (creates an orphan; validator will fail).
- Extracting knowledge but leaving the original copy in place (creates a duplicate).
- Merging without confirming the canonical truth (silent contradiction).
- Skipping the validate step "because the change was small" (small changes are how graphs degrade).
- Creating a sub-folder inside core/workflows/domains/context (violates Iron Law 5 in SOUL.md: encode the category in the filename or extract it to a domain node).

## References

- `references/type-decision-tree.md` — the silent classification logic.
- `references/core-skill.template.md`
- `references/workflow-skill.template.md`
- `references/domain-skill.template.md`
- `references/context-overlay.template.md`
- `references/growth-heuristics.md` — the growth tests for when to split, merge, extract, retire, plus the weekly ritual.

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt. License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
