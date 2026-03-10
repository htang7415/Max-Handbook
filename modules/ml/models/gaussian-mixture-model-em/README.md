# Gaussian Mixture Model EM Step

> Track: `ml` | Topic: `models`

## Purpose

Use this module to understand how EM fits a Gaussian mixture with soft cluster
assignments.

## First Principles

- A Gaussian mixture models data as a weighted sum of Gaussian components.
- The E-step computes soft responsibilities for each point and component.
- The M-step updates weights, means, and variances from those responsibilities.
- EM is a local optimization method, so initialization matters.

## Core Math

$$
r_{ik} = \frac{\pi_k \, \mathcal{N}(x_i \mid \mu_k, \sigma_k^2)}{\sum_{j=1}^{K} \pi_j \, \mathcal{N}(x_i \mid \mu_j, \sigma_j^2)}
$$

$$
\mu_k' = \frac{\sum_i r_{ik} x_i}{\sum_i r_{ik}}
$$

$$
\sigma_k^{2\prime} = \frac{\sum_i r_{ik}(x_i-\mu_k')^2}{\sum_i r_{ik}}
$$

$$
\pi_k' = \frac{1}{n}\sum_i r_{ik}
$$

- $r_{ik}$ -- responsibility of component $k$ for point $i$
- $\pi_k$ -- mixture weight of component $k$
- $\mu_k$ -- mean of component $k$
- $\sigma_k^2$ -- variance of component $k$
- $K$ -- number of components

## From Math To Code

- The E-step computes one responsibility vector per data point.
- The M-step turns those soft assignments into updated weights, means, and variances.

## Minimal Code Mental Model

```python
resp = responsibilities_1d(data, weights, means, variances)
weights, means, variances = em_step_1d(data, weights, means, variances)
```

## Function

```python
def responsibilities_1d(
    data: list[float],
    weights: list[float],
    means: list[float],
    variances: list[float],
) -> list[list[float]]:
def em_step_1d(
    data: list[float],
    weights: list[float],
    means: list[float],
    variances: list[float],
) -> tuple[list[float], list[float], list[float]]:
```

## When To Use What

- Use GMMs when clusters are soft or overlapping rather than hard-separated.
- Use EM when latent assignments are hidden but the likelihood is tractable.
- Pair this with BIC/AIC or kernel-PCA ideas when model selection or nonlinearity becomes the next question.

## Run tests

```bash
pytest modules/ml/models/gaussian-mixture-model-em/python -q
```
