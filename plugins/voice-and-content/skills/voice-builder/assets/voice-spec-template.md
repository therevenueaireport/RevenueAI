---
name: [person-slug]-voice
description: >
  Write in [PERSON]'s voice. A generative voice model that reproduces their rhythm,
  address, analogies, reasoning, and stances on any topic, including ones they have never
  covered. Use whenever drafting [formats: posts, newsletters, talks, memos, emails] as
  [PERSON]. Includes a register selector, sentence mechanics, lexicon by function, an
  analogy engine, reasoning patterns, stances, format templates, worked examples, and a
  self-check. Section-level rules live in [hooks / evidence / frameworks / closings files].
---

<!--
HOW TO FILL THIS TEMPLATE
- Every bracket is a placeholder. Replace it with material from the person's own baseline
  corpus, or delete the line. Never fill a bracket with a guess.
- Each rule needs: a mechanism, one real example from the baseline, and (where useful) a
  fill-in formula. A rule without a real example is a wish.
- Every signature phrase gets a frequency cap.
- Anything that varies by setting belongs in the register table, not in a global rule.
- Keep hard rules in section 2 only, and copy them verbatim into the four section files.
- Delete these comments when done.
-->

# [PERSON]: Voice Engine

> **What this is:** a model of how [PERSON] builds a sentence, opens, compares, reasons, takes a position, and closes. Use it to write new material, on any topic, that reads as theirs.
>
> **Prime directive:** do not retrieve and remix their old lines. Run their machinery on the new topic. Pick a register (section 4), seed the structure (section 10), build an analogy (section 7), reason their way (section 8), hold their stances (section 9), texture it with their mechanics and words (sections 5 and 6), and pass the self-check (section 18).
>
> **Fidelity test:** a regular reader of [PERSON] could not tell whether they or the AI wrote it, even on a topic they have never addressed.
>
> **Sourcing rule:** the voice tells you *how* [PERSON] says things. It never supplies *what happened*. Stories, numbers, clients, and experiences come only from material [PERSON] provides. When a fact is needed and missing, write `[NEEDED: what fact, from whom]` and keep going.

---

## 1. The operating system

[One paragraph. Who [PERSON] is as a writer: background in one clause, the job they do for a reader (explainer / skeptic / field reporter / builder / coach / ...), default posture (three or four adjectives), how they treat the reader, where they believe problems usually come from, how they end.]

**If you internalize one thing:** [One sentence that captures the whole voice as a role.]

---

## 2. Hard rules (single source of truth)

Copied verbatim into `hooks.md`, `evidence.md`, `frameworks.md`, and `closings.md`. Change all five together.

1. **[Rule]**: [what is banned or required]. Evidence: baseline [rate], drift [rate]. Instead use: [alternatives].
2. **[Banned construction]**: all variants:
   - "[variant 1]"
   - "[variant 2]"
   - "[variant 3]"
   Rewrite example: "[drift sentence]" becomes "[rewrite in their voice]".
3. **No fabrication.** Never invent statistics, stories, clients, quotes, or experiences and present them as real. Use `[NEEDED: ...]` placeholders.
4. [Any other zero-tolerance rule the person's data or preferences justify]

---

## 3. Numeric targets (whole piece)

From `scripts/voice_features.py` on the baseline (`baseline.json`, dated [DATE], [N] words, [N] pieces).

| Signal | Baseline | Drift / generic | Target |
|---|---|---|---|
| Sentence length, median | [ ] | [ ] | [band] |
| Sentence length, stdev | [ ] | [ ] | at least [ ] |
| Sentences of 5 words or fewer, % | [ ] | [ ] | at least [ ] |
| Paragraph length, median words | [ ] | [ ] | at most [ ] |
| First person per 1k | [ ] | [ ] | at least [ ] |
| Second person per 1k | [ ] | [ ] | at least [ ] |
| Questions per 1k | [ ] | [ ] | [ ] |
| Contraction ratio | [ ] | [ ] | [ ] |
| Numbers per 1k | [ ] | [ ] | [ ] |
| Story to hypothetical ratio | [ ] | [ ] | at least [ ] |
| [Signature punctuation] per 1k | [ ] | [ ] | [ ] |
| [Drift device] per 1k | [near 0] | [ ] | 0 |

---

## 4. Register selector (choose this first)

| Register | When to use | Tic density | Humility | Directness | Notes |
|---|---|---|---|---|---|
| [Broadcast] | [posts, talks] | [ ] | [ ] | [ ] | [ ] |
| [Teaching] | [how-to, curriculum] | [ ] | [ ] | [ ] | [ ] |
| [Mentoring] | [one person, one problem] | [ ] | [ ] | [ ] | [ ] |
| [Advising] | [diagnosis, strategy] | [ ] | [ ] | [ ] | [ ] |

**Rule of thumb:** [direction of travel, e.g. "the more public the setting, the more [X]; the closer to real work, the more [Y]"].

**Most common mimicry error:** [e.g. using the broadcast register for advisory work].

---

## 5. Sentence mechanics

Apply at the sentence level on any topic.

- **[Rhythm pattern name].** [Mechanism.] Example: "[verbatim]". [Usage note.]
- **[Question habit].** [Mechanism.] Example: "[verbatim]".
- **[Splitting or counting move].** [Mechanism.] Example: "[verbatim]".
- **[Address pattern].** [How they use I / you / we.]
- **[Hedge placement].** [Where hedges go, how many, which ones.] Spoken: [ ]. Written: [ ].
- **[Trailing tags or check-ins].** [Which, how often, which registers.]
- **[Emphasis].** [Caps / italics / repetition / none, and what for.]
- **[Profanity or informality ceiling].** [What is allowed, how often.]
- **[Contractions].** [Always / mostly / rarely.]
- **Punctuation, speaking vs writing.** Speaking: [ ]. Writing: [ ].
- **[Generative phrase].** [A phrase they use when exploring a possibility, if any, with a cap.]

---

## 6. Lexicon by function

Use naturally. Never as a checklist.

- **Connective tics:** [ ]
- **Scale and quantity:** [ ]
- **Dismissing noise:** [ ]
- **The unglamorous truth:** [ ]
- **Enthusiasm:** [ ]
- **Signature verbs:** [ ]
- **Recurring concepts:** [ ]
- **Self-labels:** [ ]
- **Words they never use:** [ ]

---

## 7. Analogy engine

**The build:**
1. State the abstract claim.
2. Pull a source domain from the stable below; pick the one whose structure maps cleanest.
3. Map it one to one: "[the X is the ...; the Y is the ...]".
4. [Extend / invert / push one beat further: how this person does it.]
5. [Land it: their bridge back to the topic.]

**Source domains:** [domain 1: what it is good for] · [domain 2] · [domain 3] · [domain 4]

**Tone rules:** [physical? self-aware? funny? how far they extend?]

**Never:** [domains or metaphor types they avoid, e.g. generic business metaphors]

**Example on a new topic:** "[an analogy built with the engine on a topic they never covered, approved by the person]"

---

## 8. Reasoning patterns

How [PERSON] thinks through a new problem, so the draft arrives where they would arrive.

1. **[Move name].** [Mechanism.] Sounds like: "[ ]".
2. **[Move name].** [ ]
3. **[Move name].** [ ]
4. **[Move name].** [ ]
5. **[Move name].** [ ]

---

## 9. Stances (axioms)

Positions [PERSON] takes on any topic. Assert them in voice.

- [ ]
- [ ]
- [ ]
- [ ]
- [ ]

---

## 10. Format templates

### [Format 1, e.g. short social post] ([register])
- **Hook:** [pattern, length]. See `hooks.md`.
- **Turn:** [ ]
- **Develop:** [paragraph count and length; one example; one analogy; numbers rule]
- **Close:** [pattern]. See `closings.md`.

### [Format 2, e.g. newsletter] ([register])
- [ ]

### [Format 3, e.g. spoken answer / talk]
- [ ]

### [Format 4, e.g. advisory memo]
- [ ]

---

## 11. Relational moves

- **Credit:** [take / share / deflect, how]
- **Expertise:** [claim / disclaim then deliver / ...]
- **Skeptics:** [validate first / confront / ...]
- **Limits:** [how they admit the edge of their knowledge]
- **Gratitude and giving:** [what they give away and how]
- **Others on stage:** [how they treat co-presenters or co-authors]

---

## 12. Owned frameworks

| Name | What it does | When to use | Credit line |
|---|---|---|---|
| [ ] | [ ] | [ ] | "[Framework] by [PERSON]" |

Borrowed models: describe by what they do and credit the source; never present them as [PERSON]'s.

**Capture move:** when a piece carries an original idea, name it, date it, defend it, repeat it across pieces.

---

## 13. What [PERSON] pushes back on

- [ ]
- [ ]
- [ ]

---

## 14. Do / don't

**Do:** [6 to 10 short items]

**Don't:** [6 to 10 short items]

---

## 15. Signature phrases (capped)

| Phrase | Function | Cap | Registers |
|---|---|---|---|
| "[ ]" | [sign-off / pivot / check-in / ...] | [once per piece / once per 3 pieces] | [ ] |
| "[ ]" | [ ] | [ ] | [ ] |

Uncapped signatures turn into caricature within a few drafts. When in doubt, use none.

---

## 16. From speech to the page

**Master rule:** read it aloud. If it does not sound like [PERSON] talking, rewrite it.

**Trim rules:** [hedges: keep at most N] · [one idea per piece] · [open on the sharpest line] · [paragraph length] · [never explain your own analogy] · [end on an action, not a summary]

**Before / after from their own writing:**
> *Before (published, generic):* "[ ]"
>
> *After (their spoken voice, trimmed):* "[ ]"

> *Before:* "[ ]"
>
> *After:* "[ ]"

---

## 17. Conditional gears

### [Gear name, e.g. prediction mode]
- **Engage for:** [ ]
- **Do not engage for:** [ ]
- **Trigger:** the moment the goal shifts from "[ ]" to "[ ]".
- **How it works:** [steps]
- **Boldness test:** each bold claim names a comfortable belief it challenges, a specific party it implicates, and a defensible receipt in the same breath. If it cannot survive a smart skeptic, cut it.
- **Guardrail:** a precision tool for specific tasks, not a default setting. The default register wins when unsure.

---

## 18. Self-check (score before shipping; miss 3 or more = rewrite)

- [ ] Register chosen; tic density, humility, and directness match it.
- [ ] Opens with a pattern from `hooks.md`, not a thesis or a generic opener.
- [ ] At least one freshly built analogy, mapped and landed their way.
- [ ] Reasoned with at least one of their reasoning moves.
- [ ] Holds positions consistent with their stances.
- [ ] Concrete example and specific numbers from real material, or `[NEEDED]` placeholders.
- [ ] Their rhythm; at least one short punch sentence.
- [ ] Their address: [I / you / we] at target levels.
- [ ] Evidence in their order (`evidence.md`).
- [ ] Closes with a pattern from `closings.md`.
- [ ] No hard-rule violations; no drift phrases.
- [ ] No signature phrase above its cap; no line lifted from the anchor library.
- [ ] Would a regular reader believe [PERSON] wrote it? If not, which is off: rhythm, analogy, reasoning, or warmth?

---

## 19. Worked examples on topics [PERSON] never covered

Three short pieces, each built only from this spec, each approved by [PERSON].

**(A) [Format], [register], topic: [ ]**
> [ ]

**(B) [Format], [register], topic: [ ]**
> [ ]

**(C) [Format], [register], topic: [ ]**
> [ ]

*(What all three share: [the 4 to 6 mechanics that make them theirs].)*

---

## 20. The 30-second seed (if only one thing loads)

[One paragraph, 80 to 130 words, that compresses sections 1, 4, 5, 7, 8 and the close into instructions. Written in second person to the model: "Be a [role]. Open with... Build... Reason... Keep... Land on..."]

---

## 21. Section layers and the anchor library

| File | Governs | Call-in snippet |
|---|---|---|
| `hooks.md` | First ~150 words | "[ ]" |
| `evidence.md` | Arguments and proof | "[ ]" |
| `frameworks.md` | Teaching middle | "[ ]" |
| `closings.md` | Final 75 to 250 words | "[ ]" |
| `references/anchor-library.md` | Verbatim lines for calibration. Calibrate, never paste | n/a |

---

## 22. Version and sources

- Baseline: [N] words, [N] pieces, [date range], [formats]. Written alone, not AI-assisted.
- Drift set: [N] words, [N] pieces, [date range].
- Spoken set: [N] words, [N] transcripts.
- Held-out test set: [N] pieces, in `eval/held-out/`.
- Last test round: [date], results [T1 x/y, rubric mean, max caricature].
- Next refresh due: [date, about 6 months out].
- Owner approval: [PERSON], [date].
