---
type: dashboard
summary: "One-time setup steps for community plugins (Dataview, Templater, Calendar), Templater's automatic templates, a quick functionality check and optional hotkeys."
tags:
  - setup
---
# Plugin Setup Checklist

Tick these off the first time you open the vault. Full explanations are in the the blueprint repo's README; how this vault is organized is in [[README]].

## 1. Turn on community plugins
- [ ] If Obsidian asked "Do you trust the author of this vault?", choose **Trust author and enable plugins**.
- [ ] Otherwise: **Settings → Community plugins → Turn on community plugins** (this turns off Restricted mode).

## 2. Install the three recommended plugins
Skip this if you ran `install-plugins.sh` / `install-plugins.ps1` before opening the vault.
- [ ] **Settings → Community plugins → Browse** → search **Dataview** → Install → Enable
- [ ] Search **Templater** → Install → Enable
- [ ] Search **Calendar** (by Liam Cain) → Install → Enable

The settings for all three are already included in this vault, so you do not need to configure folders or formats.

## 3. Enable Templater's automatic templates (one switch, once per device)
- [ ] **Settings → Templater → Trigger Templater on new file creation → On** (confirm the warning).

This switch is stored per device for safety, so it cannot ship pre-enabled. Without it, new notes will be created blank.

## 4. Check it works
- [ ] Press `Ctrl/Cmd + N` → you should be asked for a title and the note should appear in `01 Fleeting` with properties filled in.
- [ ] Open today's daily note from the Calendar → dates and Yesterday/Tomorrow links should be filled in.
- [ ] Open [[Home]] → the code blocks should render as tables.

## 5. Optional hotkeys (Settings → Hotkeys)
- [ ] `Templater: Create new note from template` → e.g. `Ctrl/Cmd + Shift + N`
- [ ] `Daily notes: Open today's daily note` → e.g. `Ctrl/Cmd + D`
- [ ] `Note composer: Extract current selection` → e.g. `Ctrl/Cmd + Shift + E` (great for turning a paragraph into its own permanent note)
