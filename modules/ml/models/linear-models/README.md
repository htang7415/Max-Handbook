# Linear Models

> Track: `ml` | Topic: `models`

## Purpose

Use this module to compare the main linear-model family:
linear regression, logistic regression, softmax regression, and elastic-net regularization.

## First Principles

- Linear regression predicts a number from an affine function.
- Logistic regression turns the affine score into a binary probability with a sigmoid.
- Softmax regression generalizes that probability view to multiple classes.
- Elastic Net keeps the same linear core but changes the penalty to balance sparsity and stability.

## Core Math

$$
\hat y = w^\top x + b
$$

$$
p(y=1 \mid x) = \sigma(w^\top x + b),
\quad
p_i = \frac{e^{z_i}}{\sum_j e^{z_j}}
$$

## Minimal Code Mental Model

```python
score = linear_predict(x, w, b)
prob = logistic_predict_proba(x, w, b)
probs = softmax_probabilities(logits)
```

## Function

```python
def linear_predict(x: list[float], w: list[float], b: float) -> float:
def logistic_predict_proba(x: list[float], w: list[float], b: float) -> float:
def softmax_probabilities(logits: list[float]) -> list[float]:
def elastic_net_penalty(weights: list[float], l1: float, l2: float) -> float:
```

## When To Use What

- Use linear regression for fast numerical prediction baselines.
- Use logistic regression for binary classification.
- Use softmax regression for multiclass linear classification.
- Use Elastic Net when you want a linear model with both shrinkage and sparsity pressure.

## Run tests

```bash
pytest modules/ml/models/linear-models/python -q
```
