# Nonterminal Fraction

> Track: `ml` | Topic: `reinforcement-learning`

## Concept

Nonterminal fraction measures what share of transitions continue the episode rather than ending it.

## Math

$$
\mathrm{NonterminalFraction} = \frac{\sum_{i=1}^{N} \mathbf{1}[\neg d_i]}{N}
$$

- $d_i$ -- done flag for transition $i$

## Key Points

- This is a descriptive batch statistic for how often bootstrap terms stay active.
- It complements terminal-mask style primitives.
- This module returns the fraction of `False` done flags.

## Function

```python
def nonterminal_fraction(done_flags: list[bool]) -> float:
```

## Run tests

```bash
pytest modules/ml/reinforcement-learning/nonterminal-fraction/python -q
```
