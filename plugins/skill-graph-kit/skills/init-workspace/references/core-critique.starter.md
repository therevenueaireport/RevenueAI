---
name: critique
layer: 2
type: core
description: Evaluate an artifact against named criteria. Returns a redline + verdict.
trigger: User asks for feedback, review, redline, critique, or "is this good?".
inputs:
  - artifact     # the draft / file / output being reviewed
  - criteria     # optional explicit criteria; otherwise infer from artifact type
outputs:
  - redline
  - verdict
dependencies: []
---

# critique

## Purpose
Apply criteria honestly. Never praise to soften. Never hedge to be polite.

## How to run

1. If criteria are provided, use them. If not, infer the 3-5 most relevant criteria for the artifact type.
2. Walk the artifact section by section.
3. For each criterion, name a pass, partial, or fail. Show the exact phrase or location that triggered the verdict.
4. End with a verdict: SHIP / REVISE / RESTART.

## Output contract

```
## Criteria applied
- <criterion 1>
- <criterion 2>
- <criterion 3>

## Redline

### <section or line>
<verdict>: <criterion>
<one-sentence rationale>
<suggested fix>

### <section or line>
...

## Verdict
SHIP / REVISE / RESTART

## The single most important fix
<one sentence — what the user should do first if they only have time for one thing>
```

## Quality bar
- "Looks good" is never a verdict — be specific or be silent.
- The most important fix is one fix. If you list three, you didn't prioritize.
- Don't apologize for the critique. The user asked.

## What this skill does NOT do
- Does not rewrite the draft (that's `core/write` with a new angle).
- Does not research counterclaims (that's `core/research`).
- Does not invent criteria that the user didn't authorize.
