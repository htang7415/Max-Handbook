# Learning Rate Schedules

> Track: `ml` | Topic: `optimization`

## Purpose

Use this module to compare the main learning-rate schedules used in modern training:
constant, decay-based, warmup-based, cosine-based, and one-cycle schedules.

## First Principles

- The optimizer says how to update.
- The learning-rate schedule says how large the update should be over time.
- Warmup stabilizes the earliest steps.
- Decay reduces step size as training progresses.
- Cosine and one-cycle schedules are common modern defaults because they are smooth and easy to tune.

## Core Math

$$
\eta_t = \eta_0,\quad
\eta_t = \eta_0 \gamma^{\lfloor t/s \rfloor},\quad
\eta_t = \eta_0 e^{-kt}
$$

$$
\eta_t = \eta_0 \frac{1 + \cos(\pi t / T)}{2}
$$

## Minimal Code Mental Model

```python
lr = warmup_cosine_lr(base_lr=1e-3, step=200, warmup_steps=100, total_steps=1000)
peak = one_cycle_lr(max_lr=1e-2, step=50, total_steps=500)
```

## Function

```python
def constant_lr(lr: float) -> float:
def step_decay(lr: float, step: int, gamma: float, t: int) -> float:
def exp_decay(lr: float, k: float, t: float) -> float:
def cosine_decay(lr: float, t: int, t_max: int) -> float:
def warmup_lr(lr: float, t: int, warmup_steps: int) -> float:
def cosine_restart_lr(base_lr: float, step: int, cycle_length: int) -> float:
def warmup_cosine_lr(base_lr: float, step: int, warmup_steps: int, total_steps: int) -> float:
def one_cycle_lr(max_lr: float, step: int, total_steps: int, pct_start: float = 0.3, div_factor: float = 25.0, final_div_factor: float = 1.0e4) -> float:
```

## When To Use What

- Use constant LR only as a baseline or for very simple settings.
- Use step or exponential decay when you want a simple monotone schedule.
- Use warmup when early steps are unstable.
- Use cosine or warmup-plus-cosine as strong defaults for modern deep learning.
- Use one-cycle when you want a short training run with aggressive exploration and strong annealing.

## Run tests

```bash
pytest modules/ml/optimization/learning-rate-schedules/python -q
```
