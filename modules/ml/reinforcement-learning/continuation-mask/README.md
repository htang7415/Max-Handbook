# Continuation Mask

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Continuation masks convert done flags into numeric masks that are 1 for continuing transitions and 0 for terminal ones.

## Math

$$
m_i = 1 - d_i
$$

- $d_i$ -- terminal indicator, 1 if the transition ends the episode
- $m_i$ -- continuation mask used in vectorized bootstrap equations

## Key Points

- This is a small implementation primitive for RL training loops.
- It is equivalent to a nonterminal mask but named from the continuation perspective.
- This module returns floats for direct multiplication in target formulas.

## Function

```python
def continuation_mask(done_flags: list[bool]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/continuation-mask/python -q
```
