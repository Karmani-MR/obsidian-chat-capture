#!/usr/bin/env python3
"""Build a new vault from vault-template/ and an answers file.

Usage:
  python3 scripts/build_vault.py --answers my-answers.json --dest "~/Documents/My Vault"

answers.json shape: see blueprint/answers.example.json.
Refuses to write into a folder that already has files. Standard library only.
"""
import argparse, datetime, json, pathlib, re, shutil, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from new_course import add_course

REPO = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = REPO / "vault-template"

def main():
    a = argparse.ArgumentParser(); a.add_argument("--answers", required=True); a.add_argument("--dest", required=True)
    x = a.parse_args()
    ans = json.loads(pathlib.Path(x.answers).expanduser().read_text())
    dest = pathlib.Path(x.dest).expanduser()
    if dest.exists() and any(dest.iterdir()):
        sys.exit(f"Refusing: {dest} already has files. Pick a new folder.")
    today = ans.get("today") or datetime.date.today().isoformat()
    plus7 = (datetime.date.fromisoformat(today) + datetime.timedelta(days=7)).isoformat()
    school = bool(ans.get("student")) and bool(ans.get("courses"))
    areas = ans.get("areas", [])
    palette = json.loads((REPO / "blueprint" / "palette.json").read_text())["course_palette"]

    shutil.copytree(TEMPLATE, dest, dirs_exist_ok=True)
    for g in dest.rglob(".gitkeep"):
        g.unlink()
    if (dest / "vault.gitignore").exists():
        (dest / "vault.gitignore").rename(dest / ".gitignore")

    subs = {
        "USER_NAME": ans.get("name", "Me"), "USER_ROLE": ans.get("role", ""), "TIMEZONE": ans.get("timezone", ""),
        "ANSWER_STYLE": ans.get("answer_style", "Short and direct."), "TODAY": today, "TODAY_PLUS_7": plus7,
        "TERM": ans.get("term", "Current Term"),
        "AREA_LIST": ", ".join(ar["name"] for ar in areas) or "—",
        "AREA_MOC_LINKS": "\n".join(f"- [[{ar['name']} MOC]] — {ar.get('description','')}" for ar in areas),
        "AREA_CHAT_SECTIONS": "\n\n".join(f"## {ar['name']}" for ar in areas),
        "COURSE_COLOR_ROWS": "", "COURSE_TABLE_ROWS": "",
    }
    # rename files whose names contain placeholders
    for p in sorted(dest.rglob("*{{*}}*"), key=lambda p: -len(p.parts)):
        p.rename(p.with_name(p.name.replace("{{TODAY}}", today)))
    for p in dest.rglob("*.md"):
        if "09 Templates" in p.parts:
            continue
        t = p.read_text()
        for k, v in subs.items():
            t = t.replace("{{" + k + "}}", v)
        if not school:
            t = "\n".join(l for l in t.splitlines() if "<!-- if:school -->" not in l) + "\n"
        t = t.replace(" <!-- if:school -->", "")
        p.write_text(t)

    # Area MOCs
    for ar in areas:
        (dest / "04 Maps" / f"{ar['name']} MOC.md").write_text(
            f"---\ntype: map\nsummary: Hub for {ar['name']}. {ar.get('description','')}\ntags: [map]\n---\n# {ar['name']} MOC\n\n"
            f"{ar.get('description','')}\n\n## Notes\n- \n\n## Projects\n```dataview\nLIST FROM \"05 Projects\" WHERE contains(file.outlinks, this.file.link)\n```\n\nBack to [[Home]]\n")

    if school:
        term = ans.get("term", "Current Term")
        for i, c in enumerate(ans["courses"]):
            add_course(dest, c["code"], c["name"], term, c.get("days", []), c.get("start", ""), c.get("end", ""),
                       c.get("location", ""), c.get("instructor", ""), c.get("term_start", ""), c.get("term_end", ""),
                       c.get("color") or palette[i % len(palette)])
    else:
        shutil.rmtree(dest / "12 School", ignore_errors=True)
        (dest / "04 Maps" / "School MOC.md").unlink(missing_ok=True)
        for n in ["Add Course", "Retire Course"]:
            (dest / "00 Home" / "Agent" / "Skills" / f"Skill - {n}.md").unlink(missing_ok=True)
        moc = dest / "04 Maps" / "AI Agent MOC.md"
        moc.write_text("\n".join(l for l in moc.read_text().splitlines() if "Add Course" not in l and "Retire Course" not in l) + "\n")
        for course_tpl in ["Course Hub", "Course Materials", "Course Prep"]:
            (dest / "09 Templates" / f"{course_tpl}.md").unlink(missing_ok=True)
    print(f"Built vault at {dest}")

if __name__ == "__main__":
    main()
