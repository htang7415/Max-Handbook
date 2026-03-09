# Token Budgeting

> Track: `ml` | Topic: `data`

## Concept

Token budgeting clips segment lengths to fit within a fixed maximum, which is useful for prompt construction and length-capped feature pipelines.

## Math

For ordered segments with requested lengths $l_i$ and remaining budget $b_i$:

$$
\tilde{l}_i = \min(l_i, b_i)
$$

$$
b_{i+1} = b_i - \tilde{l}_i
$$

## Key Points

- Earlier segments keep priority when the budget is exhausted.
- The module returns both allocated tokens and the dropped overflow.
- This is a budgeting primitive, not a tokenizer.

## Function

```python
def budget_token_segments(segment_lengths: list[int], max_tokens: int) -> tuple[list[int], int]:
```

## Run tests

```bash
pytest modules/ml/data/token-budgeting/python -q
```
