# Mean Reciprocal Rank

> Track: `ml` | Topic: `evaluation`

## Concept

Mean reciprocal rank (MRR) measures how early the first relevant item appears across multiple ranked queries.

## Math

$$
\mathrm{MRR} = \frac{1}{Q} \sum_{q=1}^{Q} \frac{1}{\mathrm{rank}_q}
$$

- $Q$ -- number of queries
- $\mathrm{rank}_q$ -- rank of the first relevant result for query $q$

## Key Points

- MRR focuses only on the first relevant hit.
- It is useful for retrieval and ranking tasks where early precision matters.
- This complements Recall@k, which measures coverage instead of early rank.

## Function

```python
def mean_reciprocal_rank(relevance_lists: list[list[int]]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/mean-reciprocal-rank/python -q
```
