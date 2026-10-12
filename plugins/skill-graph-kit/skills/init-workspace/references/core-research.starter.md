---
name: research
layer: 2
type: core
description: Gather sourced evidence to answer one focused question. (Synthesis lives in core/synthesize.)
trigger: User asks for research, background, market scan, or a brief on a specific topic.
inputs:
  - question
  - depth   # quick / standard / deep
outputs:
  - brief
dependencies: []
---

# research

## Purpose
Produce a focused, sourced brief that answers ONE question. Not a literature review. Not a summary of everything. A point of view backed by evidence.

## How to run

1. Restate the question in one sentence. If the question is fuzzy, narrow it before searching.
2. Run 3-5 searches across distinct source types (industry publications, primary sources, expert commentary).
3. Triangulate — never trust a single source for a load-bearing claim.
4. Synthesize into the output shape below.

## Output contract

```
## Question
<one sentence>

## Short answer
<two to three sentences. The point of view.>

## Evidence
- <claim> — [source](url)
- <claim> — [source](url)
- <claim> — [source](url)

## What I am NOT certain about
- <unknown 1>
- <unknown 2>

## Suggested next probe
<one question the user should ask next>
```

## Quality bar
- Every load-bearing claim has a real, working URL.
- "What I am NOT certain about" is never empty. If it is, you weren't honest.
- Length scales with depth input: quick = 150 words, standard = 400, deep = 800.

## What this skill does NOT do
- It does not draft content from the research (that's `core/write`).
- It does not pick a strategy (that's a workflow's job).
- It does not load domain knowledge — if the workflow that called you needed it, it loaded it.
