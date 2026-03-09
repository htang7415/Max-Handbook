# PR-AUC

> Track: `ml` | Topic: `evaluation`

## Concept

PR-AUC summarizes the precision-recall tradeoff, which is often more informative than ROC-AUC when positives are rare.

## Math

For sampled precision-recall points, this module uses trapezoidal interpolation:

$$
\mathrm{PR\text{-}AUC} \approx \sum_{i=2}^{N} (r_i - r_{i-1}) \frac{p_i + p_{i-1}}{2}
$$

- $r_i$ -- recall at point $i$
- $p_i$ -- precision at point $i$

## Key Points

- PR-AUC focuses attention on positive-class retrieval quality.
- It is especially useful for imbalanced classification.
- This module expects recall to be sorted from low to high.

## Function

```python
def pr_auc(recall: list[float], precision: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/pr-auc/python -q
```
