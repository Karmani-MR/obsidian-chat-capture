#!/usr/bin/env python3
"""Build a new vault from vault-template/ and an answers file.

Usage:
  python3 scripts/build_vault.py --answers my-answers.json --dest "~/Documents/My Vault"

answers.json shape: blueprint/answers.example.json.
Refuses to write into a folder that already has files. Standard library only.
"""
import argparse, datetime, json, pathlib, re, shutil, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from new_course import add_course, slug

REPO = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = REPO / "vault-template"
TEXT = {".md", ".json", ".css", ".js", ".py", ".base"}

def main():
    a = argparse.ArgumentParser(); a.add_argument("--answers", required=True); a.add_argument("--dest", required=True)
    x = a.parse_args()
    ans = json.loads(pathlib.Path(x.answers).expanduser().read_text())
    dest = pathlib.Path(x.dest).expanduser().resolve()
    if dest.exists() and any(dest.iterdir()):
        sys.exit(f"Refusing: {dest} already has files. Pick a new folder.")
    today = ans.get("today") or datetime.date.today().isoformat()
    plus7 = (datetime.date.fromisoformat(today) + datetime.timedelta(days=7)).isoformat()
    school = bool(ans.get("student")) and bool(ans.get("courses"))
    areas = ans.get("areas", [])
    pal = json.loads((REPO / "blueprint" / "palette.json").read_text())
    term = ans.get("term", "Current Term")

    shutil.copytree(TEMPLATE, dest, dirs_exist_ok=True)
    for g in dest.rglob(".gitkeep"): g.unlink()
    (dest / "vault.gitignore").rename(dest / ".gitignore")
    for p in sorted(dest.rglob("*{{TODAY}}*"), key=lambda p: -len(p.parts)):
        p.rename(p.with_name(p.name.replace("{{TODAY}}", today)))

    subs = {
        "USER_NAME": ans.get("name", "Me"), "USER_ROLE": ans.get("role", ""), "TIMEZONE": ans.get("timezone", ""),
        "ANSWER_STYLE": ans.get("answer_style", "Short and direct."), "TODAY": today, "TODAY_PLUS_7": plus7,
        "TERM": term, "VAULT_PATH": str(dest),
        "AREA_LIST": ", ".join(ar["name"] for ar in areas) or "notes",
        "AREA_LINKS_INLINE": "".join(f"[[{ar['name']} MOC|{ar['name']}]] · " for ar in areas),
        "AREA_TABLE_ROWS": "".join(f"| {ar['name']} | {ar.get('description','')} | [[{ar['name']} MOC]] |\n" for ar in areas),
        "AREA_CHAT_SECTIONS": "".join(f"## {ar['name']}\n\n" for ar in areas),
        "COURSE_COLOR_ROWS": "", "COURSE_TABLE_ROWS": "", "CLASS_TABLE_ROWS": "", "LIBRARY_ROWS": "",
    }
    for p in dest.rglob("*"):
        if not p.is_file() or p.suffix not in TEXT or "09 Templates" in p.parts: continue
        t = p.read_text()
        if "{{" not in t and "if:school" not in t and (school or "School" not in t): continue
        if p.suffix == ".md":
            if not school:
                t = re.sub(r"\s*·\s*\[\[(School MOC|School Library)(\|[^\]]*)?\]\]", "", t)
                t = "\n".join(l for l in t.splitlines() if "[[School MOC" not in l and "[[School Library" not in l) + "\n"
                t = "\n".join(l for l in t.splitlines() if "<!-- if:school -->" not in l) + "\n"
            t = t.replace(" <!-- if:school -->", "")
        for k, val in subs.items():
            t = t.replace("{{" + k + "}}", val)
        p.write_text(t)

    for i, ar in enumerate(areas):
        tag = slug(ar["name"])
        (dest / "04 Maps" / f"{ar['name']} MOC.md").write_text(f"""---
type: map
summary: "{ar['name']} hub: {ar.get('description','')}"
created: {today}
tags:
  - map
  - {tag}
---
# {ar['name']} MOC

{ar.get('description','')}

## Active
```dataview
LIST summary
FROM "05 Projects"
WHERE status = "active" AND contains(file.outlinks, this.file.link)
```

## Notes
- 

## AI chats
```dataview
LIST
FROM "11 AI Chats"
WHERE contains(file.outlinks, this.file.link)
SORT file.name DESC
```

← [[Home]]
""")
        css = dest / ".obsidian/snippets/color-coding.css"
        c = pal["area_tag_colors"][i % len(pal["area_tag_colors"])]
        css.write_text(css.read_text().replace("/* Area tags */\n", f"/* Area tags */\n.tag[href=\"#{tag}\"], .cm-hashtag.cm-tag-{tag} {{ --tag-color: {c}; --tag-background: color-mix(in srgb, {c} 15%, transparent); }}\n", 1))
    css = dest / ".obsidian/snippets/color-coding.css"
    css.write_text(re.sub(r'\.tag\[href="#(investing|career|networking|work)"\][^\n]*\n', "", css.read_text()) if areas else css.read_text())

    if school:
        for i, c in enumerate(ans["courses"]):
            p = pal["course_palette"][i % len(pal["course_palette"])]
            add_course(dest, c["code"], c.get("name", ""), term, c.get("days", []), c.get("start", ""), c.get("end", ""),
                       c.get("location", ""), c.get("instructor", ""), c.get("term_start", ""), c.get("term_end", ""),
                       c.get("color") or p["hex"], c.get("color_name") or ("" if c.get("color") else p["name"]))
    else:
        shutil.rmtree(dest / "12 School", ignore_errors=True)
        for rel in ["04 Maps/School MOC.md", "09 Templates/Course.md"]:
            (dest / rel).unlink(missing_ok=True)
    print(f"Built vault at {dest}")

if __name__ == "__main__":
    main()
