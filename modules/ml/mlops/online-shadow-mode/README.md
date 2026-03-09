# Online Shadow Mode

> Track: `ml` | Topic: `mlops`

## Concept

Online shadow mode runs a new model beside the live model on real traffic but serves only the live output, so teams can measure disagreement before rollout.

## Math

$$
\mathrm{disagreement\_rate} = \frac{1}{n} \sum_{i=1}^{n} \mathbf{1}[\hat{y}^{live}_i \ne \hat{y}^{shadow}_i]
$$

- $\hat{y}^{live}_i$ -- prediction from the serving model
- $\hat{y}^{shadow}_i$ -- prediction from the shadow model
- $n$ -- number of mirrored requests

## Key Points

- Shadow mode separates evaluation from user-facing rollout.
- It is useful before canaries when regressions are too risky to expose.
- A disagreement spike is a strong signal to inspect before promotion.

## Function

```python
def shadow_disagreement_rate(
    live_predictions: list[object],
    shadow_predictions: list[object],
) -> tuple[int, float]:
```

## Run tests

```bash
pytest modules/ml/mlops/online-shadow-mode/python -q
```
