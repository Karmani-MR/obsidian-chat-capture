---
type: skill
summary: Check links, orphans, summaries and secrets; report, don't fix.
tags: [skill, agent]
---
# Skill - Vault Health

Check links, orphans, summaries and secrets; report, don't fix.

## Steps
Run `python3 scripts/verify_vault.py <vault>` from the blueprint repo if available, otherwise check: broken links, notes with no inbound links, notes missing `summary`, possible secrets. Write the report to `01 Fleeting/AI Drafts/YYYY-MM-DD - Vault Health.md`.

## Rules
Follow [[AGENTS]]. Append, don't overwrite. List every note touched.

Back to [[AI Agent MOC]]
