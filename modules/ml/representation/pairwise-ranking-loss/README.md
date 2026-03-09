# Pairwise Ranking Loss

> Track: `ml` | Topic: `representation`

## Concept

Pairwise ranking loss trains a model to score a preferred item above a rejected item.

## Math

$$
\mathcal{L} = \log \left(1 + e^{-(s^+ - s^-)}\right)
$$

- $s^+$ -- score of the preferred item
- $s^-$ -- score of the rejected item

## Key Points

- The loss is small when the preferred item already scores higher.
- This is a simple bridge from preference pairs to learned ranking signals.
- Variants of this idea appear in recommender systems, reranking, and alignment.

## Function

```python
def pairwise_logistic_loss(preferred_score: float, rejected_score: float) -> float:
```

## Run tests

```bash
pytest modules/ml/representation/pairwise-ranking-loss/python -q
```
