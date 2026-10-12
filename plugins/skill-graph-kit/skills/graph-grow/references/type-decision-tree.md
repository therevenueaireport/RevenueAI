# Type Decision Tree

**The silent classification logic graph-grow runs after the plain-English diagnostic questions.** The user never sees this tree. They see the proposal it produces.

---

## The tree

Walk it top to bottom. Stop at the first YES.

```
1. Is it about one project, client, deal, campaign, or week, and will it be
   done with within a month or two?
      YES → CONTEXT overlay   (skills/context/, needs an expires: date)
      NO  ↓

2. Is it facts about the user's world (audience, offer, voice, pricing,
   competitors, rules) rather than steps to follow?
      YES → Will two or more skills need it, now or soon?
              YES → DOMAIN    (skills/domains/)
              NO  → keep it inline in the one skill that uses it.
                    The "third copy" rule extracts it later if it spreads.
      NO  ↓

3. Is it a finished deliverable that takes several steps or pulls from
   other nodes?
      YES → WORKFLOW          (skills/workflows/, composition + output contract)
      NO  ↓

4. Is it one verb, one job, no dependencies, describable without the word "and"?
      YES → CORE              (skills/core/)
      NO  → It is two things. SPLIT the request and classify each half.
```

**Not a skill at all?** Two more exits, checked before the tree:
- If it should apply to every session (tone, a hard rule, a boot step), it is identity. It goes in `SOUL.md` or `AGENTS.md`, not in `skills/`.
- If it is state (a project's status, a person, a decision and its reasons), it goes in `knowledge/` using the knowledge templates from the `init-workspace` skill.

---

## How the diagnostic answers map to the tree

| Diagnostic question (plain English) | Branch it decides |
|---|---|
| "What's the input, and what's the output?" | Separates deliverables (3) from single actions (4). Several outputs usually means a workflow. |
| "One specific thing in one step, or a finished deliverable with several steps?" | 3 vs 4 directly |
| "Will multiple other skills need to reference this?" | 2 (domain vs inline) |
| "Scoped to one project, client, or week, or something you'll use repeatedly?" | 1 |

---

## Tie-breakers

| Ambiguity | Rule |
|---|---|
| Could be a core or a workflow | If it needs any domain knowledge to do well, it is a workflow that composes a core with that domain. Cores stay knowledge-free. |
| Could be a domain or context | If it would still be true after the current project ends, domain. If not, context. |
| Could be a workflow or context | A repeatable outcome is a workflow. A one-time push is context that links to existing workflows. |
| Name collides with an existing node | Read the existing node first. Usually the request is the existing node with different inputs, or a workflow that composes it (a "cold email" request is usually a workflow composing `core/write` with audience and voice domains). |
| Still unclear after all four questions | Default to CONTEXT with a short expiry. It is the lowest-stakes bucket and can be promoted later. |

---

## Scope (org modes only)

After the type is set, in `org-admin` mode ask the four governance questions from the governance guide in the `graph-concept` skill:

1. Would two people writing this independently produce conflicting versions? → `scope: org`, name a steward (domains) or a fork policy (workflows).
2. Does it change per account, per week, or per person? → `scope: individual`.
3. Canonical knowledge about the company, buyer, or market? → `scope: org`.
4. Canonical knowledge about how one person works? → `scope: individual`.

Context overlays are always individual.

---

## Worked examples

| User says | Path through the tree | Result |
|---|---|---|
| "Turn my call notes into a follow-up email in my voice." | 1 no, 2 no, 3 yes (synthesize notes, write email, check it) | WORKFLOW composing `domains/voice`, `core/synthesize`, `core/write`, `core/critique` |
| "Remember that our buyer is the head of RevOps at 200-1,000 person software companies." | 1 no, 2 yes, used by several skills | DOMAIN `domains/audience` |
| "For the Acme renewal, everything should be formal and reference the security review." | 1 yes | CONTEXT `context/acme-renewal`, expires at renewal date |
| "Score a draft against our messaging rules." | 1 no, 2 no, 3 yes (needs the messaging domain) | WORKFLOW composing `domains/messaging` + `core/critique`, not a new core |
| "Summarize and prioritize my inbox." | 4 fails the "and" test | SPLIT: summarize is `core/synthesize`; prioritize needs priorities knowledge, so it becomes a workflow |
