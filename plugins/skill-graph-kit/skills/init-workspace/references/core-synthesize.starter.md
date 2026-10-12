---
name: synthesize
layer: 2
type: core
description: Compress multi-source input into a single clear point of view.
trigger: User has multiple inputs (transcripts, articles, notes) and needs the through-line.
inputs:
  - source_set   # array of texts, transcripts, or URLs
  - focus        # what angle to filter through
outputs:
  - synthesis
dependencies: []
---

# synthesize

## Purpose
Take many sources, find the one thing they collectively say, and state it. This is NOT a summary — it's a synthesis. Summary lists; synthesis takes a position.

## How to run

1. Read every source. Pull the one strongest claim from each.
2. Find the through-line — the claim that appears across sources (even when phrased differently).
3. Find the tension — where sources disagree.
4. State your synthesis: the through-line, the tension, and your call.

## Output contract

```
## Through-line
<one sentence — the single thing the sources collectively say>

## Tension
<one sentence — where they disagree, and what that disagreement is about>

## Call
<one to three sentences — what the user should DO with this, given the through-line and the tension>

## Sources used
- [<source 1>](url)
- [<source 2>](url)
```

## Quality bar
- The through-line is a sentence, not a topic. "AI agents are replacing middle management" — yes. "AI agents in management" — no.
- The synthesis cannot be a list. If you produce bullets, you summarized, not synthesized.
- The call is concrete. "Consider X" is not a call. "Stop doing Y by Friday" is.

## What this skill does NOT do
- Does not produce prose (that's `core/write`).
- Does not gather sources (that's `core/research`).
- Does not evaluate quality (that's `core/critique`).
