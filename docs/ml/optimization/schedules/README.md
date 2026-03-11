# Learning Rate Schedules

Schedules shape how aggressively optimization explores early and settles late.

## Purpose

Use this guide to choose the right schedule family:
- constant and monotone decay
- warmup
- cosine-style annealing
- one-cycle and restart patterns

## First Principles

- The optimizer defines the update rule; the schedule defines how large the updates should be over time.
- Warmup exists because the earliest steps are often the least stable.
- Decay exists because late training usually benefits from smaller steps.
- Smooth schedules are easier to tune than brittle hand-crafted piecewise jumps.

## Core Math

- Step decay and exponential decay shrink the base learning rate over time.
- Cosine schedules use a smooth annealing curve:
  $$
  \eta_t = \eta_0 \frac{1 + \cos(\pi t / T)}{2}
  $$

## Minimal Code Mental Model

```python
warm = warmup_factor(t=20, warmup_steps=100)
decay = cosine_decay_factor(t=200, t_max=1000)
lr = warmup_cosine_lr(base_lr=1e-3, step=200, warmup_steps=100, total_steps=1000)
```

## Canonical Modules

- Family module: `learning-rate-schedules`

## When To Use What

- Start with `learning-rate-schedules` for the family overview.
- Use monotone decay when you want a simple conservative schedule.
- Use warmup when early-step instability is the main issue.
- Use cosine or warmup-plus-cosine as strong modern defaults.
- Use one-cycle when you want an aggressive short-run schedule with strong annealing.
