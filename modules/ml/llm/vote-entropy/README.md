# Vote Entropy

> Track: `ml` | Topic: `llm`

## Concept

Vote entropy measures how spread out normalized answer votes are across distinct responses.

## Math

For vote shares $p_1, \ldots, p_K$:

$$
H = -\sum_{k=1}^{K} p_k \log p_k
$$

## Key Points

- Vote entropy is low when one answer dominates and high when votes are diffuse.
- It complements majority-vote margin and answer stability.
- This module normalizes answers before counting votes.

## Function

```python
def vote_entropy(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/vote-entropy/python -q
```
