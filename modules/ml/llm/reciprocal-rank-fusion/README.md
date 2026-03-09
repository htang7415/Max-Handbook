# Reciprocal Rank Fusion

> Track: `ml` | Topic: `llm`

## Concept

Reciprocal rank fusion (RRF) combines ranked lists by rewarding documents that appear near the top of multiple rankings, even when raw scores are not comparable.

## Math

$$
\mathrm{RRF}(d) = \sum_{r \in \mathcal{R}} \frac{1}{k + \mathrm{rank}_r(d)}
$$

- $\mathcal{R}$ -- set of ranked lists
- $\mathrm{rank}_r(d)$ -- 1-based rank of document $d$ in list $r$
- $k$ -- smoothing constant that controls how sharply top ranks dominate

## Key Points

- RRF works on ranks, not raw similarity scores.
- It is often more robust than weighted score fusion when retriever scales differ.
- The same document gains strength by appearing in multiple lists.

## Function

```python
def reciprocal_rank_fusion(rankings: list[list[str]], k: int = 60) -> list[tuple[str, float]]:
```

## Run tests

```bash
pytest modules/ml/llm/reciprocal-rank-fusion/python -q
```
