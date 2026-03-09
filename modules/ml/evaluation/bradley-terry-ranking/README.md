# Bradley-Terry Pairwise Probability

> Track: `ml` | Topic: `evaluation`

## Concept

The Bradley-Terry model assigns each item a latent score and turns score differences into pairwise win probabilities.

## Math

$$P(i \succ j) = \frac{e^{s_i}}{e^{s_i} + e^{s_j}} = \frac{1}{1 + e^{-(s_i - s_j)}}$$

- $s_i$ -- latent score for item $i$
- $s_j$ -- latent score for item $j$
- $P(i \succ j)$ -- probability that item $i$ beats item $j$

## Key Points

- Equal scores imply a win probability of `0.5`.
- Only the score difference matters, not the absolute scale.
- Bradley-Terry is a common bridge from pairwise preferences to a global ranking.

## Function

```python
def bradley_terry_probability(score_a: float, score_b: float) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/bradley-terry-ranking/python -q
```
