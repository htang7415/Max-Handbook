# Risk Ratio

> Track: `ml` | Topic: `evaluation`

## Concept

Risk ratio compares two binary positive rates multiplicatively, often under the baseline/exposed naming convention.

## Math

$$
\mathrm{RiskRatio} = \frac{p_{\mathrm{exposed}}}{p_{\mathrm{baseline}}}
$$

- $p_{\mathrm{exposed}}$ -- positive rate of the exposed or treatment group
- $p_{\mathrm{baseline}}$ -- positive rate of the baseline or control group

## Key Points

- This is another common name for multiplicative prevalence comparison.
- A value above 1 means the exposed group has a higher positive rate.
- This module treats a zero baseline rate as infinite when the exposed rate is positive.

## Function

```python
def risk_ratio(exposed_labels: list[int], baseline_labels: list[int]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/risk-ratio/python -q
```
