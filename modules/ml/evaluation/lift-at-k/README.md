# Lift At K

> Track: `ml` | Topic: `evaluation`

## Concept

Lift@k measures how much more concentrated positives are in the top-ranked prefix than in the full population.

## Math

$$
\mathrm{Lift@k} = \frac{\mathrm{Precision@k}}{\mathrm{BaseRate}}
$$

$$
\mathrm{Precision@k} = \frac{\sum_{i=1}^{k} y_i}{k}, \quad \mathrm{BaseRate} = \frac{\sum_{i=1}^{N} y_i}{N}
$$

- $y_i \in \{0,1\}$ -- relevance label in ranked order

## Key Points

- Lift@k is useful for ranking, targeting, and retrieval scenarios.
- A value above 1 means the top of the ranking is denser in positives than random sampling.
- This module operates on one ranked list of binary labels.

## Function

```python
def lift_at_k(labels: list[int], k: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/lift-at-k/python -q
```
