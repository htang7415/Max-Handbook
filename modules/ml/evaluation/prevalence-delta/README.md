# Prevalence Delta

> Track: `ml` | Topic: `evaluation`

## Concept

Prevalence delta measures the signed change in positive rate from a baseline group to a comparison group.

## Math

$$
\Delta = p_{\mathrm{comparison}} - p_{\mathrm{baseline}}
$$

- $p_{\mathrm{baseline}}$ -- positive rate of the baseline group
- $p_{\mathrm{comparison}}$ -- positive rate of the comparison group

## Key Points

- The sign tells you whether prevalence increased or decreased.
- This is a directional version of a base-rate comparison.
- This module expects binary labels only.

## Function

```python
def prevalence_delta(baseline_labels: list[int], comparison_labels: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/prevalence-delta/python -q
```
