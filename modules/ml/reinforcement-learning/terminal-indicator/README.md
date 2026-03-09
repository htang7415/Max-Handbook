# Terminal Indicator

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Terminal indicators convert a single done flag into a scalar numeric indicator.

## Math

$$
i = d
$$

- $d$ -- terminal indicator, 1 if the transition ends the episode

## Key Points

- This is a scalar helper for code paths that need a numeric terminal flag.
- It is the single-value analogue of end-of-episode masks.
- This module returns `1.0` for terminal and `0.0` otherwise.

## Function

```python
def terminal_indicator(done: bool) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/terminal-indicator/python -q
```
