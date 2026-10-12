# First Task Walkthrough
**A 10-minute walkthrough so you can feel the graph working. Do this right after `/init-workspace`, before you build anything big.**

You start with four working core skills (research, write, synthesize, critique) and empty folders for everything else. In this walkthrough you load one core, add your first shared knowledge, build one workflow on top of it, watch a gap surface instead of being faked, and audit the result.

---

## Step 0: Confirm setup

You should have:
- A workspace folder created by `/init-workspace`, open in your agent session.
- `MODE.md`, `SOUL.md`, `AGENTS.md`, `USER.md`, `IDENTITY.md` at the root. `USER.md` has at least your role and mission line filled in.
- `skills/core/` with `research.md`, `write.md`, `synthesize.md`, `critique.md`, all four listed in `skills/INDEX.md`.
- `tools/validate.sh` (the bash validator).

If the agent platform does not read `AGENTS.md` on its own, fix that first. See the troubleshooting guide in the `graph-concept` skill.

---

## Step 1: Start a fresh session

Open a new agent session in the workspace. The agent should load SOUL, USER, AGENTS, IDENTITY, and MODE. It should NOT load any skill files yet.

**Test:** ask the agent:
```
What's in your skills/ folder right now, and what have you loaded into context?
```

A healthy answer names the INDEX it scanned and says it has not loaded any skill contents and is waiting for intent. If the agent says it loaded all your skills, `AGENTS.md` is not being respected. Re-paste the boot sequence and try again.

---

## Step 2: Use one core skill

Paste a paragraph you wrote recently, then:

```
Critique this against clarity, specificity, and a single clear ask.
```

The agent should open `skills/core/critique.md` and nothing else, then return the output contract from that file: criteria applied, redline, verdict (SHIP / REVISE / RESTART), and the single most important fix.

**If it loads write or research too**, it is preloading. That is the org-chart habit the kit exists to break.

---

## Step 3: Add your first shared knowledge, on purpose half-empty

```
/graph-grow
I want the agent to know who my audience is. For now just put TODO in it.
```

The agent should ask plain-English questions, then propose a shared-knowledge file (a domain), for example `skills/domains/audience.md`, show you the file, add one line to `skills/INDEX.md`, log the change in `GRAPH_CHANGES.md`, and run `/graph-validate`.

Leave the content as TODO for now. You will see why in Step 5.

---

## Step 4: Build one workflow on top of it

```
/graph-grow
I want a skill that turns a meeting transcript into five short social posts for my audience.
```

The agent should NOT just write a file. It should walk you through it:

- "Is this one step or several? Several: pull the through-line, write five posts, check them. So it's a multi-step deliverable."
- "It needs to know your audience, which you already have a file for. I'll link to it instead of copying it."
- "Here is the proposed file and the INDEX line. Approve?"

A good proposal composes `skills/domains/audience`, `skills/core/synthesize`, `skills/core/write`, and `skills/core/critique`, in that order, and has an output contract. You approve, the agent writes, then runs `/graph-validate`.

---

## Step 5: Watch a gap surface instead of being faked

Paste any transcript or long set of notes and ask for the five posts.

Because `domains/audience` still says TODO, the agent should STOP and say something like: "Your audience file is not filled in. Fill it in, or tell me to proceed with a placeholder audience."

That is the graph working. A hierarchy would have pushed ahead with a generic audience and handed you generic posts. The graph makes the gap visible.

Fill in the audience file with two sentences. Re-run. Notice: only the audience file changed; the workflow runs unchanged. Every future workflow that links to `audience` gets the same update for free.

---

## Step 6: Validate the graph

```
/graph-validate
```

You should get a PASS report with stats: N core, N workflows, N domains, N wikilinks, largest file. Keep this report. It is your baseline.

You can also run the bash version from the workspace root:

```bash
./tools/validate.sh .
```

Same structural checks, no agent required. Useful in a scheduled job or as a git pre-commit hook.

---

## What you just proved

| Step | What you proved |
|---|---|
| 1 | Identity loads; skills don't preload |
| 2 | A request loads only the node it needs |
| 3 | Knowledge gets one home, added through one controlled door |
| 4 | Workflows link to knowledge instead of copying it |
| 5 | Missing knowledge surfaces instead of being faked |
| 6 | The whole thing can be audited in one command |

If all six worked, you're operating as a graph. If any failed, the fix is almost always in `AGENTS.md`: its rules aren't being honored. Re-paste the relevant section to the agent.

---

## What to do next

- Spend a week using the kit on real work.
- Every time the agent says "I don't have a node for that," run `/graph-grow`.
- Every Friday, run `/graph-validate`, then `/graph-evolve`.
- When you can't tell whether a change is a split, a merge, or an extraction, read the growth heuristics in the `graph-grow` skill.

The goal isn't a "complete" graph. The goal is a graph that **grows on purpose**: every new node added through the loop, every old node retired through the loop, every change auditable.
