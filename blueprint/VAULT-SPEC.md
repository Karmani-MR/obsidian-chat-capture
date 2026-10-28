# Vault spec

The design this repo reproduces. `vault-template/` implements it; read this to understand why it is shaped this way or to rebuild it by hand.

## Principles

1. **One center.** Everything links back to `00 Home/Home.md`, directly or through a hub. Nothing is an orphan.
2. **Hubs, not deep folders.** Each area has one hub note (a map, a course Materials note, Calendar MOC, Top of Mind). Notes link to their hub; hubs link to Home. This is what makes the graph form clean starbursts around Home.
3. **Numbered folders by note type**, not by topic. Topics live in maps.
4. **AI is a guest with rules.** A root `AGENTS.md` says what agents read first, where they may write, and how to name and link notes. AI-made notes are tagged `ai-assisted` until reviewed.
5. **Dates live in tasks.** Every dated item is a checkbox with `[due:: YYYY-MM-DD]`, so calendars are queries, not hand-kept lists.
6. **Nothing is lost.** Append instead of overwrite, `Older versions` folders instead of deletion, local Git snapshots for undo.

## Folders

| Folder | Purpose | Hub |
|---|---|---|
| `00 Home` | Home, Weekly/Monthly Calendar, AI Context, Top of Mind, Color Key, `Agent/` | Home |
| `01 Fleeting` | Quick captures (new notes land here); `AI Drafts/` for agent proposals | Note-taking MOC |
| `02 Literature` | Notes on sources, in your own words | Note-taking MOC |
| `03 Permanent` | One idea per note, titled as a claim | Note-taking MOC / area MOCs |
| `04 Maps` | MOCs: AI Chats, Calendar, AI Agent, Note-taking, School, one per life area | Home |
| `05 Projects` | Active projects (outcome, next actions, log) | Top of Mind |
| `06 Daily` | `YYYY/MM/YYYY-MM-DD` daily notes | Calendar MOC |
| `07 Weekly` | `GGGG-[W]WW` weekly reviews | Calendar MOC |
| `08 Archive` | Finished material | Home |
| `09 Templates` | Templater templates (excluded from search and graph) | — |
| `10 Attachments` | Loose files not owned by a course or project | — |
| `11 AI Chats` | `YYYY-MM-DD - Topic` takeaways from AI chats | AI Chats MOC |
| `12 School/<Term>/<CODE - Name>/` | Current courses | the course's Materials note |
| `12 School/Past Courses/` | Finished courses, moved whole, all gray | School MOC |
| `13 Calendar/Events` · `Prep` · `To-Do.md` · `System` | Event notes, per-course prep, other to-dos, calendar scripts/config | Calendar MOC |

## Courses

Each course folder has a hub (`CODE - Name.md`), a Materials note (`CODE Materials.md`) and eight subfolders: `01 Syllabus & Admin`, `02 Lecture Slides`, `03 Readings`, `04 Assignments`, `05 Cases & Projects`, `06 Exams & Review`, `07 Notes`, `08 Resources`. Every file in the folder is linked from the Materials note, so each course becomes its own starburst. Pre-class prep lives in `13 Calendar/Prep/CODE Prep.md`. Course-owned notes elsewhere (prep, exam events) carry the course color.

The hub's properties drive the Weekly Calendar: `status: current`, `days: [Tue, Thu]`, `start_time: "11:00"`, `end_time: "12:15"`, `location`, `term_start`, `term_end`, optional `no_class: [dates]` for breaks.

Retiring a course: move its folder inside Obsidian to `12 School/Past Courses/` (so links update), set `status: past`, remove its color. See `personalize.md`.

## Calendar

- **Weekly Calendar** (DataviewJS): recurring classes from course hubs plus one-off events from `13 Calendar/Events` (`type: event`, `date`, `start`, `end`, `location`). An event with `cancels: "[[Course hub]]"` hides that day's class.
- **Monthly Calendar** (DataviewJS): a month grid of every unchecked task with `[due::]` or `[scheduled::]`, plus Overdue and Next 7 days lists you can check off in place.
- **Routing rules:** course deadlines → course hub; readings → Prep note; meetings/calls/exams → event note + Calendar MOC log line; anything else → `13 Calendar/To-Do.md`.

## Agent layer

- `AGENTS.md` (root) — read order, write permissions, naming, task format, never-save list. `CLAUDE.md` contains `@AGENTS.md` so Claude Code loads it.
- `00 Home/AI Context.md` — who the user is and where things live.
- `00 Home/Top of Mind.md` — this week's priorities; agents may edit.
- `00 Home/Agent/` — `USER.md`, append-only dated `Agent Memory.md`, draft `Goals`, `Principles`, `Writing Style`.
- `00 Home/Agent/Skills/` — one note per repeatable job: Today's Focus, Weekly Review, Process Notes, Ingest, Vault Health, Write Like Me, Calendar Capture, Add Course, Retire Course. Any AI can follow them; Claude Code users can point `.claude/skills/` at them.
- Free-write zones: `01 Fleeting/AI Drafts`, `11 AI Chats`, today's daily note, Top of Mind. Everywhere else: append or propose.

## Properties

Every note: `type`, `summary` (one sentence, helps AI retrieval), `tags`. Common types: `dashboard`, `context`, `skill`, `map`, `fleeting`, `literature`, `permanent`, `project`, `daily`, `weekly`, `ai-chat`, `event`, `course`, `materials`, `prep`, `lecture`.

## Plugins and settings

- Core: Daily notes (`06 Daily`, `YYYY/MM/YYYY-MM-DD`), Bases, Properties, Graph, Canvas, Bookmarks.
- Community: Dataview (JS enabled), Templater (folder templates for 01–07, 11 and `13 Calendar/Events`), Calendar (Monday start, weekly notes in `07 Weekly`), Obsidian Git (30-minute local commits, push disabled).
- `alwaysUpdateLinks: true`; Office lock files (`~$…`) and `09 Templates` excluded.
- CSS snippet `color-coding` colors folders and adds a color bar to each note in the file explorer.
