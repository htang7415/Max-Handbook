# Transition Indicators

> Track: `ml` | Topic: `reinforcement-learning`

## Purpose

Use this module to convert done-state information into masks and simple summary
signals for RL targets and batched updates.

## First Principles

- Done-state logic decides whether future value should be bootstrapped.
- Masks are the most important form because they directly zero or keep the bootstrap term.
- Fractions are useful for rollout diagnostics.
- Numeric indicators exist mostly because vectorized RL code prefers tensors over booleans.

## Core Math

- Terminal indicator:
  $$
  \mathbf{1}[\text{done}]
  $$
- Continuation mask:
  $$
  1 - \mathbf{1}[\text{done}]
  $$
- Done fraction:
  $$
  \frac{1}{N}\sum_{i=1}^{N}\mathbf{1}[\text{done}_i]
  $$

## Minimal Code Mental Model

```python
mask = terminal_mask(done_flags)
done_rate = done_fraction(done_flags)
```

## Function

```python
def terminal_mask(done_flags: list[bool]) -> list[float]:
def continuation_mask(done_flags: list[bool]) -> list[float]:
def end_of_episode_mask(done_flags: list[bool]) -> list[float]:
def done_fraction(done_flags: list[bool]) -> float:
def episode_end_rate(done_flags: list[bool]) -> float:
def terminal_indicator(done: bool) -> float:
def nonterminal_indicator(done: bool) -> float:
def continuing_transition_batch(done_flags: list[bool]) -> list[float]:
def persistent_transition_batch(done_flags: list[bool]) -> list[float]:
def resilient_transition_batch(done_flags: list[bool]) -> list[float]:
```

## When To Use What

- Use terminal or continuation masks in TD targets and return computation.
- Use done fraction for replay-buffer or rollout health summaries.
- Use numeric indicators when the downstream code expects tensors instead of booleans.
- Keep these helpers simple; they should clarify bootstrapping logic, not hide it.

## Run tests

```bash
pytest modules/ml/reinforcement-learning/transition-indicators/python -q
```
