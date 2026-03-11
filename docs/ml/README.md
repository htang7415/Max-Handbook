# Machine Learning

Use this track to learn the ML stack from first principles without getting buried in low-value variants.

## Purpose

This track is optimized for:
- clear mental models
- enough math to understand why a method works
- enough code to make the idea concrete
- the topics that matter most for AI work in 2026

## First Principles

- Learn ML in this order: concept, math, then code.
- Prefer canonical family modules over narrow variants or old aliases.
- Use docs pages as routing maps and modules as executable learning units.
- Treat classical ML, deep learning, LLMs, and systems as one connected stack rather than separate silos.

## How To Use This Track

- Start with one section, not the whole tree.
- Use section docs for the concept map.
- Use canonical modules for the main learning unit.
- Use alias or narrow modules only after the canonical family is clear.
- Treat `artifacts/deepml/problem_titles.md` as the main scope boundary.

## Math And Code

- Learn each ML topic in this order: intuition, equation, then code.
- Use the equation to understand the quantity being optimized or measured.
- Use the code to see the smallest executable version of that equation.
- If a topic turns into a long catalog of variants, go back to the canonical family first.

```python
# The default ML learning loop in this repo:
concept = understand_problem()
equation = write_core_formula(concept)
code = implement_smallest_working_version(equation)
```

## Start Here

- If your goal is interview prep, use `docs/ml/path-interview`.
- Otherwise, start with `docs/ml/fundamentals`, then move to `docs/ml/data` and `docs/ml/models`.

## Main Sections

- Foundations: `docs/ml/fundamentals`
- Data: `docs/ml/data`
- Models: `docs/ml/models`
- Evaluation: `docs/ml/evaluation`
- Deep learning: `docs/ml/deep-learning`
- LLMs: `docs/ml/llm`
- Systems and MLOps: `docs/ml/systems`, `docs/ml/mlops`
- Reinforcement learning: `docs/ml/reinforcement-learning`
- Generative and representation: `docs/ml/generative`, `docs/ml/representation`
- Computer vision: `docs/ml/computer-vision`

## Canonical Families

- Deep learning: `activation-functions`, `normalization-methods`
- Evaluation: `classification-metrics-core`, `ranking-metrics`, `calibration-metrics`, `uncertainty-intervals`, `agreement-metrics`, `binary-rate-comparison-metrics`
- Data: `scaling-methods`, `categorical-encoding-methods`, `sparse-text-feature-methods`, `structured-feature-methods`, `overflow-metrics`
- LLM: `reasoning-and-test-time-compute`, `long-context-and-caching`, `multimodal-llms`, `decoding-methods`, `retrieval-metrics`, `vote-metrics`
- Production and RL helpers: `capacity-stress-metrics`, `transition-indicators`

## When To Use What

- Use the top-level section docs when you need the next concept family, not the final detail.
- Use canonical family modules before narrow variants or preserved alias pages.
- Add systems and MLOps after you can already choose models, metrics, and core deep-learning tools.
- Treat reinforcement learning, generative models, representation learning, and computer vision as specializations after the main spine is comfortable.

## Scope Rule

- Prefer concise explanations over exhaustive catalogs.
- Prefer canonical families over many near-duplicate modules.
- Only add ML topics outside `problem_titles.md` when they are clearly important to AI practice in 2026.
