---
name: voice-builder
description: >
  Build a voice skill from a person's own writing, so an AI assistant can draft new material
  that reads like them on topics they have never written about. Use when someone says "make
  the AI sound like me", "build my voice skill", "clone my writing style", "my AI drafts sound
  generic", "my writing has drifted since I started using AI", "create a voice guide for our
  exec", or wants to measure and test how close a draft is to their real voice. Covers corpus
  collection and sizing, pre-AI vs post-AI drift analysis, measurable style features (with a
  dependency-free Python script), qualitative pattern extraction, section-level signatures for
  hooks, evidence, frameworks and closings, a fill-in voice spec template, blind A/B testing,
  and the iteration loop. Works for any professional who writes: founders, revenue leaders,
  sellers, marketers, consultants, teachers.
---

# Voice Builder

Most "write like me" prompts produce a costume: the person's three favorite phrases stapled onto a generic draft. Readers smell it in one paragraph.

This skill builds the real thing: a **generative voice model**. It captures the machinery of how a person builds a sentence, opens, argues, explains, reasons, takes a stance, and closes. With that machinery, an AI assistant can write a new piece, on a topic the person has never covered, that their regular readers would accept as theirs.

The output is a voice skill folder for one person:

```
<person>-voice/
  SKILL.md                     master voice spec (from assets/voice-spec-template.md)
  hooks.md                     section signature: openings
  evidence.md                  section signature: arguments and proof
  frameworks.md                section signature: the teaching middle
  closings.md                  section signature: endings and asks
  references/anchor-library.md verbatim lines, grouped by theme and register
  references/baseline.json     numbers from scripts/voice_features.py
  eval/                        held-out pieces, test prompts, test log
```

Each section signature can live as its own skill if your content skills (post writer, newsletter writer, report writer) call them as layers. See "Architecture" below.

---

## When to use this skill, and when not to

**Use it** to build a voice skill for yourself, to rebuild one that has gone stale, to diagnose why AI-assisted drafts no longer sound like you, or to build an executive's voice with their explicit consent.

**Do not use it** to imitate someone who has not agreed to it, to put words in a real person's mouth in public, or to pass AI-written work off as hand-written where your audience or your employer's policy expects disclosure. A voice skill is a writing aid for the owner of the voice. Get written consent before building one for anyone else, and let them review the spec and the anchor library before it is used.

---

## Inputs

### 1. The corpus: the person's own words

| Source | What it gives you | Watch out for |
|---|---|---|
| Long-form posts, articles, newsletters | Structure, openings, closings, argument style | Pieces heavily edited by someone else carry the editor's voice |
| Short social posts | Hooks, rhythm, sign-offs | Platform conventions (line breaks, hashtags) are not voice |
| Emails and memos the person wrote alone | Advisory register, directness | Strip names, numbers, and client details |
| Talk, podcast, webinar, class transcripts | Spoken voice, metaphors, reasoning out loud, stories | Filler words inflate some rates; keep them out of written targets |
| 1:1 coaching or meeting transcripts (with consent) | Mentoring register, how they soften or push | Highest privacy risk; quote only the person, never the other party |
| Their own edits to AI drafts (before and after) | What they add and cut, which is the voice in its purest form | Rare and valuable; ask for these explicitly |

### 2. How much is enough (rule of thumb, not a law)

| Goal | Minimum | Comfortable |
|---|---|---|
| Rough qualitative spec | 5,000 words, 10+ pieces | 15,000 words |
| Stable quantitative baseline (rates per 1,000 words) | 10,000 words written | 25,000+ words |
| Section signatures (hook and closing pattern counts) | 15 complete pieces of the same format | 30+ pieces |
| Each register you want to support | 2,000 to 3,000 words of that register | 8,000+ |
| Pre-AI vs post-AI drift comparison | 10,000 baseline words; the post-AI side can be smaller (2,000+) | Both sides 10,000+ |

Two notes. Section signatures need **piece counts**, not word counts: 40,000 words from four whitepapers gives you only four openings. And spoken transcripts expand fast; one hour of talking is roughly 7,000 to 9,000 words, which makes them the cheapest way to fill thin registers.

### 3. A manifest

Label every item before you analyze anything. One row per piece:

```
file, date, format (post/article/email/transcript/...), register (see Step 4),
audience, written alone? (Y/N), AI-assisted? (Y/N/unknown), edited by others? (Y/N),
include in baseline? (Y/N), held out for testing? (Y/N)
```

The manifest is what lets you split the corpus cleanly. Without it, every later number is contaminated.

---

## Architecture: why a master spec plus section layers

A single voice file fails in a predictable way: the model applies the person's tics evenly across the whole piece, and the opening and closing (where voice matters most) come out generic. The structure that works:

1. **A master spec** (the generative engine). Who the person is as a writer, their registers, sentence-level mechanics, lexicon by function, how they invent analogies, how they reason, what they believe, what they push against, format templates, worked examples on new topics, a self-check, and a 30-second seed.
2. **Four section signatures**, one for each part of a piece where voice behaves differently:
   - **Hooks**: the first 1 to 3 paragraphs.
   - **Evidence**: how claims get backed up and defended.
   - **Frameworks**: how the middle teaches, names, numbers, and explains.
   - **Closings**: the final 75 to 250 words and the ask.
3. **An anchor library**: verbatim lines grouped by theme and register, used to calibrate rhythm, never pasted.

Each section signature carries the same internal parts: the universal hard rules (copied verbatim at the top, because a section file may be loaded alone), a one-sentence core principle, a numeric target table, a pattern catalog with formulas and real examples, anti-patterns, a compressed **call-in snippet** that other skills paste into their prompts, and a self-test with hard fails and a pass threshold.

**One source of truth for hard rules.** Write the universal rules once in the master spec, copy them verbatim into each section file, and when you change one, change all five. Contradictions between files (for example, "use this device sparingly" in the master and "zero tolerance" in a section file) are the most common defect in hand-built voice systems, and the model resolves them unpredictably.

---

## The build process

| Step | What you do | Output | Time (rule of thumb) |
|---|---|---|---|
| 1 | Collect, label, and hold out | Corpus + manifest + 15% held-out test set | 2-4 hours |
| 2 | Split the corpus | Baseline set, drift set, spoken set | 30 min |
| 3 | Extract measurable features | `baseline.json`, drift comparison, phrase lists | 30 min with the script |
| 4 | Extract qualitative patterns | Coded notes per pattern family | 4-8 hours |
| 5 | Define section-level signatures | `hooks.md`, `evidence.md`, `frameworks.md`, `closings.md` | 3-5 hours |
| 6 | Write the voice spec | Master `SKILL.md` + anchor library | 3-4 hours |
| 7 | Test with blind comparisons | Test log with scores | 2-3 hours per round |
| 8 | Iterate | Changelog, revised spec | 1-2 hours per round, 2-4 rounds |

### Step 1: Collect, label, hold out

Gather everything in the table above into one folder of `.txt` or `.md` files, one piece per file. Fill the manifest. Strip anything private: family details, client names, colleagues' words, deal numbers, health, anything the person would not post publicly.

Then **hold out 10 to 20 percent of pieces before you read anything closely.** Pick them across formats and registers. They become your test set in Step 7. If you build from them, your blind test is rigged.

### Step 2: Split the corpus

Make three subsets from the manifest:

- **Baseline (the true voice):** written alone, not AI-assisted, not heavily edited by others. Usually the pre-AI period. The cutoff is the date *this person* started drafting with an AI assistant, not a calendar date for the world.
- **Drift set:** AI-assisted or post-cutoff writing. Used only for comparison, never as a model.
- **Spoken set:** transcripts. Used for metaphors, stories, reasoning, and registers, but not for written punctuation or rhythm targets.

Why the split matters: for many professionals the published writing of the last few years was co-written with an AI assistant, and it has quietly converged toward a generic institutional voice. If that writing goes into the baseline, the voice skill learns the drift and reproduces it. The comparison between baseline and drift set is also the single best source of rules: what disappeared is what to restore; what appeared is what to ban.

No pre-AI writing? Use transcripts (spoken voice rarely drifts), emails written fast, and fresh writing done by hand for this purpose. Ask the person to write three short pieces without any AI help and treat those as the baseline.

### Step 3: Extract measurable features

Run the script on each subset:

```bash
python3 scripts/voice_features.py profile corpus/baseline --per-doc --json baseline.json
python3 scripts/voice_features.py compare corpus/baseline corpus/drift
python3 scripts/voice_features.py phrases corpus/baseline corpus/drift --n 3
python3 scripts/voice_features.py phrases corpus/baseline --n 3 --min-docs 3
```

It computes 49 scalar features and 8 distributions: sentence and paragraph length distributions, rhythm swing, pronoun rates, question rate, contractions, hedges, number density, list usage and style, punctuation habits, emphasis, simile and story markers, readability, opener and closer types, and a drift watchlist. `compare` flags every feature that moved by 1.5x or more. `phrases` lists recurring n-grams, and with two folders lists the phrases lost and the phrases introduced.

Turn the output into a **three-column target table** for each feature that matters: baseline value, drift value, target. That table goes at the top of every section signature. Full definitions, computation, and how to read each number: [references/feature-extraction.md](references/feature-extraction.md). A runnable sample corpus (a fictional operations writer, with a deliberately drifted post-AI set) is in `scripts/sample-corpus/`.

### Step 4: Extract qualitative patterns

Numbers find the rhythm; they miss the mind. Read the baseline and spoken sets and code these pattern families, with at least three real instances each before you call something a pattern:

1. **Operating system**: the person's job as a writer in one sentence (explainer, skeptic, field reporter, coach, builder), default posture, and the one thing to internalize.
2. **Registers**: how the voice shifts by setting (broadcast, teaching, mentoring, advising). For each: tic density, humility, directness.
3. **Sentence mechanics**: rhythm shape, question habits, counting and splitting moves, address, hedges, tags, emphasis, profanity ceiling, punctuation in speech vs writing.
4. **Lexicon by function**: their words for dismissing noise, for enthusiasm, for scale, their verbs, their self-labels, their recurring concepts.
5. **Analogy engine**: their source domains and the steps they use to build, extend, and land a comparison.
6. **Reasoning patterns**: the moves they make to reach a conclusion, so the model arrives where they would arrive.
7. **Stances**: their axioms. What they believe, stated as they would state it.
8. **Against list**: what they reflexively push back on.
9. **Relational moves**: how they handle credit, expertise, skeptics, and gratitude.
10. **Owned frameworks**: their named models, with credit rules.
11. **Speech-to-writing gap**: what is strong out loud and weak on the page, and the reverse.
12. **Conditional gears**: modes that should fire only on specific tasks (for example, a sharper prediction mode), with triggers and non-triggers.

Coding method, sheets, and how to turn each family into spec text: [references/qualitative-extraction.md](references/qualitative-extraction.md).

### Step 5: Define section-level signatures

For each of hooks, evidence, frameworks, and closings: pull every instance from the baseline (every opening, every closing, every argument passage, every teaching section), classify them, count the patterns, compute section-level numbers, and write the signature file. Templates and the pattern taxonomies to classify against: [references/section-signatures.md](references/section-signatures.md).

### Step 6: Write the voice spec

Fill [assets/voice-spec-template.md](assets/voice-spec-template.md). Rules for good spec text:

- **Engine over archive.** Every section should help generate *new* material. A quote list alone teaches the model to remix old lines.
- **Mechanism plus example plus formula.** "Long sentence then short punch" is a mechanism. Add one real example and one fill-in formula.
- **Frequency caps on signatures.** Every signature phrase gets a cap ("at most once per piece"). Uncapped signatures become caricature within three drafts.
- **Register-aware.** Any rule that varies by setting lives in the register table, not as a global rule.
- **Real numbers or marked placeholders.** The spec must never tell the model to invent statistics or stories and present them as real. See failure modes.
- **Worked examples on topics the person never covered.** Three short pieces, different registers, built only from the spec. These prove the engine generalizes and become few-shot anchors.

### Step 7: Test with blind comparisons

Generate pieces from the held-out prompts, mix them with the person's real held-out pieces, and have the person and two or three regular readers sort them without knowing which is which. Score with the "sounds like me" rubric, run the quantitative distance check, and log every reason a judge gave for spotting the AI piece. Full protocol, rubric, statistics for small samples, and the log format: [references/testing.md](references/testing.md).

### Step 8: Iterate

Classify every failure reason, map it to the spec section that controls it, change one thing, regenerate the same test set, and rescore. Keep a changelog. Stop when judges cannot beat chance on held-out pairs and the person would sign drafts with light edits only. Loop details in [references/testing.md](references/testing.md).

---

## How to use the resulting voice skill

1. **Pick the register first.** Before a word is written, name the setting. The most common mimicry error is using the loud, public register for advisory or mentoring work.
2. **Load in layers.** Content skill (for example, a newsletter or post writer) produces structure. The master spec sets the voice. The section signatures govern the opening, the argument passages, the teaching middle, and the close. Paste each signature's call-in snippet into the content skill's prompt.
3. **Generate on the person's real material.** Give the model the person's actual stories, numbers, and opinions on the topic. The voice skill supplies how they say it; it cannot supply what happened.
4. **Run the self-checks.** Section self-tests first (hard fails force a rewrite), then the master self-check.
5. **Run the distance check** on anything long enough (300+ words): `python3 scripts/voice_features.py score <baseline-folder> draft.md`.
6. **The owner edits.** Save before and after. Those edit pairs are the best training data you will ever get; review them monthly and fold the patterns back into the spec.
7. **Refresh twice a year.** Voices change. Add new hand-written pieces to the baseline, rerun Step 3, and retire signatures the person has outgrown.

---

## Failure modes

| Failure | What it looks like | Cause | Fix |
|---|---|---|---|
| **Caricature** | Every paragraph carries a signature phrase; the person reads it and winces | Phrase bank without frequency caps; broadcast register used everywhere | Cap every signature; set tic density per register; add a "would they wince?" check; test with a caricature score (see testing.md) |
| **Over-indexing on tics** | Surface matches (pronouns, punctuation, catchphrases) but the argument is generic | Spec is all lexicon and no reasoning, stances, or analogy engine | Fill reasoning patterns, stances, and against list; judge "would they arrive at this conclusion?" |
| **Drift toward generic AI voice** | Institutional tone, few "I" and "you", em dashes, setup-and-reversal constructions, hypothetical "imagine a rep" examples, summary closings | Model defaults reassert over a weak spec; or the baseline included AI-assisted writing | Rebuild baseline from pre-AI or hand-written work; add the drift set's introduced phrases to banned list; make the target table numeric |
| **Register flattening** | Mentoring note sounds like a keynote; advisory memo is full of hedges | No register selector, or selector ignored | Register is step one of every use; give each register its own target values |
| **Retrieval-remix** | Old lines pasted into new topics, sometimes out of context | Anchor library used as a source, not a calibrator | Label the library "calibrate, never paste"; self-check asks "is any sentence lifted?" |
| **Fabricated specificity** | Plausible but invented numbers, stories, or client anecdotes presented as fact | Spec says "use concrete numbers and stories" without a sourcing rule | Real numbers from the person or bracketed placeholders like `[NUMBER: source?]`; stories only from the person's own material |
| **Contradictory rules** | Model alternates between two behaviors | Same rule written differently in different files | One source of truth, copied verbatim; consistency pass before every release |
| **Small-corpus overfit** | One unusual piece sets the targets | Too few pieces; one long piece dominates rates | Meet the size minimums; check per-document spread (`--per-doc`); prefer medians |
| **Gear overuse** | Every piece is a bold contrarian take | Conditional mode written as default | Write explicit triggers and non-triggers; default register wins when unsure |
| **Frozen voice** | Spec describes who the person was three years ago | No refresh cycle | Twice-yearly refresh; date the baseline |
| **Privacy leak** | Anchor library contains a client name, a family detail, or another person's words | Transcripts copied without scrubbing | Scrub at Step 1; quote only the owner; owner reviews the library |

---

## Files in this skill

- [references/feature-extraction.md](references/feature-extraction.md): every measurable feature, how it is computed, how to read it, and how to set targets.
- [references/qualitative-extraction.md](references/qualitative-extraction.md): coding the twelve pattern families and turning them into spec text.
- [references/section-signatures.md](references/section-signatures.md): building the hooks, evidence, frameworks, and closings files, with taxonomies and templates.
- [references/testing.md](references/testing.md): blind A/B protocol, the "sounds like me" rubric, small-sample statistics, and the iteration loop.
- [assets/voice-spec-template.md](assets/voice-spec-template.md): the fill-in master spec.
- `scripts/voice_features.py`: dependency-free feature extractor (`profile`, `compare`, `phrases`, `score`).
- `scripts/sample-corpus/`: a fictional writer's baseline, drifted set, and a test draft to try the script on.

---

*Part of the [Revenue AI Report open skill library](https://github.com/therevenueaireport/RevenueAI). Built by Jonathan Kvarfordt. License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

**Get the next skill before it ships here.** The Revenue AI Report is a weekly read on what AI actually did inside B2B revenue teams: receipts, benchmarks, post-mortems. [Subscribe free at therevenueaireport.com](https://www.therevenueaireport.com).
