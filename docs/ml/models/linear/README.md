# Linear Models

Linear models are the baseline family for prediction, calibration, and interpretation.

## Purpose

Use this guide to keep linear methods in one mental model:
- regression and classification from affine scores
- regularization and sparsity
- margin intuition
- when linear baselines are already enough

## First Principles

- Linear models win when the representation is already good.
- The core object is an affine score; the task changes how that score is interpreted.
- Regularization changes generalization behavior more than it changes the model family.
- Strong feature engineering often matters more than adding model complexity.

## Core Math

- Affine score:
  $$
  z = w^\top x + b
  $$
- Binary probability:
  $$
  p(y=1 \mid x) = \sigma(z)
  $$
- Margin intuition:
  $$
  y(w^\top x + b)
  $$

## Minimal Code Mental Model

```python
score = linear_predict(x, w, b)
prob = logistic_predict_proba(x, w, b)
penalty = elastic_net_penalty(weights, l1=0.1, l2=0.1)
```

## Canonical Modules

- Family module: `linear-models`
- Supporting module: `svm-pegasos`

## When To Use What

- Start with `linear-models` for the main regression/classification family.
- Use `svm-pegasos` when margin intuition is the main teaching goal.
- Prefer linear baselines before larger model families when data is limited or interpretability matters.
- Add polynomial or interaction features before abandoning the linear family on structured data.
