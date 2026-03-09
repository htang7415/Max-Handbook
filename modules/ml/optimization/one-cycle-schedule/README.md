# One-Cycle Schedule

> Track: `ml` | Topic: `optimization`

## Concept

The one-cycle schedule ramps learning rate up to a peak, then anneals it down to a very small final value within a single training run.

## Math

$$
\mathrm{lr}(t) =
\begin{cases}
\text{linear increase} & \text{during the up phase} \\
\text{cosine decay} & \text{during the down phase}
\end{cases}
$$

## Key Points

- One-cycle combines aggressive exploration early with strong annealing late.
- It is usually parameterized by a peak learning rate and a warmup fraction.
- This module focuses only on the learning-rate schedule, not momentum coupling.

## Function

```python
def one_cycle_lr(
    max_lr: float,
    step: int,
    total_steps: int,
    pct_start: float = 0.3,
    div_factor: float = 25.0,
    final_div_factor: float = 1.0e4,
) -> float:
```

## Run tests

```bash
pytest modules/ml/optimization/one-cycle-schedule/python -q
```
