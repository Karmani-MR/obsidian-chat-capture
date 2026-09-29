# Obsidian Chat Capture

An [Agent Skill](https://agentskills.io) that saves the useful part of your AI conversations, meaning decisions, takeaways and next steps, into your Obsidian vault as short, linked notes. It works in any app that supports Agent Skills and MCP: Claude Code, Claude Desktop, Cursor, Codex, Perplexity and others.

```
You:  ...ok, let's go with the catalyst framing. Save this.
AI:   Saved to Obsidian: AI Chats/2026-09-29 - HFAC Pitch Catalysts.md
```

## How it works

| Piece | What it does |
|---|---|
| **Connector**: [Local REST API with MCP](https://github.com/coddingtonbear/obsidian-local-rest-api) (Obsidian plugin) | Runs an authenticated MCP server inside Obsidian at `127.0.0.1`, so AI apps can read and write notes. |
| **Skill**: `skills/obsidian-chat-capture/` | Tells the AI when to save, where, in what format, what never to save, and to append rather than overwrite. |

Each saved note gets properties (`type: ai-chat`, `source`, `created`, `related`), a few takeaways, decisions, tasks, and `[[links]]` to notes that already exist in your vault.

## Install

1. **Vault:** in Obsidian, install and enable the community plugin **Local REST API with MCP**. Copy the API key from its settings.
2. **App:** connect your AI app to `https://127.0.0.1:27124/mcp/` with the header `Authorization: Bearer <API_KEY>`. Per-app configs (Claude Code, Claude Desktop, Cursor, Perplexity, Codex, ChatGPT) are in [`references/setup.md`](skills/obsidian-chat-capture/references/setup.md).
3. **Skill:** copy or upload `skills/obsidian-chat-capture/` into your app's skills (for example `~/.claude/skills/`), or zip the folder for apps that take uploads.
4. **Optional, automatic mode:** add this to the app's custom instructions:
   > At the end of any substantive chat, use the obsidian-chat-capture skill to save a short note to my Obsidian vault and tell me the path.

## Safety

- The server only listens on your computer, and every request needs the API key. Never commit the key. `.gitignore` excludes common config files.
- The skill redacts keys, passwords, recovery phrases and ID numbers. It won't save third parties' private data without asking, and it never deletes or overwrites notes.
- Obsidian must be running for saves to work.

## Without MCP

`scripts/save_note.py` (Python 3, standard library only) does the same create-or-append through the REST API. For cloud apps like ChatGPT, `scripts/clip_capture.py` saves any copied note block that starts with `obsidian-capture:` (see setup.md, section 4):

```bash
export OBSIDIAN_API_KEY=...        # from Settings > Local REST API
python3 skills/obsidian-chat-capture/scripts/save_note.py "AI Chats/2026-09-29 - Topic.md" < note.md
```

## Customize

The default folder is any root folder ending in `AI Chats` (for example `11 AI Chats`), or `AI Chats/`. Change the note shape in `templates/chat-note.md` and the rules in `SKILL.md`.

## License

MIT
