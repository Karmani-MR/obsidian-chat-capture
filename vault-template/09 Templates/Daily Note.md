---
type: daily
date: <% tp.date.now("YYYY-MM-DD", 0, tp.file.title, "YYYY-MM-DD") %>
summary: Daily note.
tags: [daily]
---
# <% tp.date.now("dddd, MMMM D, YYYY", 0, tp.file.title, "YYYY-MM-DD") %>

← [[06 Daily/<% tp.date.now("YYYY/MM/YYYY-MM-DD", -1, tp.file.title, "YYYY-MM-DD") %>|Yesterday]] · [[07 Weekly/<% tp.date.now("GGGG-[W]WW", 0, tp.file.title, "YYYY-MM-DD") %>|This week]] · [[06 Daily/<% tp.date.now("YYYY/MM/YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>|Tomorrow]] → · [[Calendar MOC]]

## Top 3 today
- [ ] <% tp.file.cursor() %>
- [ ] 
- [ ] 

## Log
- 

## Due today
```dataview
TASK
WHERE !completed AND (due = this.date OR scheduled = this.date)
```
