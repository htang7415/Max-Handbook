# Rerank Gain

> Track: `ml` | Topic: `llm`

## Concept

Rerank gain measures how much a reranker improves the first relevant hit compared with the baseline ranking.

## Math

$$
\mathrm{gain} = \mathrm{RR}_{\mathrm{reranked}} - \mathrm{RR}_{\mathrm{baseline}}
$$

- $\mathrm{RR}$ -- reciprocal rank of the first relevant item

## Key Points

- Positive gain means the reranker moved a relevant item earlier.
- This is a single-query primitive for analyzing reranker value.
- It complements aggregate metrics like MRR and Recall@k.

## Function

```python
def rerank_gain(baseline_relevance: list[int], reranked_relevance: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/rerank-gain/python -q
```
