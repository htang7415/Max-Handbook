# Answer Stability

> Track: `ml` | Topic: `llm`

## Concept

Answer stability measures how often repeated samples normalize to the same answer instead of drifting across runs.

## Math

For answer counts $c_1, \ldots, c_K$ over $N$ samples, this module uses pairwise agreement:

$$
\mathrm{Stability} = \frac{\sum_{k=1}^{K} c_k(c_k - 1)}{N(N - 1)}
$$

## Key Points

- Stability captures repeatability across repeated decoding attempts.
- It complements candidate diversity and self-consistency voting.
- This module normalizes answers before computing agreement.

## Function

```python
def answer_stability(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/answer-stability/python -q
```
