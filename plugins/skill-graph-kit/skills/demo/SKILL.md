---
name: demo
description: Show the user the before/after of having a populated skill graph. Run their actual current request twice — once cold without graph context loaded, once with the populated graph (pulling from their domains). Display both outputs side-by-side. Use whenever the user says "show me the difference," "what's this actually doing," "is the graph helping," "demo this," "before and after," OR proactively offer after init-workspace seeds the user's first domain. The fastest way to make the graph's value visceral instead of theoretical.
---

# demo

Take the user's next request. Run it twice. Display both side-by-side. Let the difference speak for itself.

This is the skill that turns "this kit improves quality" from a claim into a visible artifact. Use it sparingly — once or twice — because the demo loses power if it becomes routine.

## How to run

### Step 1 — Pick the request

Two paths:
- **The user just made a request** ("write a cold email to a mid-market RevOps leader") → use that as the demo request.
- **The user asked for a demo without a specific request** → ask: "What's something you'd normally ask your agent for? I'll run it both ways."

### Step 2 — Run COLD (no graph context)

Generate the output without loading ANY of the user's domain knowledge, voice rules, ICP, positioning, or memory. Pretend the user just installed a fresh agent with no setup. Use only default model knowledge.

Label this output clearly:
> **COLD — no graph context loaded** (this is what a fresh agent gives you on day 1)

### Step 3 — Run WITH graph (full context)

Now run the same request the normal way: load the relevant workflow's composition, pull from the user's domains, apply their voice rules, check their MEMORY for patterns, honor USER.md preferences.

Label clearly:
> **WITH your graph** (pulling from: <the domains actually loaded, e.g. domains/audience>, USER.md voice)

After the output, surface WHICH nodes were loaded — by name:
> *Loaded for this response: `domains/audience` (last verified <date>), `core/write`, USER.md voice rules*

This is the "remembers me" moment. The user sees the agent name the specific knowledge it's using.

### Step 4 — Highlight what differs

Below the two outputs, surface 3-5 specific differences in plain English:

> **What changed:**
> 1. COLD says "decision-makers" generically. WITH names your specific ICP: "mid-market RevOps leaders at 200-1000 person SaaS companies."
> 2. COLD uses "leverage" and "synergies." WITH respects your banned-phrases list.
> 3. COLD opens with a question. WITH leads with the insight per your voice rules.
> ...

### Step 5 — Land the point

End with one line. Not a list.

> The first output is what a fresh agent gives anyone. The second is what your graph gives YOU. Every workflow you add deepens the gap.

## Output contract

```
## Demo: <one-line summary of the request>

### COLD — no graph context loaded
<the cold output, full text>

### WITH your graph
<the contextualized output, full text>

*Loaded for this response: <comma-separated list of nodes by name with last-verified dates>*

### What changed
1. <specific difference, named>
2. <specific difference, named>
3. <specific difference, named>

### The point
<one sentence>
```

## Quality bar

- The COLD output is genuinely cold — no peeking at the user's files. If you fail to actually run it cold, the demo is a lie.
- The WITH output names which nodes it loaded. Vague "I used your context" doesn't work. Specifics or nothing.
- Three differences minimum, five maximum. Each is a concrete pattern the user can point at.
- The closing line is one sentence. Restraint matters here.

## When NOT to run

- The user has an empty graph (no domains populated). Demo would show "WITH" output identical to COLD. Postpone until at least one domain (usually the audience or ICP) has real content, not TODO. Two or more domains make the difference sharper. If the graph is empty, offer to seed the first domain via `/graph-grow` before running.
- The user has run /demo within the last 7 days. Loses impact with repetition. Use /graph-report instead for ongoing measurement.
- The request is something the graph can't help with anyway (a one-off creative task with no domain dependencies). The demo would underwhelm.

## Failure modes to avoid

- Running both passes with graph context loaded (the COLD pass MUST be cold).
- Claiming a difference that came from the domain when it came from luck. Each named difference should trace to a specific line in a loaded node.
- Hedging the comparison ("they're both pretty good!"). Pick the differences and name them.
- Demoing on a trivial request (write a tweet). Pick something where domains visibly matter — cold email, content piece, deal prep.
- Running demo too often. Once or twice in a user's lifetime is enough. After that, /graph-report carries the message.

## The dramatic moment

If the demo lands, the user will say something like "oh." That moment is the entire point of the kit. Engineer for it — pick a request where the graph clearly matters, run both passes honestly, name the differences plainly, and let the silence work.

Don't fill that silence with explanation. The output already said it.

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt. License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
