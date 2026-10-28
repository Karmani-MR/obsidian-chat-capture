---
type: dashboard
summary: Center of the vault; every hub links back here.
cssclasses: [wide]
tags: [dashboard]
---
# Home

**Today:** [[Weekly Calendar]] · [[Monthly Calendar]] · [[Top of Mind]]
**For AI:** [[AGENTS]] · [[AI Context]]
**Guides:** [[README]] · [[Color Key]] · [[Knowledge Base.base|Knowledge Base]] · [[About Archive]]

## Maps
- [[AI Chats MOC]] — saved AI conversations
- [[Calendar MOC]] — events and dated work
- [[AI Agent MOC]] — agent skills and review queue
- [[Note-taking MOC]] — fleeting, literature and permanent notes
- [[School MOC]] — current courses and Past Courses <!-- if:school -->
{{AREA_MOC_LINKS}}

## Inbox
```dataview
TABLE created AS "Captured"
FROM "01 Fleeting"
WHERE type = "fleeting" AND status = "inbox"
SORT created ASC
```

## Active projects
```dataview
TABLE status AS "Status", due AS "Due"
FROM "05 Projects"
WHERE type = "project" AND status = "active"
SORT due ASC
```

## Waiting for review (ai-assisted)
```dataview
LIST
FROM #ai-assisted
SORT file.mtime DESC
LIMIT 15
```
