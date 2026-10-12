---
name: <kebab-case-name>
layer: 2
type: core
description: <One sentence. What this skill does, in one verb phrase. The agent reads this to decide if it's relevant.>
trigger: <When to use this skill. Plain language. e.g. "User asks for research, summary, or background on a topic.">
inputs:
  - <input_1>
  - <input_2>
outputs:
  - <output_1>
dependencies: []   # core skills have NO dependencies
scope: individual  # individual | org   (org cores are canonical for everyone in the org)
---

# <Skill name>

## Purpose
*One paragraph. What does this skill DO? What is the cleanest version of that capability?*

## How to run

1. *First step the agent should take when this skill is invoked.*
2. *Second step.*
3. *Third step.*

## Output contract
*Exactly what to return. No more, no less. Format matters.*

```
<example output shape>
```

## Quality bar
- *Concrete criterion 1.*
- *Concrete criterion 2.*

## What this skill does NOT do
- *Adjacent capability that belongs in a different core skill.*
- *Domain knowledge that belongs in a domain node.*

---

## Notes for the agent
- This is a core primitive. Never call other skills from inside.
- If you need domain knowledge to do this job, the workflow that called you should have loaded it already.
