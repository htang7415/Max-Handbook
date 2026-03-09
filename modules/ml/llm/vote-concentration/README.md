# Vote Concentration

> Track: `ml` | Topic: `llm`

## Concept

Vote concentration measures how much of the total vote mass sits on the single most common normalized answer.

## Math

$$
\mathrm{VoteConcentration} = \max_k p_k
$$

- $p_k$ -- vote share for normalized answer $k$

## Key Points

- Vote concentration is the complement to more diffuse vote-entropy style metrics.
- High concentration means one answer dominates the sample pool.
- This module normalizes answers before counting votes.

## Function

```python
def vote_concentration(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/vote-concentration/python -q
```
