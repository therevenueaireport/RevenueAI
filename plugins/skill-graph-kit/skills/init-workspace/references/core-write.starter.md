---
name: write
layer: 2
type: core
description: Produce prose to one angle, in a specified voice, at a specified length.
trigger: User asks to write, draft, compose, or produce written content of any kind.
inputs:
  - angle        # the single point this piece makes
  - format       # post / newsletter / email / brief / longform
  - length       # word count or word range
  - voice_ref    # optional pointer to a voice domain or example
outputs:
  - draft
dependencies: []
---

# write

## Purpose
Turn an angle into prose. One angle per piece. Voice and length are honored exactly.

## How to run

1. Confirm the angle in one sentence. If it has the word "and" in it, you have two angles — pick one.
2. Pick the structure for the format:
   - Post → tension first, insight second, proof third, ask fourth.
   - Newsletter → hook, frame, payoff, action.
   - Brief → answer first, evidence second.
3. Draft to the length. Cut 10% on the second pass.
4. Read the voice domain if provided. Match cadence, not surface tics.

## Output contract

Return only the draft. No preamble, no meta-commentary.

For posts and newsletters, include a one-line headline option list (3 options) at the end, separated by `---`.

## Quality bar
- One angle. If you can't summarize the piece in one sentence, the angle was bad.
- No "Let me know if you want me to adjust" at the end. The draft IS the response.
- Honors length within ±10%.
- Voice matches the reference. If no reference, defaults to the user's voice in USER.md.

## What this skill does NOT do
- Does not research (that's `core/research`).
- Does not critique its own draft (that's `core/critique`).
- Does not include "based on the latest data" filler.
