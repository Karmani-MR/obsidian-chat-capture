---
type: map
summary: Hub for current courses, Past Courses and course deadlines.
tags: [map]
---
# School MOC

## {{TERM}}
| Course | Days | Time | Room |
|---|---|---|---|
{{COURSE_TABLE_ROWS}}

## Past Courses
See [[About Past Courses]].
```dataview
LIST FROM "12 School/Past Courses" WHERE type = "course"
```

## Due soon
```dataview
TASK FROM "12 School" OR "13 Calendar/Prep" WHERE !completed AND due SORT due ASC LIMIT 20
```

Back to [[Home]]
