# Agreement Rate

> Track: `ml` | Topic: `evaluation`

## Concept

Agreement rate measures the fraction of repeated labels or judge decisions that match the most common outcome.

## Math

$$
\mathrm{AgreementRate} = \frac{\max_k c_k}{N}
$$

- $c_k$ -- count of outcome $k$
- $N$ -- number of labels or decisions

## Key Points

- This is the raw agreement baseline before chance correction like Cohen kappa.
- It is useful for quick judge-consistency summaries.
- The module reports modal agreement over a set of repeated outcomes.

## Function

```python
def agreement_rate(outcomes: list[str | int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/agreement-rate/python -q
```
