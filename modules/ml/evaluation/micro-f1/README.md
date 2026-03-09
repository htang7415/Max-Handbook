# Micro F1

> Track: `ml` | Topic: `evaluation`

## Concept

Micro F1 aggregates true positives, false positives, and false negatives across classes before computing one global F1 score.

## Math

$$
\mathrm{MicroF1} = \frac{2TP}{2TP + FP + FN}
$$

- $TP$ -- total true positives across classes
- $FP$ -- total false positives across classes
- $FN$ -- total false negatives across classes

## Key Points

- Micro F1 is dominated more by frequent classes than macro F1.
- It is useful when overall label-level performance matters most.
- This module takes per-class counts and aggregates them first.

## Function

```python
def micro_f1_score(
    true_positives: list[int],
    false_positives: list[int],
    false_negatives: list[int],
) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/micro-f1/python -q
```
