# Answer Uniqueness Rate

> Track: `ml` | Topic: `llm`

## Concept

Answer uniqueness rate measures what fraction of sampled answers are distinct after normalization.

## Math

$$
\mathrm{UniquenessRate} = \frac{|\mathrm{Unique}(\hat{y}_1, \ldots, \hat{y}_N)|}{N}
$$

- $\hat{y}_i$ -- sampled answer after normalization

## Key Points

- This is a direct diversity-style metric for repeated decoding.
- Higher values mean the sample pool contains more distinct answers.
- This module normalizes answers before counting uniqueness.

## Function

```python
def answer_uniqueness_rate(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/answer-uniqueness-rate/python -q
```
