---
type: skill
summary: Move a finished course to Past Courses and turn it gray.
tags: [skill, agent]
---
# Skill - Retire Course

Move a finished course to Past Courses and turn it gray.

## Steps
1. Make sure no file in the course folder is open in Word/PowerPoint (`lsof +D <folder>`).
2. Move the folder inside Obsidian (drag, or `app.fileManager.renameFile`) to `12 School/Past Courses/` so links update.
3. Set the hub's `status: past`, remove its color group from graph settings and its block from `color-coding.css`. Past Courses is gray for every file.

## Rules
Follow [[AGENTS]]. Append, don't overwrite. List every note touched.

Back to [[AI Agent MOC]]
