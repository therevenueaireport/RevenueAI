# Feature Extraction: The Measurable Voice

**Use this file when:**
- You have a labeled corpus and need the numbers that define the voice.
- You want to know whether AI-assisted writing has drifted from the person's real voice, and in which direction.
- You are setting the numeric targets for a voice spec or a section signature.
- A draft "feels off" and you want to find out which feature is wrong.

Numbers do not capture a voice. They catch the two failures that ruin most voice skills: rhythm that has flattened, and address that has gone institutional. They also turn vague notes ("more personal") into checkable targets ("at least 3 first-person and 3 second-person words in the first 150 words").

---

## 1. Running the script

`scripts/voice_features.py` is plain Python 3 with no dependencies. It reads every `.txt`, `.md`, and `.markdown` file under a folder, recursively.

```bash
# Profile one corpus, with a per-document table and a JSON dump
python3 scripts/voice_features.py profile corpus/baseline --per-doc --json baseline.json

# Compare two corpora: baseline vs drift, spoken vs written, raw vs edited
python3 scripts/voice_features.py compare corpus/baseline corpus/drift --json compare.json

# Recurring phrases in one corpus (signature candidates)
python3 scripts/voice_features.py phrases corpus/baseline --n 3 --min-docs 3

# Phrases lost and introduced between two corpora
python3 scripts/voice_features.py phrases corpus/baseline corpus/drift --n 2
python3 scripts/voice_features.py phrases corpus/baseline corpus/drift --n 3

# Score a draft (file or folder) against the baseline's per-document spread
python3 scripts/voice_features.py score corpus/baseline drafts/new-post.md

# Add your own watchlist phrases (one per line, # for comments)
python3 scripts/voice_features.py compare corpus/baseline corpus/drift --watch my-watchlist.txt
```

Try it first on the bundled fictional corpus:

```bash
python3 scripts/voice_features.py compare scripts/sample-corpus/pre-ai scripts/sample-corpus/post-ai
python3 scripts/voice_features.py score scripts/sample-corpus/pre-ai scripts/sample-corpus/draft-test.md --min-words 100
```

The sample is a fictional operations leader. The pre-AI set is short, first-person, number-heavy, with semicolons, parentheses, `1)` lists, and imperative closings. The post-AI set is the same writer after an AI assistant took over drafting. The compare run flags the drift on almost every family: first-person and second-person rates collapse, sentence length rises, short sentences vanish, numbers drop, hypothetical "imagine" examples appear, dashes and setup-and-reversal constructions appear, and every closing becomes a summary. The sample corpus is under 1,000 words per side, so the script warns that the rates are noisy. Your real corpus should be much larger.

### What the script cleans before counting

- YAML front matter, fenced code blocks, inline code, HTML tags, images, and URLs are removed. Link text is kept.
- Block quotes (`>` lines) are dropped, because they are usually someone else's words.
- Headings are counted, then excluded from sentence statistics.
- List items are counted by style, then analyzed as sentences but not as paragraphs.
- Curly quotes and apostrophes are normalized.
- Hard-wrapped text (long lines that do not end in punctuation) is joined. One-sentence-per-line text, common in social posts, keeps each line as its own sentence.

### Preparing the corpus

- One piece per file. Name files so they sort by date.
- Keep spoken and written material in separate folders. Transcripts carry filler and run-ons that distort written targets.
- Remove other people's words: interview questions, co-author sections, quoted emails, comments.
- Remove boilerplate: signatures, legal footers, "originally published in" lines, repeated bios.

---

## 2. The features

Rates are per 1,000 words unless the name says per 10k. Percentages are of sentences or paragraphs as named. "Drift direction" describes the usual movement when an AI assistant drafts for a person; it is a qualitative tendency, not a measured constant. Your compare run tells you what actually happened in your corpus.

### 2.1 Rhythm

| Feature | How it is computed | What it tells you | Usual drift direction |
|---|---|---|---|
| `sent_len_mean`, `sent_len_median` | Words per sentence | Overall density | Up |
| `sent_len_stdev` | Population standard deviation of sentence length | Variety. Low stdev reads as machine-even | Down |
| `sent_len_p10`, `sent_len_p90` | 10th and 90th percentile length | The short floor and the long ceiling | Floor rises |
| `pct_sent_short_le5` | Share of sentences with 5 or fewer words | Punch lines and fragments | Down sharply |
| `pct_sent_long_ge25` | Share of sentences with 25 or more words | Run-on builds | Varies |
| `rhythm_swing_mean` | Mean absolute difference in length between consecutive sentences | Long-then-short alternation. Two writers can share a stdev and differ here | Down |
| `sent_len_buckets_pct` | Distribution across 1-5, 6-10, 11-15, 16-20, 21-30, 31+ | The full shape. Drift piles into 11-20 | Middle buckets swell |
| `para_len_words_mean`, `para_len_words_median` | Words per prose paragraph | White space habit | Up |
| `para_len_sents_mean` | Sentences per paragraph | Block vs line style | Varies by platform |
| `pct_one_sentence_paras` | Share of one-sentence paragraphs | Emphasis by isolation | Platform dependent; check per format |

### 2.2 Address

| Feature | How it is computed | What it tells you | Usual drift direction |
|---|---|---|---|
| `first_singular_per_1k` | I, me, my, mine, myself, I'm, I've, I'd, I'll | Ownership and lived experience | Down sharply |
| `first_plural_per_1k` | we, us, our, ours, ourselves, we're, we've, we'd, we'll, let's | Inclusive or institutional "we" (read in context: they are different voices) | Shifts from inclusive to institutional |
| `second_person_per_1k` | you, your, yours, yourself, you're, you've, you'd, you'll | Talking to the reader vs about the market | Down sharply |

Read these together. A high-first, high-second writer is having a conversation. A low-first, low-second writer is publishing a report. Most drift moves a person from the first to the second without anyone deciding it.

### 2.3 Questions and exclamations

| Feature | How it is computed | What it tells you |
|---|---|---|
| `question_marks_per_1k` | Count of `?` | Dialogic writing |
| `pct_sent_questions` | Share of sentences ending in `?` | Same, normalized by sentence count |
| `pct_paras_open_question` | Share of paragraphs whose first sentence is a question | Question-led structure, common in hooks and handoffs |
| `pct_paras_end_question` | Share of paragraphs whose last sentence is a question | Rhetorical landings and reader handoffs |
| `exclamations_per_1k` | Count of `!` | Energy ceiling. Set as a cap, not a floor |

### 2.4 Register and stance

| Feature | How it is computed | What it tells you |
|---|---|---|
| `contractions_per_1k` | Tokens ending in n't, 're, 've, 'll, 'd, 'm, plus it's, that's, here's, let's and similar | Casualness |
| `contraction_ratio` | Contractions / (contractions + expanded forms like "do not", "it is") | Casualness independent of topic. Near 1.0 is spoken; below 0.5 is formal |
| `hedges_per_1k` | I think, maybe, perhaps, probably, might, kind of, sort of, seems, I believe, and similar | Humility vs certainty. Warm in speech, mushy in writing |
| `intensifiers_per_1k` | very, really, totally, absolutely, literally, super, and similar | Enthusiasm style |
| `pct_sent_imperative` | Share of non-question sentences starting with a common command verb (try, take, ask, pick, count, run, and about 60 others) | Coaching and advisory voice. Heuristic: edit the verb list for your domain |
| `pct_sent_conj_start` | Share of sentences starting with And, But, So, Because, Or, Yet | Spoken cadence on the page |

### 2.5 Evidence and specificity

| Feature | How it is computed | What it tells you |
|---|---|---|
| `numbers_per_1k` | Numeric tokens, including $ and % | Data density |
| `pct_sent_with_number` | Share of sentences containing a number | How evenly numbers spread |
| `percent_signs_per_1k` | Count of `%` | Statistic habit specifically |
| `story_markers_per_10k` | "I remember", "when I was", "years ago", "last week", "yesterday", "one time", and similar | Lived experience as evidence |
| `hypothetical_markers_per_10k` | "imagine", "picture this", "let's say", "suppose", "what if" | Invented scenarios standing in for real ones. Rises with drift |
| `simile_markers_per_1k` | "like a", "as if", "think of it as", "it's like", "the same way", "reminds me of", and similar | A proxy for figurative language. See section 3 for the real metaphor rate |

The ratio of story markers to hypothetical markers is one of the most diagnostic numbers you have. A writer who argues from "I remember when" and drifts to "Imagine a sales manager" has lost the thing readers came for.

### 2.6 Structure

| Feature | How it is computed | What it tells you |
|---|---|---|
| `list_items_per_1k` | List lines per 1,000 words | List reliance. Drift often adds lists |
| `pct_lines_list` | List lines as a share of non-blank lines | Same, by layout |
| `list_styles` | Counts of `-`, `*`, bullet characters, `1.`, `1)`, `1-` | Numbering habits can be idiosyncratic and recognizable |
| `headings_per_1k` | Markdown heading lines | Document vs conversation |

### 2.7 Punctuation and emphasis

| Feature | How it is computed | What it tells you |
|---|---|---|
| `em_dash_per_1k` | Em dash characters plus spaced double hyphens | One of the most visible AI-drafting tells. Compare to the person's baseline, not to a general rule |
| `en_dash_or_spaced_hyphen_per_1k` | En dashes plus " - " | Writers who type dashes by hand often use this form |
| `ellipses_per_1k` | `..`, `...`, and the ellipsis character | Trailing-off, spoken softness |
| `semicolons_per_1k` | Count of `;` | A formal or precise writer's tell |
| `colons_per_1k` | Count of `:` (excluding emoticons) | Setup-and-payoff habit |
| `parentheses_per_1k` | Count of `(` | Asides, self-commentary |
| `caps_emphasis_per_1k` | ALL-CAPS tokens whose lowercase form also appears in the corpus (so "NEVER" counts, an acronym never seen in lowercase does not) | Shouted emphasis. `top_caps_emphasis` and `top_acronyms` let you check the split |
| `emoji_emoticons_per_1k` | Emoji plus `:)`, `;)`, `:D` and similar | Platform-appropriate warmth. Usually a per-format rule |

### 2.8 Lexical

| Feature | How it is computed | What it tells you |
|---|---|---|
| `avg_word_len` | Mean letters per alphabetic word | Plain vs latinate vocabulary. Drift raises it |
| `mattr_200` | Moving-average type-token ratio over 200-word windows | Vocabulary range, stable across corpus sizes |
| `flesch_reading_ease`, `fk_grade` | Standard readability formulas with a heuristic syllable counter | Ease. Use for comparison, not as an absolute |

### 2.9 Openers and closers

The script classifies the first sentence and the last paragraph of each document.

**Opener types:** `question`, `quote`, `time_or_memory_anchor` (today, last Tuesday, years ago, when I...), `number_or_stat`, `direct_address` (you, if you, have you...), `imperative`, `first_person`, `short_declarative` (6 words or fewer), `declarative`.

**Closer types:** `summary_marker` (in conclusion, bottom line, ultimately...), `forward_tease` (next week, more to come...), `question`, `warm_wish_or_invite` (I hope, let me know, reply and...), `imperative_action` (any sentence in the last paragraph starts with a command verb), `short_punch`, `declarative`.

These are first-pass labels. For section signatures you will hand-classify against a richer taxonomy (see [section-signatures.md](section-signatures.md)); the script gives you the quick distribution and catches drift like "every closing became a summary."

### 2.10 Drift tells

| Feature | How it is computed | What it tells you |
|---|---|---|
| `contrast_reversal_per_10k` | Regex for setup-and-reversal constructions: "it's not X, it's Y", "not just X, but Y", "X isn't Y, it's Z", "the question isn't..." | A construction AI drafting overuses. Some writers genuinely use it; compare to baseline |
| `watchlist_per_10k` and `watchlist_hits` | Count of about 35 generic phrases that rise with AI drafting ("in today's", "landscape", "leverage", "unlock", "seamless", "here's the thing", "in conclusion", and others). Extend with `--watch` | The generic register creeping in |
| `top_sentence_starters` | Most frequent first words | Habitual openings ("So", "Here", "And") and drift openings ("This", "By", "The") |

---

## 3. Features you code by hand

Some of the most important features cannot be counted reliably with word lists. Code them on a sample: 20 random paragraphs from the baseline and 20 from the drift set, plus every opening and closing.

| Feature | How to code | Rate to record |
|---|---|---|
| **Metaphor and analogy rate** | Mark every comparison that maps one domain onto another, explicit ("it's like a...") or implicit ("your pipeline is a leaky bucket"). Record the source domain | Analogies per 1,000 words; distribution of source domains |
| **Analogy extension** | For each analogy: does the writer extend it a beat past the obvious, invert it, or bridge back to the topic? | Share extended; share with explicit bridge |
| **Evidence type** | For each claim: lived observation, named real example, mechanism, reader pattern-match, counterargument, external data | Order of appearance; ratio of story to data |
| **Real vs hypothetical examples** | Each example: did it happen (to the writer or a real party) or is it invented ("imagine...")? | Real share |
| **Stance strength** | Each claim: hedged, plain, or absolute | Distribution by register |
| **Reader handoffs** | Questions or instructions that turn the work over to the reader | Per section |
| **Self-disclosure** | Admissions of failure, struggle, uncertainty | Per piece |

**Two-coder check.** Have a second person code 10 of the same paragraphs. If you agree on less than about 8 in 10 labels, your definitions are too loose. Tighten them before coding the rest. Manual coding takes roughly 45 to 90 minutes for 40 paragraphs.

---

## 4. Choosing which features matter

You will have over 50 numbers. Most are noise for any one person. A feature earns a place in the spec when it passes three tests:

1. **Stable within the person.** Run `profile --per-doc`. If a feature swings wildly across the person's own pieces (coefficient of variation above about 0.5 as a rule of thumb), it is topic-driven, not voice-driven. Leave it out or make it register-specific.
2. **Distinct from generic.** Build a **generic reference set**: give an AI assistant 10 of the held-in topics with no voice instructions, save the drafts, profile them. Features where the person and the generic set sit close together will not help a reader tell them apart.
3. **Moved by drift** (if you have a drift set). Features that changed the most between baseline and drift are where the model will fail first. They go at the top of every target table.

The strongest signatures are stable, distinct, and drifted. In practice that is usually 8 to 15 features: some rhythm measures, the pronoun rates, question rate, one or two punctuation habits, the story-to-hypothetical ratio, and opener and closer distributions.

---

## 5. Setting targets

### 5.1 The three-column table

For every chosen feature, record baseline, drift (or generic), and target:

| Signal | Baseline (true voice) | Drift / generic | Target |
|---|---|---|---|
| First person per 1k | [baseline median] | [drift value] | at least [about 70% of baseline] |
| Second person per 1k | [ ] | [ ] | at least [ ] |
| Sentence length stdev | [ ] | [ ] | at least [ ] |
| Short sentences (5 words or fewer) % | [ ] | [ ] | at least [ ] |
| [Device the person never uses] per 1k | [near 0] | [high] | 0 (hard rule) |
| Exclamations per 1k | [ ] | [ ] | at most [ ] |

Rules of thumb for the target column:

- **Floors for things drift removes** (first person, second person, short sentences, questions, stories). Set the floor at roughly 70 to 80 percent of the baseline median, so drafts do not need to be perfect copies.
- **Ceilings for things the person uses sparingly** (exclamations, emoji, caps). Set at the baseline 75th percentile across documents. Exceeding the person's own ceiling is how caricature starts.
- **Hard zero only when the baseline is near zero and the drift set is high.** That is the evidence that a device belongs to the machine, not the person. Do not import someone else's banned list; ban what your own data says.
- **Bands for rhythm** (sentence mean, paragraph length): baseline median plus or minus about 20 percent.

### 5.2 Converting rates into section counts

Writers and models cannot count rates while drafting. Convert to counts for a fixed window:

```
expected count = rate per 1k x (window words / 1,000)
```

If the baseline second-person rate is 20 per 1,000, the first 150 words should contain about 3 uses. Set the opening floor at that count. Openings and closings usually run hotter than the body for pronouns and questions, so compute the section-level rates separately (pull every opening into its own folder and profile it) when you have 15 or more pieces.

### 5.3 Phrase lists

Run `phrases` with two corpora at n = 2 and n = 3. Then read every candidate in context and sort it into one of four bins:

| Bin | Example (fictional) | Goes to |
|---|---|---|
| **Signature to restore** | A sign-off or a recurring instruction the person used often and stopped using | Section signature, with a frequency cap |
| **Topic word** | "pipeline review" appears because the person wrote about pipelines that year | Ignore |
| **Drift tic to ban** | "here's the thing", "in today's", "imagine a" appearing only after the cutoff | Banned list in every file |
| **Neutral** | "the next", "a day" | Ignore |

A phrase counts as a signature only if it appears in at least three separate pieces. One memorable line in one piece is an anchor for the library, not a pattern.

---

## 6. Using the score command

`score` compares a draft to the spread of the baseline's individual documents. For each core feature it reports the draft value, the baseline mean and standard deviation, and a z-score (with a minimum spread so near-zero features do not explode). It then reports the mean absolute z (each capped at 6) and the count of features outside 2 standard deviations.

Rules of thumb:

- Mean |z| under about 1.0 with 0 to 2 features out of range: inside the person's normal range.
- Mean |z| over about 1.5 or 5 or more features out: a reader is likely to notice something is off. Read the out-of-range features first; they name the fix.
- Drafts under 300 words swing hard. Score a full piece, or score several short pieces as a folder.

On the bundled sample, the in-voice draft scores about 1.1 with 4 features out (a 100-word draft, so noisy), and the drifted post-AI set scores about 1.9 with 10 out. The score is a smoke alarm. It does not replace blind human judgment ([testing.md](testing.md)), because a draft can match every number and still argue like someone else.

---

## 7. Known limits

- English-centric word lists. For other languages, rewrite the lists at the top of the script.
- Sentence splitting is heuristic. Abbreviations, decimals, and ellipses are handled; unusual punctuation styles may not be.
- The imperative detector only knows the verbs in its list. Add your domain's verbs.
- The caps-emphasis heuristic misclassifies an acronym that also appears as a lowercase word.
- Opener and closer labels are first-pass. Hand-classify for section signatures.
- Rates from fewer than about 2,000 words are noise; the script warns you.
