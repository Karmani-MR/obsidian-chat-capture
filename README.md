# Obsidian AI Vault

A blueprint your AI can use to build you an organized Obsidian vault. It's taken from a real student vault that's used every day: the template holds that vault's actual calendar code, graph plugin, settings, templates and AI operating manual, with the personal content removed. You get numbered folders, a circular graph centered on Home with one colored starburst per area and per course, weekly and monthly calendars, a standard folder for every course, and rules that tell every AI app how to read and write your notes safely.

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

Then open the folder in Obsidian, click "Trust author and enable plugins", and turn on Templater → "Trigger Templater on new file creation". You'll need Python 3 (standard library only) and Obsidian 1.9 or newer.

## What you get

| | |
|---|---|
| **Folders** | `00 Home` · `01 Fleeting` · `02 Literature` · `03 Permanent` · `04 Maps` · `05 Projects` · `06 Daily` · `07 Weekly` · `08 Archive` · `09 Templates` · `10 Attachments` · `11 AI Chats` · `12 School` · `13 Calendar` |
| **Home** | Dashboard with every area, active courses, deadlines for the next 14 days, inbox, projects and recent AI chats |
| **Weekly Calendar** | A time grid of classes (repeating weekly, with breaks skipped), calls, meetings and exams, with an Add event form |
| **To-Do Calendar** | A month grid of every dated task (assignments, exams, readings, to-dos), with filters and check-off in place |
| **Courses** | Each course gets a course map, a folder with eight numbered subfolders, a Materials note linking every file, a class note and a prep note, all in one color. Finished courses move to Past Courses and turn gray |
| **Graph** | The bundled Graph Groups plugin pins Home in the center and lays out each area and course as its own colored starburst |
| **AI layer** | `AGENTS.md` (read order, permissions table, how AI work is marked, conventions), AI Context, USER, Top of Mind, an append-only Agent Memory, and seven skills (Todays Focus, Weekly Review, Process Notes, Ingest, Vault Health, Write Like Me, Calendar Update), also available as Claude Code slash commands |
| **Calendar tool** | `add_event.py`, so any AI with a shell can add, move, cancel or list events and log each change |
| **Safety net** | Agents append instead of overwriting, anything they write is tagged `ai-assisted` until you review it, and Obsidian Git takes local snapshots every 30 minutes |

The full design is in [`blueprint/VAULT-SPEC.md`](blueprint/VAULT-SPEC.md).

## Repo layout

```
AGENTS.md                  step-by-step instructions for the AI doing the build
blueprint/                 spec, interview questions, colors, how to personalize
vault-template/            the vault itself, with {{PLACEHOLDERS}}
scripts/
  build_vault.py           template + answers.json → new vault
  new_course.py            add a course (map, folder, Materials, class, prep, colors)
  verify_vault.py          read-only check: links, orphans, placeholders, secrets
  install-plugins.sh/.ps1  Dataview, Templater, Calendar, Obsidian Git (Graph Groups is bundled)
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
