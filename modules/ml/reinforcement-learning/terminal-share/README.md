# Terminal Share

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Terminal share measures the fraction of transitions that end an episode.

## Math

$$
\mathrm{TerminalShare} = \frac{\sum_{i=1}^{N} \mathbf{1}[d_i]}{N}
$$

- $d_i$ -- done flag for transition $i$

## Key Points

- This is another naming convention for episode-end rate.
- It is useful as a quick batch summary of terminal transitions.
- This module returns the fraction of `True` done flags.

## Function

```python
def terminal_share(done_flags: list[bool]) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/terminal-share/python -q
```
