---
type: project
status: active
start: <% tp.date.now("YYYY-MM-DD") %>
due:
summary: 
tags: [project]
---
<%*
let title = tp.file.title;
if (title.startsWith("Untitled")) {
  const input = await tp.system.prompt("Project name (start with a verb)");
  title = (input && input.trim()) ? input.trim() : "Project " + tp.date.now("YYYY-MM-DD HHmm");
  title = title.replace(/[\\/:*?"<>|#^\[\]]/g, "-");
  await tp.file.rename(title);
}
-%>
# <% title %>

## Outcome
<% tp.file.cursor() %>

## Next actions
- [ ] 

## Log
- <% tp.date.now("YYYY-MM-DD") %> — Project created.

Links: [[Top of Mind]]
