# Majority Vote Margin

> Track: `ml` | Topic: `llm`

## Concept

Majority vote margin measures how far the top answer vote share is above the runner-up, which is a simple confidence proxy for repeated decoding.

## Math

For normalized answer counts $c_1 \ge c_2 \ge \dots$ over $N$ samples:

$$
\mathrm{Margin} = \frac{c_1}{N} - \frac{c_2}{N}
$$

If only one unique answer exists, the runner-up share is treated as zero.

## Key Points

- Margin is higher when one answer clearly dominates the vote.
- It complements stability and diversity metrics.
- This module normalizes answers before counting votes.

## Function

```python
def majority_vote_margin(answers: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/majority-vote-margin/python -q
```
