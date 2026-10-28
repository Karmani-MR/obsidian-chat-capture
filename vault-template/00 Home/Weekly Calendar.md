---
type: dashboard
summary: This week's timed classes and events, built from course hubs and event notes.
cssclasses: [wide]
tags: [dashboard, calendar]
week_offset: 0
---
# Weekly Calendar

Classes come from course hubs (`type: course`, `status: current`, `days`, `start_time`, `end_time`, `location`, `term_start`, `term_end`). One-off events come from `13 Calendar/Events` (`type: event`, `date`, `start`, `end`, `location`). A `cancels` property on an event (`cancels: "[[ECON 325 - Entrepreneurship]]"`) hides that day's class.

```dataviewjs
const offset = Number(dv.current().week_offset ?? 0);
const start = moment().startOf("isoWeek").add(offset, "weeks");
const days = [...Array(7)].map((_, i) => start.clone().add(i, "days"));
const iso = (v) => v && v.toISODate ? v.toISODate() : (v ? String(v).slice(0, 10) : null);
const rows = days.map(() => []);
const events = dv.pages('"13 Calendar/Events"').where(p => p.type === "event" && p.date);
const cancelled = new Set();
for (const e of events) {
  if (e.cancels) cancelled.add(iso(e.date) + "|" + (e.cancels.path ?? String(e.cancels)));
  const i = moment(iso(e.date)).diff(start, "days");
  if (i >= 0 && i < 7) rows[i].push({ t: String(e.start ?? "all day"), end: String(e.end ?? ""), what: e.file.link, where: e.location ?? "" });
}
for (const c of dv.pages('"12 School"').where(p => p.type === "course" && p.status === "current")) {
  const meet = (c.days ?? []).map(String);
  days.forEach((d, i) => {
    const day = d.format("YYYY-MM-DD");
    const inTerm = (!c.term_start || day >= iso(c.term_start)) && (!c.term_end || day <= iso(c.term_end));
    const off = (c.no_class ?? []).map(iso).includes(day) || cancelled.has(day + "|" + c.file.path);
    if (inTerm && !off && meet.includes(d.format("ddd"))) rows[i].push({ t: String(c.start_time ?? ""), end: String(c.end_time ?? ""), what: c.file.link, where: c.location ?? "" });
  });
}
dv.header(3, `Week of ${start.format("MMM D")} – ${start.clone().add(6, "days").format("MMM D, YYYY")}`);
days.forEach((d, i) => {
  const list = rows[i].sort((a, b) => a.t.localeCompare(b.t));
  const today = d.isSame(moment(), "day") ? " (today)" : "";
  dv.header(4, d.format("dddd, MMM D") + today);
  if (!list.length) { dv.paragraph("—"); return; }
  dv.table(["Time", "What", "Where"], list.map(r => [r.end ? `${r.t}–${r.end}` : r.t, r.what, r.where]));
});
```

Change `week_offset` in this note's properties to look ahead (1) or back (-1).

Back to [[Home]] · [[Calendar MOC]]
