# AI-Whisperers Marketing Strategy

> Complete marketing system for AI automation services

**GitHub:** [Ai-Whisperers/marketing-strategy](https://github.com/Ai-Whisperers/marketing-strategy) (private)  
**Default branch:** `master` · **Active work:** `feature/marketing-assets-update`

---

## Overview

All marketing content lives in **[AI-Whisperers-Marketing-Hub/](AI-Whisperers-Marketing-Hub/)**. This repository also holds Cursor/Claude automation (`.cursor/`, `.claude/`, `scripts/`) and legacy archives (`_archived/`).

See [docs/REPOSITORY.md](docs/REPOSITORY.md) for the full layout, validation commands, and GitHub workflow.

---

## Quick start

| Step | Action |
|------|--------|
| 1 | Clone: `git clone https://github.com/Ai-Whisperers/marketing-strategy.git` |
| 2 | Open [Hub README](AI-Whisperers-Marketing-Hub/README.md) |
| 3 | Run [today's action plan](AI-Whisperers-Marketing-Hub/Strategy/audit/action-plan.md) |
| 4 | Review [ICPs](AI-Whisperers-Marketing-Hub/Audience/personas/) |

---

## Repository layout

```
marketing-strategy/
├── AI-Whisperers-Marketing-Hub/   # Marketing content (single source of truth)
│   ├── Strategy/                    # Brand, positioning, channels, tools, audit
│   ├── Audience/                    # Personas, brand briefs, prospect lists
│   ├── Content/                     # Ready-to-use assets, templates, campaigns
│   ├── Sales/                       # Outreach, playbooks, battle cards
│   ├── Analytics/                   # KPIs, dashboards, CRM guides
│   └── SOURCE-OF-TRUTH/             # Canonical company facts
├── scripts/                         # Ops automation (excalibur, health, validation)
├── mcp-servers/                     # Doc coverage audit (Node)
├── .cursor/                         # Cursor rules, prompts, MCP config
├── .claude/                         # Claude Code commands & triggers
├── agent-tasks/                     # Agent workflow recipes
├── _archived/                       # Legacy root archive (pre-hub migration)
├── docs/                            # Repository & contribution guides
└── *.md                             # Root quick-reference docs
```

---

## Navigation

| Need | Location |
|------|----------|
| Hub home | [AI-Whisperers-Marketing-Hub/README.md](AI-Whisperers-Marketing-Hub/README.md) |
| Today's actions | [Strategy/audit/action-plan.md](AI-Whisperers-Marketing-Hub/Strategy/audit/action-plan.md) |
| Target audiences | [Audience/personas/](AI-Whisperers-Marketing-Hub/Audience/personas/) |
| Ready content | [Content/ready-to-use/](AI-Whisperers-Marketing-Hub/Content/ready-to-use/) |
| Outreach | [Sales/outreach/](AI-Whisperers-Marketing-Hub/Sales/outreach/) |
| Positioning | [Strategy/positioning/](AI-Whisperers-Marketing-Hub/Strategy/positioning/) |
| Brand research | [Audience/brand-briefs/](AI-Whisperers-Marketing-Hub/Audience/brand-briefs/) |
| Project rules | [PROJECT-RULES.md](PROJECT-RULES.md) |
| MCP API keys | [.env.template](.env.template) |

---

## Root reference files

| File | Purpose |
|------|---------|
| [marketing-playbook.md](marketing-playbook.md) | Strategy overview |
| [executive-summary.md](executive-summary.md) | Executive quick reference |
| [improvements-roadmap.md](improvements-roadmap.md) | Planned enhancements |
| [course-catalog.md](course-catalog.md) | Course catalog |
| [PROJECT-RULES.md](PROJECT-RULES.md) | Operating principles |
| [PROJECT-REQUIREMENTS.md](PROJECT-REQUIREMENTS.md) | Requirements baseline |

---

## Tooling & validation

```powershell
# Pre-commit (doc coverage + script syntax)
.\scripts\validate-pre-commit.ps1

# Full Cursor rule/YAML checks (when editing .cursor/)
.\scripts\validate-pre-commit.ps1 -Strict

# Documentation coverage
node .\mcp-servers\doc-coverage-audit.js
```

**MCP (Cursor):** [`.cursor/mcp.json`](.cursor/mcp.json) — enable in Cursor Settings → MCP; keys in [`.env.template`](.env.template).

**Claude Code:** magic commands in [`.claude/triggers.json`](.claude/triggers.json) (`/ops:weekly-health`, `/docs:coverage-audit`, etc.).

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Commits use `[CATEGORY] description` (e.g. `[CONTENT] Add ANDE outreach draft`).

---

## 30-day goals

| Metric | Target |
|--------|--------|
| LinkedIn connections | 500+ |
| Email subscribers | 100–200 |
| Website visitors | 1,000/month |
| Qualified leads | 20–30 |
| Strategy calls | 10–15 |
| New clients | 1–3 |

---

*Last updated: May 2026 · Hub: [AI-Whisperers-Marketing-Hub/](AI-Whisperers-Marketing-Hub/)*
