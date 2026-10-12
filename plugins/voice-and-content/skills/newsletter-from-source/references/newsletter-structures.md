# Newsletter Structure Templates

**About the examples in this file:** the episodes, teams and results below are fictional, built to show the structure. In a real issue, every number and result comes from the source.

---

## Source Summary Newsletter (primary)

**Purpose:** turn a podcast episode, interview, webinar, demo recording or transcript into an issue of executable intelligence.

### Structure template

**The rhythm rule:** balance prose paragraphs with bullets. Narrative and context in paragraphs, execution steps in bullets. Never all one or the other.

```markdown
[CONTRARIAN OR SURPRISING HOOK: 1-2 sentences, prose]
[What makes this insight non-obvious or counterintuitive]

[CREDIBILITY MARKER: a prose paragraph]
[What the episode covered and what was shown]
Example: "On this week's episode, our guest built a working lead-scoring model live,
with an AI coding assistant and no programming background. Twelve minutes from first
prompt to running code. Here's what actually matters:"

[NUMBERED INSIGHTS: 3-5]
[Each one: prose for context and strategy, bullets for execution]

1) [Insight headline: a prose paragraph]

[A strategic framing paragraph: why this matters]
Example: "Ops teams can now build the custom analytics they used to hire contractors for.
What took an outside firm two weeks happened in an afternoon, in-house. The bottleneck
is gone."

[Execution steps in bullets, when showing how]
The workflow:
- Connect an AI coding assistant to your CRM's API
- Prompt: "Analyze my last 500 closed deals and build a scoring model for new leads
  based on conversion patterns"
- Review the generated code for logic errors (ask it to explain each step)
- Test on 50 recent leads, then deploy and monitor accuracy

[The result, in prose]
Result: the guest's team reported a clear lift in scoring accuracy over the following
quarter and got hours back every week from manual qualification. (Use the guest's exact
figures and say who measured them.)

2) [Next insight headline: a prose paragraph]

[Same pattern: prose for strategy and context, bullets for tactics and steps]

[BRIDGE TO ACTION: a prose paragraph]
"The tactical shift:" or "Why this matters:"

[A prose paragraph on the strategic implication]

[NEXT STEPS: bullets]
What to do this week:
- [A specific action the reader can take today]
- [The tool, template or framework to use]
- [The metric or outcome to track]

[PUNCHY CLOSE: 1 sentence, prose]
[Reframe the shift or challenge the conventional view]
```

### Prose versus bullets

**Use prose (paragraphs) for:**
- Opening hooks and narrative setup
- Strategic context and "why this matters"
- Credibility markers and episode context
- Analysis and synthesis
- Results, outcomes and implications
- Transitions between numbered sections
- Closing lines

**Use bullets for:**
- Multi-step workflows
- Tool and configuration lists
- Prompt templates and code snippets
- How-to instructions
- Before-and-after comparisons
- Metric breakdowns
- Quick-reference action items

**The rhythm should feel like:**
Prose context, bullet execution, prose outcome.
Prose setup, bullet tactics, prose implication.

**A well-balanced section (fictional):**

```markdown
2) Ops leaders with no data background can now ship custom analytics without contractors.

What the guest demonstrated: an AI coding assistant building a lead-scoring model from
a plain-English prompt. Prompt to production-ready code in twelve minutes. No data
science degree required.

The exact workflow:
- Install the AI coding assistant (a few minutes of setup)
- Connect it to your CRM's API
- Run this prompt: "Analyze my last 500 closed deals. Build a scoring model for new
  leads based on company size, industry, engagement and buying signals"
- Review the code it writes (ask it to explain its logic)
- Test on 50 recent leads to check accuracy
- Deploy

The result: the guest's team said scoring accuracy improved over the next quarter and
manual qualification shrank from most of a day each week to under an hour. The ops team
went from taking orders to building.
```

**Why it works:**
- Opens with a strategic claim (prose)
- The demo summary sets context (prose)
- Workflow steps are scannable (bullets)
- The outcome and its impact are explained (prose)
- Readable, not overwhelming

### Source-specific elements

**Extract from demos and screen shares:**
- The exact workflow steps shown on screen
- Tool configurations and settings
- Prompt templates used
- Before-and-after results shown

**Frame for the reader:**
- Impact on pipeline, revenue or efficiency
- Team implications: who does this work now, and who does it with AI
- Time saved, quantified from the source
- The advantage gained

**Extraction pattern (fictional):**

The guest says: "I opened the coding assistant, typed 'build me a lead-scoring model using our CRM data,' and twelve minutes later I had working code."

The issue turns that into:

"2) Ops leaders with no data background can now build custom analytics in minutes, not weeks.

What the guest demonstrated: an AI coding assistant, used by someone with no programming experience, building a lead-scoring model. No data science team. Prompt to working code to deployed in twelve minutes.

The strategic shift: your ops team just became far more capable. Work that needed a contractor and a two-week turnaround now happens the same day.

How to do it:
- Install the coding assistant
- Connect it to your CRM's API
- Prompt: 'Analyze my last 500 closed deals and build a scoring model for new leads based on conversion patterns'
- Review the code, then deploy"

### Working from a raw transcript

1. Read the whole transcript once before extracting anything.
2. Mark every moment with a number, a named workflow, a disagreement with conventional wisdom, or a "here's what we got wrong." These are your candidate insights.
3. Rank the candidates by value to the reader, not by when they were said.
4. Keep the top three to five. Cut the rest, however interesting.
5. Pull verbatim quotes with timestamps for each one you keep.
6. Confirm the thesis with the user before drafting.

---

## News Analysis Newsletter (secondary)

**Purpose:** turn news, announcements and research releases into insight and action for the reader.

### Structure template

**The rhythm rule:** prose for analysis and context, bullets for tactical responses and action items.

```markdown
[CONTRARIAN TAKE ON THE NEWS: 1-2 sentences, prose]
[Your view on what everyone is missing]

[PATTERN IDENTIFICATION: a prose paragraph]
"Three things are happening at once that most people are treating as separate:"

[NUMBERED ANALYSIS: 3 connected insights]
[Prose for analysis; bullets only for tactical breakdowns or lists]

1) [News item or trend: a prose paragraph]

[Prose: why the mainstream take is wrong or incomplete, what is actually happening,
the strategic pattern]

[Optional bullets, only to list specific evidence]
Evidence:
- [Specific data point 1, with source]
- [Specific data point 2, with source]

[Prose: the implication for the reader's team]

2) [A related development: a prose paragraph]

[Prose: the connection to #1, the pattern emerging, what it means]

3) [A third data point: a prose paragraph]

[Prose: how this completes the pattern; the synthesis]

[SYNTHESIS: a prose paragraph]
"What this means for your team:"

[Prose on the strategic implications]

[TACTICAL RESPONSE: bullets]
What to do this week:
- [An immediate step, with a specific tool or approach]
- [A positioning shift to communicate to the team]
- [A process change to make, with a timeline]

[PUNCHY CLOSE: 1 sentence, prose]
[A one-sentence reframe of the landscape]
```

### When to use bullets in news analysis

**Use bullets for:**
- Several evidence points supporting one argument
- Tactical response actions
- Tool and resource lists
- Comparative data points

**Keep prose for:**
- Your contrarian thesis
- Analysis of what is actually happening
- Strategic implications
- Synthesis and pattern-finding
- Opening and closing lines

**A well-balanced section (fictional):**

```markdown
1) A major AI lab shipped a model that writes much better code. Everyone is calling it
a developer release. They're missing the revenue-team impact entirely.

The mainstream take is about engineers shipping features faster. True, but incomplete.
The bigger shift: ops teams can now build tools that used to need engineering. Custom
dashboards, integration demos and automation scripts that sat on backlogs for months
can ship the same day.

The impact across three functions:
- Revenue ops: custom analytics without data contractors (weeks become a day)
- Sales engineering: custom integration demos built live on the call (weeks become hours)
- Marketing ops: attribution models and reporting tools without an engineering sprint

The implication: your ops teams just became builders, not implementers. The "we need
engineering" bottleneck is gone for internal tools. Teams that reorganize around this
will outpace teams still waiting on the ticket queue.
```

### News-specific elements

**Find the non-obvious connection:**
- Do not summarize announcements
- Connect two or three developments that look separate
- Show the pattern others miss

**Test every item against the reader's world:**
- How does this change buyer behavior?
- How does this shift competitive dynamics?
- What does sales, marketing or customer success need to do differently?

---

## Quality filters (both templates)

### The "so what?" test

Every section must pass:

1. **Is it specific?** Not "AI will transform sales." Instead: "Reps who used AI call prep at [source team] needed fewer discovery calls per deal without losing deal quality."
2. **Is it actionable?** The reader can do it today, not "consider" or "think about" it.
3. **Is it quantified?** Time saved, cost reduced or performance gained, from the source.

### The "different, not more" test

From studying paid newsletters:
- More tips is free content.
- A different framework or insight is paid-tier value.

More: "10 more AI tools for sales prospecting"
Different: "Why AI prospecting tools fail without execution infrastructure"

### The cognitive monopoly test

Can the reader get this elsewhere?
- Generic best practices: yes, so it fails
- Specific implementation experience from the source: no, so it passes
- A summary of an industry report: yes, so it fails
- A contrarian reading of that report: no, so it passes

Full filters, ladder and examples: [quality-filters.md](quality-filters.md).

---

## Length guidelines

**Source summary:**
- Total: 600-900 words
- Opening hook: 50-75 words at most
- Each numbered insight: 100-150 words
- Tactical close: 50-75 words

**News analysis:**
- Total: 500-800 words
- Opening and pattern setup: 75-100 words
- Each numbered analysis: 125-175 words
- Synthesis and tactical response: 100-150 words

**Why these lengths:**
- Short enough to read in three or four minutes
- Long enough to deliver depth worth paying for
- Built for signal over noise

---

## Common mistakes

### 1. The tutorial trap
Wrong: step-by-step instructions with no strategic context.
Right: strategic framing first, then execution steps.

### 2. The news aggregation trap
Wrong: summarizing what happened.
Right: analyzing what it means and what to do.

### 3. The obvious insight trap
Wrong: "AI can help sales teams be more efficient."
Right: "Teams that bolted AI onto their old process saw small gains. Teams that redesigned the workflow around it saw large ones. Here is the redesign." (With the source's numbers.)

### 4. The feature description trap
Wrong: explaining what tools can do.
Right: showing what problems they solve and how to implement.

### 5. The hedge language trap
Wrong: "This might be helpful for some teams."
Right: "This gives the ops lead who builds the Monday report most of their Monday back."

### 6. The invented precision trap
Wrong: adding a percentage the source never said, to sound specific.
Right: use the source's number, ask the user for one, or make the claim specific through context and exact steps.

---

## Template selection guide

**Use the source summary template when:**
- The source is an episode, interview, webinar or transcript
- It includes a screen-share demo
- The focus is how to execute
- There are several tactical steps to extract

**Use the news analysis template when:**
- The source is news, announcements or research releases
- The focus is strategic implications
- You are connecting several data points
- You are challenging the conventional reading

**Use a hybrid when:**
- An episode covers breaking news
- News needs a demo to show its application
- Combine the news context with the episode's tactical response
