# Answer Repeat Rate

> Track: `ml` | Topic: `llm`

## Concept

Answer repeat rate measures the share of sampled answers that are repeats after normalization.

## Math

$$
\mathrm{RepeatRate} = 1 - \frac{|\mathrm{Unique}(\hat{y}_1, \ldots, \hat{y}_N)|}{N}
$$

- $\hat{y}_i$ -- normalized sampled answer

## Key Points

- This is the complement of answer uniqueness rate.
- Higher repeat rate means more answers collapse to the same normalized responses.
- This module normalizes answers before counting uniqueness.

## Function

```python
def answer_repeat_rate(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/answer-repeat-rate/python -q
```
