# Contributing

Thank you for improving the AI-Whisperers marketing repository.

**Repository:** https://github.com/Ai-Whisperers/marketing-strategy

---

## Before you start

1. Read [PROJECT-RULES.md](PROJECT-RULES.md) and [AI-Whisperers-Marketing-Hub/README.md](AI-Whisperers-Marketing-Hub/README.md).
2. Place new marketing files under `AI-Whisperers-Marketing-Hub/` in the correct function folder (`Strategy`, `Audience`, `Content`, `Sales`, `Analytics`).
3. Use language suffixes: `-es.md` (primary), `-en.md` when needed.
4. Date-stamp time-sensitive assets: `YYYY-MM-DD-name-es.md`.

---

## Workflow

```bash
git checkout master
git pull origin master
git checkout -b feature/your-topic
# edit, then:
.\scripts\validate-pre-commit.ps1
git add -A
git commit -m "[CATEGORY] Brief description"
git push -u origin feature/your-topic
```

Open a pull request to `master` on GitHub.

---

## Commit message format

```
[CATEGORY] Imperative description

Optional body with context.
```

**Categories:** `CONTENT`, `STRATEGY`, `SALES`, `AUDIENCE`, `ANALYTICS`, `DOCS`, `TOOLING`, `ARCHIVE`

Examples:

- `[CONTENT] Add LinkedIn draft for ANDE campaign`
- `[TOOLING] Wire doc coverage audit into pre-commit`
- `[ARCHIVE] Move superseded briefs to _archived`

---

## Validation

All commits should pass:

```powershell
.\scripts\validate-pre-commit.ps1
```

Use `-Strict` when changing `.cursor/rules` or YAML prompt collections.

---

## Archives

- Outdated hub content → `AI-Whisperers-Marketing-Hub/_archived/`
- Legacy root folders → `_archived/` at repo root (reference only)
- Do not delete historical assets without team agreement

---

## Secrets

Never commit `.env`, API keys, tokens, or personal prospect data exports. Use `.env.template` as the key catalog only.
