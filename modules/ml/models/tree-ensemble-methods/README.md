# Tree and Ensemble Methods

> Track: `ml` | Topic: `models`

## Purpose

Use this module to learn the main tree-based modeling ideas in one place:
single-tree impurity, bagging, boosting, and XGBoost-style split gain.

## First Principles

- A decision tree chooses splits that reduce impurity or loss.
- Bagging reduces variance by training many trees on resampled data.
- Boosting reduces bias by sequentially correcting current mistakes.
- XGBoost extends boosting with a second-order split objective and regularization.

## Core Math

Gini impurity:

$$
\mathrm{Gini} = 1 - \sum_c p_c^2
$$

AdaBoost reweighting:

$$
w_i \leftarrow w_i \cdot \exp\left(\alpha\,\mathbb{I}[y_i \ne \hat{y}_i]\right)
$$

Gradient boosting update:

$$
\hat{y}_i' = \hat{y}_i + \eta h_i
$$

Residual after one boosting step:

$$
r_i' = y_i - \hat{y}_i'
$$

XGBoost split gain:

$$
\mathrm{Gain} = \frac{1}{2}
\left(
\frac{G_L^2}{H_L + \lambda}
+ \frac{G_R^2}{H_R + \lambda}
- \frac{(G_L + G_R)^2}{H_L + H_R + \lambda}
\right) - \gamma
$$

- $p_c$ -- class probability for class $c$
- $\alpha$ -- AdaBoost stage weight
- $\mathbb{I}[y_i \ne \hat{y}_i]$ -- indicator that example $i$ was misclassified
- $\eta$ -- learning rate for the boosting step
- $G_L, G_R$ -- summed gradients for left and right child nodes
- $H_L, H_R$ -- summed Hessians for left and right child nodes
- $\lambda$ -- leaf-weight regularization
- $\gamma$ -- split penalty

## From Math To Code

- Trees score a candidate split from class probabilities and impurity.
- Bagging resamples indices.
- Boosting changes either example weights or stage-wise residual predictions.

## Minimal Code Mental Model

```python
probs = class_probabilities(labels)
impurity = gini_impurity(labels)
bagged = bootstrap_indices(n=100, seed=0)
weights = update_weights(weights, errors, alpha=0.7)
updated, residuals = gradient_boosting_step(targets, predictions, weak_learner_output, learning_rate=0.1)
residuals = boosting_residuals(targets, updated)
gain = split_gain(left_grad, left_hess, right_grad, right_hess, lambda_reg=1.0, gamma=0.0)
```

## Functions

```python
def class_probabilities(labels: list[int]) -> list[float]:
def gini_impurity(labels: list[int]) -> float:
def bootstrap_indices(n: int, seed: int = 0) -> list[int]:
def update_weights(weights: list[float], errors: list[int], alpha: float) -> list[float]:
def boosting_residuals(targets: list[float], predictions: list[float]) -> list[float]:
def gradient_boosting_step(
    targets: list[float],
    predictions: list[float],
    weak_learner_output: list[float],
    learning_rate: float,
) -> tuple[list[float], list[float]]:
def split_gain(
    left_grad: float,
    left_hess: float,
    right_grad: float,
    right_hess: float,
    lambda_reg: float,
    gamma: float,
) -> float:
```

## When To Use What

- Use `gini_impurity` when learning how a single decision tree scores candidate splits.
- Use `bootstrap_indices` when learning why random forests reduce variance through bagging.
- Use `update_weights` when learning how AdaBoost emphasizes errors.
- Use `gradient_boosting_step` when learning stage-wise residual fitting.
- Use `split_gain` when learning why XGBoost chooses one split over another under regularization.

## Run tests

```bash
pytest modules/ml/models/tree-ensemble-methods/python -q
```
