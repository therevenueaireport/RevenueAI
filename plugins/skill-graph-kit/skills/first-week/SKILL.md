---
name: first-week
description: Walk a brand-new user through their first 5 graph-grow operations with full hand-holding. Use whenever the user's GRAPH_CHANGES.md shows fewer than 5 graph-grow operations and no GRADUATE line, OR says "walk me through this," "I'm new," "guide me," "I don't know what I'm doing," "what's a workflow?" OR graph-grow detects beginner-level confusion. One teaching moment per add, in plain English. Self-retires after 5 successful adds by writing a GRADUATE entry.
---

# first-week

A patient guided tour — not a single response. The agent's job is to make 5 successful graph-grow ADD operations happen with the user fully in the driver's seat. After that, this skill stops triggering.

## Open the tour

Say to the user (in plain English):

> Welcome. The kit can feel overwhelming the first few times, so I'll walk you through your first 5 additions with full hand-holding. After that, you'll know the rhythm and we can drop the training wheels.
>
> The kit has exactly four kinds of things. You don't have to memorize the technical names — I'll translate.
>
> 1. **Small one-step skills.** "Write a cold email." "Research this company."
> 2. **Multi-step deliverables.** "Build me a pipeline." "Ship a content drop."
> 3. **Knowledge that lots of things will need.** "Who our customers are." "Our brand voice."
> 4. **Just-for-now stuff scoped to one project / client / week.** "The Acme deal."
>
> That's the whole vocabulary. I'll ask plain-English questions and figure out the type for you.
>
> Ready to add your first one? Just tell me what you wish your agent could do that it can't right now.

Wait for the user to describe something.

If `/init-workspace` already seeded a first domain (such as the audience file), count it as addition 1 and open with "You've already made your first addition. Four to go."

## Walk through each of the 5 additions

For each of the user's 5 first additions:

1. Listen to what they describe in their own words.
2. Ask diagnostic questions in plain English (NEVER "is this a core or workflow"):
   - "What's the input you'd give it, and what's the output you'd expect back?"
   - "Is this one specific thing in one step, or a finished deliverable with several steps?"
   - "Will other skills need to know this? Or is it specific to this task?"
   - "Is this for one specific project, or something you'll use over and over?"
3. Classify silently. Use the Type Decision Tree that ships with the `graph-grow` skill.
4. Surface the proposal in plain English:
   > "Based on what you described, this sounds like a [plain-English type] — I'll set it up so it [what it'll do]. It'll pull from [list of existing nodes it references]. Sound right?"
5. Run `/graph-grow` ADD with the user's approval.
6. Show them the file before saving.
7. Validate after saving (`/graph-validate`).
8. Celebrate the addition explicitly:
   > "That's 1 of 5. The agent can now do this for you any time you ask. Want to add another, or take a break and use it?"

## After each addition, teach ONE micro-lesson

Use the 5 additions to teach 5 things, one at a time. Don't dump them at the start.

| Addition # | Micro-lesson |
|---|---|
| 1 | "Notice I never made you name a 'type' — I asked plain questions. That's how every addition works." |
| 2 | "When you described this, you said 'use the customer profile we built last time' — that's exactly how the graph saves you typing. Previous knowledge just links in." |
| 3 | "This one was knowledge, not a skill — I put it in a different place so other skills can reference it without copying it." |
| 4 | "We already have 3 places that need to know your audience. The third copy triggers the agent to extract it into one shared place. That's how the graph stays clean." |
| 5 | "You've now added 5 things. Tomorrow when you ask for any of them by name, the agent loads just that one file plus what it needs — not the whole kit. That's why this stays fast." |

## Graduation

After the 5th successful add:

> You've graduated. From here on, when you want to add something, just ask /graph-grow directly — same conversation, no training wheels.
>
> Three things to remember:
> 1. **You never need to use the words "core / workflow / domain / context."** Describe what you want in your own language; I classify.
> 2. **When in doubt, start it as "just for now" (context).** I can promote it later if it turns out to be more useful.
> 3. **Once a week, run /graph-evolve.** It'll tell you what the kit learned about how you actually work, and propose improvements. Approve the good ones, reject the bad ones — the kit gets smarter on its own.
>
> I'll stop triggering /first-week from now on. If you ever want hand-holding again, just say "walk me through this."

Append a line to `GRAPH_CHANGES.md`:
```
YYYY-MM-DD  GRADUATE  user completed first-week tour with 5 successful adds
```

This is the signal that future sessions should NOT auto-trigger first-week. (INIT, MIGRATE, and GRADUATE lines are not graph-grow operations and never count toward the five.)

## Quality bar

- NEVER use the technical words "core / workflow / domain / context" during the 5 additions.
- NEVER move to the next step without explicit confirmation.
- Each of the 5 has its own teaching moment — but only one per add.
- The user finishes with 5 real, usable nodes — not toy examples.
- After graduation, stop volunteering hand-holding.

## Failure modes to avoid

- Lecturing about graph theory. (The kit teaches by doing.)
- Forcing the user to pick a type when they don't know. (Always classify silently.)
- Marathoning all 5 in one sitting. (Better to stop after each and let them use what they just built.)
- Skipping the celebration after each add. (Beginners need the reps to feel they're winning.)
- Surfacing technical features (signals, evolve, validate) before the 5 adds. Save those for graduation.

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt (Coach K). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
