# Novice Guide
**Read this if you're brand new and the docs are throwing words like "core," "workflow," "domain," and "context" at you. 5 minutes.**

You do not need to learn graph theory. You don't need to memorize the terminology. The agent translates between plain English and the technical words for you. This file is just so you can answer the agent's questions confidently the first few times it asks.

---

## The mental picture

Think of your AI agent as someone you just hired. To do their job, they need to know:

1. **How to do specific things.** (Write an email. Research a company. Summarize a meeting.)
2. **How to do bigger pieces of work that take several steps.** (Build a sales pipeline. Ship a newsletter. Prep for a QBR.)
3. **What's true about your world.** (Who your customers are. Your brand voice. Your pricing. Your product.)
4. **What's happening right now.** (The deal you're working on this week. The client you're talking to today. The project you started Tuesday.)

Those four buckets are the entire skill graph. Everything you ever add to the kit goes in one of them. The technical names are CORE, WORKFLOWS, DOMAINS, and CONTEXT — but you don't need those words to use the kit.

---

## The four questions that decide where anything goes

When the agent asks "what kind of thing is this?", just answer one of these four:

### 1. "Is this one specific small thing I want done in one step?"
*"Write a cold email." "Research this company." "Summarize this transcript." "Critique this draft."*

→ The agent calls this a **CORE** skill. You don't have to.

### 2. "Is this a finished deliverable that takes multiple steps and uses several smaller skills?"
*"Build me a sales pipeline." "Ship a multi-channel content drop." "Prep me for my QBR." "Tear down this competitor."*

→ The agent calls this a **WORKFLOW**. You don't have to.

### 3. "Is this knowledge or facts that multiple things will need to know about?"
*"Who our customers are." "Our brand voice." "Our pricing." "What our competitors offer." "Our positioning statement."*

→ The agent calls this a **DOMAIN**. You don't have to.

### 4. "Is this just about one specific project, client, week, or moment — something that will be done with in a month or two?"
*"The Acme deal I'm working on." "Q4 launch prep." "This week's priorities." "Prep notes for Tuesday's call."*

→ The agent calls this **CONTEXT**. You don't have to.

That's it. Four questions. Every piece of knowledge or skill you ever add fits one of them.

---

## Examples by profession

### If you're in sales
- **Small things in one step:** write a cold email, qualify a lead, summarize a discovery call, build a deck slide
- **Multi-step deliverables:** run a full discovery, build an outbound sequence, prep for a renewal conversation, run a close play
- **Knowledge everything needs:** who your ICP is, your pricing, your objection bank, your competitive intel, your product truth
- **Just-this-moment stuff:** the specific deal you're working on, your weekly priorities, prep notes for tomorrow's meeting

### If you're in marketing
- **Small things in one step:** write a headline, draft a social post, research a topic, critique a draft
- **Multi-step deliverables:** ship a campaign, build a content engine for one insight, plan a launch week
- **Knowledge everything needs:** your brand voice, your audience definition, your messaging pillars, your proof library
- **Just-this-moment stuff:** the campaign in flight, this week's editorial calendar, this client's overlay

### If you're a founder / operator
- **Small things in one step:** write an investor update, research a candidate, summarize an article
- **Multi-step deliverables:** run a hiring round, prep for a board meeting, build a quarterly plan
- **Knowledge everything needs:** your company narrative, your hiring rubric, your operating principles, your financials
- **Just-this-moment stuff:** the current quarter's priorities, this candidate's notes, this board cycle's prep

### If you're a coach / consultant
- **Small things in one step:** write a session recap, draft a one-pager, research a client's industry
- **Multi-step deliverables:** build a client onboarding, design a workshop, ship a research report
- **Knowledge everything needs:** your methodology, your frameworks, your case studies, your pricing
- **Just-this-moment stuff:** this client's engagement, this week's deliverables, prep for tomorrow's session

---

## How to answer the agent when it asks

When the agent asks **"what kind of thing is this?"** — pick the closest of these four phrasings:

| If you'd say... | The agent hears... |
|---|---|
| "It's a small thing I want done in one step." | CORE |
| "It's a deliverable that needs several steps." | WORKFLOW |
| "It's knowledge that lots of things will need." | DOMAIN |
| "It's just about this one project / client / week." | CONTEXT |

You can also just **describe what you want and let the agent classify it**. The agent will say back: "Sounds like a multi-step deliverable — I'll set it up as a workflow. The steps it'll use are: [list]. Sound right?"

You say "yes" or you say "no, it's actually more like X."

That's the whole interaction. You never have to learn the words.

---

## What if you genuinely don't know?

Two answers:

1. **Ask the agent to ask you simpler questions.** "I don't understand what you mean. Walk me through the choice in plain English." The agent will run through the four diagnostic questions above with you.

2. **Default to "it's just for this week."** When in doubt, treat new things as CONTEXT (just-this-moment stuff). It's the lowest-stakes bucket — if it turns out to be more important than that, the agent can promote it later via graph-grow. Better to start something low-stakes and promote than to over-engineer something that turns out to be a one-off.

---

## What the agent does for you that you don't see

When you say "I want a skill that turns my podcast transcript into 5 social posts," the agent silently runs through:

1. Is this one verb or several? *Several — extract, write, format.* → not a CORE, probably a WORKFLOW
2. Does it need knowledge that already exists in domains? *Yes — voice, audience.* → it'll compose those domains
3. Is it scoped to one project, or will I use it repeatedly? *Repeatedly.* → not CONTEXT
4. Verdict: WORKFLOW. Compose `domains/messaging` + `domains/icp` + `core/synthesize` + `core/write` + `core/critique`.

It then tells you in plain English: "I'll set this up as a workflow that takes a transcript, extracts the through-line, and writes 5 posts in your voice. It'll pull from your audience and brand voice automatically. Sound right?"

You never see the classification logic. You only see the proposal. You approve, the kit handles the rest.

---

## When you're ready for the technical names

After 2-3 weeks of using the kit, you'll start to notice the patterns yourself. At that point, ask for `/graph-concept`: it has the technical model. You'll find it obvious because you've been using it the whole time.

You don't need to read it now. The kit doesn't need you to know graph theory; it just needs you to know your work.

---

## The shortest possible version

- Want to do one specific thing in one step? → tell the agent "small skill"
- Want a finished deliverable that takes multiple steps? → tell the agent "multi-step thing"
- Want to record knowledge that lots of things will need? → tell the agent "knowledge"
- Just about this one project / client / week? → tell the agent "just for now"

The agent does the rest.
