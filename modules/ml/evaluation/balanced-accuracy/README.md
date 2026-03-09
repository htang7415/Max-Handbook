# Balanced Accuracy

> Track: `ml` | Topic: `evaluation`

## Concept

Balanced accuracy averages recall across classes so common classes do not dominate the score.

## Math

$$
\mathrm{BalancedAccuracy} = \frac{1}{C} \sum_{c=1}^{C} \frac{TP_c}{TP_c + FN_c}
$$

- $C$ -- number of classes
- $TP_c$ -- true positives for class $c$
- $FN_c$ -- false negatives for class $c$

## Key Points

- Balanced accuracy is useful under class imbalance.
- Each class contributes equally through its recall.
- This module computes the score from per-class recall counts.

## Function

```python
def balanced_accuracy(true_positives: list[int], false_negatives: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/balanced-accuracy/python -q
```
