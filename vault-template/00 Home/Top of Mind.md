---
type: context
summary: This week's priorities, deadlines and open loops. Agents may edit freely.
tags: [context]
---
# Top of Mind

## This week
- [ ] 

## Deadlines
```dataview
TASK
WHERE !completed AND due AND due <= date(today) + dur(14 days)
SORT due ASC
```

## Active projects
```dataview
LIST
FROM "05 Projects"
WHERE status = "active"
```

Back to [[Home]]
