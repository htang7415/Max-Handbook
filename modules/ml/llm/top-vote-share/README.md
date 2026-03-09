# Top Vote Share

> Track: `ml` | Topic: `llm`

## Concept

Top vote share measures the fraction of normalized votes taken by the most common answer.

## Math

$$
\mathrm{TopVoteShare} = \max_k p_k
$$

- $p_k$ -- vote share of normalized answer $k$

## Key Points

- This is the direct top-answer fraction from repeated decoding.
- It complements vote entropy and majority-vote margin.
- This module normalizes answers before counting votes.

## Function

```python
def top_vote_share(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/top-vote-share/python -q
```
