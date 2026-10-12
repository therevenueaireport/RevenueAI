# Example BEFORE — Org-Chart Folder

A representative example of a GTM operator's skill folder before migration (the shape most real folders take). Notice how skills are arranged by role, content is duplicated, and there's no clear trigger for any of them.

```
agent/
  INSTRUCTIONS.md                      ← 800 lines: identity + operating rules
                                         + ICP + voice + project context all
                                         crammed in
  skills/
    marketing-skills.md                ← "all marketing stuff" — covers SEO,
                                         email, content, social
    sales-skills.md                    ← "all sales stuff" — covers SDR,
                                         AE, demo prep, follow-up
    content-marketing/
      write-blog-post.md               ← contains the ICP description again
      write-linkedin-post.md           ← contains the voice rules again
      write-newsletter.md              ← contains the voice rules AGAIN
      seo-research.md                  ← mostly web-search instructions
    sales-enablement/
      build-sequence.md                ← duplicates the ICP. Has its own
                                         voice rules that contradict
                                         content-marketing's voice rules.
      write-cold-email.md              ← duplicates the voice rules
      qualify-lead.md                  ← duplicates the ICP, with slight
                                         drift from the version in
                                         build-sequence.md
    customer-success/
      onboarding-runbook.md            ← project-specific runbook from a
                                         client engagement from 8 months ago
                                         that's still being loaded every
                                         session
      qbr-prep.md                      ← also project-specific
    misc/
      check-grammar.md
      summarize-meeting.md
      old-experiment-do-not-use.md     ← still in the folder. Still loaded.
      copy-of-write-blog-post.md       ← duplicate from when the original
                                         was being edited
```

## Problems in this structure

1. **INSTRUCTIONS.md is 800 lines.** Half is identity, half is domain knowledge that should live in `domains/`.
2. **ICP appears in at least 4 different files** — with subtle drift between versions.
3. **Voice rules appear in at least 3 different files** — and `build-sequence.md`'s version actually contradicts `write-blog-post.md`'s version.
4. **Project-specific files** (`onboarding-runbook.md`, `qbr-prep.md`) are still loaded for every task, even when that client isn't being worked on.
5. **A `misc/` folder exists.** That's a sign the architecture has no opinion.
6. **A `copy-of-` file exists.** No agent should ever see this.
7. **Files are named by who would do them** (marketing, sales, CS), not by what they do.

## What the agent does in this folder

- Loads ~600 KB of skill content at session start.
- Picks the wrong voice rules half the time because two contradicting versions exist.
- Never references `seo-research.md` because nothing tells it when to.
- Drifts in ICP definition over time because it's averaging across the inconsistent copies.

## Why the user blames the model

The user thinks the agent is "getting worse." It isn't. The folder is poisoning every response with conflicting context. Same model, worse outcomes — because the architecture got heavier.
