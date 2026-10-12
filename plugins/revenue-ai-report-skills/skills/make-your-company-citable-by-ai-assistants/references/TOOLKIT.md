# Citable by AI Toolkit: Buyer Question Set, AGENT Grid, and the Fix Library

**Use this file when:**
- Buyers arrive with a shortlist formed and you were not on it.
- You asked an AI assistant about your category and it named competitors, not you.
- Your pricing, security, or implementation answers live only in decks, PDFs, or sales calls.
- You are about to commission "AI search" content and want to know which pages matter first.

This file holds the instruments. The SKILL.md holds the logic. The five checks are AGENT ([AGENT, a framework from The Revenue AI Report](https://www.therevenueaireport.com/frameworks/agent)): **A**nswerable, **G**rounded in evidence, **E**asy for a machine to read, **N**amed human attached, **T**rail back to the source. You score buyer questions, not pages, because a buyer asks a question and the assistant goes looking for a page that answers it.

---

## 1. The audit sequence

| Step | What you do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1 | Build the ten pre-shortlist buyer questions | Question set | 15 min |
| 2 | Sample what assistants say now | Answer log | 15 min |
| 3 | Find the public page that answers each question | Page map | 10 min |
| 4 | Score each question on the five checks | Question-by-check grid | 15 min |
| 5 | Separate missing pages from badly written pages | Diagnosis column | 5 min |
| 6 | Order fixes by questions unlocked | Fix list | 10 min |
| 7 | List what you will not answer publicly | Do-not-publish list | 5 min |
| 8 | Re-ask two weeks after publishing | Re-test log | 15 min |

---

## 2. Step 1: Build the buyer question set

Use the buyer's words, not yours. A question in your internal language ("does it support multi-entity rollups?") is not the question an assistant receives ("can it handle several subsidiaries?").

### Where to find the real questions

| Source | System category | How far back | What to pull |
|---|---|---|---|
| First-call recordings | Call recorder | Last 90 days | The questions buyers ask in the first ten minutes |
| Sales team chat | Team chat | Last 90 days | Questions reps forward to experts |
| Security questionnaires and RFPs | Shared drive, deal desk | Last 12 months | Recurring questions, especially the first five |
| Site search and chat logs | Website analytics, site chat | Last 90 days | What visitors type |
| Lost and no-decision notes | CRM | Last two quarters | Questions that went unanswered |
| Inbound form free text | Marketing automation | Last 90 days | What people ask before talking to anyone |

### Question categories to cover

| Category | Example buyer phrasing | Pre- or post-shortlist |
|---|---|---|
| What it is and who it is for | "What does [company] do and who uses it?" | Pre |
| Pricing model | "How is [company] priced?" | Pre |
| Cost range | "Roughly what does it cost for a team of 200?" | Pre |
| Security and data handling | "Is [company] compliant with [standard]? Where is data stored?" | Pre |
| Integrations | "Does it work with our CRM?" | Pre |
| Implementation | "How long does it take to roll out?" | Pre |
| Results | "What results do customers see?" | Pre |
| Comparison | "[Company] vs [alternative]?" | Pre |
| Fit and non-fit | "Is it right for a company our size?" | Pre |
| Support and terms | "What support is included? Is there a minimum term?" | Often post |

**Rule:** take the ten most frequent pre-shortlist questions. Post-shortlist questions wait. The SKILL.md decision rule: fix what buyers ask before shortlisting first.

---

## 3. Step 2: Sample what assistants say now

One sample is a signal, not a measurement. Assistant answers vary by model and by day.

| Setting | Rule of thumb |
|---|---|
| Assistants | Two or three of the general-purpose assistants your buyers use |
| Phrasings per question | Three: with your name, category-only (no name), and a comparison |
| Sessions | Fresh session each time, logged out or with memory off where possible |
| Repeat | Two sampling rounds, at least a few days apart |
| Log | Date, assistant, phrasing, whether you were named, what it said, which URL it cited, whether the answer was accurate |

```
ANSWER LOG

Date | Assistant | Question # | Phrasing (named / category / comparison) |
Named us? (Y/N) | Cited URL (ours / third party / none) | Accurate? (Y/N/partly) | Notes
```

**What to look for:** a category-only phrasing where you are never named is the shortlist problem. A named phrasing with an inaccurate answer is a source problem: the assistant is filling a gap you left with someone else's page.

---

## 4. Step 4: Scoring each check

Score each question pass or fail on each check, using the page you mapped to it. If no public page answers it, all five checks fail and the diagnosis is "missing page."

| Check | Pass | Fail |
|---|---|---|
| **A** Answerable | The question is answered in the first paragraph of a public page, in plain words | Answer buried below setup, spread over several pages, or not there |
| **G** Grounded | Every claim in the answer carries a named benchmark or measure, a date, and a source link | Adjectives ("leading," "fast," "secure") or undated, unsourced numbers |
| **E** Easy for a machine | Plain HTML text; video has a transcript; no login, form, or click needed to see it | Locked in a PDF, behind a form or login, rendered only after interaction, or inside an image |
| **N** Named human | A real person with a relevant role is named on the page as owner or author | "By the team," no author, or a name with no role |
| **T** Trail | Every cited source opens to the source itself, live, with no dead end | Links to a landing page, a dead link, a gated asset, or no link |

Per-page score is the number of passes out of five. Rule of thumb from the framework: 4 to 5 is consistently citable, 2 to 3 is sometimes lifted, 0 to 1 is skipped.

### Missing page or badly written page?

| Pattern | Diagnosis | Fix type |
|---|---|---|
| No public page addresses the question | Missing page | Write a new page |
| A page exists but fails A | Badly written: buried answer | Rewrite the first paragraph |
| A page exists but fails E | Badly written: trapped format | Move to HTML, add transcript, ungate |
| Page passes A and E, fails G or T | Badly written: unsupported | Add dated evidence and working source links |
| Page passes A, G, E, T, fails N | Badly written: anonymous | Name the owner with a role |

Keep these separate in the output. A missing page needs an owner and a draft. A badly written page needs an edit, often in under an hour.

---

## 5. The grid template

```
QUESTION-BY-CHECK GRID

#  | Buyer question (buyer's words) | Page used (live URL or "none") | A | G | E | N | T | Score | Diagnosis
1  |                                |                                |   |   |   |   |   |  /5   | Missing / Rewrite-A / Format-E / Evidence-G,T / Name-N
2  |
...
10 |
```

**Quality check from the SKILL.md:** every pass cites a live public URL. A pass with no URL is a fail.

---

## 6. The fix library

| Page type | Minimum content to pass all five | Usually unlocks |
|---|---|---|
| Pricing model | First paragraph: how you price (per seat, usage, platform), what drives the price, any minimum, what is included. Dated. Named owner (finance or revenue lead). Ranges if you will publish them | Pricing, cost range, fit, support tiers |
| Security and trust | First paragraph: certifications held with report dates, where data is stored, who can access it. Links to verifiable sources (certificate or attestation summary, subprocessor list). Named security owner | Security, data handling, compliance |
| Integrations | One section per major integration, each answering "does it work with X, and how" in the first line. What syncs, which direction, setup time | Integrations, implementation |
| Implementation | Typical timeline by customer size, the steps, what the customer must provide. Named implementation lead | Implementation, effort, fit |
| Results | Customer results with the metric, the period, the method, and permission. Dated. HTML, not a gated PDF | Results, proof, comparison |
| Fit and non-fit | Who it is built for and who it is not, plainly | Fit, comparison, cost range |
| Comparison | Factual differences only, each sourced or dated. Named author | Comparison |

### Writing the first paragraph (check A)

| Do | Do not |
|---|---|
| Restate the question in the heading, in the buyer's words | Use a clever headline the buyer would never type |
| Answer in the first one to three sentences | Open with company history or market context |
| Use numbers and nouns | Use adjectives the machine cannot verify |
| Say "it depends on X and Y" and then give the range | Say "contact sales" as the whole answer |

---

## 7. Ordering the fix list

| Order by | Then break ties by |
|---|---|
| 1. Number of pre-shortlist questions the fix unlocks | 2. Fixes for questions where an assistant gave a wrong answer, or no answer, about you |
| | 3. Effort: rewrites before new pages |
| | 4. Owner availability |

```
FIX LIST

Rank | Fix | Type (new page / rewrite) | Questions unlocked (#s) | Owner (named) | Due | Re-test date
```

---

## 8. What not to answer publicly

The SKILL.md asks you to list questions you should not answer publicly, and why. Leaving a gap is a choice; make it on purpose.

| Topic | Publish | Do not publish | Why |
|---|---|---|---|
| Pricing | Model, drivers, ranges or starting points | Discount levels, deal-specific terms | Discounts are negotiation, not fact |
| Security | Certifications, data location, access policy | Architecture details that help an attacker | Risk |
| Customers | Results with written permission | Names or numbers without permission | Trust and contracts |
| Roadmap | Shipped features, dated | Unreleased features or dates | Creates claims you may not meet |
| Competitors | Sourced, dated factual differences | Claims about them you cannot source | A claim with no source is a marketing line |

---

## 9. Decision table

| If | Then |
|---|---|
| Category-only phrasings never name you | Prioritize "what it is and who it is for," fit, and results pages |
| Named phrasings return wrong facts about you | Missing-page fixes for those facts come first |
| The answer exists only in a deck or a sales call | It cannot be cited. Publish it or list it under do-not-publish |
| Evidence exists but is in a gated PDF | Ungate the evidence, keep the form for the deeper asset if you must |
| A page fails only N | Add a named owner today. Smallest fix in the list |
| A claim has no verifiable source | Remove it or source it. Do not publish it as an answer |
| The re-test shows no change after two weeks | Check E and T first, then give it another round. Publishing removes a reason not to cite you; it does not force a citation |

---

## 10. Red flags

| Red flag | What it usually means |
|---|---|
| "Contact sales for pricing" is the only pricing content | Every pricing question fails; assistants fill the gap from third parties |
| Security answers live in a questionnaire behind a form | Security fails E for every buyer at shortlist stage |
| Every page says "by the team" | N fails site-wide |
| Results pages quote percentages with no period or method | G fails; the claim reads as marketing |
| Citations link to your own homepage or a press page | T fails |
| A third-party review page answers questions about you better than your own site | Assistants will cite it, accurate or not |

---

## 11. Worked example: Acme (illustrative)

Acme is a fictional 400-person B2B software company selling a revenue planning product. All details are illustrative.

**Question set (from first-call recordings and sales chat).** 1. What does Acme do and who uses it? 2. How is it priced? 3. Roughly what does it cost for 200 users? 4. What security certifications does it hold? 5. Does it work with our CRM? 6. How long is implementation? 7. What results do customers see? 8. Acme vs the main alternative? 9. Is it right for a company our size? 10. What support is included?

**Assistant sample.** Category-only phrasings ("best revenue planning tools for mid-market") named Acme in none of six samples. Named phrasings described Acme's pricing using a third-party review site's outdated figure.

**Grid (abridged).**

| # | Page used | A | G | E | N | T | Score | Diagnosis |
|---|---|---|---|---|---|---|---|---|
| 1 | Homepage | F | F | P | F | F | 1/5 | Rewrite-A: headline says "the AI platform for modern revenue," not what or for whom |
| 2 | None | F | F | F | F | F | 0/5 | Missing |
| 3 | None | F | F | F | F | F | 0/5 | Missing |
| 4 | Security PDF behind a form | F | P | F | F | F | 1/5 | Format-E |
| 5 | Integrations page (logos only) | F | F | P | F | F | 1/5 | Rewrite-A |
| 6 | None (lives in sales deck) | F | F | F | F | F | 0/5 | Missing |
| 7 | Case study PDF behind a form | F | F | F | F | F | 0/5 | Format-E |
| 8 | None | F | F | F | F | F | 0/5 | Missing |
| 9 | None | F | F | F | F | F | 0/5 | Missing |
| 10 | Help center behind login | F | F | F | F | F | 0/5 | Format-E |

**Fix list.**

| Rank | Fix | Type | Unlocks | Owner | Reasoning |
|---|---|---|---|---|---|
| 1 | Pricing model page: per-seat model, drivers, minimum, support tiers included, who it is and is not for | New page | 2, 3, 9, 10 | Head of revenue operations | Four questions; also corrects the third-party pricing figure assistants are using |
| 2 | Implementation and integrations page: timeline by size, CRM sync details | New page plus rewrite | 5, 6 | Implementation lead | Two questions; content already exists in the sales deck |
| 3 | Results page in HTML: two customer results with metric, period, method, permission | Format move | 7, part of 1 | Product marketing lead | Evidence exists, trapped in a PDF |
| 4 | Ungated security page: certifications with report dates, data location, subprocessor list | New page from existing PDF | 4 | Security lead | One question. Ties with ranks 5 and 6; ranked first among them because assistants returned no security answer at all |
| 5 | Homepage first paragraph: what, for whom, in plain words | Rewrite | 1 | Head of marketing | One question, about an hour of work |
| 6 | Comparison page, factual and sourced | New page | 8 | Product marketing lead | One question, highest effort, needs sourcing discipline |

The order follows questions unlocked. Ranks are a priority, not a queue: fixes with different owners run in parallel, so the security lead starts rank 4 the same week the pricing page is drafted, because the security question comes up in every enterprise first call.

**Do not publish.** Discount bands (negotiation), two customers' results without written permission, and the release date of a planned feature.

**Re-test.** Same 30 phrasings, same assistants, two weeks after the pricing and security pages go live. Owner: head of marketing.

---

## 12. Step 8: The re-test protocol

| Check | How |
|---|---|
| Same questions, same phrasings | Reuse the answer log rows exactly |
| Same assistants | Fresh sessions |
| What counts as progress | You are named more often in category-only phrasings; named phrasings cite your page; wrong facts are gone |
| What does not count | A single new mention in one session |
| Cadence | Two weeks after each publish, then quarterly |
| Expiry | Every dated claim (pricing, certifications, results) gets a review date and a named owner |

---

## 13. AI assist

### Split the work

| Task | AI assistant | Human |
|---|---|---|
| Turn call notes and chat logs into buyer-phrased questions | Draft | Picks the ten that are truly pre-shortlist |
| Score the grid from pasted page text | Draft scores with quoted evidence | Opens every URL and confirms it is live and public |
| Draft first paragraphs for new pages | Draft | Checks every fact; adds dates, sources, named owner |
| Draft the do-not-publish list | Draft | Decides with legal, security, and finance |
| Run the answer sampling | Cannot sample itself reliably; can format the log | Runs the sessions and records results |

### Follow-up prompts after the Quick prompt

```text
For each pass in the grid, quote the exact sentence from the page that earns it and the URL. Change any pass without a quote and a URL to fail.
```

```text
Split the failures into two lists: questions with no public page at all, and questions with a page that fails one or more checks. For the second list, name the check and the smallest edit that would fix it.
```

```text
Draft the first paragraph for a page answering "[buyer question]" using only these facts: [paste]. Answer in the first two sentences. Mark every place where a date, a source link, or a named owner is needed with [NEEDED]. Do not add numbers, customers, or results I did not give you.
```

```text
List every claim on this page: [paste]. For each, say whether it has a named measure, a date, and a working source. Flag adjectives that make an unverifiable claim.
```

### Check the AI's output for these errors

| Error this job invites | How to spot it |
|---|---|
| Invented proof | A customer name, number, or result in a draft that you did not supply |
| Passing a gated page | E marked pass for a PDF, form, or login page |
| Treating its own answer as the market's | The AI says "assistants would say X" without a logged sample |
| Ranking by effort instead of unlocks | Easy rewrites placed above a fix that unlocks four questions |
| Adjectives in drafts | "Industry-leading," "seamless," "robust" in a first paragraph |

---

## 14. Common mistakes and how to spot them

| Mistake | How to spot it | Fix |
|---|---|---|
| Using your own words for the questions | Questions contain product jargon | Pull phrasing from calls and site search |
| Scoring pages, not questions | Grid rows are URLs | Rows are buyer questions; pages are evidence |
| One assistant sample treated as truth | One row per question in the answer log | Three phrasings, two rounds, two or more assistants |
| Publishing claims you cannot defend | Results without method or permission | Source it or cut it |
| No named owner | New page bylined "the team" | Name a person with a role |
| No re-test | Fix list ends at publish | Put the re-test date on the fix list |

---

## 15. The 5-minute version

1. Ask two assistants "how is [your company] priced?" and "best [category] tools for [your buyer]." Note whether you are named and which page is cited.
2. Check whether your pricing and security answers are on public HTML pages. If not, those are your first two fixes.
3. Open your homepage. Does the first paragraph say what you do and for whom, in plain words? If not, rewrite it.
4. Put a named owner on every page you just touched.
5. Set a date two weeks out to ask the same questions again.

## The deep version (category push or a lost-shortlist problem)

- Build the question set from 90 days of first calls, sales chat, and site search, and validate it with five AEs.
- Run the full sampling protocol: three phrasings, two or three assistants, two rounds, logged.
- Score all ten questions, separate missing from badly written, and order fixes by unlocks with explicit tie-breaks.
- Add an evidence standard: no claim publishes without a source, a date, and an owner, and dated claims get a review date.
- Re-test two weeks after each publish and quarterly after that, and correct wrong claims openly with a visible, dated note.

---
*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next toolkit before it ships here.** [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
