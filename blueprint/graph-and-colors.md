# Graph and colors

## Target look

A live, circular, force-directed graph with **Home** in the middle. Around it, each hub (AI Chats MOC, Calendar MOC, Top of Mind, AI Agent MOC, Note-taking MOC, School MOC, each area MOC) forms its own starburst. Each course is a separate starburst around its Materials note, in the course color. Past courses are gray all the way down to their smallest file. Tags and unresolved links are hidden.

## How the template gets there

1. **Structure does most of the work.** Every note links to exactly one hub, and hubs link to Home. Obsidian's physics then clusters each group on its own.
2. **Color groups** in `.obsidian/graph.json`, first match wins, so `12 School/Past Courses` (gray) is listed first and each current course is inserted right after it by `new_course.py`. Each course group covers both its folder and its Prep note.
3. **Forces** taken from the original vault: center 0.494, repel 14.33, link strength 0.88, link distance 286. Tags off, unresolved off, `09 Templates` filtered out.
4. **File explorer** colors come from `.obsidian/snippets/color-coding.css` (folder title color plus a left bar on each note). Course rules sit between the `COURSES:START/END` markers.

## Palette

See `palette.json` and `vault-template/00 Home/Color Key.md`. Folders: Home gold, Fleeting gray, Literature blue, Permanent green, Maps purple, Projects orange, Daily/Weekly teal, Archive brown, Templates/Attachments slate, AI Chats pink, Calendar cyan. Courses draw from an eight-color course palette (indigo, magenta, amber, emerald, coral, teal, brown, violet).

## Gotchas

- **Close Obsidian before editing `graph.json`**, or edit through the running app. Obsidian keeps graph settings in memory and will save over a file edit.
- If folder colors disappear: Settings → Appearance → CSS snippets → enable `color-coding`.
- Group-aware physics (pinning Home, pulling only within groups) needs a custom plugin and is not included. The hub structure plus the forces above gets close.
