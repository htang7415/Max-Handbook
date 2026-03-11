# Max Handbook

This repository powers the Max Handbook website. The `web/` app renders the notes
in `docs/` and the labs in `modules/` into a browseable site.

## Website overview

```
max-handbook/
  docs/          # Concept notes (website-ready)
  modules/       # Concept labs — one idea + minimal code + tiny test
  web/           # Next.js website (TypeScript, Vercel-deployable)
```

The website reads content from these folders:

- `docs/` for short concept notes
- `modules/` for runnable labs (Python by default; Rust optional)

## Tracks

| Track | Path prefix |
|-------|-------------|
| Data Structures & Algorithms | `dsa/` |
| Machine Learning (incl. LLM, RL) | `ml/` |
| AI Agents | `ai-agents/` |
| Databases | `databases/` |
| Software Engineering | `software-engineering/` |

## Run the site locally

Prerequisites:

- Node.js 18+
- `pnpm`

From the repo root:

```bash
cd web
pnpm install
pnpm --filter @max-handbook/site dev
```

For deployment details, see `web/README.md`.

## Content workflow

The website picks up changes from `docs/` and `modules/`. If you add a new
module, keep the folder naming and layout consistent so the content indexer can
find it. See `CONTRIBUTING.md` for naming rules and conventions.

## Site

The site is deployed from the `web/` workspace on Vercel.

## License

[MIT](LICENSE)
