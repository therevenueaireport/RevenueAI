#!/usr/bin/env python3
"""
voice_features.py - quantitative style features for building a voice skill.

Standard library only. Reads every .txt and .md file under a folder (recursive).

Subcommands
  profile  DIR                  Feature profile of one corpus.
  compare  BASELINE_DIR OTHER   Side-by-side profile, flags features that moved.
                                Use it for pre-AI vs post-AI drift, or raw vs edited.
  phrases  DIR [OTHER]          Recurring n-grams. With OTHER: phrases lost and
                                phrases introduced between the two corpora.
  score    BASELINE_DIR DRAFT   Z-scores of a draft (file or folder) against the
                                per-document spread of the baseline.

Common options
  --json PATH     also write machine-readable results
  --per-doc       (profile) print a short per-document table
  --watch PATH    extra watchlist phrases, one per line (case-insensitive)

Examples
  python3 voice_features.py profile corpus/pre-ai
  python3 voice_features.py compare corpus/pre-ai corpus/post-ai
  python3 voice_features.py phrases corpus/pre-ai corpus/post-ai --n 3
  python3 voice_features.py score corpus/pre-ai drafts/new-post.md

All rates are heuristics. They describe surface style, not quality. Read
references/feature-extraction.md for what each number means and where it lies.
"""

import argparse
import json
import math
import os
import re
import statistics
import sys
from collections import Counter

# ---------------------------------------------------------------------------
# Word lists (edit freely; they are English-centric heuristics)
# ---------------------------------------------------------------------------

FIRST_SINGULAR = {"i", "me", "my", "mine", "myself", "i'm", "i've", "i'd", "i'll"}
FIRST_PLURAL = {"we", "us", "our", "ours", "ourselves", "we're", "we've", "we'd",
                "we'll", "let's"}
SECOND = {"you", "your", "yours", "yourself", "yourselves", "you're", "you've",
          "you'd", "you'll", "y'all"}

CONTRACTION_SUFFIX = re.compile(r"(n't|'re|'ve|'ll|'d|'m)$")
S_CONTRACTION_HEADS = {"it's", "that's", "there's", "here's", "what's", "who's",
                       "where's", "how's", "let's", "he's", "she's", "when's",
                       "why's", "everyone's", "nobody's", "something's"}
FULL_FORMS = [
    "do not", "does not", "did not", "is not", "are not", "was not", "were not",
    "cannot", "will not", "would not", "should not", "could not", "have not",
    "has not", "had not", "i am", "i have", "i will", "i would", "you are",
    "you have", "you will", "we are", "we have", "we will", "they are",
    "they have", "it is", "that is", "there is", "here is", "what is", "let us",
]

HEDGES = ["i think", "i guess", "i feel like", "i suspect", "maybe", "perhaps",
          "probably", "possibly", "might", "kind of", "sort of", "somewhat",
          "arguably", "seems", "it seems", "in my opinion", "i believe"]
INTENSIFIERS = ["very", "really", "totally", "absolutely", "incredibly", "super",
                "extremely", "literally", "completely", "insanely", "massively",
                "hugely", "seriously"]
SIMILE_MARKERS = ["like a", "like an", "like the", "as if", "as though",
                  "think of it as", "it's like", "is like", "the same way",
                  "similar to", "kind of like", "reminds me of"]
HYPOTHETICAL_MARKERS = ["imagine", "picture this", "let's say", "suppose",
                        "what if", "envision"]
STORY_MARKERS = ["i remember", "when i was", "years ago", "last week",
                 "yesterday", "one time", "i once", "the first time i",
                 "a few years back", "early in my career", "last year",
                 "this morning", "last month"]
IMPERATIVE_VERBS = {"try", "take", "ask", "stop", "start", "pick", "write", "look",
                    "go", "do", "don't", "make", "read", "think", "use", "build",
                    "give", "let", "get", "find", "run", "check", "keep",
                    "remember", "consider", "notice", "choose", "focus", "map",
                    "list", "open", "call", "send", "block", "cut", "skip",
                    "spend", "test", "track", "measure", "audit", "drop", "add",
                    "book", "reply", "share", "tell", "show", "set", "watch",
                    "count", "shadow", "pull", "publish", "sort", "name", "pick",
                    "delete", "schedule", "draft", "record", "compare", "label"}
CONJ_STARTERS = {"and", "but", "so", "because", "or", "yet"}

TIME_ANCHORS = re.compile(
    r"^(today|yesterday|tonight|this (morning|week|month|year|quarter)|"
    r"(last|this|on|one|that) (night|week|month|year|quarter|monday|tuesday|"
    r"wednesday|thursday|friday|saturday|sunday|morning|spring|summer|fall|"
    r"autumn|winter)|years ago|a (few|couple of) "
    r"(days|weeks|months|years) ago|when i|for (over |more than )?(years|"
    r"decades|\d+)|in (19|20)\d\d|back in|early in|on (monday|tuesday|"
    r"wednesday|thursday|friday|saturday|sunday))", re.I)
FORWARD_MARKERS = ["next week", "next time", "more to come", "stay tuned",
                   "coming soon", "next issue", "part two", "part 2",
                   "until next", "more soon", "next month"]
SUMMARY_MARKERS = ["in conclusion", "bottom line", "in short", "to sum up",
                   "ultimately", "in summary", "the takeaway", "at the end of the day"]
WISH_MARKERS = ["i hope", "i'd love", "let me know", "i want you to", "i wish",
                "reply and", "hit reply", "tell me"]

# Generic AI-drift watchlist. Not anyone's personal list: phrases that rise
# when drafts are produced or heavily edited by an AI assistant. Extend with --watch.
DEFAULT_WATCHLIST = [
    "in today's", "delve", "tapestry", "landscape", "game-changer", "game changer",
    "unlock", "leverage", "seamless", "robust", "navigate the", "in conclusion",
    "the bottom line", "at the end of the day", "it's worth noting", "crucial",
    "pivotal", "transformative", "here's the thing", "here's the kicker",
    "here's the truth", "let's dive", "dive in", "dig deeper", "let's break it down",
    "fast-paced", "ever-evolving", "rapidly evolving", "paradigm", "synergy",
    "empower", "elevate", "harness", "realm", "embark", "testament to",
]
CONTRAST_REVERSAL = [
    re.compile(r"\b(it's|it is|this is|that's|that is|this isn't|it isn't|that isn't)"
               r"\s+not\s+(just\s+|only\s+|about\s+)?[^.?!\n]{1,60}?[,;:]\s*"
               r"(it's|it is|but|this is|that's|they're)\b", re.I),
    re.compile(r"\b(isn't|is not|aren't|are not)\s+[^.?!\n]{1,40}?[,;]\s*"
               r"(it's|they're|it is|they are)\b", re.I),
    re.compile(r"\bnot\s+(just|only|merely)\s+[^.?!\n]{1,60}?,\s*but\b", re.I),
    re.compile(r"\bthe question isn't\b", re.I),
]

ABBREVIATIONS = ["e.g.", "i.e.", "etc.", "vs.", "mr.", "mrs.", "ms.", "dr.",
                 "prof.", "inc.", "ltd.", "co.", "jr.", "sr.", "st.", "u.s.",
                 "u.k.", "a.m.", "p.m.", "approx.", "no.", "fig.", "cf."]

EMDASH = "\u2014"
ENDASH = "\u2013"
ELLIPSIS_CHAR = "\u2026"
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF]")
EMOTICON_RE = re.compile(r"(?<!\w)[:;]-?[)(DPp](?!\w)")
TOKEN_RE = re.compile(r"\$?\d[\d,]*(?:\.\d+)?%?|[A-Za-z]+(?:'[A-Za-z]+)*")
NUM_RE = re.compile(r"^\$?\d[\d,]*(?:\.\d+)?%?$")
STOPWORDS = set("""a an the and or but so to of in on at for with by from as is are
was were be been being it this that these those i you we they he she me my your
our their his her them us not no do does did have has had will would can could
should just than then there here what which who when where how if about into
out up down over very really also its it's i'm you're we're don't""".split())

# ---------------------------------------------------------------------------
# Reading and cleaning
# ---------------------------------------------------------------------------


def read_corpus(path):
    """Return list of (relative_name, raw_text). Accepts a folder or one file."""
    docs = []
    if os.path.isfile(path):
        with open(path, encoding="utf-8", errors="replace") as f:
            return [(os.path.basename(path), f.read())]
    for root, _dirs, files in os.walk(path):
        for name in sorted(files):
            if name.lower().endswith((".txt", ".md", ".markdown")):
                full = os.path.join(root, name)
                with open(full, encoding="utf-8", errors="replace") as f:
                    docs.append((os.path.relpath(full, path), f.read()))
    return docs


LIST_PATTERNS = [
    ("bullet_dash", re.compile(r"^\s*-\s+\S")),
    ("bullet_star", re.compile(r"^\s*[*+]\s+\S")),
    ("bullet_other", re.compile(r"^\s*[\u2022\u25aa\u25cf\u2023]\s*\S")),
    ("num_dot", re.compile(r"^\s*#?\d{1,2}\.\s+\S")),
    ("num_paren", re.compile(r"^\s*\(?\d{1,2}\)\s+\S")),
    ("num_hyphen", re.compile(r"^\s*#?\d{1,2}\s?-\s?[A-Za-z]")),
]
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+\S")


def clean_and_structure(raw):
    """Strip markup, return (blocks, structure_counts).

    blocks: list of dicts {kind: 'prose'|'list'|'heading', text}
    """
    text = raw.replace("\r\n", "\n").replace("\u2019", "'").replace("\u2018", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)          # front matter
    text = re.sub(r"```.*?```", "", text, flags=re.S)                   # code fences
    text = re.sub(r"<[^>\n]+>", "", text)                               # html tags
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)                    # images
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)                # links
    text = re.sub(r"https?://\S+", "", text)                            # bare urls
    text = re.sub(r"`([^`]*)`", r"\1", text)                            # inline code

    structure = Counter()
    blocks = []
    for block in re.split(r"\n\s*\n", text):
        lines = [ln for ln in block.split("\n") if ln.strip()]
        if not lines:
            continue
        prose_lines = []
        for ln in lines:
            if re.match(r"^\s*>", ln):
                # block quotes are usually someone else's words: count, then drop
                structure["blockquote_lines"] += 1
                continue
            if HEADING_RE.match(ln):
                structure["headings"] += 1
                blocks.append({"kind": "heading", "text": ln.lstrip("# ").strip()})
                continue
            style = next((name for name, rx in LIST_PATTERNS if rx.match(ln)), None)
            if style:
                structure["list_items"] += 1
                structure["list_" + style] += 1
                item = re.sub(r"^\s*(#?\d{1,2}\s?[.)-]\s?|\(?\d{1,2}\)\s|[-*+\u2022\u25aa\u25cf\u2023]\s*)", "", ln)
                blocks.append({"kind": "list", "text": strip_emphasis(item)})
                continue
            prose_lines.append(ln)
        if prose_lines:
            blocks.append({"kind": "prose", "lines": [strip_emphasis(x) for x in prose_lines]})
    structure["nonblank_lines"] = sum(1 for ln in text.split("\n") if ln.strip())
    return blocks, structure


def strip_emphasis(s):
    s = re.sub(r"(\*\*|__)(.+?)\1", r"\2", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"\1", s)
    s = re.sub(r"(?<![\w_])_(?!\s)(.+?)(?<!\s)_(?!\w)", r"\1", s)
    return s.strip()


def join_lines(lines):
    """Hard-wrapped text gets joined; one-sentence-per-line text keeps breaks."""
    if len(lines) == 1:
        return lines
    avg = sum(len(x) for x in lines) / len(lines)
    unterminated = sum(1 for x in lines[:-1] if not re.search(r"[.!?:\"')]\s*$", x))
    if avg > 60 and unterminated >= (len(lines) - 1) / 2:
        return [" ".join(x.strip() for x in lines)]
    return lines


def split_sentences(line):
    s = line.strip()
    if not s:
        return []
    protected = s
    for ab in ABBREVIATIONS:
        protected = re.sub(re.escape(ab), ab.replace(".", "\u0000"), protected, flags=re.I)
    protected = re.sub(r"(\d)\.(\d)", "\\1\u0000\\2", protected)
    protected = re.sub(r"\.{2,}", ELLIPSIS_CHAR, protected)
    parts = re.split(r"(?<=[.!?" + ELLIPSIS_CHAR + r"])[\"')\]]*\s+(?=[\"'(\[]?[A-Z0-9])", protected)
    return [p.replace("\u0000", ".").strip() for p in parts if p.strip()]


def tokens(s):
    return [t.lower() for t in TOKEN_RE.findall(s)]


def count_phrases(text_lower, phrases):
    total = 0
    for p in phrases:
        total += len(re.findall(r"(?<![a-z'])" + re.escape(p) + r"(?![a-z'])", text_lower))
    return total


def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    return max(1, len(re.findall(r"[aeiouy]{1,2}", w)))


def mattr(words, window=200):
    if len(words) < window:
        return len(set(words)) / len(words) if words else 0.0
    counts = Counter(words[:window])
    total = len(counts) / window
    n = 1
    for i in range(window, len(words)):
        out = words[i - window]
        counts[out] -= 1
        if counts[out] == 0:
            del counts[out]
        counts[words[i]] += 1
        total += len(counts) / window
        n += 1
    return total / n


# ---------------------------------------------------------------------------
# Opener and closer classification
# ---------------------------------------------------------------------------


def classify_opener(sentence):
    s = sentence.strip()
    low = s.lower()
    first = (tokens(s) or [""])[0]
    if s.endswith("?"):
        return "question"
    if s.startswith('"'):
        return "quote"
    if TIME_ANCHORS.match(low) or re.search(r"\bago\b", " ".join(low.split()[:6])):
        return "time_or_memory_anchor"
    if re.match(r"^\$?\d", s) or re.search(r"\d+%|\$\d", s):
        return "number_or_stat"
    if re.match(r"^(if you|you|your|have you|do you|ever)\b", low):
        return "direct_address"
    if first in IMPERATIVE_VERBS:
        return "imperative"
    if first in FIRST_SINGULAR or first in FIRST_PLURAL:
        return "first_person"
    if len(tokens(s)) <= 6:
        return "short_declarative"
    return "declarative"


def classify_closer(sentence, last_para):
    s = sentence.strip()
    low = last_para.lower()
    first = (tokens(s) or [""])[0]
    if any(m in low for m in SUMMARY_MARKERS):
        return "summary_marker"
    if any(m in low for m in FORWARD_MARKERS):
        return "forward_tease"
    if s.endswith("?"):
        return "question"
    if any(m in low for m in WISH_MARKERS):
        return "warm_wish_or_invite"
    para_starts = [(tokens(x) or [""])[0] for x in split_sentences(last_para)]
    if any(w in IMPERATIVE_VERBS for w in para_starts):
        return "imperative_action"
    if len(tokens(s)) <= 6:
        return "short_punch"
    return "declarative"


# ---------------------------------------------------------------------------
# Feature extraction
# ---------------------------------------------------------------------------


def analyze_docs(docs, watch_extra=None):
    """Aggregate features over a list of (name, raw). Returns dict."""
    watch = DEFAULT_WATCHLIST + (watch_extra or [])
    sent_lens, para_words, para_sents = [], [], []
    para_open_q = para_end_q = paras = one_sent_paras = 0
    swing = []
    all_words, all_text_parts = [], []
    structure = Counter()
    starters = Counter()
    openers, closers = Counter(), Counter()
    sentences_total = q_sents = imp_sents = conj_sents = num_sents = 0
    caps_tokens = []
    doc_count = 0
    for _name, raw in docs:
        blocks, struct = clean_and_structure(raw)
        structure.update(struct)
        doc_sents = []
        last_prose = ""
        for b in blocks:
            if b["kind"] == "heading":
                continue
            if b["kind"] == "list":
                sents = split_sentences(b["text"])
                doc_sents.extend(sents)
                all_text_parts.append(b["text"])
                continue
            lines = join_lines(b["lines"])
            para_sentences = []
            for ln in lines:
                para_sentences.extend(split_sentences(ln))
            if not para_sentences:
                continue
            ptext = " ".join(para_sentences)
            all_text_parts.append(ptext)
            last_prose = ptext
            paras += 1
            pw = len(tokens(ptext))
            para_words.append(pw)
            para_sents.append(len(para_sentences))
            if len(para_sentences) == 1:
                one_sent_paras += 1
            if para_sentences[0].rstrip("\"')").endswith("?"):
                para_open_q += 1
            if para_sentences[-1].rstrip("\"')").endswith("?"):
                para_end_q += 1
            doc_sents.extend(para_sentences)
        if not doc_sents:
            continue
        doc_count += 1
        openers[classify_opener(doc_sents[0])] += 1
        closers[classify_closer(doc_sents[-1], last_prose or doc_sents[-1])] += 1
        prev = None
        for s in doc_sents:
            toks = tokens(s)
            if not toks:
                continue
            n = len(toks)
            sent_lens.append(n)
            if prev is not None:
                swing.append(abs(n - prev))
            prev = n
            sentences_total += 1
            if s.rstrip("\"')").endswith("?"):
                q_sents += 1
            if toks[0] in IMPERATIVE_VERBS and not s.rstrip().endswith("?"):
                imp_sents += 1
            if toks[0] in CONJ_STARTERS:
                conj_sents += 1
            if any(NUM_RE.match(t) for t in toks):
                num_sents += 1
            starters[toks[0]] += 1
            all_words.extend(toks)
            caps_tokens.extend(t for t in re.findall(r"(?<![\w'])[A-Z]{2,}(?![\w'])", s))

    text = "\n".join(all_text_parts)
    low = text.lower()
    W = len(all_words) or 1
    per1k = lambda c: round(1000.0 * c / W, 2)
    per10k = lambda c: round(10000.0 * c / W, 2)

    word_set_lower = Counter(all_words)
    lower_seen = set(re.findall(r"\b[a-z][a-z']+\b", text))
    caps_emph = [t for t in caps_tokens if t.lower() in lower_seen and t not in ("I", "A", "OK")]
    acronyms = Counter(t for t in caps_tokens if t.lower() not in lower_seen)

    contractions = sum(1 for t in all_words
                       if CONTRACTION_SUFFIX.search(t) or t in S_CONTRACTION_HEADS)
    full_forms = count_phrases(low, FULL_FORMS)
    numbers = sum(1 for t in all_words if NUM_RE.match(t))
    syl = sum(syllables(w) for w in all_words if w.isalpha())
    alpha_words = sum(1 for w in all_words if w.isalpha()) or 1
    S = sentences_total or 1

    def pct(c, d):
        return round(100.0 * c / d, 1) if d else 0.0

    def sd(xs):
        return round(statistics.pstdev(xs), 2) if len(xs) > 1 else 0.0

    def quant(xs, q):
        if not xs:
            return 0
        xs = sorted(xs)
        return xs[min(len(xs) - 1, int(q * (len(xs) - 1) + 0.5))]

    buckets = Counter()
    for n in sent_lens:
        key = ("01-05" if n <= 5 else "06-10" if n <= 10 else "11-15" if n <= 15
               else "16-20" if n <= 20 else "21-30" if n <= 30 else "31+")
        buckets[key] += 1

    contrast_hits = sum(len(rx.findall(text)) for rx in CONTRAST_REVERSAL)
    watch_hits = Counter()
    for p in watch:
        c = count_phrases(low, [p.lower()])
        if c:
            watch_hits[p] = c

    lists = structure.get("list_items", 0)
    f = {
        "documents": doc_count,
        "words": len(all_words),
        "sentences": sentences_total,
        "paragraphs": paras,
        # rhythm
        "sent_len_mean": round(statistics.mean(sent_lens), 2) if sent_lens else 0,
        "sent_len_median": statistics.median(sent_lens) if sent_lens else 0,
        "sent_len_stdev": sd(sent_lens),
        "sent_len_p10": quant(sent_lens, 0.10),
        "sent_len_p90": quant(sent_lens, 0.90),
        "pct_sent_short_le5": pct(sum(1 for n in sent_lens if n <= 5), S),
        "pct_sent_long_ge25": pct(sum(1 for n in sent_lens if n >= 25), S),
        "rhythm_swing_mean": round(statistics.mean(swing), 2) if swing else 0,
        "para_len_words_mean": round(statistics.mean(para_words), 1) if para_words else 0,
        "para_len_words_median": statistics.median(para_words) if para_words else 0,
        "para_len_sents_mean": round(statistics.mean(para_sents), 2) if para_sents else 0,
        "pct_one_sentence_paras": pct(one_sent_paras, paras),
        # address
        "first_singular_per_1k": per1k(sum(word_set_lower[w] for w in FIRST_SINGULAR)),
        "first_plural_per_1k": per1k(sum(word_set_lower[w] for w in FIRST_PLURAL)),
        "second_person_per_1k": per1k(sum(word_set_lower[w] for w in SECOND)),
        # questions and exclamation
        "question_marks_per_1k": per1k(text.count("?")),
        "pct_sent_questions": pct(q_sents, S),
        "pct_paras_open_question": pct(para_open_q, paras),
        "pct_paras_end_question": pct(para_end_q, paras),
        "exclamations_per_1k": per1k(text.count("!")),
        # register
        "contractions_per_1k": per1k(contractions),
        "contraction_ratio": round(contractions / (contractions + full_forms), 2)
        if (contractions + full_forms) else 0,
        "hedges_per_1k": per1k(count_phrases(low, HEDGES)),
        "intensifiers_per_1k": per1k(count_phrases(low, INTENSIFIERS)),
        "pct_sent_imperative": pct(imp_sents, S),
        "pct_sent_conj_start": pct(conj_sents, S),
        # evidence and specificity
        "numbers_per_1k": per1k(numbers),
        "pct_sent_with_number": pct(num_sents, S),
        "percent_signs_per_1k": per1k(text.count("%")),
        "story_markers_per_10k": per10k(count_phrases(low, STORY_MARKERS)),
        "hypothetical_markers_per_10k": per10k(count_phrases(low, HYPOTHETICAL_MARKERS)),
        "simile_markers_per_1k": per1k(count_phrases(low, SIMILE_MARKERS)),
        # structure
        "list_items_per_1k": per1k(lists),
        "pct_lines_list": pct(lists, structure.get("nonblank_lines", 0)),
        "headings_per_1k": per1k(structure.get("headings", 0)),
        "list_styles": {k[5:]: v for k, v in structure.items()
                        if k.startswith("list_") and k != "list_items"},
        # punctuation
        "em_dash_per_1k": per1k(text.count(EMDASH) + len(re.findall(r"\s--\s", text))),
        "en_dash_or_spaced_hyphen_per_1k": per1k(text.count(ENDASH) + len(re.findall(r"\s-\s", text))),
        "ellipses_per_1k": per1k(text.count(ELLIPSIS_CHAR) + len(re.findall(r"\.{2,}", text))),
        "semicolons_per_1k": per1k(text.count(";")),
        "colons_per_1k": per1k(len(re.findall(r":(?![)(DPp/])", text))),
        "parentheses_per_1k": per1k(text.count("(")),
        "caps_emphasis_per_1k": per1k(len(caps_emph)),
        "emoji_emoticons_per_1k": per1k(len(EMOJI_RE.findall(text)) + len(EMOTICON_RE.findall(text))),
        # lexical
        "avg_word_len": round(sum(len(w) for w in all_words if w.isalpha()) / alpha_words, 2),
        "mattr_200": round(mattr(all_words), 3),
        "flesch_reading_ease": round(206.835 - 1.015 * (W / S) - 84.6 * (syl / alpha_words), 1),
        "fk_grade": round(0.39 * (W / S) + 11.8 * (syl / alpha_words) - 15.59, 1),
        # drift tells
        "contrast_reversal_per_10k": per10k(contrast_hits),
        "watchlist_per_10k": per10k(sum(watch_hits.values())),
        # distributions
        "sent_len_buckets_pct": {k: pct(v, S) for k, v in sorted(buckets.items())},
        "opener_types": dict(openers.most_common()),
        "closer_types": dict(closers.most_common()),
        "top_sentence_starters": dict(starters.most_common(12)),
        "top_caps_emphasis": dict(Counter(caps_emph).most_common(8)),
        "top_acronyms": dict(acronyms.most_common(8)),
        "watchlist_hits": dict(watch_hits.most_common(15)),
    }
    return f


SCALAR_ORDER = [
    ("Rhythm", ["sent_len_mean", "sent_len_median", "sent_len_stdev", "sent_len_p10",
                "sent_len_p90", "pct_sent_short_le5", "pct_sent_long_ge25",
                "rhythm_swing_mean", "para_len_words_mean", "para_len_words_median",
                "para_len_sents_mean", "pct_one_sentence_paras"]),
    ("Address", ["first_singular_per_1k", "first_plural_per_1k", "second_person_per_1k"]),
    ("Questions", ["question_marks_per_1k", "pct_sent_questions", "pct_paras_open_question",
                   "pct_paras_end_question", "exclamations_per_1k"]),
    ("Register", ["contractions_per_1k", "contraction_ratio", "hedges_per_1k",
                  "intensifiers_per_1k", "pct_sent_imperative", "pct_sent_conj_start"]),
    ("Evidence", ["numbers_per_1k", "pct_sent_with_number", "percent_signs_per_1k",
                  "story_markers_per_10k", "hypothetical_markers_per_10k",
                  "simile_markers_per_1k"]),
    ("Structure", ["list_items_per_1k", "pct_lines_list", "headings_per_1k"]),
    ("Punctuation", ["em_dash_per_1k", "en_dash_or_spaced_hyphen_per_1k", "ellipses_per_1k",
                     "semicolons_per_1k", "colons_per_1k", "parentheses_per_1k",
                     "caps_emphasis_per_1k", "emoji_emoticons_per_1k"]),
    ("Lexical", ["avg_word_len", "mattr_200", "flesch_reading_ease", "fk_grade"]),
    ("Drift tells", ["contrast_reversal_per_10k", "watchlist_per_10k"]),
]
DIST_KEYS = ["sent_len_buckets_pct", "opener_types", "closer_types", "list_styles",
             "top_sentence_starters", "top_caps_emphasis", "top_acronyms", "watchlist_hits"]
SCORE_KEYS = ["sent_len_mean", "sent_len_stdev", "pct_sent_short_le5", "pct_sent_long_ge25",
              "rhythm_swing_mean", "para_len_words_mean", "first_singular_per_1k",
              "first_plural_per_1k", "second_person_per_1k", "question_marks_per_1k",
              "exclamations_per_1k", "contractions_per_1k", "hedges_per_1k",
              "pct_sent_imperative", "numbers_per_1k", "em_dash_per_1k", "ellipses_per_1k",
              "semicolons_per_1k", "parentheses_per_1k", "caps_emphasis_per_1k",
              "avg_word_len", "contrast_reversal_per_10k", "watchlist_per_10k"]


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------


def warn_size(label, f):
    w = f["words"]
    if w < 2000:
        print(f"  WARNING: {label} has {w} words. Rates below ~2,000 words are noisy.")
    elif w < 10000:
        print(f"  NOTE: {label} has {w} words. Treat per-10k rates as directional.")


def print_profile(f, label="corpus"):
    print(f"\n=== {label}: {f['documents']} docs, {f['words']} words, "
          f"{f['sentences']} sentences, {f['paragraphs']} paragraphs")
    warn_size(label, f)
    for group, keys in SCALAR_ORDER:
        print(f"\n[{group}]")
        for k in keys:
            print(f"  {k:<34} {f[k]}")
    for k in DIST_KEYS:
        print(f"\n[{k}]")
        if not f[k]:
            print("  (none)")
        for kk, vv in f[k].items():
            print(f"  {kk:<34} {vv}")


def print_compare(a, b, la, lb):
    print(f"\n=== compare: A={la} ({a['words']} words, {a['documents']} docs)  "
          f"B={lb} ({b['words']} words, {b['documents']} docs)")
    warn_size("A", a)
    warn_size("B", b)
    print("  Flag: '<<' or '>>' means B moved by 1.5x or more in that direction "
          "(and by a non-trivial amount).")
    for group, keys in SCALAR_ORDER:
        print(f"\n[{group}]")
        print(f"  {'feature':<34} {'A':>9} {'B':>9} {'B/A':>7}")
        for k in keys:
            va, vb = a[k], b[k]
            ratio = (vb / va) if va else (float("inf") if vb else 1.0)
            flag = ""
            if abs(vb - va) >= max(0.5, 0.1 * abs(va)):
                if ratio >= 1.5:
                    flag = ">>"
                elif ratio <= 0.67:
                    flag = "<<"
            rs = "inf" if ratio == float("inf") else f"{ratio:.2f}"
            print(f"  {k:<34} {va:>9} {vb:>9} {rs:>7} {flag}")
    for k in ("opener_types", "closer_types", "watchlist_hits"):
        print(f"\n[{k}]  A | B")
        keys = sorted(set(a[k]) | set(b[k]))
        for kk in keys:
            print(f"  {kk:<34} {a[k].get(kk, 0):>5} | {b[k].get(kk, 0):<5}")


# ---------------------------------------------------------------------------
# Phrases
# ---------------------------------------------------------------------------


def ngram_counts(docs, n):
    counts, doc_freq = Counter(), Counter()
    total = 0
    for _name, raw in docs:
        blocks, _ = clean_and_structure(raw)
        seen = set()
        for b in blocks:
            if b["kind"] == "heading":
                continue
            lines = [b["text"]] if b["kind"] == "list" else join_lines(b["lines"])
            for ln in lines:
                for s in split_sentences(ln):
                    toks = [t for t in tokens(s) if not NUM_RE.match(t)]
                    total += len(toks)
                    for i in range(len(toks) - n + 1):
                        g = tuple(toks[i:i + n])
                        if all(t in STOPWORDS for t in g):
                            continue
                        counts[g] += 1
                        seen.add(g)
        doc_freq.update(seen)
    return counts, doc_freq, max(total, 1)


def cmd_phrases(args):
    a_docs = read_corpus(args.dir)
    ca, dfa, ta = ngram_counts(a_docs, args.n)
    if not args.other:
        print(f"\n=== recurring {args.n}-grams in {args.dir} (in >= {args.min_docs} docs), per 10k words")
        rows = [(g, c) for g, c in ca.items() if dfa[g] >= args.min_docs]
        rows.sort(key=lambda r: (-dfa[r[0]], -r[1]))
        for g, c in rows[:args.top]:
            print(f"  {' '.join(g):<40} count={c:<4} docs={dfa[g]:<3} per10k={10000*c/ta:.1f}")
        return
    b_docs = read_corpus(args.other)
    cb, dfb, tb = ngram_counts(b_docs, args.n)
    lost, introduced = [], []
    for g, c in ca.items():
        if dfa[g] >= args.min_docs:
            ra, rb = 10000 * c / ta, 10000 * cb.get(g, 0) / tb
            if rb <= 0.25 * ra:
                lost.append((ra - rb, g, ra, rb))
    for g, c in cb.items():
        if dfb[g] >= args.min_docs:
            ra, rb = 10000 * ca.get(g, 0) / ta, 10000 * c / tb
            if ra <= 0.25 * rb:
                introduced.append((rb - ra, g, ra, rb))
    print(f"\n=== {args.n}-grams LOST (common in A={args.dir}, rare or absent in B={args.other})")
    print("    Candidates for signatures to restore. Verify each by reading it in context.")
    for _d, g, ra, rb in sorted(lost, reverse=True)[:args.top]:
        print(f"  {' '.join(g):<40} A={ra:6.1f}/10k  B={rb:6.1f}/10k")
    print(f"\n=== {args.n}-grams INTRODUCED (common in B, rare or absent in A)")
    print("    Candidates for drift tics to ban. Verify each by reading it in context.")
    for _d, g, ra, rb in sorted(introduced, reverse=True)[:args.top]:
        print(f"  {' '.join(g):<40} A={ra:6.1f}/10k  B={rb:6.1f}/10k")


# ---------------------------------------------------------------------------
# Score
# ---------------------------------------------------------------------------


def cmd_score(args, watch):
    base = [d for d in read_corpus(args.baseline)]
    per_doc = []
    for d in base:
        f = analyze_docs([d], watch)
        if f["words"] >= args.min_words:
            per_doc.append(f)
    if len(per_doc) < 5:
        print(f"Need at least 5 baseline docs with >= {args.min_words} words; have {len(per_doc)}.")
        print("Lower --min-words or add documents.")
        sys.exit(1)
    draft = analyze_docs(read_corpus(args.draft), watch)
    print(f"\n=== score: draft {args.draft} ({draft['words']} words) vs "
          f"{len(per_doc)} baseline docs")
    if draft["words"] < 300:
        print("  NOTE: drafts under ~300 words give unstable rates. Score sections together.")
    print(f"  {'feature':<32} {'draft':>8} {'base_mean':>10} {'base_sd':>8} {'z':>6}")
    zs, out = [], {}
    for k in SCORE_KEYS:
        vals = [p[k] for p in per_doc]
        m = statistics.mean(vals)
        s = statistics.pstdev(vals)
        floor = max(0.25 * abs(m), 0.5)
        s_eff = max(s, floor)
        z = (draft[k] - m) / s_eff
        zs.append(min(abs(z), 6.0))
        flag = "  OUT" if abs(z) > 2 else ("  edge" if abs(z) > 1.5 else "")
        out[k] = {"draft": draft[k], "base_mean": round(m, 2), "base_sd": round(s, 2),
                  "z": round(z, 2)}
        print(f"  {k:<32} {draft[k]:>8} {m:>10.2f} {s:>8.2f} {z:>6.2f}{flag}")
    dist = statistics.mean(zs)
    n_out = sum(1 for z in zs if z > 2)
    print(f"\n  mean |z| (each capped at 6) = {dist:.2f}; features OUT of range: {n_out}")
    print("  Rule of thumb: mean under 1.0 with 0-2 OUT sits inside your range; mean over 1.5")
    print("  or 5+ OUT reads as someone else. Short drafts swing; judge sections together.")
    print("  Opener:", draft["opener_types"], "  Closer:", draft["closer_types"])
    if draft["watchlist_hits"]:
        print("  Watchlist hits:", draft["watchlist_hits"])
    return {"draft": args.draft, "mean_abs_z": round(dist, 2), "out_count": n_out,
            "features": out}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def load_watch(path):
    if not path:
        return []
    with open(path, encoding="utf-8") as fh:
        return [ln.strip() for ln in fh if ln.strip() and not ln.startswith("#")]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("profile")
    p.add_argument("dir")
    p.add_argument("--per-doc", action="store_true")
    c = sub.add_parser("compare")
    c.add_argument("baseline")
    c.add_argument("other")
    ph = sub.add_parser("phrases")
    ph.add_argument("dir")
    ph.add_argument("other", nargs="?")
    ph.add_argument("--n", type=int, default=3)
    ph.add_argument("--min-docs", type=int, default=2)
    ph.add_argument("--top", type=int, default=30)
    s = sub.add_parser("score")
    s.add_argument("baseline")
    s.add_argument("draft")
    s.add_argument("--min-words", type=int, default=150)
    for sp in (p, c, ph, s):
        sp.add_argument("--json")
        sp.add_argument("--watch")
    args = ap.parse_args()
    watch = load_watch(args.watch)

    result = None
    if args.cmd == "profile":
        docs = read_corpus(args.dir)
        if not docs:
            sys.exit(f"No .txt or .md files found under {args.dir}")
        result = analyze_docs(docs, watch)
        print_profile(result, args.dir)
        if args.per_doc:
            print(f"\n[per document]\n  {'doc':<40} {'words':>6} {'sentM':>6} {'sentSD':>6} "
                  f"{'I/1k':>6} {'you/1k':>6} {'?/1k':>6} opener / closer")
            rows = []
            for d in docs:
                f = analyze_docs([d], watch)
                rows.append({"doc": d[0], **{k: f[k] for k in SCORE_KEYS}})
                print(f"  {d[0][:40]:<40} {f['words']:>6} {f['sent_len_mean']:>6} "
                      f"{f['sent_len_stdev']:>6} {f['first_singular_per_1k']:>6} "
                      f"{f['second_person_per_1k']:>6} {f['question_marks_per_1k']:>6} "
                      f"{list(f['opener_types'])} / {list(f['closer_types'])}")
            result = {"aggregate": result, "per_doc": rows}
    elif args.cmd == "compare":
        a = analyze_docs(read_corpus(args.baseline), watch)
        b = analyze_docs(read_corpus(args.other), watch)
        print_compare(a, b, args.baseline, args.other)
        result = {"A": a, "B": b}
    elif args.cmd == "phrases":
        cmd_phrases(args)
    elif args.cmd == "score":
        result = cmd_score(args, watch)

    if args.json and result is not None:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=2)
        print(f"\nWrote {args.json}")


if __name__ == "__main__":
    main()
