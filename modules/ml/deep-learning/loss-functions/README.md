# Loss Functions

> Track: `ml` | Topic: `deep-learning`

## Purpose

Use this module to compare the core loss families that matter in modern ML:
classification losses, regression losses, and robust losses.

## First Principles

- A loss tells the model what kind of error matters.
- Cross-entropy is the default classification loss because it rewards correct probability mass.
- Focal loss is a variant of cross-entropy for imbalanced classification with many easy examples.
- Hinge loss is margin-based rather than probability-based.
- MSE, MAE, RMSE, and Huber are regression-style losses that differ mainly in how strongly they punish large residuals.

## Core Math

$$
L_{\text{CE}} = -\log p_{\text{target}},
\quad
L_{\text{focal}} = -(1-p)^\gamma \log p
$$

$$
L_{\text{hinge}} = \max(0, 1-y \cdot s)
$$

$$
\mathrm{MAE} = \frac{1}{n}\sum_i |y_i-\hat y_i|,
\quad
\mathrm{MSE} = \frac{1}{n}\sum_i (y_i-\hat y_i)^2
$$

## Minimal Code Mental Model

```python
ce = cross_entropy(logits, target)
reg = mse(y_true, y_pred)
robust = huber(y_true_scalar, y_pred_scalar, delta=1.0)
```

## Function

```python
def cross_entropy(logits: list[float], target: int) -> float:
def focal_loss(p: float, gamma: float = 2.0) -> float:
def hinge_loss(score: float, label: int) -> float:
def huber(y: float, y_hat: float, delta: float = 1.0) -> float:
def mae(y: list[float], y_hat: list[float]) -> float:
def mse(y: list[float], y_hat: list[float]) -> float:
def rmse(y: list[float], y_hat: list[float]) -> float:
```

## When To Use What

- Use cross-entropy for most classification setups.
- Use focal loss when class imbalance creates many easy negatives.
- Use hinge loss when you want a margin-based classifier rather than calibrated probabilities.
- Use MSE for standard regression, MAE for more outlier robustness, RMSE when you want the error back on the original scale, and Huber when you want a smooth compromise.

## Run tests

```bash
pytest modules/ml/deep-learning/loss-functions/python -q
```
