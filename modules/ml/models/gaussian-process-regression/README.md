# Gaussian Process Regression

> Track: `ml` | Topic: `models`

## Purpose

Use this module to understand how kernel similarity turns into both a
predictive mean and an uncertainty estimate.

## First Principles

- A GP assumes similar inputs should often produce similar outputs.
- The kernel matrix is the data structure that stores that similarity.
- Prediction is a weighted combination of observed targets.
- Uncertainty is part of the output, not an extra afterthought.

## Core Math

$$k(x,x') = \exp\left(-\frac{\lVert x-x' \rVert^2}{2\ell^2}\right)$$

$$\mu_* = K_*^{\top}(K + \sigma_n^2 I)^{-1} y,\quad \Sigma_* = K_{**} - K_*^{\top}(K + \sigma_n^2 I)^{-1} K_*$$

$$
\alpha = (K + \sigma_n^2 I)^{-1} y
$$

- $k(x, x')$ -- kernel measuring similarity between inputs
- $\ell$ -- kernel length scale
- $K$ -- training-training kernel matrix
- $K_*$ -- training-test kernel matrix
- $K_{**}$ -- test-test kernel matrix
- $\sigma_n^2$ -- observation noise variance
- $y$ -- observed training targets
- $\mu_*$ -- predictive mean
- $\Sigma_*$ -- predictive covariance

## From Math To Code

- Build the training kernel matrix.
- Add noise to the diagonal.
- Solve for posterior weights $\alpha$.
- Reuse those weights to form predictions at test points.

## Minimal Code Mental Model

```python
alpha = gp_posterior_weights(x_train, y_train, length_scale=1.0, noise=0.1)
mean, var = gp_posterior_predict(x_train, y_train, x_test, length_scale=1.0, noise=0.1)
```

## Function

```python
def gp_posterior_weights(
    x_train: list[list[float]],
    y_train: list[float],
    length_scale: float,
    noise: float,
) -> list[float]:
def gp_posterior_predict(
    x_train: list[list[float]],
    y_train: list[float],
    x_test: list[list[float]],
    length_scale: float,
    noise: float,
) -> tuple[list[float], list[float]]:
```

## When To Use What

- Use `gp_posterior_weights` when you want to see the actual linear solve behind GPR.
- Use `gp_posterior_predict` when you want both predictive means and variances.

## Run tests

```bash
pytest modules/ml/models/gaussian-process-regression/python -q
```
