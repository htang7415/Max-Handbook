# Retrieval Recall@k

> Track: `ml` | Topic: `llm`

## Concept

Retrieval Recall@k measures how many relevant documents appear within the top-k retrieved results.

## Math

$$
\mathrm{Recall@}k = \frac{|\mathrm{TopK} \cap \mathrm{Relevant}|}{|\mathrm{Relevant}|}
$$

- $\mathrm{TopK}$ -- set of retrieved documents in the first $k$ positions
- $\mathrm{Relevant}$ -- set of relevant documents

## Key Points

- Recall@k asks coverage, not ranking quality among retrieved items.
- It is especially useful when multiple relevant passages exist.
- This metric complements reranker metrics and reciprocal-rank style scores.

## Function

```python
def retrieval_recall_at_k(retrieved_ids: list[str], relevant_ids: set[str], k: int) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/retrieval-recall-at-k/python -q
```
