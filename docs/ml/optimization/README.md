# Optimization and Training Dynamics

Optimization is about turning gradients into stable parameter updates.

## Purpose

Use this page to keep optimization in three layers:
- choose an update rule
- choose a learning-rate schedule
- add stability tools only when training becomes numerically fragile

## First Principles

- The optimizer decides the update direction and how much gradient history to remember.
- The schedule decides how step size changes over time.
- Stability tools are not substitutes for a bad optimizer or bad data; they are safeguards.

## Core Math

Most optimization questions reduce to:
$$
w_{t+1} = w_t - \eta_t \cdot \text{update}_t
$$

- `update_t` comes from the optimizer.
- `\eta_t` comes from the schedule.

## Minimal Code Mental Model

```python
lr = warmup_cosine_lr(base_lr, step, warmup_steps, total_steps)
w, m, v = adamw_step(w, grad, m, v, lr, wd, beta1, beta2, eps)
```

## Canonical Modules

- Optimizers: `optimizer-methods`
- Learning-rate schedules: `learning-rate-schedules`
- Schedule guide: `docs/ml/optimization/schedules`

## Supporting Modules

- Stability tools: `gradient-clipping`, `loss-scaling`, `detect-nans`
- Specialized optimizer intuition: `muon-optimizer`

## When To Use What

- Start with the optimizer family before comparing single update rules one by one.
- Start with the schedule family before memorizing individual decay variants.
- Add clipping, loss scaling, or NaN detection only when the training loop is unstable.
