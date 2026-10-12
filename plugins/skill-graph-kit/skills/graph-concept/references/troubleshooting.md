# Troubleshooting
**The failure modes you'll hit, and the exact fix. Search this file by symptom.**

---

## Symptom: "The agent is loading everything anyway"

You set up the kit but the agent still feels heavy and slow on session start.

**Likely cause:** Your agent platform doesn't respect AGENTS.md as system context.

**Fix:**
1. Check that AGENTS.md is being loaded. Ask the agent: "What boot sequence are you following?" If it can't recite the AGENTS.md boot sequence, the file isn't reaching context.
2. For Claude Code: put the boot sequence in `CLAUDE.md` at the workspace root (or have `CLAUDE.md` tell the agent to read `AGENTS.md` first). AGENTS.md alone isn't a Claude Code convention.
3. For editor-based coding assistants (e.g. Cursor): paste the AGENTS.md boot sequence into the project's rules or instructions file.
4. For custom agents: include AGENTS.md in the always-on system prompt.

The graph model assumes the agent respects the boot sequence. If it doesn't, the architecture is theater.

---

## Symptom: "The agent picks the wrong workflow"

You ask for X, the agent runs Y.

**Likely cause:** Two workflows have overlapping trigger language.

**Fix:**
1. Open both workflows. Look at the `## When to trigger` sections.
2. The conflict is almost always in the **Fires when** examples. Tighten them so each is uniquely identifiable.
3. Add a **Does NOT fire when** line to each workflow pointing at the OTHER workflow.
4. Re-run graph-validate; this isn't auto-detected, so manually re-test with a sample query.

---

## Symptom: "ICP keeps drifting across responses"

The agent's ICP definition changes from session to session, even though you wrote it down.

**Likely cause:** ICP is defined in more than one place, or the workflow isn't actually loading `domains/icp.md`.

**Fix:**
1. Grep the whole workspace: `grep -rl "ICP" --include="*.md" .` (excluding `domains/icp.md`).
2. Any match outside `domains/icp.md` is a duplicate. Run graph-grow EXTRACT.
3. Confirm the workflow's frontmatter `composition:` AND its `## Composition` section both list `[[skills/domains/icp]]`.

---

## Symptom: "I added a new file but the agent doesn't find it"

You wrote a new skill, asked the agent to use it, and the agent says "I don't have that skill."

**Likely cause:** You added a file but didn't add it to `skills/INDEX.md`. Orphan.

**Fix:**
1. Run `./tools/validate.sh .` — it will report the orphan.
2. Add a one-line entry to the appropriate section of `skills/INDEX.md`.
3. Never create skill files by hand again — use `/graph-grow`, which handles INDEX automatically.

---

## Symptom: "Two skills want the same name"

You tried to create `write` as a core skill, and one already exists.

**Likely cause:** You're either duplicating an existing capability or your new skill is more specific.

**Fix:**
1. Re-read the existing `core/write.md`. Does it cover what you need?
2. If YES → don't make a new file. Use the existing one with different inputs.
3. If NO → your new skill is a *different* capability. Rename to something more specific: `write-cold-email`, `write-tweet`. But first ask: is `cold-email` actually a workflow that composes `write` with `messaging` + `icp`? Almost always yes.

---

## Symptom: "The agent ran a skill that wasn't in the composition"

A workflow has 4 nodes in its composition, but the agent loaded a 5th.

**Likely cause:** AGENTS.md's composition law isn't being enforced, or the agent inferred the extra node "to be helpful."

**Fix:**
1. Quote the AGENTS.md composition law back to the agent verbatim: "Load only the linked skills, in order. Do not pull in skills that aren't linked, even if they seem related."
2. If the inference was actually correct (you DO need that 5th node), update the workflow's composition. Don't let the agent silently add it next time.

---

## Symptom: "A domain file is becoming a novel"

`domains/icp.md` is now 400 lines and harder to read than your old monolithic file.

**Likely cause:** The domain is too coarse, OR you've put project-specific state in a domain node.

**Fix:**
1. Re-read the file. Is most of it generic ICP knowledge, or is it specific to one client / project / campaign?
2. Specific stuff → move to `knowledge/projects/<x>.md`. Domain stays generic.
3. Truly generic but too long → SPLIT via graph-grow. e.g., `domains/icp-enterprise.md` and `domains/icp-mid-market.md`.

---

## Symptom: "The agent restructured my graph without asking"

You came back to your folder and files have moved.

**Likely cause:** The agent ran graph-grow without surfacing the change, OR it edited files outside graph-grow.

**Fix:**
1. Check `GRAPH_CHANGES.md` (root). If the change is logged with your approval, you forgot you approved it. If not, the agent violated graph-grow's "never silent" rule.
2. Re-paste the graph-grow rules to the agent. Check that SOUL.md still carries the iron law "Never restructure the graph without explicit user approval via graph-grow," and restore it if it was edited out.
3. Restore from git. (You ARE using git on this folder, right?)

---

## Symptom: "The agent says my graph is fine but it feels broken"

graph-validate returns PASS but outputs are still wrong.

**Likely cause:** Validate checks structure, not content. The structure is sound; the content is stale, wrong, or contradicting itself.

**Fix:**
1. Open `domains/messaging.md`. Read it. Does it actually reflect your current voice? If not, update.
2. Open `MEMORY.md`. Are the patterns still true? Prune what isn't.
3. Open any context overlay. Is the project still active? If not, delete.
4. Validate doesn't audit truthfulness — only YOU do.

---

## Symptom: "I want to undo a graph-grow operation"

You ran a SPLIT, hated the result, want it back.

**Fix:**
1. If you're using git: `git restore .` Done.
2. If you're not using git: the file you split lives in `_retired/` (graph-grow moves originals there before deleting). Pull it back, remove the new split files, re-add the original to INDEX.
3. Start using git on this folder. The kit assumes it.

---

## Symptom: "The migrator ran but the output looks wrong"

You ran `/migrate-folder`, got a reconstructed folder, and it doesn't feel right.

**Fix:**
1. Open `MIGRATION_LOG.md` — every decision is there with the rationale.
2. Find the decision you'd make differently. Fix it in the new folder with the matching `/graph-grow` operation (SPLIT a file that was merged, MERGE two that should be one, EXTRACT knowledge that stayed inline). The source folder is untouched, so you can always re-read the original.
3. If multiple decisions are wrong, re-run from scratch with destination = a NEW folder. Don't try to surgically repair a bad migration.

---

## Symptom: "The wikilinks don't work in my note-taking tool"

You expected `[[skills/domains/icp]]` to click through, but it doesn't.

**Cause:** The kit uses wikilinks as a *protocol* for the agent, not as a feature of your editor. The agent reads `[[link]]` and treats it as "load this file." If your editor also makes them clickable, that's a bonus.

**Fix (if you want clickable links):**
- Markdown note-taking apps with wikilink support (e.g. Obsidian): open the workspace folder as a vault. Links work natively.
- Code editors (e.g. VS Code): install a wikilink extension such as Foam.
- Plain text editor: links won't be clickable. Use grep.

---

## Symptom: "I migrated and now I miss my old structure"

Hierarchy felt familiar. The graph feels weird.

**Cause:** You're 2 days in. The graph rewards muscle memory you don't have yet.

**Fix:** stick with it for one full workflow cycle. After you've felt the agent compose a workflow cleanly, watched a missing domain surface instead of fake itself, and added a node through graph-grow — the org chart will start to feel cluttered, not familiar.

If after two weeks you still hate it, that's real data. Open an issue on the [library's repository](https://github.com/therevenueaireport/RevenueAI) and say what broke.
