---
name: icp-reader-test
description: >
  Test content, subject lines, offers, prices and product ideas against a named-by-role
  persona built from your own ideal customer profile, before you publish or build.
  Builds the persona first if you do not have one (role, company size, pressures, what
  they skim, what makes them forward or unsubscribe, how they buy), then scores the asset
  on a six-dimension rubric, runs offers through buying rules, checks secondary readers,
  and returns a verdict, the top three fixes and the cheapest real-reader test.
  Triggers on: "reader test," "ICP test," "would my buyer read this," "test this subject
  line," "will this land," "would they pay for this," "pressure-test this offer," "test
  this product idea against my ICP," "build a reader persona," or any request for audience
  feedback before publishing.
---

# ICP Reader Test

A fast first filter for anything aimed at your buyer or reader: a newsletter issue, a subject line, a teaser or call to action, a landing page, a sponsor placement, a membership offer, a price, a social post, or a product or software idea.

The test works by simulating one specific person: a persona built from your own ideal customer profile and named by role ("the Head of RevOps," "the Founder-Seller"), not by a cute first name. The role name keeps everyone honest about who this is and stops the persona from drifting into a character.

**The persona is a model, not data.** Its reaction is a fast way to catch weak work before real readers do. It never replaces real reader signal: replies, filtered votes, survey answers, paid conversions, renewals. Every run ends with what to test on real people.

## When to use it

- Before sending: an issue, a subject line, a teaser, a post.
- Before launching: a landing page, an offer, a price, a sponsor package.
- Before building: a product, a feature, a paid tier, a course, a tool.
- After a miss: to diagnose why something underperformed, by checking which dimension the persona would have flagged.

## Step 0: Get or build the persona

Check whether the user already has a reader persona (in a file, a previous conversation, or a brand or positioning doc). If they do, load it and confirm the data date. If they do not, build one with the template in [references/persona-template.md](references/persona-template.md). Do not run the test against a generic "B2B buyer." A test against nobody in particular returns advice that fits nobody in particular.

Minimum viable persona (enough to run a first test, refine later):

1. Role, company size band, and who they report to
2. The decisions they own (buy, renew, expand, kill, budget, hire, report upward)
3. What they are measured on, and their biggest fear
4. Where and how they read (phone in a meeting gap, desktop triage, forwarded by a boss)
5. What makes them forward something, and to whom
6. What makes them unsubscribe, unfollow or ignore
7. How they buy: what they can sign alone, what needs approval, what they compare you to

Tag every trait with its evidence level:

| Tag | Meaning | Example source |
|---|---|---|
| **[Measured]** | Comes from your own data with a date | Subscriber export, CRM closed-won list, survey, paid-conversion data |
| **[Reported]** | The persona's peers told you directly | Interviews, reply threads, sales call notes |
| **[Inferred]** | Reasoned from measured facts, not measured | "Probably promoted from a VP role," "likely owns the tool budget" |
| **[Assumed]** | A placeholder until you have data | Anything filled in to get started |

Two illustrative fictional personas, fully built, are in [references/example-personas.md](references/example-personas.md). Use them to see the depth a persona needs, not as a substitute for your own.

### Secondary readers

Most content and most offers reach more than one person. Define one or two secondary personas around the primary:

- **The forwardee:** the person the primary forwards it to with "can we do this?" Usually the implementer. Often a different buyer with a different budget and different needs (prompts, templates, step-by-step material).
- **The broad reader:** the large, average-engagement segment of your audience. Matters for reach, sponsors and list growth; rarely the buyer.

Secondary readers get one line each in every test. Their job is to stop you from optimizing for the primary in a way that alienates everyone else, or to catch content that belongs to the forwardee, not the primary.

## Step 1: Identify the asset

Name what is being tested, because each asset type is judged on a different window:

| Asset | The window that matters | Main risk |
|---|---|---|
| Subject line + preview text | The inbox row, on a phone | Ignored or deleted unopened |
| Issue, article, post | First two lines, then the skim | Opened, skimmed, nothing forwarded |
| Teaser or call to action | One sentence | Click with no follow-through, or no click |
| Landing page | Headline, subhead, first screen | Bounce before the offer is understood |
| Sponsor placement | Disclosure and relevance | Trust damage that outlasts the revenue |
| Offer, price, membership | The buying rules | "Not my budget" or "I already have that" |
| Product or software idea | The buying rules plus usage | Bought once, never used, not renewed |

## Step 2: The 10-second read

Read only what the persona would see first: subject line, preview text and first two lines, or the post's first two lines before the fold, or the landing page headline and subhead. Read them as the persona would, on the device and in the moment from the persona file.

Say plainly: **keeps reading**, **skims**, or **deletes**, and why. Most content fails here, so this verdict carries more weight than the scores that follow.

## Step 3: Score the six dimensions

Score 1 to 5 on each. Calibrate every score against the persona's own priorities, not a general standard of quality.

| Dimension | The question | 1 looks like | 5 looks like |
|---|---|---|---|
| **Decision relevance** | Is it tied to a live decision this persona owns? | Interesting, no decision attached | Names their decision in the first lines (buy, renew, kill, budget, report upward) |
| **Evidence** | Are claims sourced, dated, with sample sizes shown? | Unsourced or recycled statistics | Every number has a source, a sample and a date; vendor research labeled as vendor research |
| **Actionability** | Can they do or forward something this week? | Theory, trend list, "the future of" | A test, memo, scorecard, checklist or kill criterion they can use today |
| **Upward value** | Does it make their next conversation with their boss, board or CEO easier? | Nothing they could repeat upward | A line, chart or decision rule they would paste into their next update |
| **Trust** | Is it independent, with no hidden agenda? | Pitch dressed as content, undisclosed sponsor | Clear about who benefits; disagrees with vendors when the evidence does |
| **Time cost** | Is the value worth the time it takes? | Ten minutes to reach the point | Useful in the time the persona actually has (often under ten minutes) |

Adapt the labels if your persona is not a leader. For an individual contributor, "Upward value" becomes "Career value" (does it make them look sharp to their manager or peers). For a founder, it becomes "Investor or team value." Keep six dimensions; change the wording, not the discipline.

**Reading the scores:**

- Any **1** is a blocker. Fix it before anything else, whatever the average.
- **Decision relevance and Time cost below 3** together means the persona will not read past the fold. Restructure, do not polish.
- **Evidence and Trust below 3** together means the persona will read it and quietly discount you. That damage compounds over issues.
- An average of **4.0 or above** with no score under 3 is ready to test on real readers.

## Step 4: For offers, prices and products, run the buying rules

Apply these to any offer, membership, price, paid tier or product idea. Each one comes from the persona file's buying section.

1. **Who signs and who uses?** These are often different people. A leader signs; an operator uses. A product the signer must log into weekly will usually fail. A product that delivers into the signer's inbox, calendar or existing meeting usually wins. A product the user loves but the signer cannot justify will not get bought.
2. **What decision does it change?** If it does not change a buy, renew, kill, budget, hire or report-upward decision, a leader will not pay for it. An operator might, if it saves real hours.
3. **What does it replace, and what does the alternative cost?** List the real alternatives the persona already has: a general AI assistant subscription, free benchmark reports, a peer community membership, an advisory or research subscription, an internal analyst's time, doing nothing. Price and position against those, not against an empty field.
4. **Which price band is it in?** Every persona has bands with different buying motions. Fill these from the persona file:
   - **Self-serve band:** a card swipe with no approval
   - **Expense band:** an individual or executive expense without procurement
   - **Program band:** needs a business case, procurement, or a budget line
   Crossing a band changes who decides and how long it takes. Price just under a band edge unless the value clearly justifies the next motion.
5. **Cold start:** anything that promises peer benchmarks, community or network value must say how many peers are in it on day one. An empty benchmark or a quiet community kills trust faster than a missing feature.
6. **Proof of value at renewal:** name the one number the persona would point to when deciding to renew (money saved, a bad deal or pilot killed early, hours returned, a board or leadership meeting that went well). If you cannot name it, the renewal is at risk before the first sale.

Give a verdict: **Buy**, **Buy if** (name the condition), or **Pass**, with the rule that decided it.

## Step 5: Secondary check

One line each on how the forwardee and the broad reader react. Flag any case where the content belongs to the forwardee (the primary would skim it and pass it down) and suggest whether to retarget it, split it, or keep it as forwardable material on purpose.

## Step 6: Fixes and the real-reader test

Give the three most important specific edits, ranked by impact, with rewritten lines where useful. A fix names the line and the replacement, not a direction ("make it more specific" is not a fix).

Then name the cheapest test on real people that would confirm or overturn the persona's verdict:

- **Subject lines:** split test two versions on a small slice of the list before the full send.
- **Content ideas:** a one-click vote in the current issue, filtered for bots.
- **Offers and prices:** a reply question ("would you pay X for Y? reply yes or no"), a short survey item, or a limited founding-seat offer with a real payment link.
- **Product ideas:** five conversations with people who match the persona, or a waitlist with a deposit.

## Output format

```
**The [persona role]'s take:** "<one or two sentences in the persona's voice, first person, blunt>"

**10-second read:** <keeps reading / skims / deletes, and why>

| Dimension | Score (1-5) | Why |
| --- | --- | --- |
| Decision relevance | | |
| Evidence | | |
| Actionability | | |
| Upward value | | |
| Trust | | |
| Time cost | | |

**Average:** <x.x>  **Blockers:** <any 1s, or none>

**Would they buy?** (offers and products only) Buy / Buy if ... / Pass, with the deciding buying rule

**Forwardee:** <one line>  **Broad reader:** <one line>

**Top 3 fixes:**
1. ...
2. ...
3. ...

**Test it with real readers:** <the cheapest real-world test>

**Persona data date:** <date of the data the persona was built on; list any [Inferred] or [Assumed] traits that drove the verdict>
```

## Running a batch

When testing several options at once (five subject lines, three offer framings, a list of product ideas):

1. Run the 10-second read on all of them first and cut anything that gets "deletes."
2. Score the survivors in one table, one row per option.
3. Pick a winner and a runner-up, and explain the deciding dimension.
4. Recommend testing the winner against the runner-up on real readers, not the winner alone.

## Keeping the persona honest

- **Backtest it.** Before trusting a new persona, run it against your five best and five worst past pieces (by replies, filtered votes, conversions). If it cannot tell them apart, it is not modeling your reader yet. Revise the traits that would have predicted the difference.
- **Label inferred traits.** Never present the simulated reaction as data. When an [Inferred] or [Assumed] trait drives a verdict, say so in the output.
- **Measure engagement with care.** Raw clicks are inflated by email security scanners that open and click links automatically. Use filtered votes, replies, re-opens, forwards and payments. A persona built on raw click data is built on bots.
- **Refresh on new data.** Update the persona when a new subscriber export, survey, closed-won analysis or paid-conversion data arrives, and record the date of the data used.
- **Be blunt.** The persona's value is catching weak work before real readers do. A polite persona is a useless one.

## Rules for rewritten copy

When the test produces rewritten lines, write them in the user's voice. If the user has a voice profile (for example, one built with the `voice-builder` skill in this pack), apply it. Otherwise default to spartan and professional: no jargon, no hype, no em dashes, and never the "it's not this, it's that" construction.

## Related skills

- `voice-builder`: define the personal voice that rewritten copy should follow.
- `social-post`: write the post, then test the hook here.
- `newsletter-from-source`: write the issue, then test the subject line and first two lines here.

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt (Coach K). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
