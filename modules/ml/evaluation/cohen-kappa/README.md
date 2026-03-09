# Cohen Kappa

> Track: `ml` | Topic: `evaluation`

## Concept

Cohen kappa measures annotator or model agreement after discounting the amount of agreement expected by chance.

## Math

$$
\kappa = \frac{p_o - p_e}{1 - p_e}
$$

- $p_o$ -- observed agreement from the diagonal of the confusion matrix
- $p_e$ -- expected agreement from row and column marginals

## Key Points

- Raw accuracy overstates agreement when one class dominates.
- Kappa is common for comparing labelers or classifiers against human labels.
- This module computes kappa from a square confusion matrix.

## Function

```python
def cohen_kappa(confusion_matrix: list[list[int]]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/cohen-kappa/python -q
```
