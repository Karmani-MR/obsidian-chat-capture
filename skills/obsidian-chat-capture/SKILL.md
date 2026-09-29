---
name: obsidian-chat-capture
description: "Save AI chat takeaways into an Obsidian vault as linked notes via Local REST API MCP server, appending instead of overwriting and redacting secrets. Use for 'save this chat to Obsidian', 'log this conversation', automatic end-of-chat capture, or connecting an AI app to a vault. Not for importing chat exports."
license: MIT
compatibility: "Needs Obsidian desktop with the 'Local REST API with MCP' plugin (v5+) and an MCP client connected to it, or Python 3 for the fallback script. Works in any Agent Skills host."
metadata:
  author: Marc Rainone
  version: "1.1.0"
---

# Obsidian Chat Capture

Turn the useful part of a conversation into one short, linked note in the user's Obsidian vault. Capture decisions, insights and next steps, not transcripts.

## When to save

- The user says "save this", "log this", "add to Obsidian", or similar: save now.
- The user's custom instructions ask for automatic capture: save at the end of a substantive chat (a decision, a plan, research findings or tasks), then say so in one line. Skip small talk and one-line lookups.
- Otherwise, offer once near the end of a substantive chat. Never nag.

## Pick the write path

1. **MCP tools available** (`vault_list`, `vault_read`, `vault_write`, `vault_append`, `search_simple` from the `obsidian` server): use them.
2. **Shell on the same computer as Obsidian, but no MCP**: run `scripts/save_note.py` (below). A cloud code sandbox is not that computer.
3. **Neither** (for example ChatGPT on the web, or a phone app): cloud-hosted apps cannot reach `localhost`, so do not ask for a URL, API key or tunnel, and do not say the save failed. Put the target path on one line, then the finished note in one Markdown code block, and tell the user to paste it into a new note at that path.
4. **Tools missing, or the user asks how to connect an app**: read `references/setup.md`.

## Save a note

1. **Find the folder.** `vault_list` the vault root. Use the existing folder whose name ends in `AI Chats` (for example `11 AI Chats`). If there isn't one, create notes in `AI Chats/`.
2. **Name the file** `YYYY-MM-DD - <Topic in Title Case>.md`, using today's date and a 3–7 word topic. Strip `\ / : * ? " < > | # ^ [ ]`.
3. **Find links.** Run `search_simple` for 2–4 key names from the chat, such as a project, course, company or person. Link only to notes that exist, as `[[Exact Note Name]]`. Never invent links.
4. **Fill `templates/chat-note.md`.** Keep the body under about 300 words. Write tasks as `- [ ] task [due:: YYYY-MM-DD]` only when a date was stated.
5. **Never overwrite.** `vault_read` the target path first. If the note exists (the same topic was saved earlier today), `vault_append` a `## Update HH:MM` section instead of calling `vault_write`.
6. **Confirm** in one line with the vault path, for example `Saved to Obsidian: 11 AI Chats/2026-09-29 - HFAC Pitch Catalysts.md`.

## Never save

- API keys, passwords, tokens, recovery phrases, card numbers, government ID numbers or account numbers. Replace them with `[redacted]`.
- Third parties' private details (client data, health or financial information) unless the user explicitly asks. Ask first when unsure.
- Raw transcripts, or quotes longer than two sentences.

Do not delete, move or rename existing vault notes as part of capture.

## Fallback script

`scripts/save_note.py` creates or appends a note through the REST API. It reads `OBSIDIAN_API_KEY` from the environment and never takes the key as an argument. Pipe the note body to stdin:

```bash
python3 scripts/save_note.py "11 AI Chats/2026-09-29 - Topic.md" < note.md
```

It creates the note, or appends it under `## Update HH:MM` if the note already exists. Add `--dry-run` to preview.
