# Answer Frequency Table

> Track: `ml` | Topic: `llm`

## Concept

Answer frequency tables count how often each normalized answer appears across repeated samples.

## Math

For normalized answers $\hat{y}_1, \ldots, \hat{y}_N$, this module returns counts $c_k$ for each unique normalized answer.

## Key Points

- Frequency tables are a useful primitive before deriving vote shares or entropy.
- They make repeated-decoding ambiguity directly inspectable.
- This module normalizes answers before counting.

## Function

```python
def answer_frequency_table(answers: list[str]) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/ml/llm/answer-frequency-table/python -q
```
