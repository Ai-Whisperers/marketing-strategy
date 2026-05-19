# Repository guide

**Remote:** https://github.com/Ai-Whisperers/marketing-strategy  
**Organization:** [Ai-Whisperers](https://github.com/Ai-Whisperers)

---

## Branches

| Branch | Purpose |
|--------|---------|
| `master` | Stable marketing hub snapshot |
| `feature/*` | Active campaigns, assets, tooling updates |

Create feature branches from `master` and open PRs into `master` when ready.

---

## What belongs where

| Path | Contents |
|------|----------|
| `AI-Whisperers-Marketing-Hub/` | All marketing strategy, content, sales, and analytics assets |
| `AI-Whisperers-Marketing-Hub/_archived/` | Deprecated hub content (do not delete; reference only) |
| `_archived/` (repo root) | Legacy folders from pre-hub layout; superseded by hub structure |
| `.cursor/` | Cursor rules, prompts, quality scripts (shared engineering standards) |
| `.claude/` | Claude Code settings, triggers, slash commands |
| `scripts/` | PowerShell ops scripts invoked by Claude triggers |
| `mcp-servers/` | Node utilities (documentation coverage audit) |
| `agent-tasks/` | Reusable agent workflow definitions |
| `project-todos/` | Generated GitHub org todo snapshots (gitignored except README) |
| `logs/` | Generated reports (gitignored) |
| `docs/` | Repository meta-documentation (this file, contributing) |

Do not add new marketing markdown at repo root except quick-reference summaries listed in the root README.

---

## Local setup

1. Clone the repository and `cd` into it.
2. Copy `.env.template` to `.env` (local only; never commit).
3. Optional: `npm install` if you add Node dependencies later.
4. Authenticate GitHub CLI for ops scripts: `gh auth login`.

---

## Validation

| Command | When |
|---------|------|
| `.\scripts\validate-pre-commit.ps1` | Before every commit |
| `.\scripts\validate-pre-commit.ps1 -Strict` | After editing `.cursor/rules` or prompts |
| `node .\mcp-servers\doc-coverage-audit.js` | After README or hub structure changes |

Optional: add `.github/workflows/marketing-validate.yml` to run validation on push/PR (requires GitHub token with `workflow` scope).

---

## Ops scripts (Claude / manual)

| Script | Purpose |
|--------|---------|
| `scripts/excalibur-command.ps1` | Sync org issues → `project-todos/` |
| `scripts/weekly-activity-report.ps1` | Weekly repo health report → `logs/` |
| `scripts/dependency-tracker.ps1` | Dependency manifest inventory |
| `scripts/azure-devops-sync.ps1` | ADO sync plan (dry-run) |
| `scripts/todo-manager.ps1` | Todo status / sync |

---

## GitHub integration

- **Issues & PRs:** use the [marketing-strategy](https://github.com/Ai-Whisperers/marketing-strategy) repo.
- **Org automation:** set `$env:GITHUB_ORG = 'Ai-Whisperers'` (or `AI-Whisperers` per your org slug) before running excalibur/weekly-health scripts.
- **MCP GitHub server:** set `GITHUB_PERSONAL_ACCESS_TOKEN` for Cursor MCP tools.

---

## Ignored paths (not committed)

See `.gitignore`: `.env`, `logs/`, `.specstory/`, `.venv/`, `node_modules/`, generated `project-todos/*.md`, dependency reports.
