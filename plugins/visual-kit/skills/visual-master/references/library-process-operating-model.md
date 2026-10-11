# Process, workflow, and operating-model visuals

Use when explaining how work flows, who owns what, how systems connect, and when things happen — AI workflows, revenue operations, transformation programs.

Columns: **Visual** · **Best for** (the claim it answers) · **Example use** · **Claim type** (what `select_visual.py` matches on) · **Render** (`chart` = matplotlib/native chart; `svg:<type>` = `render_svg.py <type>`; `shapes` = pptx/HTML shapes; `text` = typographic slide).

| Visual | Best for | Example use | Claim | Render |
|---|---|---|---|---|
| Linear process flow | A simple sequence | Research -> strategy -> execution -> measurement | sequence | `svg:chevron` |
| Chevron process | A clean executive sequence | Diagnose -> decide -> deploy -> optimize | sequence | `svg:chevron` |
| Swimlane diagram | Showing ownership across teams | Marketing, sales, product, customer success handoffs | ownership | `svg:swimlane` |
| BPMN-style process map | Detailed operational workflow | Lead routing, approval, onboarding, campaign production | sequence | `svg:swimlane` |
| Service blueprint | Showing customer-facing and back-office steps | Enterprise onboarding journey | ownership | `svg:swimlane` |
| User journey map | Showing customer experience over time | Awareness through advocacy | customer | `svg:columns` |
| Journey with emotional curve | Showing friction and moments of delight | Buying or onboarding experience | customer | `svg:journey_curve` |
| Touchpoint map | Showing all interactions with a brand | Website, newsletter, sales call, webinar, product | customer | `svg:grid` |
| Decision tree | Showing conditions and routing | Which accounts receive ABM, nurture, or outbound motion | decision | `svg:tree` |
| If/then workflow | Explaining automation logic | If intent spike occurs, then trigger account play | sequence | `svg:chevron` |
| Trigger-action loop | Showing event-driven operating model | Signal -> enrichment -> orchestration -> outcome | loop | `svg:chevron` |
| Human-in-the-loop workflow | Clarifying AI boundaries | AI drafts, human approves, system executes, team learns | ownership | `svg:swimlane` |
| Agent workflow | Explaining multi-agent systems | Research agent -> analyst -> writer -> reviewer -> publisher | sequence | `svg:chevron` |
| Orchestration diagram | Showing tools, data, and agents | CRM, warehouse, LLM, workflow engine, human reviewer | architecture | `svg:network` |
| RACI matrix | Showing role clarity | Responsible, accountable, consulted, informed | ownership | `svg:table` |
| DACI matrix | Showing decision-making roles | Driver, approver, contributor, informed | ownership | `svg:table` |
| Operating cadence diagram | Showing recurring rituals | Weekly pipeline review, monthly planning, quarterly reset | timing | `svg:columns` |
| Closed-loop workflow | Showing learning and optimization | Signal -> action -> measurement -> insight -> refinement | loop | `svg:flywheel` |
| OODA loop | Showing rapid decision cycles | Observe -> orient -> decide -> act | loop | `svg:flywheel` |
| PDCA loop | Showing continuous improvement | Plan -> do -> check -> act | loop | `svg:flywheel` |
| Funnel-to-flywheel transition | Showing a philosophy shift | Acquisition funnel feeding retention and advocacy loop | transition | `svg:funnel_flywheel` |
| Handoff map | Showing where work or data moves between functions | Marketing -> SDR -> AE -> CS | ownership | `svg:chevron` |
| Exception flow | Showing what happens when standard workflow fails | High-risk account or low-confidence AI output | sequence | `svg:tree` |
| Escalation ladder | Showing governance path | Frontline -> manager -> steering committee -> executive sponsor | hierarchy | `svg:ladder` |
| Process maturity ladder | Showing current and desired operational state | Manual -> automated -> intelligent -> autonomous | maturity | `svg:staircase` |
| Capability map | Showing business capabilities | Strategy, content, demand, sales enablement, analytics | inventory | `svg:grid` |
| Reference architecture | Showing technical components | Data layer, model layer, application layer, governance layer | architecture | `svg:stack` |
| Layered architecture | Explaining an AI stack | Foundation models -> tools -> agents -> workflows -> outcomes | architecture | `svg:stack` |
| Data flow diagram | Showing how information moves | Website signals -> CDP -> CRM -> campaign activation | flow | `svg:chevron` |
| Integration map | Showing systems and connectors | CRM, MAP, warehouse, analytics, enrichment, AI tools | architecture | `svg:network` |
| Control tower view | Showing centralized visibility | Pipeline health, signals, actions, owners, risks | visibility | `svg:dashboard` |
| Command-center dashboard | Showing key live operational measures | Targets, trends, blockers, next actions | visibility | `svg:dashboard` |
| Kanban board | Showing work status | Backlog, in progress, review, launched | status | `svg:columns` |
| Roadmap lane | Showing workstreams over time | Product, brand, demand, ops, enablement | timing | `svg:gantt` |
| Now / next / later roadmap | Showing prioritization without fake precision | Near-term, upcoming, exploratory initiatives | timing | `svg:columns` |
| Gantt chart | Showing timing and dependencies | Launch plan across teams | timing | `svg:gantt` |
| Critical-path diagram | Showing dependencies that determine timing | Product readiness, customer proof, launch, sales enablement | timing | `svg:network` |
| Milestone map | Showing major moments | Research complete, beta, launch, expansion | timing | `svg:timeline` |
| Release train | Showing recurring launch cadence | Monthly campaign, quarterly product, annual category event | timing | `svg:timeline` |
| Implementation wave diagram | Showing phased rollout | Pilot -> validate -> scale -> institutionalize | timing | `svg:chevron` |
| Adoption curve | Showing groups that adopt at different rates | Innovators, early adopters, mainstream teams | distribution | `chart` |
| Change-management journey | Showing organizational stages | Awareness -> skill -> adoption -> reinforcement | sequence | `svg:chevron` |
| Capability-building blueprint | Showing people, process, data, and technology | AI transformation program structure | architecture | `svg:grid` |

43 visuals. Get the full record for any of them with `python scripts/select_visual.py --show <id>`; list ids with `--list process`.
