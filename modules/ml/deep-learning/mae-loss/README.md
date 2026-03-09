# Mean Absolute Error

> Track: `ml` | Topic: `deep-learning`

## Concept

Mean absolute error penalizes prediction errors by their absolute size. It grows
linearly with the residual, so it is less sensitive to outliers than MSE.

## Math

$$\mathrm{MAE} = \frac{1}{n}\sum_i |y_i - \hat{y}_i|$$

- $\mathrm{MAE}$ -- mean absolute error
- $y_i$ -- i-th target value
- $\hat{y}_i$ -- i-th prediction
- $n$ -- number of samples
- $i$ -- index

## Key Points

- MAE weights all residual magnitudes linearly.
- It is more robust to outliers than MSE.
- The absolute value introduces a non-differentiable point at zero residual.

## Function

```python
def mae(y: list[float], y_hat: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/mae-loss/python -q
```
