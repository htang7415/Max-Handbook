# Terminal Mask

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Terminal masks convert done flags into numeric masks so bootstrap terms can be multiplied away for terminal transitions.

## Math

$$
m_i = 1 - d_i
$$

- $d_i$ -- terminal indicator, 1 if the transition ends the episode
- $m_i$ -- nonterminal mask used in bootstrap equations

## Key Points

- Terminal masks are a small but common RL implementation primitive.
- They make bootstrap equations easy to vectorize.
- This module maps booleans to `1.0` for nonterminal and `0.0` for terminal.

## Function

```python
def terminal_mask(done_flags: list[bool]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/terminal-mask/python -q
```
