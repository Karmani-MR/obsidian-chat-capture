---
type: manual
summary: Operating manual for any AI agent working in this vault. Read first.
tags: [manual]
---
# AGENTS.md — vault operating manual

Any AI working in this vault (Claude Code, Perplexity, Cursor, Codex, ChatGPT with vault access) follows these rules. `CLAUDE.md` imports this file.

## Read order
1. This file.
2. `00 Home/AI Context.md` — who {{USER_NAME}} is and where everything lives.
3. `00 Home/Top of Mind.md` — this week's priorities and deadlines.
4. `00 Home/Agent/USER.md` and the newest entries in `00 Home/Agent/Agent Memory.md`.
5. The skill note in `00 Home/Agent/Skills/` that matches the task.

## Where you may write
- **Freely:** `01 Fleeting/AI Drafts/`, `11 AI Chats/`, today's daily note, `00 Home/Top of Mind.md`.
- **Everywhere else:** append only. Never overwrite a note, rewrite its properties, delete, move or rename without an explicit request. Propose bigger changes in `01 Fleeting/AI Drafts/`.
- `00 Home/Agent/Agent Memory.md` is append-only, newest entry at the bottom, each dated `### YYYY-MM-DD`.

## Every note you create
- Starts with YAML frontmatter containing `type`, `created`, a one-sentence `summary`, and `tags`.
- Carries the `ai-assisted` tag until {{USER_NAME}} removes it after review.
- Links to at least one map in `04 Maps` and is listed as a pointer line in the matching map (for chats: `04 Maps/AI Chats MOC.md`, format `- [[Note]] → [[Related MOC]]`).
- Never becomes an orphan: something must link to it.
- Uses existing names exactly in `[[wikilinks]]`. Non-Markdown files need the extension: `[[Deck.pptx]]`.

## Naming
| Folder | Pattern | Example |
|---|---|---|
| 02 Literature | `Source - Type - Detail` | `CPRT - 10-K - FY2026` |
| 03 Permanent | a full claim | `Linking beats filing` |
| 04 Maps | `<Topic> MOC` | `Investing MOC` |
| 05 Projects | starts with a verb | `Launch club website` |
| 06 Daily | `YYYY/MM/YYYY-MM-DD` | `06 Daily/2026/10/2026-10-27` |
| 07 Weekly | `GGGG-[W]WW` | `2026-W44` |
| 11 AI Chats | `YYYY-MM-DD - Topic in Title Case` | `2026-10-27 - Vault Blueprint` |
| 12 School | `<CODE> - <Name>` hub, `<CODE> Materials` | `ECON 325 - Entrepreneurship` |
| 13 Calendar/Events | `YYYY-MM-DD - Event` | `2026-11-03 - Coffee chat` |

Superseded drafts go in an `Older versions` subfolder next to the current file, never deleted.

## Dates and tasks
- Dated to-dos: `- [ ] task [due:: YYYY-MM-DD]`. Optional reading: `[scheduled:: YYYY-MM-DD]`.
- Course deadlines go in the course hub; pre-class readings in `13 Calendar/Prep/<CODE> Prep.md`; everything else in `13 Calendar/To-Do.md`.
- Timed commitments (calls, meetings, interviews, exams, trips) become event notes in `13 Calendar/Events/` and a line in `04 Maps/Calendar MOC.md`.
- When a chat reveals a date, add it without being asked and confirm in one line.

## Never save
API keys, passwords, tokens, recovery phrases, card, account or government ID numbers. Replace with `[redacted]`. Ask before saving third parties' private details.

## Finish every task by
Listing each note read, created or appended, and confirming every new link resolves.
