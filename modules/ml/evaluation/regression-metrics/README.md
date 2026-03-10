# Regression Metrics

> Track: `ml` | Topic: `evaluation`

## Purpose

Use this module for the small set of regression metrics that matter most in practice:
absolute error, squared error, and explained variance.

## First Principles

- Regression metrics compare predicted numbers against target numbers.
- MAE keeps the original error scale and is less sensitive to outliers.
- MSE squares errors, so large misses matter more.
- $R^2$ asks how much better the model is than always predicting the mean.

## Core Math

$$
\mathrm{MAE} = \frac{1}{n}\sum_i |y_i - \hat y_i|,
\quad
\mathrm{MSE} = \frac{1}{n}\sum_i (y_i - \hat y_i)^2
$$

$$
R^2 = 1 - \frac{\sum_i (y_i - \hat y_i)^2}{\sum_i (y_i - \bar y)^2}
$$

## Minimal Code Mental Model

```python
mae, mse = mae_mse(y_true, y_pred)
score = r2_score(y_true, y_pred)
```

## Function

```python
def mae_mse(y_true: list[float], y_pred: list[float]) -> tuple[float, float]:
def r2_score(y_true: list[float], y_pred: list[float]) -> float:
```

## When To Use What

- Use MAE when you want a direct average error scale.
- Use MSE when large misses should be penalized more heavily.
- Use $R^2$ when you want a normalized regression summary relative to a mean baseline.

## Run tests

```bash
pytest modules/ml/evaluation/regression-metrics/python -q
```
