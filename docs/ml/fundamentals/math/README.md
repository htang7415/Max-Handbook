# Math Foundations for ML

Math connects model behavior to geometry, curvature, and optimization.

## Purpose

Use this guide to route the small set of math ideas that make ML models legible:
- linear maps and geometry
- low-rank structure
- local sensitivity and curvature
- optimization steps and conditioning

## First Principles

- Linear algebra is the language of features, parameters, and layers.
- Jacobians and Hessians explain how outputs change locally and why optimization can be unstable.
- PCA and SVD explain compressed structure and directional variance.
- Optimization math matters when it clarifies training behavior, not as a separate memorization task.

## Core Math

- Linear map:
  $$
  y = Ax
  $$
- Matrix factorization:
  $$
  A = U \Sigma V^\top
  $$
- Gradient step:
  $$
  \theta_{t+1} = \theta_t - \eta \nabla L(\theta_t)
  $$

## Minimal Code Mental Model

```python
projection = x @ w
u, s, v_t = svd(matrix)
w = w - lr * grad
```

## Canonical Modules

- Linear structure: `vectors-matrices`, `cosine-similarity`
- Sensitivity and curvature: `jacobian`, `hessian`
- Low-rank structure: `pca`, `svd`
- Optimization basics: `gradient-descent`, `newtons-method`, `convex-vs-nonconvex`

## When To Use What

- Start with `vectors-matrices` and `gradient-descent`.
- Use `jacobian` and `hessian` when local sensitivity or curvature is the main question.
- Use `pca` and `svd` when dimensionality reduction or compressed structure matters.
- Use `convex-vs-nonconvex` when reasoning about optimizer behavior rather than model architecture.
