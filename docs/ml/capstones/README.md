# Capstones

Use ML capstones to combine modeling, evaluation, serving, and rollout decisions into one engineering workflow.

## Purpose

Capstones are for practicing the full ML decision path:
- define the behavior
- choose the metric and baseline
- evaluate quality and calibration
- check serving cost and latency
- decide ship, hold, or rollback

## First Principles

- A capstone should connect the offline metric to the production decision.
- The release gate should fail closed when quality, calibration, latency, cost, or regression risk is unclear.
- LLM systems should treat retrieval quality, judge quality, and serving constraints as first-class model behavior.

## Canonical Modules

- `llm-eval-serving-gate`

## When To Use What

- Use `llm-eval-serving-gate` after LLM evaluation, calibration, and inference-serving basics are clear.
- Add more capstones only when they combine several canonical families into one production-shaped decision.
- Prefer one dense capstone over many narrow scenario modules.
