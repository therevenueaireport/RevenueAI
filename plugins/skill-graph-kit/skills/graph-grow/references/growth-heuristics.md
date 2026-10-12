# Growth Heuristics
**How this graph grows after the migration. The self-extension loop.**

`/init-workspace` (or `/migrate-folder`) builds your first version. After that, every change to the graph runs through **one** skill: `/graph-grow`. Every change ends with `/graph-validate`.

If you only remember one thing: **never edit the graph structure by hand. Use the meta-skills.** They keep INDEX, wikilinks, and the iron laws in sync.

---

## The five operations you'll ever need

| You want to... | Operation | Skill |
|---|---|---|
| Capture a new capability | ADD | graph-grow |
| One skill is doing two jobs | SPLIT | graph-grow |
| Two skills overlap | MERGE | graph-grow |
| Same knowledge is repeated in 2+ files | EXTRACT (to domain) | graph-grow |
| A skill is no longer used | RETIRE | graph-grow |

That's it. There is no sixth structural operation. Editing what is inside a node (a trigger phrase, a definition) is a content edit that graph-grow logs as UPDATE; it does not change the graph's shape. If you want to do something else, you're probably trying to put behavior where state belongs, or vice versa.

---

## The growth heuristics

Use these without thinking. They prevent most of the ways a graph degrades.

### 1. The "and" test
If a core skill description has the word "and" in its verb phrase, it's doing two jobs. SPLIT.
> "Gather and synthesize" → split into `research` + `synthesize`.

### 2. The "third copy" test
The first time you write knowledge into a workflow: fine. The second time it appears in another workflow: copy it. The **third time** it appears anywhere: EXTRACT into a domain node.

### 3. The "always loaded" test
If a skill ends up loaded in literally every session, it isn't a skill — it's identity. Promote to SOUL.md or AGENTS.md.

### 4. The "doesn't fire" test
If a skill hasn't been triggered in 90 days, ask: is the trigger wrong, or is the skill dead? Fix the trigger or RETIRE.

### 5. The "where does this live?" test
Before writing anything new, ask:
- Is it behavior? → `skills/`
- Is it knowledge (truths about the world)? → `domains/` or `knowledge/`
- Is it state (current projects, decisions, people)? → `knowledge/`
- Is it temporary scope? → `context/`

If you can't answer in 5 seconds, you're trying to write two things at once. Split before writing.

### 6. The hierarchy smell test
If you find yourself wanting to create a sub-folder (`workflows/sales/`, `domains/enterprise/`), STOP. That is hierarchy talking. Two correct moves:
- Encode the category in the filename: `pipeline-build-sales.md`, `messaging-enterprise.md`.
- Better: extract the category into a **domain node** (`domains/sales.md`) and let the workflows reference it. The category becomes a shared graph node, not a parent folder.

If you ignore this, graph-validate Check 9 will fail your next commit anyway.

---

## What the agent does without you asking

The agent should proactively flag growth-loop opportunities during normal work. Examples:

| What the agent notices | What it surfaces |
|---|---|
| It just wrote ICP into a workflow that already had ICP elsewhere | "Heads up — ICP is duplicated in 2 files. Want to extract via graph-grow?" |
| A workflow's composition is 8+ nodes | "This workflow is getting heavy. Want to split it?" |
| A core skill ran with the same input twice in one session | "This pattern repeats. Want to extract it into a workflow?" |
| You asked for something that doesn't have a node yet | "No node for that. Want to add one via graph-grow?" |

These are surfacing prompts, not silent actions. The agent never restructures the graph on its own.

---

## The weekly growth ritual (5 minutes)

Every Friday (or whenever you wrap a sprint), run two commands in this order:

```
1. Run /graph-validate.
   → returns PASS/FAIL with structural violations to fix.

2. Run /graph-evolve with lookback_days=7.
   → reads your week of signal data and surfaces ranked proposals
     for FUSION / EXTRACTION / SPLIT / RETIREMENT / PROMOTION / TRIGGER_DRIFT.
   → approve or reject each one. Approved ones run through graph-grow.
```

That's the entire growth + improvement ritual. graph-validate keeps the structure honest. graph-evolve keeps the structure **fit for actual use**. Together they prevent both kinds of decay (broken structure / wrong shape).

You can wire this to a scheduled task. See the scheduling guide in the `graph-evolve` skill.

---

## When you (the human) should override

The meta-skills are opinionated. They will sometimes say "split this" when you know you want it whole, or "merge these" when you know two near-duplicates should stay separate for a reason the graph can't see.

You always win that fight. The growth-loop is a *forcing function for thinking*, not an authority. When you override, leave a one-line note in the file's frontmatter:

```yaml
override_note: "Kept as one skill — both jobs always run together in our workflow."
```

Now the next reader knows it's intentional, not an accident.

---

## The three loops, layered

This kit ships three meta-skills for the loop. Together they form a complete self-maintaining graph:

| Loop | Workflow | Cadence | Question it answers |
|---|---|---|---|
| **Structural** | `/graph-grow` | Per change | "Where does this new piece go?" |
| **Integrity** | `/graph-validate` | After every graph-grow + weekly | "Is the structure still sound?" |
| **Evolutionary** | `/graph-evolve` | Weekly | "Is the structure still the right shape for how I actually work?" |

graph-grow is **reactive** — you trigger it when you want to change the graph.
graph-validate is **defensive** — it stops bad changes from shipping.
graph-evolve is **proactive** — it tells you what to change based on what you actually did.

A novice who only ever runs graph-grow gets a clean graph that may not match their real work. A novice who runs all three gets a graph that **gets fitter over time without them having to know graph theory**.

## What this loop produces over time

After 90 days of using all three weekly:
- The graph adds nodes but doesn't deepen the hierarchy.
- Domains stabilize — they get updated, not added to.
- Workflows multiply linearly (one per outcome you care about).
- Core skills barely move — they're primitives.
- Context overlays are short-lived and noisy on purpose.
- **Trigger phrases match what you actually say** (graph-evolve trims drift).
- **Skills you don't use get retired honestly** (not forgotten in a folder).
- **EVOLUTION_LOG.md shows you which auto-improvements actually helped** — so the loop itself improves.

If that's not what your graph looks like after 90 days, run graph-validate, then graph-evolve, then read EVOLUTION_LOG to see where the loop is failing you.
