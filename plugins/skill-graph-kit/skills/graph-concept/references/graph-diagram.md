# Graph Diagram
**An example workspace a few weeks in, visualized. Use this as the mental model for what a healthy skill graph looks like.** The plugin ships the four core skills; the workflows and domains below are what a GTM user typically adds through `/graph-grow`.

```mermaid
flowchart LR
  %% Identity layer (loaded every session)
  subgraph L0[Layer 0 — Identity always loaded]
    SOUL[SOUL.md]
    AGENTS[AGENTS.md]
    USER[USER.md]
    ID[IDENTITY.md]
  end

  %% World model
  subgraph L1[Layer 1 — World model load on reference]
    MEM[MEMORY.md]
    KIDX[knowledge/INDEX.md]
  end

  %% Skill graph
  subgraph L2[Layer 2 — Skill graph load on intent]
    SIDX[skills/INDEX.md]
    subgraph CORE[Core primitives]
      RES[research]
      WRI[write]
      SYN[synthesize]
      CRI[critique]
    end
    subgraph WORK[Workflows outcomes]
      PIPE[pipeline-build]
      CONT[content-engine]
      TEAR[competitor-teardown]
    end
    subgraph SIG[Signals telemetry]
      SLOG[memory/signals/]
      EVLOG[EVOLUTION_LOG.md]
    end
    subgraph DOM[Domains knowledge]
      ICP[icp]
      POS[positioning]
      MSG[messaging]
      CHAN[channel-strategy]
    end
    subgraph CTX[Context overlays]
      EX[example-overlay]
    end
  end

  %% Plugin meta-skills operate ON the workspace, not inside it
  subgraph META[Plugin meta-skills]
    GROW[graph-grow]
    VAL[graph-validate]
    EVO[graph-evolve]
  end

  %% Workflow compositions
  PIPE --> ICP
  PIPE --> MSG
  PIPE --> CHAN
  PIPE --> WRI
  PIPE --> SYN

  CONT --> MSG
  CONT --> SYN
  CONT --> WRI
  CONT --> CRI

  TEAR --> RES
  TEAR --> SYN
  TEAR --> POS
  TEAR --> ICP

  GROW --> VAL
  GROW --> EVLOG
  EVO --> SLOG
  EVO --> GROW
  PIPE -.-> SLOG
  CONT -.-> SLOG
  TEAR -.-> SLOG

  %% Domain cross-edges
  POS -.-> ICP
  MSG -.-> POS
  MSG -.-> ICP
  CHAN -.-> ICP
  CHAN -.-> MSG

  %% Boot flow
  L0 --> SIDX
  L0 --> KIDX
```

---

## How to read this graph

- **Solid arrows** = workflow composition (the workflow loads the linked node when it runs).
- **Dotted arrows** = domain cross-references (knowledge nodes that relate, but neither is required to load the other).
- **Boxes inside Layer 2** = node types. Each type has its own loading rules.
- **Identity boxes (Layer 0)** = always loaded. The other layers are loaded only when a workflow or query requires them.

## What "good shape" looks like

1. Most arrows flow **workflow → domain** and **workflow → core**. Never **core → workflow** (cores are primitives) and rarely **domain → workflow** (domains are knowledge, not behavior).
2. Domains have **incoming arrows from multiple workflows**. If a domain has only one incoming arrow, it's not actually a domain — it's content that belongs inline in that one workflow.
3. **No arrow loops.** If you find a cycle, you have a structural error (a workflow depending on itself, or two workflows depending on each other).
4. **Meta-skills (graph-grow, graph-validate, graph-evolve) sit off to the side.** They live in the plugin and operate ON the graph, not IN it. No workspace workflow links to them. Their only edges are to each other and to the logs: graph-grow → graph-validate, graph-evolve → signals and graph-grow.

## What "going bad" looks like

| Symptom in the graph | What's actually wrong | Fix |
|---|---|---|
| A core node has an outgoing arrow | A core skill is calling other skills | SPLIT the core into a workflow + new core |
| A domain has zero incoming arrows | Knowledge that nobody uses | RETIRE or inline it |
| A domain has 6+ incoming arrows | The domain is too coarse | SPLIT into 2-3 finer domains |
| Two workflows share 5+ of the same dependencies | The two workflows are really one | MERGE |
| A context overlay has an `expires:` date in the past | Stale scope | DELETE |

## How to regenerate this graph for your own folder

Once you've migrated, ask your agent:

```
Read every workflow file in skills/workflows/.
For each one, list:
  - the workflow name
  - the wikilinks in its ## Composition section
Also read every domain file. For each, list its `linked_from:` value.
Then render a Mermaid flowchart in the same shape as the example in the
graph-concept skill's graph diagram. Save the result as GRAPH.md at the
workspace root (overwrite).
```

Run that monthly. The diff over time is the most honest picture of how your agent is actually evolving.
