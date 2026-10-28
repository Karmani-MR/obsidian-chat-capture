<%*
const start = moment(tp.file.title, "GGGG-[W]WW").startOf("isoWeek");
const end = start.clone().endOf("isoWeek");
-%>
---
type: weekly
week: <% tp.file.title %>
start: <% start.format("YYYY-MM-DD") %>
summary: Weekly review.
tags: [weekly]
---
# Week <% tp.file.title %> · <% start.format("MMM D") %>–<% end.format("MMM D, YYYY") %>

## Days
<%* for (let i = 0; i < 7; i++) { const d = start.clone().add(i, "days"); -%>
- [[06 Daily/<% d.format("YYYY/MM/YYYY-MM-DD") %>|<% d.format("ddd D") %>]]
<%* } -%>

## Review
1. Empty `01 Fleeting`.
2. Literature → permanent notes; link each to a map.
3. Update projects and [[Top of Mind]].
4. Pick 1–3 priorities.

## Wins
- <% tp.file.cursor() %>

## Priorities for next week
- [ ] 
