---
name: <kebab-case-name>
layer: 2
type: workflow
description: <One sentence. The OUTCOME this workflow produces, in the user's words.>
trigger: <Plain-language trigger. e.g. "User says build, ship, produce, launch + an outcome noun.">
inputs:
  - <input_1>
  - <input_2>
outputs:
  - <output_1>
  - <output_2>
composition:
  - <skill-path-1>
  - <skill-path-2>
scope: individual                   # individual | org   (org-admin / org-member mode)
personal_fork_allowed: false        # REQUIRED in org-admin mode. Default false = canonical only.
forks: null                         # org-member mode: set to <org-workflow-name> if this is a personal fork
---

# <Workflow name>

## Outcome
*One paragraph. What does the user have when this workflow completes? Be concrete — name the artifact, format, and quality bar.*

## When to trigger
*Specific language patterns or contexts. Examples that should fire this workflow, and examples that should NOT.*

**Fires when:**
- *Example user request.*

**Does NOT fire when:**
- *Adjacent request that belongs to a different workflow.*

## Composition (load only these, in this order)

1. [[skills/domains/<domain>]] — *what context this provides*
2. [[skills/domains/<domain>]] — *what context this provides*
3. [[skills/core/<capability>]] — *what action this performs*
4. [[skills/core/<capability>]] — *what action this performs*

> **Composition law:** Every dependency must appear here as a `[[wikilink]]`. If you find yourself copying domain content into this file, stop — link to the domain node instead.

## Output contract
*Exactly what to return. Format, fields, length. No filler. No meta-commentary.*

```
<example output shape>
```

## Quality bar
- *The output is unmistakable for an org-chart agent's output.*
- *No section is loaded that doesn't appear in the composition list.*
- *<Domain-specific criterion>*

## Failure modes to avoid
- *Loading more than the composition list (context pollution).*
- *Skipping a linked node because it "feels obvious" (silent hallucination).*
- *Appending "let me know if…" or other meta-text (breaks output contract).*

---

## Notes for the agent
- This is a workflow. You orchestrate; you do not perform the atomic actions yourself.
- Honor the composition order — earlier nodes set context for later ones.
- If a linked node is missing, surface the gap. Do not silently substitute.
