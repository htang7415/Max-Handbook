# Retrieval Fusion Methods

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to compare the two main ways to combine retrieval signals:
weighted score fusion and reciprocal-rank fusion.

## First Principles

- Retrieval fusion combines evidence from multiple retrievers into one ranking.
- Weighted fusion assumes the scores are already on comparable scales.
- Reciprocal-rank fusion ignores raw scores and uses only ranking positions.
- Rank-based fusion is often more robust when sparse and dense retrievers have very different score ranges.

## Core Math

Weighted score fusion:

$$
s(d) = \alpha s_{\text{sparse}}(d) + (1-\alpha)s_{\text{dense}}(d)
$$

Reciprocal-rank fusion:

$$
\mathrm{RRF}(d) = \sum_{r \in \mathcal{R}} \frac{1}{k + \mathrm{rank}_r(d)}
$$

## Minimal Code Mental Model

```python
weighted = weighted_retrieval_fusion(sparse_scores, dense_scores, alpha=0.5)
rrf = reciprocal_rank_fusion(rankings, k=60)
```

## Function

```python
def weighted_retrieval_fusion(sparse_scores: dict[str, float], dense_scores: dict[str, float], alpha: float = 0.5) -> list[tuple[str, float]]:
def reciprocal_rank_fusion(rankings: list[list[str]], k: int = 60) -> list[tuple[str, float]]:
```

## When To Use What

- Use weighted fusion when sparse and dense scores are calibrated enough to average directly.
- Use reciprocal-rank fusion when retriever score scales are not comparable.

## Run tests

```bash
pytest modules/ml/llm/retrieval-fusion-methods/python -q
```
