# Episode End Rate

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Episode end rate measures what fraction of transitions terminate the episode.

## Math

$$
\mathrm{EpisodeEndRate} = \frac{\sum_{i=1}^{N} \mathbf{1}[d_i]}{N}
$$

- $d_i$ -- done flag for transition $i$

## Key Points

- This is the complement of nonterminal fraction.
- It is a simple batch summary for how often bootstrap terms are turned off.
- This module returns the fraction of `True` done flags.

## Function

```python
def episode_end_rate(done_flags: list[bool]) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/episode-end-rate/python -q
```
