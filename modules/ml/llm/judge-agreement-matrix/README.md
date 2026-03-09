# Judge Agreement Matrix

> Track: `ml` | Topic: `llm`

## Concept

Judge agreement matrices summarize how often different judges produce the same decision over the same evaluation set.

## Math

For judges $i$ and $j$ over $N$ items:

$$
A_{ij} = \frac{1}{N} \sum_{n=1}^{N} \mathbf{1}[d_{i,n} = d_{j,n}]
$$

- $d_{i,n}$ -- decision from judge $i$ on item $n$

## Key Points

- This is a raw agreement table, not a chance-corrected measure.
- The diagonal is always 1 when at least one item exists.
- This module uses ternary judge outcomes `-1`, `0`, and `1`.

## Function

```python
def judge_agreement_matrix(judge_decisions: list[list[int]]) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/llm/judge-agreement-matrix/python -q
```
