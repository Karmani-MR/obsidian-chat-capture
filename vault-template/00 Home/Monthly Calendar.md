---
type: dashboard
summary: Day-by-day grid of everything due this month, plus overdue and next-seven-days lists.
cssclasses: [wide]
tags: [dashboard, calendar]
month_offset: 0
---
# Monthly Calendar

Every unchecked task with `[due:: YYYY-MM-DD]` or `[scheduled:: YYYY-MM-DD]` anywhere in the vault shows up here. Checking a box below checks it in its source note.

```dataviewjs
const offset = Number(dv.current().month_offset ?? 0);
const m = moment().startOf("month").add(offset, "months");
const iso = (v) => v && v.toISODate ? v.toISODate() : (v ? String(v).slice(0, 10) : null);
const tasks = dv.pages('-"09 Templates"').file.tasks.where(t => !t.completed && (t.due || t.scheduled));
const byDay = {};
for (const t of tasks) { const k = iso(t.due ?? t.scheduled); (byDay[k] ??= []).push(t); }
const esc = (s) => String(s).replace(/[&<>]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));
const clean = (s) => esc(s.replace(/\[(due|scheduled)::[^\]]*\]/g, "").trim()).slice(0, 60);
let html = `<h3>${m.format("MMMM YYYY")}</h3><table style="width:100%;table-layout:fixed;border-collapse:collapse"><tr>`;
for (const d of ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]) html += `<th>${d}</th>`;
html += "</tr><tr>";
const first = m.clone().startOf("isoWeek"), last = m.clone().endOf("month").endOf("isoWeek");
for (let d = first.clone(), i = 0; d.isSameOrBefore(last, "day"); d.add(1, "day"), i++) {
  if (i && i % 7 === 0) html += "</tr><tr>";
  const k = d.format("YYYY-MM-DD"), list = byDay[k] ?? [];
  const dim = d.month() !== m.month() ? "opacity:.35;" : "";
  const today = d.isSame(moment(), "day") ? "outline:2px solid var(--interactive-accent);" : "";
  html += `<td style="vertical-align:top;height:90px;border:1px solid var(--background-modifier-border);padding:4px;${dim}${today}"><b>${d.date()}</b>`;
  for (const t of list) html += `<div style="font-size:11px;margin-top:2px">${t.scheduled && !t.due ? "○" : "•"} <a class="internal-link" data-href="${esc(t.path)}">${clean(t.text)}</a></div>`;
  html += "</td>";
}
html += "</tr></table>";
dv.el("div", "", { attr: { style: "overflow-x:auto" } }).innerHTML = html;

const today = dv.date("today");
dv.header(3, "Overdue");
dv.taskList(tasks.where(t => t.due && t.due < today), false);
dv.header(3, "Next 7 days");
dv.taskList(tasks.where(t => (t.due ?? t.scheduled) >= today && (t.due ?? t.scheduled) <= today.plus({ days: 7 })).sort(t => t.due ?? t.scheduled), false);
```

Change `month_offset` in properties to see next month (1).

Back to [[Home]] · [[Calendar MOC]]
