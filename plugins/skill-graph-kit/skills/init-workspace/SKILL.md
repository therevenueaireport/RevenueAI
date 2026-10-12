---
name: init-workspace
description: Initialize a new skill-graph workspace in 60 seconds with a wow-worthy first experience. Use when the user says "set up the kit," "initialize my workspace," "start a new skill graph," "first install," "I just installed the plugin," OR auto-runs on first plugin install. Asks three plain-English questions, writes a complete workspace (identity files + 4 universal core skills already populated + empty scaffolds for workflows/domains/context/knowledge/memory), validates it, then seeds one piece of shared knowledge and offers /demo to make the value visceral. Ends with a connected, validated workspace and the user having seen the graph work — not just having a folder.
---

# init-workspace

**60-second first impression. Three questions max, then write everything, then show the user it works.**

This is the most important skill in the plugin. A user's first 60 seconds either makes them say "oh" or makes them close the tab. Engineer the wow.

## The 60-second flow

### Question 1 — Where (10 sec)

> "Where should I create your skill-graph workspace? Default: `~/Documents/skill-graph-workspace/`. Just hit enter to accept, or paste a different path."

Accept the answer. If the folder exists with a MODE.md, stop and ask whether to migrate (`/migrate-folder`) or abort.

### Question 2 — Mode (10 sec)

> "Just you, or a team?"
> - **Just you** → individual mode (default — most people)
> - **Team admin** → org-admin
> - **Joining a team's existing setup** → org-member (then ask for org workspace path)

### Question 3 — Identity in one sentence (20 sec)

> "Tell me in one sentence: who are you, and what's this agent for? Examples: 'I'm a GTM consultant; this agent helps me run client engagements' or 'I'm a marketer; this writes my content in my voice.'"

That ONE sentence populates:
- USER.md identity line (role)
- USER.md mission (what the agent's for)
- SOUL.md identity-in-one-sentence

Don't ask anything else upfront. Voice rules, allergies, tools — leave them as TODO markers. The user fills them in as the agent gets things wrong over the first week. That's how voice gets calibrated; pre-asking is fake.

### Write the workspace (15 sec)

Create this structure in one pass:

```
<workspace>/
├── MODE.md                    ← from mode.template.md, mode pre-set
├── SOUL.md                    ← from soul.template.md: identity sentence + iron laws
├── AGENTS.md                  ← from agents.template.md: boot sequence + signal capture + plain-English defaults
├── USER.md                    ← from user.template.md: role + mission + TODO markers for voice/allergies/tools
├── IDENTITY.md                ← from identity.template.md: default name + tone matrix
├── MEMORY.md                  ← from memory.template.md
├── GRAPH_CHANGES.md           ← header + one INIT line (see below)
├── EVOLUTION_LOG.md           ← header only (format lives in the graph-evolve skill)
├── README.md                  ← 5-line readme pointing at /graph-concept and /demo
│
├── memory/
│   ├── YYYY-MM-DD.md          ← today's daily log, from memory-daily-log.template.md
│   └── signals/
│       └── YYYY-MM-DD.md      ← today's signal log, from signal-log.template.md
│
├── knowledge/
│   ├── INDEX.md               ← from index-knowledge.template.md
│   ├── projects/
│   ├── people/
│   ├── decisions/
│   └── reference/
│
├── tools/
│   └── validate.sh            ← copied from references/validate.sh, made executable
│
└── skills/
    ├── INDEX.md               ← from index-skills.template.md (lists the 4 universal cores)
    ├── core/
    │   ├── research.md        ← from core-research.starter.md (UNIVERSAL — every knowledge worker)
    │   ├── write.md           ← from core-write.starter.md
    │   ├── synthesize.md      ← from core-synthesize.starter.md
    │   └── critique.md        ← from core-critique.starter.md
    ├── workflows/             ← empty — user adds via /graph-grow as needs arise
    ├── domains/               ← empty; the first one is seeded in "Show it works" below
    └── context/               ← empty
```

When copying templates: drop the "— Template" suffix from headings, replace `YYYY-MM-DD` with today's date, and leave the italic placeholder prompts in place as TODO markers.

`GRAPH_CHANGES.md` starts with a header and one line, so `/graph-evolve` can date the kit and first-30-days mode works:

```
# GRAPH_CHANGES.md
Append-only. One line per structural change: date, operation, target, rationale.

YYYY-MM-DD  INIT  workspace  —  created by init-workspace (mode: <mode>)
```

The INIT line does not count toward the user's first five graph-grow operations.

The 4 core skills are universal primitives — every knowledge worker writes, researches, synthesizes, critiques. They are NOT role-specific. They give the user something working on day 1 instead of a blank scaffold.

### Validate (5 sec)

Run `/graph-validate` (or `./tools/validate.sh .` from the workspace root). A fresh workspace must PASS: four cores, all indexed, no dead links, no sub-folders. If it fails, fix the write before showing the user anything.

### Show it works (15 sec)

Don't just say "done." The demo needs at least one piece of the user's own knowledge to compare against, so seed it in the same breath:

> Workspace created at `<path>` and validated. Right now you have 4 working skills (research, write, synthesize, critique) and empty slots for everything else.
>
> Want to see the graph in action? Give me two sentences about who you serve (your audience or customer), and I'll save it as your first piece of shared knowledge. Then I'll run one of your real requests twice, once cold and once with your graph, and show you exactly which files I loaded and why. Takes about two minutes.

If the user gives the two sentences → run `/graph-grow` ADD to create `skills/domains/audience.md` (this counts as their first add), then invoke `/demo` immediately. Their first interaction after install is the "oh" moment, not a static doc.

If the user skips → offer `/first-week` as the next step: "When you're ready to add your first custom skill, just say 'walk me through adding a skill' and I'll guide you." Also point at `references/first-task-walkthrough.md` as a 10-minute self-test they can run any time.

## Connect-folder reminder

The kit ONLY works once the agent session can read the workspace folder. Surface this clearly, in the terms of the platform the user is on:

> **Critical:** I created the folder, but your agent sessions need access to it before the graph does anything. In Claude Code, start your sessions from `<path>` (or add it as a working directory). In Claude Cowork or another desktop agent app, connect `<path>` as a folder for the session. After that, every session sees your skill graph automatically.

If the platform does not read `AGENTS.md` on its own, tell the user where the boot sequence must go (for Claude Code, a `CLAUDE.md` at the workspace root that points to `AGENTS.md`). See the troubleshooting guide in `/graph-concept`.

## Optional: git init

After the workspace is written, offer:

> "Want me to also git-init this folder? Every graph change becomes recoverable, and you can wire a pre-commit hook to catch architecture violations. Recommended."

If yes: `git init`, `git add .`, `git commit -m "initial workspace from skill-graph-kit plugin"`. The pre-commit hook and scheduling options are in the `graph-evolve` skill's scheduling guide.

## Quality bar

- **Three questions max.** Not five. Not seven. Three. The user is judging the kit by the install experience.
- **One sentence populates three fields.** Don't ask the same thing three different ways.
- **Validate before you celebrate.** A fresh workspace that fails its own validator is a broken first impression.
- **Show, don't tell.** End by seeding one domain and offering /demo, not by handing over a doc.
- **Pre-populate the 4 universal cores.** A workspace with 4 working skills > a workspace with 0 working skills, regardless of role.
- **Never overwrite an existing workspace** without explicit confirmation.
- **TODO markers are fine.** Voice, allergies, tools, sacred cows — those calibrate from real work over the first week. Don't pre-interrogate.

## Failure modes to avoid

- Asking seven setup questions upfront ("what's your voice?" "what's your audience?"). The user doesn't know yet. They'll learn by using. (The audience prompt comes after the workspace exists, and it is optional.)
- Creating sub-folders inside core/workflows/domains/context (violates Iron Law 5 in SOUL.md).
- Leaving placeholder links in `skills/INDEX.md`. Placeholder links fail the validator's dead-link check.
- Forgetting the connect-folder reminder. The kit is invisible until the session can read the folder.
- Writing without confirming the destination path.
- Running /demo against an empty graph. With no domains, the "with graph" output looks like the cold one and the demo falls flat.
- Pre-populating workflows or domains on the user's behalf. Those are role-specific; users add their own.

## What this skill does NOT do

- Does not classify or build the user's specific skills (that's `/graph-grow`).
- Does not run a guided tour of multiple additions (that's `/first-week`).
- Does not migrate an existing skills folder (that's `/migrate-folder`).
- Does not explain the architecture (that's `/graph-concept`).

## References

See `references/` for everything this skill writes:

**Identity templates:** soul, agents, user, identity, mode, memory, index-skills, index-knowledge
**Universal core starters:** core-research.starter.md, core-write.starter.md, core-synthesize.starter.md, core-critique.starter.md
**Knowledge node templates:** knowledge-project, knowledge-person, knowledge-decision, knowledge-reference
**Daily log templates:** memory-daily-log.template.md, signal-log.template.md
**Validator:** validate.sh (same script the `graph-validate` skill ships; copied into the workspace's `tools/`)
**Org-mode template:** steward-charter
**Walkthrough doc:** first-task-walkthrough.md (the static 10-min self-test users can run anytime)

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt. License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
