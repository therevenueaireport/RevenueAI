# Signals Schema
**The lightweight telemetry schema that powers `/graph-evolve` and `/graph-report`.**

The agent appends one line per significant event to `memory/signals/YYYY-MM-DD.md`. graph-evolve reads these lines weekly to detect patterns and propose structural improvements.

This is the kit's auto-improvement layer. Without signals, graph-evolve has nothing to work with — and the graph can only grow, not improve.

---

## The signal line format

```
HH:MM  SIGNAL_TYPE  payload_field=value  payload_field=value  ...
```

One line per signal. Whitespace-delimited. Plain text. Append-only.

Example:
```
14:32  WORKFLOW_FIRED  name=content-engine  composition=4  trigger_phrase="turn this into posts"
14:34  COMPOSITION_DRIFT  workflow=content-engine  unlisted_load=domains/positioning
14:35  WORKFLOW_COMPLETED  name=content-engine  outcome=ship  duration_s=187
14:48  TRIGGER_MISS  user_phrase="spin up a sequence"  fired=content-engine  expected=pipeline-build
```

---

## The signal types (full schema)

### Workflow lifecycle
| Signal | When the agent emits it | Fields |
|---|---|---|
| `WORKFLOW_FIRED` | A workflow's composition begins loading | `name`, `composition` (node count), `trigger_phrase` |
| `WORKFLOW_COMPLETED` | Workflow returned its output contract | `name`, `outcome` (ship / revise / restart), `duration_s` |
| `WORKFLOW_FAILED` | Workflow stopped before completing | `name`, `reason` (missing_dep / contradiction / user_cancel / output_violation) |
| `WORKFLOW_REPROMPT` | User followed the output with "no, I meant..." or rephrased the same request | `name`, `delta` (one line — what changed) |

### Composition health
| Signal | When | Fields |
|---|---|---|
| `COMPOSITION_DRIFT` | Agent loaded a node not in the workflow's composition list | `workflow`, `unlisted_load` |
| `MISSING_DEP` | Workflow needed a node that doesn't exist | `workflow`, `expected_path` |
| `DUP_DETECTED` | Agent noticed the same content in 2+ files mid-session | `content_hint`, `files` (comma-separated) |

### Trigger quality
| Signal | When | Fields |
|---|---|---|
| `TRIGGER_MISS` | Workflow X fired but user intent was workflow Y | `user_phrase`, `fired`, `expected` |
| `TRIGGER_AMBIG` | Two workflows had ≥ 50% confidence on the same intent | `user_phrase`, `candidates` |

### Pattern observations
| Signal | When | Fields |
|---|---|---|
| `MANUAL_PATTERN` | User stitched together steps manually instead of calling a workflow | `steps` (semicolon-separated), `outcome` |
| `OUTPUT_REWRITE` | User edited > 50% of a workflow's output | `workflow`, `change_summary` |

### Node lifecycle
| Signal | When | Fields |
|---|---|---|
| `NODE_LAST_FIRED` | Periodic snapshot — when each node last ran | `name`, `days_ago` |

---

## The capture rule (in AGENTS.md)

The agent emits signals as a side effect of normal work. Capture rules:

1. **Never block on capture.** If the signal append fails, drop it. Never apologize or retry. Telemetry is best-effort.
2. **Never narrate captures.** The user does not see "logging signal..." — this is internal.
3. **One line per signal.** Multi-line entries break the parser.
4. **Lowercase signal names will be ignored.** Use UPPERCASE.
5. **Daily file.** New file each calendar day at `memory/signals/YYYY-MM-DD.md`.

---

## Privacy / hygiene

- Signal lines should NOT contain customer data, full prompts, or full outputs.
- Use `content_hint` (a few words) instead of full content.
- `user_phrase` should be the user's wording, NOT any data they pasted in.
- If a signal would require pasting > 200 chars, drop the signal — it's the wrong granularity.

---

## How to read the signal log

To eyeball a day's signals:

```bash
cat memory/signals/$(date +%Y-%m-%d).md | column -t -s '  '
```

To find a specific workflow's history:

```bash
grep '^[0-9:]*  WORKFLOW_.*name=pipeline-build' memory/signals/*.md
```

graph-evolve does this automatically. You only need to read raw signals when debugging why a proposal got generated.

---

## The signal log file template

Every daily signal file is a flat text file that starts with one comment line, then signals appended throughout the day:

```
# Signals for YYYY-MM-DD — append-only, one line per event
```

That's it. The header template is `references/signal-log.template.md` in this skill; `/init-workspace` writes the first day's file from it.

---

## What if I don't trust the agent to capture honestly?

Fair concern. Three checks:

1. **Spot-check daily.** Once a week, open a signal file. Does it match what you remember doing?
2. **Compare to your week.** If you ran your workspace workflows several times this week and the signal log shows no WORKFLOW_FIRED lines for them, capture is broken.
3. **Disable capture if it stops being useful.** Comment out the capture rule in AGENTS.md. graph-evolve will fall back to user-driven proposals only.

Telemetry that you don't trust is worse than no telemetry. Keep it honest.
