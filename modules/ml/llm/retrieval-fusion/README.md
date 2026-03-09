# Weighted Retrieval Fusion

> Track: `ml` | Topic: `llm`

## Concept

Retrieval fusion combines signals from multiple retrievers, such as sparse BM25 and dense embeddings, into one final ranking.

## Math

$$s(d) = \alpha s_{\mathrm{sparse}}(d) + (1 - \alpha) s_{\mathrm{dense}}(d)$$

- $s(d)$ -- fused score for document $d$
- \alpha -- sparse-score weight
- $s_{\mathrm{sparse}}(d)$ -- sparse retrieval score
- $s_{\mathrm{dense}}(d)$ -- dense retrieval score

## Key Points

- Fusion can recover documents that either retriever alone would miss.
- This simple weighted sum assumes the component scores are already on comparable scales.
- More advanced variants include reciprocal-rank fusion and learned rerankers.

## Function

```python
def weighted_retrieval_fusion(
    sparse_scores: dict[str, float],
    dense_scores: dict[str, float],
    alpha: float = 0.5,
) -> list[tuple[str, float]]:
```

## Run tests

```bash
pytest modules/ml/llm/retrieval-fusion/python -q
```
