# Obsidian AI Vault

A blueprint your AI can use to build you an organized Obsidian vault, modeled on a real student vault that's used every day. It includes numbered folders, a Home-centered graph with color coding, weekly and monthly calendars, course folders, and an operating manual that tells every AI app how to read and write your notes safely.

It also includes [`obsidian-chat-capture`](skills/obsidian-chat-capture/), a skill that saves the useful parts of AI chats into the vault.

## Use it

Give this repo to an AI that can run code (Claude Code, Codex, Cursor, Perplexity Computer and others) and say:

> Read AGENTS.md in this repo and build me an Obsidian vault.

The AI asks you a few questions (your life areas and, if you're a student, your courses), builds the vault, installs the plugins, and runs a check before handing it over.

To do it yourself:

```bash
cp blueprint/answers.example.json my-answers.json      # edit it
python3 scripts/build_vault.py --answers my-answers.json --dest "~/Documents/My Vault"
bash scripts/install-plugins.sh "~/Documents/My Vault"
python3 scripts/verify_vault.py "~/Documents/My Vault"
```

Then open the folder in Obsidian, click "Trust author and enable plugins", and turn on Templater → "Trigger Templater on new file creation". You'll need Python 3 (standard library only) and Obsidian 1.9 or newer for Bases.

## What you get

| | |
|---|---|
| **Folders** | `00 Home` · `01 Fleeting` · `02 Literature` · `03 Permanent` · `04 Maps` · `05 Projects` · `06 Daily` · `07 Weekly` · `08 Archive` · `09 Templates` · `10 Attachments` · `11 AI Chats` · `12 School` · `13 Calendar` |
| **Home** | A dashboard linking every map, the calendars, your inbox, active projects and AI notes waiting for review |
| **Calendars** | Weekly view of classes and events; monthly day-by-day grid of everything due, built from `[due:: date]` tasks anywhere in the vault |
| **School** | One folder per course with eight numbered subfolders, a hub with schedule and deadlines, a Materials note linking every file, a Prep note, and its own color. Finished courses move to Past Courses and turn gray |
| **Graph** | Home in the center, each hub and each course forming its own colored starburst |
| **AI layer** | `AGENTS.md` (read order, where AI may write, naming, task format), AI Context, Top of Mind, an append-only Agent Memory, and nine skill notes such as Today's Focus, Weekly Review, Calendar Capture and Add Course |
| **Safety net** | AI writes are append-only outside a few scratch areas, AI-made notes are tagged `ai-assisted` until you review them, and Obsidian Git takes local snapshots every 30 minutes |
| **Templates** | Daily, Weekly, Fleeting, Literature, Permanent, Map, Project, AI Chat, Event, Lecture, Course Hub/Materials/Prep |

The full design is in [`blueprint/VAULT-SPEC.md`](blueprint/VAULT-SPEC.md).

## Repo layout

```
AGENTS.md                  step-by-step instructions for the AI doing the build
blueprint/                 spec, interview questions, colors, how to personalize
vault-template/            the vault itself, with {{PLACEHOLDERS}}
scripts/
  build_vault.py           template + answers.json → new vault
  new_course.py            add a course (folders, notes, colors)
  verify_vault.py          read-only check: links, orphans, placeholders, secrets
  install-plugins.sh/.ps1  Dataview, Templater, Calendar, Obsidian Git
skills/
  obsidian-vault-builder/  Agent Skill wrapper for this blueprint
  obsidian-chat-capture/   Agent Skill that saves chat takeaways into 11 AI Chats
```

## Chat capture

Install the **Local REST API with MCP** plugin, connect your AI app (setup per app is in [`setup.md`](skills/obsidian-chat-capture/references/setup.md)), and add the `obsidian-chat-capture` skill. It saves `11 AI Chats/YYYY-MM-DD - Topic.md` notes with takeaways, decisions and next steps, links them to existing notes, never overwrites, and redacts secrets. Cloud apps without vault access get a note they can paste in, or `scripts/clip_capture.py` can save it from the clipboard.

## Privacy

The template has no personal data. The scripts only write inside the destination folder, never upload anything, and refuse to build into a folder that already has files. Never commit API keys; `.gitignore` covers common config files.

## License

MIT
