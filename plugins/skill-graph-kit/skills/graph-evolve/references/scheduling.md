# Scheduling the weekly evolve

The auto-improvement loop works best on a cadence. You don't have to remember to run it — wire it up once.

---

## Option A — Scheduled task inside your agent

If your agent supports scheduled tasks, paste this prompt to create the weekly run:

```
Every Friday at 4pm in my timezone:

  1. Run /graph-validate. If FAIL, stop and notify me.
  2. If PASS, run /graph-evolve with lookback_days=7.
  3. Present the proposals as a numbered list with the approval syntax.
  4. Wait for my approval reply.
  5. For each approved proposal, run /graph-grow with the proposed operation.
  6. Append decisions to EVOLUTION_LOG.md, and fill in the outcome for any
     proposal approved 14+ days ago that has no outcome yet.
```

If your agent platform supports scheduled tasks, it will create the recurring task and you'll get a Friday ping with the proposals. If it does not, use Option B as the reminder and run the prompt by hand.

---

## Option B — Cron (your own machine)

If you keep the kit in a git repo and want a local nudge:

```cron
# Friday 4pm: run the bash validator and write a flag file if it fails.
0 16 * * 5  cd /path/to/your/agent/workspace && ./tools/validate.sh . > memory/validate-last.txt 2>&1 || touch VALIDATE_FAILED
```

This won't run graph-evolve (that needs the agent), but it'll catch structural drift between agent sessions. Swap the `touch` for whatever desktop notification command your operating system provides.

---

## Option C — Pre-commit hook (the strictest)

If you keep the kit in git, fail commits that break the graph:

```bash
# .git/hooks/pre-commit
#!/usr/bin/env bash
./tools/validate.sh . || {
  echo "Graph integrity check failed. Use /graph-grow in your agent to fix."
  exit 1
}
```

Then `chmod +x .git/hooks/pre-commit`.

You'll never commit a broken graph. Hierarchy can't sneak back in via sub-folders or orphans.

---

## Recommended for most users

**Start with Option A** (scheduled task in the agent). It's the lowest-friction and it runs both validate and evolve. Add Option C (pre-commit hook) once you're committing graph changes frequently.

Option B is overkill unless you're operating multiple agents against the same kit.
