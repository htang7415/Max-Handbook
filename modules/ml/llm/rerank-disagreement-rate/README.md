# Rerank Disagreement Rate

> Track: `ml` | Topic: `llm`

## Concept

Rerank disagreement rate measures how often the reranked list differs from the baseline list at each position.

## Math

$$
\mathrm{disagreement\_rate} = \frac{1}{k} \sum_{i=1}^{k} \mathbf{1}[b_i \ne r_i]
$$

- $b_i$ -- document at position $i$ in the baseline ranking
- $r_i$ -- document at position $i$ in the reranked output
- $k$ -- number of compared positions

## Key Points

- This summarizes how aggressive the reranker is.
- A high disagreement rate means the reranker is rewriting much of the baseline order.
- This complements rerank gain, which looks at relevance improvement instead of pure ordering change.

## Function

```python
def rerank_disagreement_rate(baseline_ids: list[str], reranked_ids: list[str], k: int | None = None) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/rerank-disagreement-rate/python -q
```
