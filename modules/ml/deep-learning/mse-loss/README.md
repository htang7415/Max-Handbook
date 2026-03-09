# Mean Squared Error

> Track: `ml` | Topic: `deep-learning`

## Concept

Mean squared error penalizes prediction errors quadratically. Larger mistakes are
punished disproportionately more than smaller ones, which makes MSE sensitive
to outliers but smooth and easy to optimize.

## Math

$$\mathrm{MSE} = \frac{1}{n}\sum_i (y_i - \hat{y}_i)^2$$

- $\mathrm{MSE}$ -- mean squared error
- $y_i$ -- i-th target value
- $\hat{y}_i$ -- i-th prediction
- $n$ -- number of samples
- $i$ -- index

## Key Points

- Squaring makes all errors non-negative and emphasizes large deviations.
- MSE is the standard loss for least-squares regression.
- The derivative grows linearly with the residual, which gives smooth gradients.

## Function

```python
def mse(y: list[float], y_hat: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/deep-learning/mse-loss/python -q
```
