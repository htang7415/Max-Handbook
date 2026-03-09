# End Of Episode Mask

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

End-of-episode masks convert done flags into numeric indicators that are 1 for terminal transitions and 0 otherwise.

## Math

$$
m_i = d_i
$$

- $d_i$ -- terminal indicator, 1 if the transition ends the episode
- $m_i$ -- mask used when explicitly selecting terminal transitions

## Key Points

- This is the terminal-side counterpart to continuation masks.
- It is useful when logging or masking terminal-only updates.
- This module returns floats for direct multiplication in vectorized code.

## Function

```python
def end_of_episode_mask(done_flags: list[bool]) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/end-of-episode-mask/python -q
```
