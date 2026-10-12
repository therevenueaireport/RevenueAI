---
name: graph-validate
description: Audit the skill graph for broken links, orphan nodes, sub-folder hierarchy, duplicate knowledge, and iron-law violations. Use whenever the user says "validate the graph," "audit," "check the graph," "did I break anything," OR automatically after every graph-grow operation, OR on a weekly cadence. Reads MODE.md to determine which checks run (different per individual / org-admin / org-member mode). Returns PASS or FAIL with one-line fixes for every violation.
---

# graph-validate

Audit the skill graph in the workspace folder the current session can read. Run twelve checks (some are mode-gated). Return a clean report with PASS/FAIL and one-line fixes for any violations.

## How to run

1. Read `MODE.md` from the workspace root. Extract the `mode:` value (default: individual).
2. Walk the workspace tree: `skills/INDEX.md`, `skills/core/`, `skills/workflows/`, `skills/domains/`, `skills/context/`. Skip `_retired/` and lines in INDEX that contain no link (such as "(none yet)").
3. Run the checks below in order. Stop on first FAIL ONLY if the user explicitly asks; otherwise collect all violations and report together.

## The twelve checks

### Always run (every mode)

**Check 1 — Every node is indexed**
For every `.md` file in `skills/core/`, `skills/workflows/`, `skills/domains/`, `skills/context/`: is it listed in `skills/INDEX.md`?
- If NO → FAIL: "Orphan node: `<path>`. Add a line to INDEX or move to `_retired/`."

**Check 2 — Every indexed link resolves**
For every `[[wikilink]]` in `skills/INDEX.md`: does the file exist?
- If NO → FAIL: "Dead link in INDEX: `<link>`. Create the file or remove the line."

**Check 3 — Every workflow composition resolves**
For every workflow file's `composition:` frontmatter list AND every `[[wikilink]]` in its `## Composition` section: does each linked file exist?
- If NO → FAIL: "Workflow `<path>` links to missing `<link>`."

**Check 4 — No "and" in core descriptions**
For every file in `skills/core/`: does the frontmatter `description:` contain " and "?
- If YES → FAIL: "Core skill `<path>` describes two jobs. Split it via /graph-grow."

**Check 5 — No duplicate domain knowledge**
For every term defined in `skills/domains/*.md` under `## Core definitions`: does the same definition appear inline in any workflow or core file?
- If YES → FAIL: "Domain `<X>` duplicated inline in `<path>`. Extract via /graph-grow."

**Check 6 — Identity layer size discipline**
- SOUL.md ≤ 60 lines
- AGENTS.md ≤ 150 lines
- USER.md ≤ 80 lines
- IDENTITY.md ≤ 40 lines
- MEMORY.md ≤ 200 lines
- If over → FAIL: "`<file>` is N lines. Curate or extract to domain/."

**Check 7 — Context overlay expiration**
For every file in `skills/context/`: does the `expires:` frontmatter field exist? Is it in the past?
- If expired → FAIL: "Expired overlay still active: `<path>`. Delete or extend."

**Check 8 — Workflow output contracts present**
For every workflow file: does it contain an `## Output contract` section with a code block?
- If NO → FAIL: "Workflow `<path>` has no output contract. Add one."

**Check 9 — Flat-folder discipline (no sub-folders)**
For every directory under `skills/core/|workflows/|domains/|context/`: is there a sub-directory?
- If YES → FAIL: "Sub-folder found at `<path>`. The four skill folders must stay flat. Encode category in filenames OR extract to a domain node. Run /graph-grow."

### Mode: org-admin only

**Check 10 — Stewardship on org domains**
For every file in `skills/domains/` with `scope: org`: does it have a non-empty `steward:` field?
- If NO → FAIL: "Org-level domain `<path>` has no steward. Name a human or downgrade scope to individual."

**Check 11 — Fork policy on org workflows**
For every file in `skills/workflows/` with `scope: org`: does it have `personal_fork_allowed: true|false`?
- If MISSING → FAIL: "Org-level workflow `<path>` has no fork policy. Set personal_fork_allowed."

### Mode: org-member only

**Check 12 — Fork lineage on personal workflows**
For every workflow in user's `skills/workflows/` whose filename matches a workflow in `<org_workspace>/skills/workflows/`: does it declare `forks: <org-workflow-name>`?
- If NO → FAIL: "Personal workflow `<path>` shadows an org workflow but doesn't declare lineage. Add `forks: <name>`."

## Output contract

```
## graph-validate report — YYYY-MM-DD

**Result:** PASS / FAIL (N violations)
**Mode:** individual | org-admin | org-member

### Violations
1. [Check N] <file>: <one-line violation>
   Fix: <one-line fix>
...

### Graph stats
- Core: N | Workflows: N | Domains: N | Context: N
- Total wikilinks: N (resolved: N, broken: N)
- Largest file: <path> (N lines)
- Oldest file by mtime: <path> (YYYY-MM-DD)
```

## Quality bar

- PASS means EVERY applicable check passed. No partial credit.
- Each violation has a one-line fix the user can act on without thinking.
- Graph stats let the user spot drift over time without reading every file.
- Validator REPORTS only — never auto-fixes. /graph-grow EXECUTES.

## Bash validator for CLI, scheduled, and pre-commit use

This skill ships `references/validate.sh`, a bash-only validator that runs Checks 1, 2, 4, 7, and 9, plus the mode-gated Checks 10 and 11 (org-admin) and 12 (org-member), with no agent required. Checks 3, 5, 6, and 8 need reading and judgment, so they run only when the agent runs this skill. The script detects mode from MODE.md and exits 0 on PASS, 1 on any violation.

Workspaces created by `/init-workspace` already have a copy at `tools/validate.sh`. For any other workspace, copy this skill's `references/validate.sh` into the workspace's `tools/` folder, then:

```bash
chmod +x tools/validate.sh
./tools/validate.sh .
```

The pre-commit and scheduled-run setups are in the `graph-evolve` skill's scheduling guide.

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt. License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
