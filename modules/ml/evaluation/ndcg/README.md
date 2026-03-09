# NDCG

> Track: `ml` | Topic: `evaluation`

## Concept

Normalized discounted cumulative gain (NDCG) measures ranking quality while giving higher weight to relevant items that appear earlier in the list.

## Math

$$
\mathrm{DCG@}k = \sum_{i=1}^{k} \frac{2^{rel_i} - 1}{\log_2(i + 1)}
$$

$$
\mathrm{NDCG@}k = \frac{\mathrm{DCG@}k}{\mathrm{IDCG@}k}
$$

- $rel_i$ -- graded relevance at rank $i$
- $\mathrm{IDCG@}k$ -- DCG of the ideal ranking

## Key Points

- NDCG supports graded relevance, not just binary hits.
- Early relevant items matter more because of the logarithmic discount.
- This is a natural complement to MRR and Recall@k.

## Function

```python
def ndcg_at_k(relevance: list[float], k: int) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/ndcg/python -q
```
