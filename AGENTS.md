# Code Lab — AGENTS.md

## What this repo is
Code Lab is a learning-first repo with:
- `docs/`  : concise concept notes (website-ready)
- `modules/`: compact learning modules with code and focused tests
- `web/`   : TypeScript Next.js site that renders repo content (Vercel deploy)

## Non-negotiable workflow
- **Run tests one module at a time.** Do NOT default to “run all tests”.
- Prefer **small, incremental edits** and keep everything easy to learn.
- Keep **structure and naming consistent** so content can be indexed for the website.

## Folder conventions
- Folder names: **kebab-case** (e.g., `prefix-sum`, `attention-causal`)
- Python files: **snake_case.py**

### Module layout
```
modules/<track>/<subtopic>/<slug>/
  README.md
  python/<name>.py
  python/test_<name>.py
  rust/ (optional)
    Cargo.toml
    src/lib.rs
    tests/<name>_test.rs
```

## How to run (one target)
### Python
Run pytest in the target folder:
```bash
pytest modules/<...>/python -q
```

### Rust
Run cargo test for the single crate:
```bash
cargo test --manifest-path modules/<...>/rust/Cargo.toml
```

### Web (Next.js)
```bash
cd web
pnpm install
pnpm --filter @codelab/site dev
```

## Adding new content
### Add a module (concept lab)
- Goal: teach **one** idea (short README + minimal code + tiny test).
- Use the repo template/script if available, otherwise copy an existing module and rename.

### ML authoring policy
- For the `ml` track, prefer **one coherent learning unit** over overly fragmented one-formula modules.
- A good ML module may cover a **concept family** when people naturally learn the ideas together.
  Examples: activation functions, normalization methods, decoding methods, calibration metrics.
- Keep separate modules only when the mental model, implementation pattern, or failure mode is clearly different.
  Examples: PCA, GMM-EM, backpropagation, PPO, KV cache.
- Do **not** create a new ML module for a narrow metric or variant if it adds little intuition beyond an existing family module.
- Avoid duplicate ML modules. Before adding a new module, check whether the idea is already covered by:
  - an existing canonical family module
  - a near-duplicate slug with only naming differences
  - a docs guide that should be expanded instead of creating a new module
- If a topic is already covered, prefer one of these actions instead of adding a duplicate:
  - improve the existing module
  - merge related narrow modules into a denser canonical module
  - add cross-links, aliases, or redirects for discoverability
- Only add a separate ML module when it contributes at least one of:
  - a distinct mental model
  - a distinct implementation pattern
  - a distinct failure mode
  - a materially better learning path
- For ML docs and modules, optimize for **concise and clear learning**, not exhaustive coverage.
- Start from **first principles** whenever possible:
  - what problem this concept solves
  - the minimum useful math
  - the minimum useful code shape
  - when to use it
- Avoid heavy ML pages that read like flat catalogs of metrics, variants, or historical trivia.
- Prefer a small number of important ideas over long lists of narrow siblings.
- For each ML topic, cover the **most important concepts for the current AI era** rather than trying to preserve every older idea.
- Treat `artifacts/deepml/problem_titles.md` as the primary scope boundary for ML coverage work.
- Do not add ML topics outside `problem_titles.md` unless they are clearly important for AI practice in 2026.
- When selecting what to emphasize, bias toward topics that matter most for modern AI workflows in 2026:
  - LLMs and evaluation
  - deep learning fundamentals that still matter in practice
  - inference and systems
  - modern optimization and training patterns
  - classical ML concepts that remain foundational
- Dense ML modules are encouraged when they stay easy to scan. A strong ML module usually includes:
  - purpose
  - first-principles intuition
  - compact math
  - compact code
  - grouped formulas or a comparison table when useful
  - trade-offs or failure modes
  - links to the canonical neighboring modules
  - one focused test file for the family
- Dense ML docs should usually follow a teaching-first shape:
  - Purpose
  - First Principles
  - Core Math
  - Minimal Code Mental Model
  - Canonical Modules
  - When To Use What
- For the ML track, avoid dedicated `Pitfalls` or `Common Mistakes` sections in docs unless a topic is unusually error-prone.
- Prefer folding warnings into:
  - First Principles
  - When To Use What
  - short inline cautions near the relevant concept
- Use `docs/` to provide the system map and comparisons. Use `modules/` to provide the smallest **useful** learning unit, which may be larger than a single formula.
- If consolidating existing ML modules, preserve URL stability. Prefer redirects or compatibility handling over breaking slugs.

## Website sync rule
- The website should NOT duplicate source content.
- If a change affects URL stability, prefer adding redirects rather than renaming slugs.

## Editing guidelines
- Keep docs short and correct.
- Avoid new dependencies unless clearly necessary.
- Prefer clarity over clever optimizations.
