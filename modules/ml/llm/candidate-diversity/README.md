# Candidate Diversity

> Track: `ml` | Topic: `llm`

## Concept

Candidate diversity measures how much variety appears across multiple sampled answers instead of only checking whether the top answer is correct.

## Math

$$
\mathrm{Diversity} = \frac{|\mathrm{Unique}(\hat{y}_1, \ldots, \hat{y}_n)|}{n}
$$

- $\hat{y}_i$ -- a sampled candidate answer
- $n$ -- number of sampled candidates

## Key Points

- Diversity is useful when comparing decoding settings or self-consistency pools.
- Higher diversity means the sample set explores more distinct answers.
- This module uses normalized string uniqueness as a simple diversity proxy.

## Function

```python
def candidate_diversity(candidates: list[str]) -> float:
```

## Run tests

```bash
pytest modules/ml/llm/candidate-diversity/python -q
```
