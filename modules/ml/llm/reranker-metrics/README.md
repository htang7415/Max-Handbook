# Reranker Metrics

> Track: `ml` | Topic: `llm`

## Concept

Reranking evaluation checks whether relevant items move to the top of a ranked list after a retrieval or scoring stage.

## Math

$$\mathrm{MRR@}k = \frac{1}{r_1} \quad \text{if a relevant item appears within top-}k$$

$$\mathrm{Recall@}k = \frac{\text{relevant items in top-}k}{\text{total relevant items}}$$

- $r_1$ -- rank of the first relevant item
- $k$ -- cutoff rank

## Key Points

- MRR emphasizes how early the first relevant result appears.
- Recall@k captures coverage of relevant results, not just the first hit.
- This module evaluates one ranked list at a time.

## Function

```python
def reranker_metrics(relevance: list[int], k: int) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/llm/reranker-metrics/python -q
```
