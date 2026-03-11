# Transition Indicators and Masks

Transition indicators turn episode termination state into tensors that control bootstrapping and loss masking.

## Purpose

Use this guide to keep RL transition state in the right order:
- per-transition masks for targets
- numeric indicators for pipelines
- dataset summaries for debugging
- vectorized helpers for batch code

## First Principles

- Bootstrapped targets depend on whether a transition continues.
- Loss masking and target masking are the same structural signal in different code paths.
- Dataset-level fractions help debug data quality but do not replace per-transition masks.
- Transition indicators should be learned as one family before memorizing narrow variants.

## Core Math

- TD target masking:
  $$
  y = r + \gamma (1-d) V(s')
  $$
- Here `d` is the done or terminal indicator controlling whether bootstrapping continues.

## Minimal Code Mental Model

```python
mask = terminal_mask(done_flags)
target = reward + gamma * mask * next_value
fraction = done_fraction(done_flags)
```

## Canonical Modules

- Family module: `transition-indicators`
- Neighboring module: `td-control-methods`

## When To Use What

- Start with `transition-indicators` before narrower done-mask helpers.
- Use terminal masks for TD target logic and bootstrapped returns.
- Use done fractions for replay-buffer diagnostics.
- Use numeric per-transition indicators when the downstream pipeline expects features instead of booleans.
- Pair this guide with `td-control-methods` when learning value targets end to end.
