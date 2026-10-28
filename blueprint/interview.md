# Interview

Ask a few questions at a time, in plain language. Skip what the user already told you. Record answers in `answers.json` (see `answers.example.json`).

## About you
1. What should the vault call you? → `name`
2. One line on what you do (student, analyst, founder…)? → `role`
3. Your time zone? → `timezone`
4. How do you like AI answers: short and direct, detailed, bullet points? → `answer_style`

## Life areas
5. What are the 2–6 big areas of your life you want notes for? Examples: Investing, Career, Clubs, Health, Side projects, Work. → `areas[]` (name + one-line description). Each becomes `04 Maps/<Area> MOC.md`, linked from Home.

## School (skip if not a student)
6. Are you a student right now? → `student`
7. What is this term called (e.g. "Fall 2026")? → `term`
8. For each course: code, name, meeting days (Mon–Sun), start and end time (24-hour `HH:MM`), room, instructor, first and last day of class. → `courses[]`. Pasting a registration table is fine; parse it.
9. Any course color preferences? Otherwise colors come from `palette.json`. → `courses[].color`

## Destination
10. Where should the vault go? Default `~/Documents/<Name>'s Vault`. Must be a new or empty folder.

## Optional
11. Do you want AI chats saved into the vault automatically? If yes, set up `skills/obsidian-chat-capture` after the build.
12. Do you want local version history (Obsidian Git, commits every 30 minutes, nothing uploaded)? Default yes.
