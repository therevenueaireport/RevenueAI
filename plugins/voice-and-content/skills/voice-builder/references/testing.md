# Testing a Voice Skill: Blind Comparisons and the Iteration Loop

**Use this file when:**
- A voice spec is written and you need to know whether it works.
- The owner says drafts "sound off" but cannot say why.
- You changed the spec and need to know whether it got better or just different.

A voice skill is done when two things are true: people who know the voice cannot reliably pick the AI piece out of a blind pair, and the owner would sign drafts after light edits. Everything below serves those two tests.

---

## 1. Build the test set before you build the spec

In Step 1 of the build you held out 10 to 20 percent of the pieces. That is the test set. Rules:

- **Never read held-out pieces closely while building.** If you build from them, the test measures memory, not voice.
- **Spread across formats and registers.** At least two pieces per format you care about (post, newsletter, memo) and per register (broadcast, teaching, mentoring, advising).
- **Write a content brief for each held-out piece.** Topic, the three to five points it makes, and the real stories, numbers, and examples it uses. Ideally someone other than the person building the spec writes the briefs. The brief carries the content so the test measures voice, not ideas.
- **Freeze it.** The same test set is used every iteration round. Changing it between rounds hides whether the spec improved.
- **Keep a reserve.** Hold back a few more pieces that you never use until the final round. They catch overfitting to the frozen set.

---

## 2. The test battery

| Test | Question it answers | Judges | When |
|---|---|---|---|
| T1. Held-out reconstruction (blind A/B) | Can people tell the AI piece from the real piece on the same content? | Owner + 2 to 4 regular readers | Every round |
| T2. Section swap | Are openings and closings convincing on their own? | Same judges, faster | Every round |
| T3. New-topic generalization | Does the voice survive a topic the person never covered? | Owner, plus rubric scoring | Every round |
| T4. Register test | Does the skill shift correctly by setting? | Owner + 1 reader | Rounds 1 and final |
| T5. Caricature check | Is it exaggerated? | Owner + 1 reader who knows the person well | Every round |
| T6. Quantitative distance | Are the numbers inside the person's range? | Script | Every draft |
| T7. Live edit load | How much does the owner change before publishing? | Owner's before and after | Ongoing after launch |

### T1. Held-out reconstruction (the core blind A/B)

1. For each held-out piece, generate a version from its content brief using the voice skill. Target the same length (within about 15 percent) and format.
2. **Normalize the pair.** Same title treatment, no images, same formatting, same line-break style. Remove anything that gives away the source other than the writing itself (dates, platform artifacts, a reference to an event after the piece was published).
3. **Randomize** which one appears as A and which as B, with a coin flip or a random number, recorded in a key the judges never see.
4. **Calibration pairs.** Add two or three pairs where B is a generic AI draft from the same brief with no voice instructions. Judges should spot these easily; if they cannot, they do not know the voice well enough to judge, and their other answers are noise.
5. **Ask each judge, per pair:**
   - Which one did a machine write? (A or B)
   - How sure are you? (1 guessing, 2 leaning, 3 certain)
   - What gave it away? (one sentence, required even when guessing)
6. **Score.** Count correct identifications per judge and pooled. Read every "what gave it away" answer; those reasons are the most valuable output of the whole test.

**How many correct answers mean the AI piece is detectable?** If judges are guessing, each pair is a coin flip. The table shows the number of correct picks out of *n* pairs at which guessing becomes an unlikely explanation (one-sided, about the 5 percent level):

| Pairs judged | Correct picks that mean "detectable" |
|---|---|
| 8 | 7 or more |
| 10 | 9 or more |
| 12 | 10 or more |
| 16 | 12 or more |
| 20 | 15 or more |
| 30 | 20 or more |
| 40 | 26 or more |

Pool judges' answers to reach 20 to 40 judgments. Two cautions:
- Scoring below the threshold with few pairs is weak evidence that the voice is right. It may only mean the test was too small. Treat the reasons as the real result.
- Scoring *well below* chance (judges confidently picking the real piece as the AI one) is a signal too: the AI version is more like the person's idea of themselves than their actual writing. That often means caricature.

### T2. Section swap

Same as T1, but pair only openings (first 150 words) or only closings (last 150 words). It takes judges a fraction of the time, so you can run more pairs, and it isolates the two sections that drift hardest. If T1 fails and T2 passes, the problem is in the middle: evidence or frameworks.

### T3. New-topic generalization

Pick three topics the person has never written about, in different registers, ideally outside their field. Generate one piece per topic. There is no real counterpart, so:
- The owner answers: "Would I sign this after light edits?" (yes / with heavy edits / no) and "Is there any sentence I would never say?" (mark them).
- Score with the rubric in section 3.
- Check reasoning: "Did it arrive at a conclusion I would arrive at?" A voice skill that sounds right and argues wrong has a thin reasoning and stance section.

### T4. Register test

Generate the same content in two registers (for example, a public post and a one-to-one note to a struggling colleague). Shuffle them with real examples of each register. Ask the owner to label the register of each. If the AI pieces get labeled wrong, the register table needs sharper differences.

### T5. Caricature check

Ask the owner and one person who knows them well, for each AI piece: "On a scale of 0 to 3, how much does this exaggerate me?" (0 none, 1 a little heavy in places, 2 noticeably overdone, 3 parody). Any 2 or 3 is a fail regardless of other scores. Common causes: uncapped signature phrases, the broadcast register used everywhere, several hook patterns stacked in one opening, every analogy extended to its limit.

### T6. Quantitative distance

```bash
python3 scripts/voice_features.py score corpus/baseline eval/round-3/
```

Record mean |z| and the out-of-range features per piece. Use it to explain human failures ("judges said 'too formal'; first-person rate is 2.4 standard deviations low") and to catch regressions between rounds. Never use it as the pass criterion on its own. See [feature-extraction.md](feature-extraction.md) section 6.

### T7. Live edit load (after launch)

Save every AI draft and the version the owner actually published. Once a month, measure:
- Share of sentences changed, added, or deleted (a word-level diff tool or a simple sentence comparison is enough).
- What the owner added (often: a real story, a sharper opener, a specific number) and what they cut (often: hedges, summaries, generic transitions).

Falling edit load over time means the skill is learning. Recurring edits of the same kind are spec changes waiting to be made.

---

## 3. The "sounds like me" rubric

Score each AI piece 1 to 5 on eight dimensions. Anchors are for scores 1, 3, and 5; use 2 and 4 between them.

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| **Rhythm** | Even, mid-length sentences throughout; no punches | Some variety, but the long-short pattern is mechanical or misplaced | Sentence and paragraph shape indistinguishable from the person's; punches land where they would put them |
| **Address and relationship** | Talks about the market; no "I" or "you"; institutional | Some direct address, but the relationship feels borrowed (too chummy or too distant) | Talks to the reader exactly the way the person does: same closeness, same kind of "we" |
| **Lexicon** | Generic business vocabulary; drift words present | Some of the person's words, some foreign ones; or their words used in odd places | Words chosen by function as they would; nothing they would never say |
| **Analogy and imagery** | None, or generic business metaphors | An analogy from the right domain, but stiff, or explained after it is made | A new analogy they would plausibly invent, mapped and landed their way |
| **Reasoning and stance** | Conclusion they would not reach, or no position at all | Right conclusion, reached by a route they would not take | Reasons the way they do and lands where they would land |
| **Evidence style** | Stacked statistics, hypotheticals, "studies show" | Mix of real and hypothetical; data and story order off | Their evidence order, their story-to-data ratio, real anchors only |
| **Structure: opening and closing** | Generic opener, summary closer | One of the two is theirs | Both open and close in a pattern from their signature files |
| **Register fit** | Wrong setting entirely (keynote voice in a mentoring note) | Right register, wrong intensity | Exactly the voice they use in this setting |

**Penalties and hard fails:**
- **Caricature:** subtract the T5 score (0 to 3) from the total.
- **Drift tells:** subtract 1 for each hard-rule violation (banned construction, banned device).
- **Fabrication (hard fail):** any invented statistic, story, client, quote, or experience presented as real. The piece fails regardless of score.
- **Lifted line (hard fail):** any sentence pasted from the anchor library into a new context.

**Pass bar (rule of thumb):** 32 or more out of 40 after penalties, no dimension below 3, no hard fail, and the owner answers "yes" or "with light edits" to "Would I sign this?".

**The owner's two questions** are the tie-breaker for everything. A piece can score 36 and still fail if the owner says "I would never say that." Find out which sentence and why.

---

## 4. The iteration loop

```
run the battery  ->  log every failure reason  ->  classify  ->  map to spec section
       ^                                                                  |
       |                                                                  v
  regression check  <-  regenerate the frozen set  <-  change ONE thing
```

### 4.1 Classify each failure reason

| Reason category | Example judge comment (fictional) | Spec section to change |
|---|---|---|
| Rhythm | "Every sentence was the same length" | Sentence mechanics; numeric targets |
| Address | "Too corporate, not talking to me" | Pronoun floors in hooks and closings |
| Lexicon | "They'd never say 'leverage'" | Lexicon; banned list |
| Analogy | "That comparison is not something they'd reach for" | Analogy engine source domains; tone rules |
| Reasoning | "They'd blame the process, not the tool" | Reasoning patterns; stances |
| Evidence | "Too many stats, no story" | Evidence stack; citation cap; real-over-hypothetical |
| Opening or closing | "Ended with a summary; they always give you a task" | Hooks or closings signature; number-one drift |
| Register | "Too salesy for a mentoring note" | Register table |
| Caricature | "Their catchphrase three times" | Frequency caps; tic density by register |
| Fabrication | "That story never happened" | Sourcing rule; placeholder rule |

### 4.2 Change one thing per round

Pick the category with the most failures. Make one targeted change: a sharper rule, a new formula, a frequency cap, a better real example, a new banned phrase. Changing five things at once makes it impossible to know which one helped, and voice specs are prone to side effects (fixing "too formal" by adding tics often produces caricature).

### 4.3 Regenerate and compare

Regenerate the whole frozen test set with the changed spec. Rerun T1, T2, T5, and T6 at minimum. Compare to the previous round:
- Did the targeted failure category shrink?
- Did any other category grow? (regression)
- Did mean |z| move toward the baseline?

Keep the change only if the targeted category improved without a regression. Otherwise revert.

### 4.4 Log it

```
## Round [n], [date]
Change: [one sentence: what changed, in which file and section]
Reason: [failure category, count last round]
Results: T1 [correct/pairs], T2 [correct/pairs], T5 max caricature [0-3],
         rubric mean [x/40], mean |z| [x]
Effect: [category count before -> after]; regressions: [none / which]
Decision: keep / revert
```

### 4.5 When to stop

Stop iterating and ship when all of these hold:
- T1 and T2 pooled judgments are below the "detectable" threshold for your number of pairs.
- No caricature score above 1.
- Rubric mean of 32 or more with no hard fails.
- The owner says "with light edits" or better for every T3 piece.
- The final reserve pieces (never seen before) pass T1 at the same level as the frozen set. If they do noticeably worse, you overfit; add patterns from a broader slice of the baseline.

Most voice skills need two to four rounds. If round five still fails on the same category, the problem is usually upstream: a contaminated baseline (AI-assisted writing slipped in), too small a corpus for that register, or a family that was never coded (most often reasoning or stances).

---

## 5. Test log template

```
eval/
  briefs/           one content brief per held-out piece
  held-out/         the real pieces (never used for building)
  reserve/          final-round pieces
  rounds/
    round-1/        generated pieces + key.csv (pair id, which side is AI)
    round-2/
  judgments.csv     round, judge, pair_id, pick, confidence, reason
  rubric.csv        round, piece_id, 8 dimension scores, penalties, owner_sign (Y/light/N)
  changelog.md      one entry per round (format in 4.4)
```
