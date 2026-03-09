# Reciprocal Rank Metric

> Track: `ml` | Topic: `llm`

## Concept

Reciprocal rank measures how early the first relevant result appears for a single query.

## Math

$$
\mathrm{RR} =
\begin{cases}
\frac{1}{r} & \text{if the first relevant item is at rank } r \\
0 & \text{if no relevant item is retrieved}
\end{cases}
$$

## Key Points

- Reciprocal rank is the query-level building block behind MRR.
- It focuses only on the first relevant hit.
- This is useful for inspecting one query before averaging across many.

## Function

```python
def reciprocal_rank(relevance: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/reciprocal-rank-metric/python -q
```
