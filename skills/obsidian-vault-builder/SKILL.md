---
name: obsidian-vault-builder
description: "Build a new Obsidian vault from the Obsidian AI Vault blueprint: numbered folders, Home-centered colored graph, weekly and monthly calendars, course folders, and an AGENTS.md operating layer. Use for 'build me an Obsidian vault', 'set up Obsidian like this', 'add a course to my vault'. Not for saving chats (use obsidian-chat-capture)."
license: MIT
compatibility: "Needs Python 3 and a copy of the obsidian-ai-vault repo (scripts/, vault-template/, blueprint/). Works in any Agent Skills host that can run code."
metadata:
  author: Marc Rainone
  version: "1.0.0"
---

# Obsidian Vault Builder

The full procedure is in the repo's root `AGENTS.md`. In short:

1. **Get the repo.** If `scripts/build_vault.py` isn't next to this skill's parent folders, clone the repo this skill came from.
2. **Interview** with `blueprint/interview.md`. Write `answers.json` like `blueprint/answers.example.json` and confirm a summary with the user.
3. **Build:** `python3 scripts/build_vault.py --answers answers.json --dest "<new folder>"`. It refuses non-empty folders.
4. **Plugins:** `bash scripts/install-plugins.sh "<dest>"` (or the `.ps1` on Windows). Then the user trusts plugins in Obsidian and turns on Templater's "Trigger on new file creation".
5. **Verify:** `python3 scripts/verify_vault.py "<dest>"` must print `PASS`.
6. **Report** the path, what to open first (Home) and any manual steps left.

Add a course to an existing blueprint vault with `scripts/new_course.py` (close Obsidian first). Retire one with the steps in `blueprint/personalize.md`.

Never write into an existing vault unless the user asks. If they do, back up first, add only missing files, and merge settings without overwriting their values.
