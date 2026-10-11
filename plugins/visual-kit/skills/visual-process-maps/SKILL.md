---
name: visual-process-maps
description: "Build a PROCESS, WORKFLOW, or OPERATING-MODEL visual - sequence, ownership, cadence, timing, or architecture. Use for linear and chevron flows, swimlanes, BPMN and service blueprints, journey maps, decision trees, if/then and trigger-action loops, human-in-the-loop and agent workflows, RACI/DACI, operating cadence, OODA/PDCA/closed loops, roadmaps (now/next/later, Gantt, milestones), maturity ladders, capability maps, reference and layered architecture, and data-flow and integration maps. Triggers on \"map the process\", \"who owns what\", \"swimlane this\", \"show the workflow / operating model / roadmap / architecture\", or a process passage that visual-cue flagged. Renders via visual-master (scripts/render_svg.py)."
---

# Visual Process & Operating-Model Maps

Use these to make a **sequence, an ownership boundary, a cadence, timing, or an architecture** legible - especially when explaining AI systems, revenue operations, or a transformation program.

## Claim -> visual

| The claim is about... | Use |
|---|---|
| A simple sequence | linear flow; chevron for a clean exec sequence |
| Ownership across teams / handoffs | swimlane; handoff map |
| Detailed operational workflow | BPMN-style map; service blueprint |
| Customer experience over time | user journey (add an emotional curve to show friction) |
| Conditions & routing | decision tree; if/then workflow |
| Event-driven operating model | trigger-action loop |
| AI boundaries | human-in-the-loop; agent workflow; orchestration diagram |
| Role clarity | RACI (DACI for decision roles) |
| Recurring rituals | operating-cadence diagram |
| Continuous improvement | closed loop; OODA; PDCA |
| Timing & dependencies | Gantt / critical path; now-next-later to avoid fake precision |
| Phased rollout / maturity | implementation waves; maturity ladder (manual -> autonomous) |
| Business or technical capabilities | capability map; reference / layered architecture |
| How information moves | data-flow diagram; integration map |
| Centralized visibility | control tower / command-center view |

## Discipline

- One clear direction: left-to-right or top-down, never both in one diagram.
- Limits: <=6 chevron steps, <=5 swimlanes readable at slide size.
- Show exception / escalation paths **only if they are the point** - otherwise they clutter.
- Title = the takeaway ("Every AI output is drafted by an agent and approved by a human before it ships"), not "Our workflow".

## Build

Render through **visual-master** `scripts/render_svg.py` (process family); shortlist with `scripts/select_visual.py "<claim>" --family process`. Related: **visual-ai-systems** (agent and model architecture), **visual-cue** (detection), **visual-storytelling** (framing).

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt.*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
