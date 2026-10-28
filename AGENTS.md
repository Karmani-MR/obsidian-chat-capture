# Instructions for the AI building a vault from this repo

You are helping someone build an Obsidian vault organized like the one this repo was modeled on. Follow these steps in order. Do not skip the interview or the verification.

## 0. Check what you can do

| You have | Do this |
|---|---|
| A shell on the user's computer (Claude Code, Codex, Cursor, a desktop agent) | Clone or download this repo there and run the scripts directly. |
| File write access to the user's computer, but no shell | Build in your sandbox with the scripts, then copy every file (including hidden `.obsidian/**`) to the destination. |
| Neither (cloud chat app) | Build in your sandbox if you have one and hand back a zip. Otherwise give the user the exact commands to run. |

Never write into an existing vault or a non-empty folder. To merge into an existing vault, see "Existing vault" below.

## 1. Interview the user

Ask the questions in [`blueprint/interview.md`](blueprint/interview.md), a few at a time. Turn the answers into a JSON file shaped like [`blueprint/answers.example.json`](blueprint/answers.example.json). Show the user a short summary of the answers before building.

## 2. Build

```bash
python3 scripts/build_vault.py --answers answers.json --dest "~/Documents/<Vault Name>"
```

This copies [`vault-template/`](vault-template/), fills in names and dates, creates one map per life area, and for students creates each course (folder, eight numbered subfolders, hub, Materials note, Prep note, School MOC row, color). Non-students get no `12 School` folder.

Add courses later with `scripts/new_course.py` (run `--help`).

## 3. Plugins

```bash
bash scripts/install-plugins.sh "<dest>"          # macOS / Linux
powershell -File scripts/install-plugins.ps1 -Vault "<dest>"   # Windows
```

Installs Dataview, Templater, Calendar and Obsidian Git. Then the user opens the folder in Obsidian (Open folder as vault), clicks "Trust author and enable plugins", and under Settings → Templater turns on "Trigger Templater on new file creation". If you can drive Obsidian's command line, you may do those steps for them.

Optional: install the Local REST API plugin and the [`obsidian-chat-capture`](skills/obsidian-chat-capture/) skill so AI chats save into `11 AI Chats`.

## 4. Verify

```bash
python3 scripts/verify_vault.py "<dest>"
```

Must print `PASS`: required folders exist, configs parse, links resolve, no orphan notes, no leftover placeholders, no secrets. If you can open Obsidian, also check that Home, Weekly Calendar and Monthly Calendar render, and that the graph is colored.

## 5. Report

Tell the user: where the vault is, what to open first (Home), the three plugin steps if you couldn't do them, and that `Goals`, `Principles` and `Writing Style` in `00 Home/Agent/` are drafts for them to rewrite.

## Existing vault

Only with the user's explicit request. Back up first (copy the vault or commit with Git). Add missing folders and notes from `vault-template/`; never overwrite or delete existing notes. Merge `.obsidian/*.json` key by key and keep the user's values. Run `verify_vault.py` and fix only what you added.

## Reference

- [`blueprint/VAULT-SPEC.md`](blueprint/VAULT-SPEC.md) — the design: folders, notes, linking, calendar, agent layer.
- [`blueprint/graph-and-colors.md`](blueprint/graph-and-colors.md) — colors and the Home-centered graph.
- [`blueprint/personalize.md`](blueprint/personalize.md) — add or retire courses, add areas, change colors.
