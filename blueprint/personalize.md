# Personalize

## Add a course
```bash
python3 scripts/new_course.py "<vault>" --code "ECON 325" --name "Entrepreneurship" --term "Fall 2026" \
  --days Tue Thu --start 11:00 --end 12:15 --location "Fetzer 109" --instructor "Prof. Name" \
  --term-start 2026-08-17 --term-end 2026-12-11 --color "#C2185B"
```
Close Obsidian first (it rewrites `graph.json` from memory). By hand: copy the three `Course …` templates from `09 Templates`, create the eight subfolders, add a School MOC row, a graph color group and a CSS block.

## File course material
Put the file in the right numbered subfolder, then add a link line to the course Materials note under that subfolder's heading. Link non-Markdown files with the extension: `[[Lecture 3.pptx]]`. Old versions go in an `Older versions` subfolder.

## Retire a course
1. Check nothing in the folder is open in Word or PowerPoint (`lsof +D "<folder>"` on Mac).
2. Move the folder inside Obsidian (drag in the file explorer) to `12 School/Past Courses/`, so every link updates.
3. Set the hub's `status: past`.
4. Delete the course's color group in Graph settings and its block in `color-coding.css`. The Past Courses gray group then covers it.

## Add a life area
Create `04 Maps/<Area> MOC.md` from the Map of Content template, add `- [[<Area> MOC]]` to Home's Maps list and AI Context, and a `## <Area>` section in AI Chats MOC.

## Change colors
Edit `Color Key.md`, the matching graph color group, and the CSS rule. Keep the three in sync.

## Connect AI apps
- Claude Code: run `claude` inside the vault; it reads `CLAUDE.md` → `AGENTS.md`.
- Any MCP app: install the Local REST API plugin and follow `skills/obsidian-chat-capture/references/setup.md`.
