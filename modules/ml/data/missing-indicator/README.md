# Missing-Value Indicators

> Track: `ml` | Topic: `data`

## Concept

Missing-value indicators preserve the information that a feature was absent, even after imputation fills the numeric value itself.

## Math

$$m_{ij} = \mathbb{I}[x_{ij} = \varnothing]$$

- $m_{ij}$ -- missingness indicator for row $i$, column $j$
- $x_{ij}$ -- original feature value
- $\varnothing$ -- missing value marker

## Key Points

- Missingness can carry predictive signal.
- Indicator features are often paired with mean or median imputation.
- This module returns the indicator matrix only, not the imputed values.

## Function

```python
def missing_indicators(table: list[list[float | None]]) -> list[list[int]]:
```

## Run tests

```bash
pytest modules/ml/data/missing-indicator/python -q
```
