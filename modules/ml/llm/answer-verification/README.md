# Answer Verification

> Track: `ml` | Topic: `llm`

## Concept

Answer verification checks whether a predicted answer matches any acceptable reference after lightweight normalization, with optional numeric tolerance.

## Math

$$
\mathrm{verified} =
\begin{cases}
1 & \text{if normalized answers match} \\
1 & \text{if numeric answers are within tolerance} \\
0 & \text{otherwise}
\end{cases}
$$

## Key Points

- This is more flexible than a single exact-match label.
- Numeric equivalence matters for reasoning and calculator-style tasks.
- The module is still intentionally small: it is a verification primitive, not a judge model.

## Function

```python
def verify_answer(prediction: str, references: list[str], numeric_tolerance: float = 1.0e-6) -> bool:
```

## Run tests

```bash
pytest modules/ml/llm/answer-verification/python -q
```
