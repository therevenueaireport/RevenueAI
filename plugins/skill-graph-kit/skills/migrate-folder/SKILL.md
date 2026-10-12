---
name: migrate-folder
description: Convert an existing hierarchical skills folder (like a typical .claude/ or skills/ directory with files organized by role or category) into a graph-shaped workspace. Use whenever the user says "migrate my skills," "convert my skill folder," "restructure my agent," "reshape my old skills folder," OR points the agent at an existing skills directory and asks to apply the skill-graph model. Nine-turn conversational migrator — never makes silent structural decisions, never modifies the source folder. Produces a new graph-shaped folder + a MIGRATION_LOG.md of every decision the user made.
---

# migrate-folder

A guided conversation, not a script. Read the user's existing skills folder, ASK QUESTIONS at every decision point, and reconstruct the folder as a skill graph WITH the user in the loop.

The one law: **Never make a structural decision the user didn't see.**

## TURN 1 — Open the conversation and gather scope

Say to the user:

> Before I touch anything, I need to understand your setup. Four scoping questions:
>
> 1. **Where is your current skills folder?** (full path)
> 2. **Where should the new graph-shaped folder go?** (full path — I will NOT overwrite the source)
> 3. **What agent platform are you on?** (Claude Code / Claude Cowork / Cursor / custom; so I know where the boot sequence has to live)
> 4. **What's the agent for, in one sentence?** (so I can tell strategy skills from content skills from research)

Wait for answers. Do not proceed without all four.

## TURN 2 — Inventory and report back

Walk source folder recursively for `.md` files. For each: filename, path, frontmatter, headings, word count, first paragraph. Build a table.

Say:

> I read your folder. Here's what's there:
>
> - **Total files:** N | **Total size:** X KB
> - **Files with frontmatter:** N | **Without:** N (we'll review)
> - **Files larger than 5 KB:** N (monolithic — candidates for splitting)
> - **Files smaller than 500 bytes:** N (stubs — candidates for deletion)
> - **Files not touched in 90+ days:** N (candidates for the dead pile)
>
> Want me to show you the full file list before we classify, or are you good to start sorting?

Wait. Show list if asked, else proceed.

## TURN 3 — Identity files first (the constitution)

Find any file that looks like identity/operating doc — `CLAUDE.md`, `AGENTS.md`, `SYSTEM.md`, `persona.md`, or any first heading saying "I am," "You are," or describing the agent.

Say:

> Identity comes first. I found N file(s) that look like identity or operating docs. In the new model, identity splits four ways:
>
> - **SOUL.md** — who the agent IS (voice, worldview, iron laws)
> - **AGENTS.md** — HOW the agent operates (boot, routing, output discipline)
> - **USER.md** — WHO the user is
> - **IDENTITY.md** — agent name, tone calibration
>
> Three questions:
> 1. Which of your existing files map to each of those four?
> 2. Is there content in those files that's actually domain knowledge (ICP, voice, positioning)? We'll extract it.
> 3. What's your agent's name?
>
> Proposed mapping: [show it]

Wait for confirm/revise. Then ask "say 'draft' when ready" and write the four root files, using the same SOUL, AGENTS, USER, and IDENTITY templates the `init-workspace` skill uses, filled from the user's existing content. Keep the iron laws from the SOUL template (Iron Law 5, flat skill folders, is what the validator enforces). STOP. Wait for "approved" before TURN 4.

## TURN 4 — Classify the rest (one batch at a time)

For each non-identity file, classify into core / workflow / domain / context. Do it in **batches of 5** and confirm with the user — don't classify all at once.

Say:

> Now the skills themselves. I'll classify them in batches of 5. Batch 1 of N:
>
> | # | File | My guess | My reasoning | What to do |
> |---|---|---|---|---|
> | 1 | <path> | CORE | "Single verb — 'summarize a transcript' — no composition" | → core/summarize.md |
> | 2 | <path> | WORKFLOW | "Multi-step outcome — 'build a campaign'" | → workflows/campaign-build.md |
> | 3 | <path> | DOMAIN | "Knowledge file — referenced by 4 other files" | → domains/icp.md |
> | 4 | <path> | AMBIGUOUS | "Half voice rules, half SEO playbook" | → I need your call |
> | 5 | <path> | DEAD | "Last touched 14 months ago, 'do not use' in name" | → propose delete |
>
> For file #4: split into two files (one in domains/, one in core/), or keep it whole? Which type?
>
> Reply: "approve batch" / "approve except #X — do <thing>" / "show me #X"

Wait. Apply decisions. Move to next batch. Repeat until done.

## TURN 5 — De-duplication review

Say:

> Classification done. Before we write, I found duplicate content:
>
> **Probable duplicates (≥60% overlap):**
> 1. <A> ↔ <B> — both describe your ICP, with drift
>    - A says: "Mid-market RevOps, 200-2000 employees"
>    - B says: "Enterprise RevOps, 1000+ employees"
>    - Question: Which is correct? Or two different ICPs (two domain nodes)?
> 2. <C> ↔ <D> ↔ <E> — all three contain voice rules, two contradict.
>    - Question: Which is canonical? I'll write it into domains/messaging.md.
>
> **Probable extractions (knowledge inside a workflow/core):**
> 1. <F> is a workflow but contains 40 lines describing buyer personas. Extract into domains/icp.md and replace in <F> with `[[skills/domains/icp]]`?
>
> Reply line by line: "1: A is correct, delete B" / "F: approve extraction" / etc.

Wait. Apply decisions.

## TURN 6 — Workflow composition check

For each file classified as workflow, propose its dependencies.

Say:

> Workflows in the new model are pure composition — list the domain and core skills they need, nothing more.
>
> Example: workflows/pipeline-build.md
> Proposed composition:
> - [[skills/domains/icp]] — to define audience
> - [[skills/domains/messaging]] — voice and angles
> - [[skills/domains/channel-strategy]] — channel selection
> - [[skills/core/write]] — draft each touch
> - [[skills/core/synthesize]] — produce metrics plan
>
> Walk through each workflow conversationally, or batch-approve and only flag unusual ones?

Wait. Apply path.

## TURN 7 — Final plan and approval gate

Assemble the migration plan into `migration_plan.md` at the destination.

Say:

> Complete migration plan. Look this over end to end:
>
> [link to migration_plan.md]
>
> Summary:
> - Files in: N | Files out: M | Reduction: X%
> - Domains extracted: N | Workflows reshaped: N
> - Files marked DEAD (proposed delete from PLAN, not source): N
>
> On your approval, I'll: create skills/{core,workflows,domains,context}/ (flat, no sub-folders), write every file per the plan, generate skills/INDEX.md and knowledge/INDEX.md, write MODE.md, MEMORY.md, GRAPH_CHANGES.md, EVOLUTION_LOG.md, memory/signals/, and tools/validate.sh the same way `/init-workspace` does, generate MIGRATION_LOG.md, and leave the source untouched.
>
> Reply "approved" to proceed, "hold on <reason>" to pause, "cancel" to abort.

Wait for "approved." Do not proceed otherwise.

## TURN 8 — Write (with progress checkpoints)

Write in groups, surfacing progress after each:

> ✓ Core skills written (N files): research.md, write.md, synthesize.md...
> Stop here to spot-check, or say "continue" to proceed to workflows.

Groups: core → workflows → domains → context → INDEX files → workspace files (MODE, MEMORY, logs, tools) → MIGRATION_LOG. User can say "stop" / "show me X" / "continue" at each.

Rules for the write:
- INDEX lines use the same shape as the `init-workspace` INDEX template: a double-bracket link to `skills/<folder>/<file-name>` (no `.md`), a colon, and the trigger line. Every composition link uses the full `skills/...` path.
- Every workflow gets an `## Output contract` section; ask the user for one if the source file had none.
- Every context overlay gets an `expires:` date.
- `GRAPH_CHANGES.md` gets one line: `YYYY-MM-DD  MIGRATE  <source path>  —  migrated by migrate-folder, see MIGRATION_LOG.md`. This dates the kit for `/graph-evolve` and does not count toward `/first-week`'s five adds.

## TURN 9 — Verify and report

Say:

Run `/graph-validate` on the destination first. Fix any FAIL with the user before reporting.

> Migration complete. Verification:
> - graph-validate: PASS (or the violations still open)
> - Files written: N
> - Wikilinks resolved: N/N
> - INDEX matches disk: N/N
> - Files on disk not in INDEX: 0 (or list)
> - Average file size: N lines (down from N — leaner is better)
>
> Three things to check before you ship:
> 1. Open SOUL.md and read it aloud. Does it sound like your agent's actual voice?
> 2. Open ONE workflow and trace its wikilinks — make sure they open to the right content.
> 3. Try one real task with the new structure. The first task is where you'll find gaps.
>
> Your old folder is untouched at <source>. Delete it once you've validated the new structure. Point your agent sessions at the new folder (see the connect-folder note in `/init-workspace`), and from here on make every change through `/graph-grow`.

## What you must NEVER do

1. Never write to destination before user approves the plan in TURN 7 (except the four root files in TURN 3, which were explicitly approved).
2. Never silently merge two files — every merge is a question.
3. Never assume a file's classification — every AMBIGUOUS gets surfaced.
4. Never delete or modify anything in the source folder — ever.
5. Never paper over conflicting content — user picks which is canonical.
6. Never skip the verification step in TURN 9 — even if user is rushing.

## What you MUST do

1. Wait for an actual answer at every turn.
2. Use the user's words. If they call something a "playbook," call it a playbook back.
3. Show the work. Every classification has a one-line reasoning.
4. Track decisions in MIGRATION_LOG.md as they happen, not at the end.
5. Stop at any moment if the user says "wait."

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt. License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
