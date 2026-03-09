# DeLong Test

> Track: `ml` | Topic: `evaluation`

## Concept

The DeLong test compares two ROC-AUC values measured on the same labeled examples and estimates whether the difference is larger than expected from sampling noise.

## Math

$$
z = \frac{\mathrm{AUC}_A - \mathrm{AUC}_B}{\sqrt{\widehat{\mathrm{Var}}(\mathrm{AUC}_A - \mathrm{AUC}_B)}}
$$

- $\mathrm{AUC}_A, \mathrm{AUC}_B$ -- paired AUC values for two models
- $\widehat{\mathrm{Var}}(\cdot)$ -- DeLong variance estimate from positive and negative structural components

## Key Points

- This is a paired significance test for AUC, not a new ranking metric.
- Shared examples matter; treating the two AUC values as independent overstates uncertainty.
- The module uses the classic positive-vs-negative pair comparison view of AUC.

## Function

```python
def delong_auc_test(
    labels: list[int],
    scores_a: list[float],
    scores_b: list[float],
) -> DeLongResult:
```

## Run tests

```bash
pytest modules/ml/evaluation/delong-test/python -q
```
