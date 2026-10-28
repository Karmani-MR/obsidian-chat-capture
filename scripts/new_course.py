#!/usr/bin/env python3
"""Add a course to a blueprint vault: folder + 8 subfolders, hub, Materials note,
Prep note, School MOC row, Color Key row, graph color group and CSS color.

Usage:
  python3 scripts/new_course.py "<vault>" --code "ECON 325" --name "Entrepreneurship" \
      --term "Fall 2026" --days Tue Thu --start 11:00 --end 12:15 --location "Fetzer 109" \
      --instructor "Prof. Name" --term-start 2026-08-17 --term-end 2026-12-11 --color "#C2185B"

Close Obsidian first, or Obsidian may overwrite .obsidian/graph.json with its in-memory copy.
Standard library only. Never overwrites an existing course folder.
"""
import argparse, json, pathlib, re, sys

SUBFOLDERS = ["01 Syllabus & Admin", "02 Lecture Slides", "03 Readings", "04 Assignments",
              "05 Cases & Projects", "06 Exams & Review", "07 Notes", "08 Resources"]

def fill(text, m):
    for k, v in m.items():
        text = text.replace("{{" + k + "}}", v)
    return text

def add_course(vault, code, name, term, days, start, end, location, instructor, term_start, term_end, color):
    vault = pathlib.Path(vault).expanduser()
    tdir = vault / "09 Templates"
    hub_name = f"{code} - {name}"
    folder = vault / "12 School" / term / hub_name
    if folder.exists():
        sys.exit(f"Refusing: {folder} already exists.")
    m = {"CODE": code, "NAME": name, "TERM": term, "DAYS": ", ".join(days), "START_TIME": start, "END_TIME": end,
         "LOCATION": location, "INSTRUCTOR": instructor, "TERM_START": term_start or "", "TERM_END": term_end or "", "COLOR": color}
    for s in SUBFOLDERS:
        (folder / s).mkdir(parents=True, exist_ok=True)
    (folder / f"{hub_name}.md").write_text(fill((tdir / "Course Hub.md").read_text(), m))
    (folder / f"{code} Materials.md").write_text(fill((tdir / "Course Materials.md").read_text(), m))
    prep = vault / "13 Calendar" / "Prep" / f"{code} Prep.md"
    prep.parent.mkdir(parents=True, exist_ok=True)
    if not prep.exists():
        prep.write_text(fill((tdir / "Course Prep.md").read_text(), m))

    # School MOC row (append under the course table)
    moc = vault / "04 Maps" / "School MOC.md"
    if moc.exists():
        t = moc.read_text()
        row = f"| [[{hub_name}]] | {', '.join(days)} | {start}–{end} | {location} |"
        if row not in t:
            t = re.sub(r"(\|---\|---\|---\|---\|\n(?:\|.*\|\n)*)", lambda x: x.group(1) + row + "\n", t, count=1)
            moc.write_text(t)
    # Color Key row
    ck = vault / "00 Home" / "Color Key.md"
    if ck.exists():
        t = ck.read_text()
        line = f"- {color} — [[{hub_name}]]"
        if line not in t:
            t = t.replace("If colors vanish", line + "\n\nIf colors vanish", 1)
            ck.write_text(t)
    # Graph color group: course folder + its prep note, inserted after Past Courses (first match wins)
    gp = vault / ".obsidian" / "graph.json"
    if gp.exists():
        g = json.loads(gp.read_text())
        q = f'path:"12 School/{term}/{hub_name}" OR path:"13 Calendar/Prep/{code} Prep"'
        if not any(c["query"] == q for c in g.get("colorGroups", [])):
            g.setdefault("colorGroups", []).insert(1, {"query": q, "color": {"a": 1, "rgb": int(color.lstrip("#"), 16)}})
            gp.write_text(json.dumps(g, indent=2) + "\n")
    # CSS
    css = vault / ".obsidian" / "snippets" / "color-coding.css"
    if css.exists():
        t = css.read_text()
        p = f"12 School/{term}/{hub_name}"
        block = (f'.nav-folder-title[data-path="{p}"] {{ color: {color}; font-weight: 600; }}\n'
                 f'.nav-file-title[data-path^="{p}/"] {{ border-left: 3px solid {color}; }}\n')
        if block not in t:
            css.write_text(t.replace("/* COURSES:END */", block + "/* COURSES:END */"))
    return folder

if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("vault"); a.add_argument("--code", required=True); a.add_argument("--name", required=True)
    a.add_argument("--term", required=True); a.add_argument("--days", nargs="*", default=[])
    a.add_argument("--start", default=""); a.add_argument("--end", default=""); a.add_argument("--location", default="")
    a.add_argument("--instructor", default=""); a.add_argument("--term-start", default=""); a.add_argument("--term-end", default="")
    a.add_argument("--color", default="#3F51B5")
    x = a.parse_args()
    f = add_course(x.vault, x.code, x.name, x.term, x.days, x.start, x.end, x.location, x.instructor, x.term_start, x.term_end, x.color)
    print(f"Created {f}")
