# AI and technology visuals

Use for AI strategy, agent architectures, governance, adoption, economics, and maturity — these make abstract AI concepts concrete without robot imagery.

Columns: **Visual** · **Best for** (the claim it answers) · **Example use** · **Claim type** (what `select_visual.py` matches on) · **Render** (`chart` = matplotlib/native chart; `svg:<type>` = `render_svg.py <type>`; `shapes` = pptx/HTML shapes; `text` = typographic slide).

| Visual | Best for | Example use | Claim | Render |
|---|---|---|---|---|
| AI capability stack | Showing the layers needed for AI outcomes | Data, models, tools, workflows, governance, people | architecture | `svg:stack` |
| AI maturity model | Showing organizational progression | Experimenting -> enabling -> scaling -> AI-native | maturity | `svg:staircase` |
| AI use-case portfolio | Prioritizing use cases | Impact versus feasibility, with risk as bubble size | prioritization | `svg:two_by_two` |
| AI value chain | Showing where AI creates value | Insight, creation, decisions, operations, customer experience | inventory | `svg:chevron` |
| Agent architecture | Explaining roles and handoffs among agents | Research, planning, execution, QA, memory, governance | architecture | `svg:network` |
| Agent swarm diagram | Showing parallel specialist agents | Multiple researchers feeding an editor or orchestrator | architecture | `svg:network` |
| Human-AI division-of-labor map | Clarifying responsibility | AI drafts/analyzes; humans decide, approve, relate, govern | ownership | `svg:before_after` |
| Augmentation vs. automation spectrum | Distinguishing types of AI value | Assistive workflows through autonomous execution | continuum | `svg:spectrum` |
| Copilot workflow | Showing embedded assistance | User prompt -> context -> model -> suggestion -> human action | sequence | `svg:chevron` |
| Agent loop | Showing iterative autonomy | Observe -> plan -> act -> evaluate -> learn | loop | `svg:flywheel` |
| Retrieval-augmented generation diagram | Explaining grounded AI | Query -> retrieve sources -> generate answer -> cite/verify | sequence | `svg:chevron` |
| Context engineering map | Showing inputs that shape an AI response | Instructions, memory, knowledge, tools, constraints, evaluation | system | `svg:orbit` |
| Knowledge graph | Showing connected entities and relationships | Accounts, contacts, products, issues, content, intent signals | system | `svg:network` |
| Data lineage map | Showing provenance and reliability | Source system -> transformation -> model -> action | flow | `svg:chevron` |
| Trust boundary diagram | Showing security and access controls | Public data, private data, PII, model boundary, audit layer | governance | `svg:concentric` |
| AI governance framework | Showing controls | Policy, privacy, security, risk, evaluation, ownership | governance | `svg:grid` |
| Risk heatmap | Mapping likelihood and impact | Hallucination, data leakage, bias, regulatory risk | risk | `svg:two_by_two` |
| Guardrails stack | Showing safety mechanisms | Prompt policy, tool permissions, approvals, monitoring, audit | governance | `svg:stack` |
| Evaluation harness diagram | Showing how output quality is measured | Test set -> model output -> rubric -> benchmark -> iteration | sequence | `svg:chevron` |
| Model selection matrix | Comparing models by task needs | Quality, latency, cost, privacy, context length | decision | `svg:table` |
| Build / buy / partner matrix | Framing AI implementation choices | Strategic differentiation versus implementation complexity | decision | `svg:two_by_two` |
| AI economics waterfall | Showing value and cost components | Labor savings, lift, inference cost, tooling, oversight | bridge | `svg:waterfall` |
| AI ROI curve | Showing investment versus expected return over stages | Pilot costs before scale benefits | trend | `chart` |
| Workflow decomposition | Breaking a job into automatable steps | Research, synthesis, drafting, approval, publishing | sequence | `svg:chevron` |
| Task automation matrix | Sorting work | Repetitive vs. judgment-heavy; low versus high consequence | classification | `svg:two_by_two` |
| AI adoption funnel | Showing movement from access to habitual use | Enabled -> trained -> activated -> recurring -> high impact | flow | `svg:funnel` |
| AI skills ladder | Showing capability development | Prompting -> workflow design -> evaluation -> orchestration | maturity | `svg:ladder` |
| AI operating model | Showing people, platforms, governance, and use cases | Center of excellence plus embedded teams | architecture | `svg:grid` |
| AI transformation roadmap | Showing stages | Foundations -> pilots -> scale -> redesign business model | timing | `svg:chevron` |
| System of record / intelligence / action | Showing AI stack roles | CRM stores, AI interprets, workflows execute | architecture | `svg:stack` |
| Prompt-to-production path | Showing operationalization | Prompt -> prototype -> workflow -> evaluation -> governed deployment | sequence | `svg:chevron` |
| Digital labor portfolio | Showing agent roles across functions | SDR research agent, content agent, analyst agent, support agent | inventory | `svg:grid` |
| Signal-to-action architecture | Showing real-time GTM | Buyer signal -> enrichment -> decisioning -> personalized action | architecture | `svg:signature_signal_to_action` |
| AI-native organization chart | Showing redesigned function structure | Strategic owners, AI operators, specialists, governance | architecture | `svg:tree` |
| Data moat loop | Explaining defensibility | Usage -> proprietary data -> better outcomes -> more usage | loop | `svg:flywheel` |
| Learning loop | Showing why a system improves | Action -> feedback -> evaluation -> refinement | loop | `svg:flywheel` |
| Autonomy ladder | Showing degrees of delegated authority | Suggest -> recommend -> execute with approval -> execute within guardrails | maturity | `svg:ladder` |
| Confidence threshold visual | Showing how risk changes approval rules | Low-confidence outputs need review; high-confidence outputs can route | decision | `svg:spectrum` |
| Model drift chart | Showing output quality or data changes over time | Triggering reevaluation or retraining | trend | `chart` |
| AI decision rights matrix | Showing what AI can recommend or execute | By use case risk and business impact | governance | `svg:two_by_two` |

40 visuals. Get the full record for any of them with `python scripts/select_visual.py --show <id>`; list ids with `--list ai`.
