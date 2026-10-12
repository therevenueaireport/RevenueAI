# Qualitative Extraction: The Mind Behind the Sentences

**Use this file when:**
- The numbers are done and you need the patterns no script can count: how the person reasons, what they believe, how they build a comparison, how they shift by setting.
- A voice skill produces drafts that match the surface but argue like someone else.
- You are filling the qualitative sections (1 and 4 to 17) of [the voice spec template](../assets/voice-spec-template.md).

The goal is a **generative** model. A list of the person's best lines teaches a model to remix old material. A description of the machinery (how they open, compare, reason, and land) lets a model write something new that the person would have written.

**Prime directive for the finished spec:** do not retrieve and remix. Run the person's machinery on the new topic.

---

## 1. Method

### 1.1 Reading order

1. Spoken set first (transcripts). People reason out loud more openly than they write. Metaphors, stories, and stances are densest here.
2. Baseline written set second. This is where you learn how the person structures a page.
3. Drift set last, and only to see what went missing.

### 1.2 Coding sheet

Work in a spreadsheet, one row per instance:

```
piece_id | register | family (1-12 below) | pattern label | verbatim excerpt | notes
```

**The three-instance rule:** a pattern goes into the spec only when you have at least three instances from at least two different pieces. Fewer than that is an anecdote. Keep anecdotes in the anchor library, not in the rules.

### 1.3 Ask the person

After the first coding pass, interview the person for 30 to 45 minutes. Show them five patterns you found and ask:

- "Is this you, or is this a habit you want to lose?"
- "Which writer do you never want to sound like?" (their answer feeds the against list and banned constructions)
- "What do you say out loud that never makes it into your writing?"
- "When you edit an AI draft, what do you always cut? What do you always add?"
- "Which of your pieces do you think sounds most like you? Least?"

The last question gives you a calibration pair. Profile both with the script; the gap is often the clearest summary of the voice.

---

## 2. The twelve pattern families

For each family: what to look for, the coding question, and what the finished spec text looks like. Examples come from a fictional writer, "Writer A", a revenue operations leader. They show the shape of good spec text, not content to copy.

### Family 1: The operating system (the generative seed)

**Look for:** the job the person does for a reader in every piece. Explainer, skeptic, field reporter, builder, coach, contrarian, cartographer. Their default posture (warm, dry, urgent, playful). Their recurring beliefs about where problems really come from.

**Coding question:** "If I removed every topic word, what would still be true of every piece?"

**Spec text shape (one paragraph, then one line):**
> Writer A is an operator who distrusts anything that has not been counted. Default posture: dry, specific, slightly impatient with ceremony, generous with method. Talks to the reader as a peer who has the same messy systems. Reaches for a number within two sentences of any claim. Ends by handing over a task small enough to do this week.
>
> **If you internalize one thing:** Writer A is an auditor who likes people. Every piece finds the waste, counts it, and gives the reader the first cut.

### Family 2: Registers

**Look for:** how the voice changes by setting. Most people have three to five registers. Common ones: broadcast (posts, talks), teaching (explaining a concept), mentoring (one person, one problem), advising (diagnosing a business). Code each instance's register, then compare tic density, humility, and directness across registers.

**Coding question:** "Would this sentence appear in their other settings? If not, what changed?"

**Spec text shape:** a table.

| Register | When | Tic density | Humility | Directness |
|---|---|---|---|---|
| Broadcast | Posts, talks | [high/medium/low] | [ ] | [ ] |
| Teaching | How-to, curriculum | [ ] | [ ] | [ ] |
| Mentoring | One person, one problem | [ ] | [ ] | [ ] |
| Advising | Diagnosis, strategy | [ ] | [ ] | [ ] |

Plus a rule of thumb for direction of travel. A common pattern: the more public the setting, the softer and more decorated the voice; the closer to real work, the sharper and more prescriptive. Check whether your person follows it or inverts it. Then name the most likely mimicry error (usually: using the public register for private work).

### Family 3: Sentence mechanics

**Look for:** rhythm shape (long build then short punch; even and measured; staccato), question habits (question then immediate answer; questions left open), splitting moves (always two sides; always three items; counting out loud), self-interruption, address (you, we), hedges and where they sit, trailing tags, enthusiasm markers, profanity ceiling, punctuation differences between speech and writing, repetition for emphasis, a generative phrase they use when exploring.

**Coding question:** "If I blurred the words, what would the shape of this paragraph look like?"

**Spec text shape:** one bullet per mechanic, each with the mechanism, one real example, and a usage note.
> **Count, then cut.** Writer A states a total, then the share that matters. "Eleven reps, 38 opportunities, four minutes of inspection." Use once per piece, in the evidence section.

### Family 4: Lexicon by function

**Look for:** the person's words grouped by the job they do, not alphabetically. Connective tics, words for scale, words for dismissing noise, words for the unglamorous work, enthusiasm words, signature verbs, recurring concepts, self-labels.

**Coding question:** "When they need to say 'this is unimportant', what word do they reach for?"

**Spec text shape:** one line per function, five to eight words each, and a warning: use naturally, never as a checklist. Grouping by function is what lets a model pick the right word for a new sentence instead of sprinkling favorites.

### Family 5: The analogy engine

The single most distinctive feature of many voices, and the one generic drafts lose first.

**Look for:** every comparison. Record the abstract claim it served, the source domain, how tightly it maps, whether it gets extended or inverted, and how the writer bridges back to the topic.

**Coding question:** "What world do they borrow from when the idea gets abstract, and what do they do with the comparison after they make it?"

**Spec text shape:** a build procedure plus a list of source domains.

> **The build (Writer A):**
> 1. State the abstract claim.
> 2. Pull a source domain from the stable: commercial kitchens, plumbing, freight logistics, household budgets.
> 3. Map it one to one: "the CRM is the walk-in fridge; the rep is the line cook; the stale data is the unlabeled container in the back."
> 4. Extend it one beat: "and nobody throws the container out, because nobody knows who put it there."
> 5. Bridge back: "Same with your routing rules."
>
> **Tone rules:** physical, visible, slightly unglamorous. Never sports. Never war.

Then test the engine: write one new analogy for a topic the person never covered and ask them whether they would have said it. If not, your domain list or your build steps are wrong.

### Family 6: Reasoning patterns

**Look for:** the moves the person makes on the way to a conclusion. Backwards from the outcome. First principles. Splitting false binaries. Asking what will not change. Finding the unglamorous root cause. Separating the tool from the process. Admitting uncertainty in a specific way.

**Coding question:** "Given a brand-new problem, what would they ask first, and where would they look for the cause?"

**Spec text shape:** five to ten numbered moves, each one sentence of mechanism plus one sentence of how it sounds. This family is what makes a model **arrive where the person would arrive**, not just sound like them. Weak voice skills skip it; their drafts have the right rhythm and the wrong opinions.

### Family 7: Stances (the axioms)

**Look for:** positions the person holds across topics. Where problems usually come from. What matters more than people think. What matters less. What they are optimistic or pessimistic about. What they believe about their audience.

**Coding question:** "If I dropped them into a topic they have never discussed, what positions would they take before learning anything?"

**Spec text shape:** 10 to 20 one-line axioms in the person's voice. Mark any the person wants to retire.

### Family 8: The against list

**Look for:** what they reflexively push back on: hype without evidence, a type of jargon, a type of leader, a type of tool purchase, a format.

**Coding question:** "What makes them roll their eyes?"

**Spec text shape:** 6 to 12 bullets. This gives the model a way to critique new things in voice, and it feeds the banned list.

### Family 9: Relational moves

**Look for:** how they handle credit (take it, share it, deflect it), expertise (claim it, disclaim it then show it), skeptics (validate first, or confront), gratitude, giving things away, people who share a stage with them, admitting the edge of their knowledge.

**Coding question:** "How do they make the reader feel about themselves?"

**Spec text shape:** 5 to 8 abstract moves, no names. These moves are much of what readers call "warmth" or "authority"; they are rarely captured by surface features.

### Family 10: Owned frameworks and the capture move

**Look for:** named models, acronyms, numbered systems the person created. Their naming style (alliteration, acronym, plain words), their numbering format, how they reintroduce a framework across a series.

**Spec text shape:** one line per framework with what it does and when to use it, plus credit rules. Distinguish clearly between the person's own frameworks and borrowed ones; the spec must never present a borrowed model as theirs.

**The capture move:** when a piece carries an original idea, name it, date it, defend it, and repeat it across pieces. A named, dated, defended idea becomes associated with its author; an unnamed, hedged one becomes common wisdom someone else claims. Put this rule in the spec if the person wants to build owned ideas.

### Family 11: The speech-to-writing gap

Many people are vivid out loud and generic on the page. When they sit down to write, they put on a costume: abstractions, listicles, borrowed corporate vocabulary.

**Look for:** features strong in the spoken set and weak in the written set (analogies, stories, rhythm, humor), and the reverse (structure, precision).

**Spec text shape:**
- **The master rule:** read the draft aloud. If it does not sound like the person talking, rewrite it. Spoken voice in, then trim. Never costume in.
- **The trim rules:** keep one hedge for humility and cut the rest (hedges are warm in speech and mushy in print); keep the analogy and cut the explanation of the analogy; one idea per piece; open on the sharpest line; short paragraphs.
- **Before/after proof:** take two passages from the person's own published writing that read generic, rewrite them in their spoken voice, and put both versions in the spec. Nothing teaches a model the target faster than a before/after pair from the same person on the same idea.

### Family 12: Conditional gears

Some people have a mode that is right for one task and wrong for all others: a sharper contrarian mode for predictions, a stricter mode for compliance writing, a gentler mode for beginners.

**Spec text shape:**
- **Engage for:** an explicit list of tasks.
- **Do not engage for:** an explicit list, usually the vulnerable audiences.
- **Trigger rule:** one sentence that names the moment the goal shifts (for example, from "help this reader feel capable" to "make this idea impossible to ignore").
- **How the gear works:** for a prediction mode, a reliable recipe is: call the second-order consequence instead of the first-order capability; name where human value concentrates as automation rises; locate the bottleneck in people, process, or systems; commit to the direction and stay honest about the timing.
- **The boldness test:** each bold claim needs a comfortable belief it challenges, a specific party it implicates, and a defensible receipt in the same breath. Run a skeptic test: if the only thing holding the claim up is the heat, cut it.
- **Guardrail:** the gear is a precision tool, not a default setting. Used everywhere, it burns the trust the default voice built.

---

## 3. Building the anchor library

The anchor library is a set of verbatim lines that calibrates the model's ear. It is the most powerful and the most dangerous part of a voice skill.

**Rules:**
1. **Verbatim only.** Trim to a coherent span. Never add or change a word. A "lightly improved" quote teaches the model your edit, not their voice.
2. **Group by theme and by register.** Identity and origin; humility; tics in real sentences; each major stance; teaching; mentoring; advising; closings. Grouping lets the model find the right rhythm for the task.
3. **Label it "calibrate, never paste."** The instruction at the top: absorb the rhythm; do not put these lines into new pieces as if the person said them there. The test: if a newly generated sentence could sit in this list unnoticed, the voice is right.
4. **Exclude private and third-party material.** Family details, clients, colleagues, anything said in confidence, anyone else's words. The owner reviews the full library before use.
5. **Size:** 100 to 300 lines is plenty. More adds tokens without adding signal.
6. **Refresh it.** Lines from the last 12 months carry the current voice. Mark each line's year.

---

## 4. Turning patterns into spec text: quality checks

Before a pattern goes into the spec, check:

- [ ] Three or more instances, two or more pieces.
- [ ] Written as a mechanism, not as a quote.
- [ ] Has one real example and, where useful, a fill-in formula.
- [ ] Has a frequency cap or a register limit if it is a signature.
- [ ] Does not contradict a rule elsewhere in the spec or a section file.
- [ ] Does not require the model to invent facts, stories, or numbers.
- [ ] The person agreed it is them and not a habit they want to lose.
