# Performance Curve
**Lean on day 1. Sharper over the first 30 days. Stable after 90. Here's why, and how to keep it that way.**

The kit is designed to produce a noticeable improvement curve. Most "skill systems" get slower and noisier as they grow because every skill adds context. This one holds its load steady as it grows, and gets sharper, because the graph learns what to load and what to ignore.

Nothing in this file is a promise of a specific percentage. Your own numbers come from `/graph-report`, which reads your signal data and compares it to your first week.

---

## Day 1 — what makes it fast immediately

Even with zero customization, the kit boots fast and responds sharp. Three reasons:

### 1. Tiny identity footprint
- `SOUL.md` ≤ 60 lines
- `AGENTS.md` ≤ 150 lines
- `USER.md` ≤ 80 lines
- `IDENTITY.md` ≤ 40 lines
- `MODE.md`: a few dozen lines (mostly explanation; only the `mode:` line matters at runtime)

Total identity load per session: **a few hundred lines**, capped by the validator's size checks. Compare to the typical setup where identity, rules, audience, voice, and old project notes all live in one ever-growing instructions file that loads every time.

### 2. INDEX-only scanning
At boot, the agent reads `skills/INDEX.md` and `knowledge/INDEX.md`: one line per node. It does NOT load skill contents. It loads them on intent, when a workflow fires.

A typical response loads: identity + the two INDEX files + one workflow and the handful of nodes in its composition. That's the entire load, and it stays about the same size no matter how many nodes the graph holds.

### 3. Output contracts
Every workflow declares exactly what to return. No "let me know if you want me to adjust." No restating the question. The output IS the response, so generation time is shorter and tokens-per-useful-word is higher.

### Day 1 expected performance
- Speed: as fast as your model and platform allow, because nothing extra is loaded.
- Consistency: the four core skills ship with output contracts, so the shape of every research brief, draft, synthesis, and critique is predictable from the first request.
- Quality: starts good if you fill in `SOUL.md`, `USER.md`, and one domain (your audience or ICP is the fastest leverage). Stays good as long as you don't preload extras.

---

## Days 2-7 — the early-learning week

This is where the kit starts to feel like *yours*. Three things happen:

### Signals begin accumulating
Every workflow you run drops a few lines into `memory/signals/YYYY-MM-DD.md`. After 7 days, graph-evolve has enough data to surface its first proposals.

### graph-evolve runs in "first-30-days mode"
For the first 30 days, graph-evolve uses **lower thresholds** so it can surface wins faster:
- Pattern detection minimum: 2 signals (vs 3+ normally).
- Lookback: 3 days (vs 7+ normally) for the first run, scaling up.
- More aggressive trigger-drift detection (catches "you keep asking for X but the workflow named Y is firing").
- Strong bias toward EXTRACTION proposals early (the most common beginner mistake is in-line knowledge).

This means **you should see your first useful proposal within 3-5 days of real use** — not 14.

### Memory promotion starts
The first time you correct the agent in the same way twice in a week, it ends up in `MEMORY.md`. Third recurrence and it's permanent — the agent stops needing to be corrected. You feel the agent "getting you."

### Week 1 expected performance
- Day 3-5: first graph-evolve proposal arrives. Approve it.
- Day 5-7: agent stops making 1-2 corrections you used to give it daily.
- Speed: same as day 1 (graph hasn't grown enough to be noticeable). The gain is in quality, not speed yet.

---

## Days 8-30 — the compounding window

This is where the curve steepens. Three loops compound:

### Loop A: the graph adapts to YOUR usage
- Workflows you actually fire get tighter triggers (TRIGGER_DRIFT proposals).
- Workflows you never fire get flagged for retirement.
- Domains that show up in 3+ workflows get extracted into shared nodes (EXTRACTION proposals).
- Patterns you manually stitched together get proposed as new workflows (PROMOTION proposals).

**Effect:** every approved proposal removes a friction point. By day 30, the kit is shaped like your work, not like the generic template you started with.

### Loop B: the agent gets better at YOU
- `MEMORY.md` accumulates the patterns you keep wanting.
- Your `USER.md` allergies, sacred cows, and working preferences get applied automatically.
- Your context overlays for active projects stay sharp.

**Effect:** you correct the agent less. Outputs feel more native faster.

### Loop C: validation prevents decay
- Weekly graph-validate runs catch orphans, dead links, and sub-folder smells before they accumulate.
- EVOLUTION_LOG.md tells you which past improvements actually helped — so the next round of proposals gets sharper.

**Effect:** the kit doesn't degrade with use. Most knowledge systems do.

### Days 8-30 expected performance
- **Speed:** workflows you use most load leaner compositions, because shared knowledge has been extracted into one place instead of repeated.
- **Quality:** voice, ICP, and framing stop drifting across outputs, because every workflow reads the same domain nodes.
- **Friction:** fewer re-prompts. Watch the WORKFLOW_REPROMPT count in `/graph-report`.
- **Your own speed:** you spend less time editing outputs. Watch the OUTPUT_REWRITE count.

---

## Days 30-90 — the maturity plateau

The big gains slow but the kit keeps getting subtly sharper.

- New skills you add cost almost nothing in context (one INDEX line; loads only on intent).
- Stale skills get flagged for retirement (graph-evolve proposes it after 90 days of inactivity; you approve).
- EVOLUTION_LOG shows you which proposals helped, which were neutral, which hurt. The kit's pattern detectors weight future proposals based on what actually worked for you.
- Domains stabilize. Workflows multiply linearly. Cores barely change.

**This is the "feels effortless" phase.** You stop thinking about the kit and just work. The agent handles compositions, retrievals, and consistency without you noticing.

### Days 30-90 expected performance
- **Speed:** stable. Adding new skills doesn't slow it down. This is the structural payoff.
- **Quality:** stable-high. No drift sessions.
- **Trust:** you stop reviewing outputs as carefully because the kit has earned it. Reserve careful review for high-stakes work; the kit handles the rest.

---

## What slows the kit down (avoid)

| Action | Why it hurts |
|---|---|
| Preloading skills "to be safe" | Wastes context, dilutes responses. The whole architecture is built around lazy loading. |
| Creating sub-folders inside `core/workflows/domains/context/` | Smuggles hierarchy back in. Check 9 fails the validator. |
| Editing nodes directly instead of running graph-grow | Drifts INDEX out of sync. Orphans appear. Wikilinks break silently. |
| Skipping graph-validate weekly | Drift accumulates invisibly until something breaks. |
| Skipping graph-evolve weekly | The kit can't learn from your usage if you don't tell it to. |
| Letting context overlays outlive their scope | Stale overlays poison every response in that project's domain. |
| Duplicating knowledge instead of extracting to a domain | The single most common reason "the AI got worse." |

---

## What speeds the kit up (do these)

| Action | Why it compounds |
|---|---|
| Add your audience (ICP) and voice or messaging domains in week 1 | Biggest single quality lever. Every workflow inherits. |
| Run `/first-week` for your first 5 adds | The classification habit you build in week 1 saves you weeks of restructuring later. |
| Approve graph-evolve proposals whose evidence you can follow | Each one is measured 14 days later in EVOLUTION_LOG.md, so a change that hurt gets caught and reversed. |
| Retire skills you stopped using | Each retired skill is one less INDEX line for the agent to scan. |
| Use git on the workspace | Free rollback for any graph change you don't like. Pre-commit hook catches drift. |
| Schedule the weekly run (see the scheduling guide in the `graph-evolve` skill) | Removes the discipline tax. The kit runs its own audit. |

---

## The honest performance claim

| Phase | Where the gain comes from | What to watch in /graph-report | What you'll feel |
|---|---|---|---|
| Day 1 | Lean boot, output contracts | Baseline week starts | "Sharper than I expected from a fresh setup." |
| Day 7 | First domains filled in, first corrections promoted to MEMORY.md | First-look report (3+ days of data) | "Agent's starting to get me." |
| Day 30 | Extractions and trigger fixes approved through graph-evolve | Re-prompts, rewrites, duplicate-content signals vs your baseline | "I'm editing outputs less." |
| Day 90 | Stable domains, retired dead weight | Trend holds; new nodes don't raise load | "I forgot I was using a kit. It just works." |

This table describes mechanisms, not guaranteed percentages. How big your gains are depends on how much drift and duplication you started with and how consistently you run the loop. Measure it: `/graph-report` gives you your own numbers against your own first week, regressions included.

If your 30-day curve is flat, the most likely cause: you're not running graph-evolve weekly. The structural gains come from setup; the compounding gains come from the loop.

---

## How to test your own curve

After day 14, ask:

```
Compare my workflow response times this week vs week 1.
Look at memory/signals/ for WORKFLOW_COMPLETED entries with duration_s.
Tell me: which workflows got faster, which got slower, which stayed the same.
Tell me: which workflows had fewer WORKFLOW_REPROMPT signals this week vs week 1.
```

The agent will read your own data and tell you what's happening. If the answer is "nothing changed," you have a usage problem, not a kit problem.
