# Section Signatures: Hooks, Evidence, Frameworks, Closings

**Use this file when:**
- The master spec exists and drafts still open or close generically.
- You are building the four section-level files of a voice skill.
- A content skill (post writer, newsletter writer, report writer, deck builder) needs a compact voice instruction to paste into its prompt.

A voice is not uniform across a piece. People open differently than they argue, and they close differently than they teach. AI drift is also uneven: it hits openings and closings hardest, because those are where generic templates are strongest ("In today's...", "In conclusion..."). Four section files, each governing one part of a piece, fix the parts that matter most.

| Section file | Governs | Typical window |
|---|---|---|
| `hooks.md` | Titles, subject lines, first 1 to 3 paragraphs, first slide | First ~150 words |
| `evidence.md` | Claims, proof, counterarguments, stakes | Every argumentative passage |
| `frameworks.md` | The teaching middle: naming, numbering, explaining, handing off | Each framework or concept section, 150 to 400 words |
| `closings.md` | The landing, the ask, the sign-off | Final 75 to 250 words |

---

## 1. Extraction procedure (same for all four)

1. **Pull the instances.** From the baseline (never the drift set), copy every opening (first ~150 words), every closing (last ~150 to 250 words), every argumentative passage, and every teaching section into four folders: `sections/hooks/`, `sections/closings/`, and so on. One instance per file. You need 15 or more pieces for hooks and closings to see a real distribution.
2. **Do the same for the drift set** (or the generic reference set) into a parallel folder.
3. **Profile both.** `python3 scripts/voice_features.py compare sections/hooks sections-drift/hooks`. Section-level rates differ from whole-piece rates: openings usually carry more pronouns and questions than the body.
4. **Hand-classify each instance** against the taxonomy for that section (below). One primary label per instance, optional secondary.
5. **Count the shares.** Keep the patterns that together cover about 80 percent of instances. Patterns under about 5 percent are anchors for the library, not rules.
6. **Find the lost and the introduced.** `phrases` on each section pair. A closing phrase that appeared in many baseline pieces and vanished in the drift set is the **number-one drift to reverse** for that section. Name it at the top of the file.
7. **Write the file** from the template in section 3.

---

## 2. Taxonomies to classify against

These are generic pattern families observed across many writers. Your person will use a few heavily, some rarely, and some never. The ones they never use are as important as the ones they do: they go in the anti-patterns.

### 2.1 Hook patterns

| Pattern | Shape | Formula |
|---|---|---|
| Direct reader question | Names a situation the reader has lived | "Have you ever [specific scene]?" |
| Memory anchor | Opens inside a specific moment from the writer's life | "[Time], I [specific thing that happened]." |
| Time anchor | Opens on today, this week, a date | "This morning I [saw / counted / deleted] [thing]." |
| Conditional entry | Qualifies the reader and offers something | "If you [situation], [what this piece gives you]." |
| Owned stance | A claim the reader must react to, owned in first person | "[Claim]. I [ownership: changed my mind / bet on it / lost money on it]." |
| Setup then turn | States the common belief, then pivots | "[Belief the audience holds]. [Short sentence that breaks it]." |
| Purpose statement | Tells the reader exactly what is coming. Usually a second move, rarely alone | "Let me show you [the thing]." |
| Scene | Drops the reader into a concrete moment, no setup | "[Place]. [Action]. [Detail]." |
| Confession | Opens on a mistake | "I [got this wrong] for [period]." |
| Number first | Leads with a statistic | "[Number] of [group] [result]." Often a drift pattern; check the baseline |
| Quote first | Opens on someone's words | Often a drift pattern; check the baseline |

**Hook-specific measures:** pronoun floors in the first 150 words (as counts), at least one sentence of 5 words or fewer, at least one question or direct-address move, first paragraph length band, where the punch line sits (usually within the first three sentences, 5 to 12 words, naming the stakes).

**Rule to include:** pick one hook pattern per piece; never combine more than two.

**Language warning to include:** when a pattern's typical wording has become a drift phrase (for example, a contrarian opener that now always starts with the same stock phrase), keep the pattern and ban the wording. Give the model two or three alternative wordings from the person's own baseline.

### 2.2 Evidence patterns

**First, record the person's evidence stack:** the order in which proof types appear when they defend a claim. Code 20 claims. A common human order is: lived observation, then a specific real example, then the mechanism (why it happens), then a reader pattern-match ("you have seen this too"), then the counterargument, then external data last, as confirmation. Drifted writing often inverts it: data first, story as decoration. Write the person's actual order and their story-to-data ratio into the file.

| Argument pattern | Shape | Formula |
|---|---|---|
| Setup, contradict, resolve | Conventional wisdom, why it fails, the writer's version | "[Common narrative]. [Full sentence stating what actually happens]. Why? Because [mechanism]." Write it in full sentences; the compressed "it's not X, it's Y" form is a drift marker for many writers |
| Story, principle, handoff | A real moment, the lesson, a question to the reader | "[Specific moment]. [What I learned]. [Question that applies it to the reader]." |
| Parallel scenarios | Three or four same-shaped examples pointing at one principle | "If [case 1], [response]. If [case 2], [response]. If [case 3], [response]." |
| Old way, new way | Two full sentences, one per era | "[Old way] was built for [X]. It was never built for [Y]." |
| Vulnerable admission | The writer's own failure before the claim | "I [failed at this]. Here is what it taught me." |
| Staged objection | The reader's pushback in quotation, then the answer | "\"[Reader's objection in first person].\" [Acknowledge it fairly]. [Answer]." |
| Stakes naming | What happens to those who act and those who do not | "[Those who do X] will [outcome]. [Those who do not] will [specific cost]." |
| Expanding agreement | Partial agreement that adds rather than narrows | "[Their point] is right. And [what it misses]." |

**Data handling rules to define (from the baseline):**
- **Wrap and land.** The writer's setup, then the statistic with its source, then the writer's interpretation. A statistic never stands alone.
- **Citation density.** Count external statistics per 1,000 words in the baseline. Set the cap at that level. Fewer citations make each one carry weight.
- **Attribution style.** How the person names sources in their own voice. Ban "studies show" without a source.
- **Real over hypothetical.** Record the real-to-hypothetical example ratio. Set a ceiling on "imagine a..." examples.
- **Specificity floor.** How often the person names a concrete thing (a tool, a moment, a place, a number) per 300 words. Real anchors must come from the person's material, never invented.
- **Informal amplifier quota.** If the person uses an occasional informal word that signals a real human is writing, measure its rate and set a quota with both a floor and a ceiling. Absence sanitizes; excess caricatures.

### 2.3 Framework (teaching middle) patterns

**Framework signature traits to record:**
1. Naming style: acronym, alliteration, numbered rule, plain phrase, metaphor name.
2. Numbering format: `1.`, `1)`, `1-`, `#1`, `Step 1:`, or none. Some people have an idiosyncratic format that readers recognize. Record it and the formats where it does not belong (formal reports).
3. Series behavior: does the person restate the whole framework before each new part?
4. Verb-rooted or noun-rooted nodes.
5. Applied or theoretical: is every node paired with an application?

**The explanation loop.** Code each teaching section for which of these moves it contains:

| Move | What it does |
|---|---|
| Name it | States the concept and its label in one short sentence |
| Define it positively | Says what it is, then proves it with one concrete detail. Never defines by contrast-reversal |
| Personal anchor | Grounds it in the writer's own experience, 2 to 4 sentences |
| Practical example | A recognizable situation from the reader's world, often as parallel conditionals |
| Reader handoff | A question or prompt that makes the reader apply it |
| Smallest rep | The smallest action the reader can take today or this week |

Count how many moves the person's sections usually contain and set the rule ("at least N of 6 per section"). Note which move the drift set lost; it is usually the personal anchor or the handoff.

**Also record:** emphasis habits in teaching (caps, bold, italics, none) with what they are used for; the example-transition phrases the person rotates (so the model rotates rather than repeating one); the person's metaphor drawers for explanation and the generic business metaphors they never use; section length and internal structure (heading, opener, 2 to 4 short paragraphs, list or questions, handoff, transition).

### 2.4 Closing patterns

| Pattern | Shape | Formula |
|---|---|---|
| Assignment | A specific, small action for this week | "[The person's assignment phrase]: [one verb-first action]." |
| Try and report | Low-stakes experiment plus an invitation back | "Try [action] for [short period]. Tell me what happened." |
| Question landing | One direct question that puts the reader in motion | "What will you [do] before [specific day]?" |
| Warm wish | The writer rooting for the reader | "[Wish for the reader's outcome]." |
| Forward tease | Points at the next piece in a series | "Next [time], [what is coming]." |
| Vision plus conviction | Big-picture statement and personal commitment. Rare, for manifesto pieces | "[Vision]. [Personal commitment]. [Invitation]." |
| Binary choice | Two paths and their outcomes | "[Group A] will [outcome]. [Group B] will [cost]. Which one is your team?" |
| Resource gift | Hands over something usable | "[The thing], free: [where]." |
| Summary | Restates the thesis. Usually drift, check the baseline | "In conclusion, [thesis]." |

**Closing-specific measures:** closing length band (often 75 to 150 words in short-form), pronoun counts in the closing, at least one short sentence, the share of baseline closings with a concrete reader action, and the person's sign-offs with a **format matrix** (where each sign-off is appropriate, optional, or inappropriate).

**Closing architecture to record:** the order of beats in a typical closing. A common human order: one-sentence principle, the ask (specific, small, verb-first), a moment of warmth or personal stake, then an optional sign-off or forward tease. Drifted closings tend to become long summary paragraphs; set a maximum length.

**Differentiate by content type.** A social post, a newsletter, a report, and a slide deck each close differently. Write one short block per format: what the ask looks like, which sign-offs are allowed, and what to remove in formal settings (for example, emoticons and casual sign-offs in a board report, while keeping first-person ownership).

---

## 3. File template (use for each of the four)

```markdown
---
name: [person]-voice-[hooks|evidence|frameworks|closings]
description: [Person]'s voice signature for [section]. Use as a voice layer whenever
  [content skills that call it] produce [the section]. Triggers on [section words: hook,
  opening, lede, subject line / claim, proof, counterargument / steps, model, explain /
  CTA, conclusion, sign-off]. Restores [the one thing drift removed from this section].
---

# [Person] Voice: [Section]

[One paragraph: what this file governs and why it matters for this section.]

## Universal hard rules (copied verbatim from the master spec; change all five files together)
1. [Hard rule, e.g. a device with near-zero baseline and high drift: zero tolerance]
2. [Banned construction, with all its variants listed, and one rewrite example]
3. [Any other hard rule]

## Core principle
[Person] [opens / argues / teaches / closes] like [a specific human role doing a specific
human thing], not like [the institutional version]. [One sentence on what the reader
should feel.]

## The number-one drift to reverse (if any)
[Signature present in N baseline pieces, absent in the drift set. Restore it as the default,
with 2-3 approved variations of wording.]

## Numeric targets
| Signal | Baseline | Drift / generic | Target |
|---|---|---|---|
| [ ] | [ ] | [ ] | [floor / ceiling / band / zero] |

## Patterns (pick one; never mix more than two)
### Pattern 1: [Name] ([share of baseline instances])
[What it does, one sentence.]
Real examples:
- "[verbatim from baseline]"
- "[verbatim from baseline]"
Formula: `[fill-in shape]`
Use when: [register / format]

[Repeat for each pattern covering ~80% of instances]

## Punctuation and rhythm
USE: [devices from baseline, with rates]
AVOID: [devices from drift, with reasons]
Rhythm: [beat pattern, e.g. punch / expansion / punch]

## Length
[Window length band; paragraph length; section length]

## Anti-patterns (reject and rewrite)
1. [Generic opener / closer / transition the person never uses]
2. [Construction that marks drift]
3. [Absence rule: e.g. no first-person in the first two paragraphs]

## Call-in snippet
> "Apply [person]-voice-[section] to [window]. [Hard rules in one line]. [Pattern rule].
> [Two or three numeric floors as counts]. [One banned phrase family]."

## Self-test
Hard fails (any one = rewrite):
- [ ] [Hard rule 1 check]
- [ ] [Hard rule 2 check]
Then pass at least [N] of these [M]:
- [ ] [Count check]
- [ ] [Pattern check]
- [ ] [Rhythm check]
- [ ] [Real-over-hypothetical check]
- [ ] [Reader action / handoff check]

---
Source: [words and piece counts, baseline and drift, date range].
```

### Why each part is there

- **Hard rules copied verbatim:** a section file is often loaded alone by another skill. If the rules live only in the master, they are missing exactly when they are needed.
- **Core principle as a human role:** "opens like a [role] starting a conversation, not a publication starting a feature" gives the model one image to check every sentence against.
- **Three-column targets:** the drift column tells the model what failure looks like in numbers, which is more useful than the target alone.
- **Pattern shares:** a model that knows 40 percent of openings are questions and 5 percent are scenes will distribute patterns naturally across many pieces instead of using the favorite every time.
- **Real examples plus a formula:** examples teach the texture; formulas let the model produce a new instance instead of copying an example.
- **Call-in snippet:** content skills cannot load four long files into every prompt. A three-line compressed instruction carries the most important rules everywhere.
- **Self-test with hard fails and a threshold:** hard fails stop the worst errors outright; the threshold ("6 of 8") avoids chasing perfection on soft checks, which produces stiff, over-corrected drafts.

---

## 4. Worked mini example (fictional)

A hooks file excerpt for Writer A, the fictional operations leader from the sample corpus:

```markdown
## Core principle
Writer A opens like an auditor walking you through what they just counted, not like a
publication announcing a trend.

## Numeric targets (first 150 words)
| Signal | Baseline | Drift | Target |
|---|---|---|---|
| First-person words | 3-5 | 0 | at least 2 |
| Second-person words | 2-4 | 0 | at least 2 |
| Numbers | 2-4 | 0-1 | at least 2 |
| Sentences of 5 words or fewer | 1-2 | 0 | at least 1 |
| "Imagine..." scenarios | 0 | 1 per piece | 0 |

## Patterns
### Pattern 1: The count (about half of baseline openings)
Opens on a specific moment and a number the writer personally counted.
Real examples:
- "Last Tuesday I sat in a forecast call that ran 74 minutes. We moved zero deals."
- "Three years ago our team had 46 dashboards. I know because I built 19 of them."
Formula: `[Time anchor] I [observed thing]. [Number]. [Short sentence naming the waste].`

## Call-in snippet
> "Apply writer-a-voice-hooks to the first 150 words. Open on a moment and a number Writer A
> counted (real numbers only; use [NUMBER?] if unknown). At least 2 'I', 2 'you', 1 sentence
> of 5 words or fewer. No 'imagine', no 'in today's', no summary of the topic."
```

Notice what it does not contain: any rule borrowed from another person's voice. Every target came from Writer A's own baseline and drift comparison.
