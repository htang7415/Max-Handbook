# Math for ML

ML fundamentals are the minimum math ideas that make model behavior legible.

## Purpose

Use this page to study math in the order that helps models make sense:
- vectors and matrices
- probability and expectation
- information measures
- optimization basics

## First Principles

- Linear algebra describes how data and parameters are represented.
- Probability describes uncertainty, noise, and prediction.
- Information measures compare distributions and representations.
- Optimization explains how parameters move during training.
- You do not need all classical math first; you need the parts that explain modern model behavior.

## Core Math

- Dot product:
  $$
  x^\top y = \sum_i x_i y_i
  $$
- Expectation:
  $$
  \mathbb{E}[X] = \sum_x x p(x)
  $$
- Covariance:
  $$
  \mathrm{Cov}(X, Y) = \mathbb{E}[(X - \mu_X)(Y - \mu_Y)]
  $$
- Gradient descent step:
  $$
  \theta_{t+1} = \theta_t - \eta \nabla_\theta L(\theta_t)
  $$

## Minimal Code Mental Model

```python
score = x @ w
loss = objective(score, target)
grad = gradient(loss, w)
w = w - lr * grad
```

## Canonical Modules

- Linear algebra: `vectors-matrices`, `cosine-similarity`, `pca`, `svd`, `jacobian`, `hessian`
- Probability and statistics: `distributions`, `expectation`, `covariance`, `beta-binomial`, `two-sample-t-test`
- Information measures: `kl-divergence`, `jensen-shannon-divergence`, `mutual-information`
- Optimization basics: `gradient-descent`, `newtons-method`, `convex-vs-nonconvex`

## Supporting Guides

- Math map (`docs/ml/fundamentals/math`)
- Probability map (`docs/ml/fundamentals/prob`)
- Statistics map (`docs/ml/fundamentals/stats`)

## When To Use What

- Start with vectors, expectation, and gradient descent before more advanced topics.
- Use `pca` and `svd` when you need the simplest linear representation story.
- Use `kl-divergence` and related information measures when comparing distributions, objectives, or representations.
- Use the probability and statistics guides when evaluation or uncertainty is the main issue.
