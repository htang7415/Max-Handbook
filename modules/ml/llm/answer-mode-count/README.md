# Answer Mode Count

> Track: `ml` | Topic: `llm`

## Concept

Answer mode count measures how many sampled answers collapse into the largest normalized vote block.

## Math

$$
\mathrm{ModeCount} = \max_k c_k
$$

- $c_k$ -- count of normalized answer $k$

## Key Points

- This is the count version of top-vote share.
- It is useful when raw sample count matters more than proportions.
- This module normalizes answers before counting votes.

## Function

```python
def answer_mode_count(answers: list[str]) -> int:
```

## Run tests

```bash
pytest modules/ml/llm/answer-mode-count/python -q
```
