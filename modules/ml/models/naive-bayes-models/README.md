# Naive Bayes Models

> Track: `ml` | Topic: `models`

## Purpose

Use this module to compare the two Naive Bayes variants worth remembering:
Gaussian Naive Bayes for continuous features and Bernoulli Naive Bayes for binary features.

## First Principles

- Naive Bayes assumes conditional independence across features.
- The model family differs mainly in the feature likelihood:
  Gaussian for continuous values, Bernoulli for binary indicators.
- In practice, the decision often comes from the feature type, not from complex tuning.

## Core Math

$$
p(x \mid y) = \prod_i \mathcal{N}(x_i; \mu_i, \sigma_i^2)
$$

$$
p(x \mid y) = \prod_i p_i^{x_i}(1-p_i)^{1-x_i}
$$

## Minimal Code Mental Model

```python
g = gaussian_log_likelihood(x, mean, var)
b = bernoulli_log_likelihood(binary_x, prob)
```

## Function

```python
def gaussian_log_likelihood(x: list[float], mean: list[float], var: list[float]) -> float:
def bernoulli_log_likelihood(x: list[int], prob: list[float]) -> float:
```

## When To Use What

- Use Gaussian NB when features are continuous and roughly bell-shaped within a class.
- Use Bernoulli NB when features are binary on/off indicators.
- Treat both as strong fast baselines, not as universal probabilistic models.

## Run tests

```bash
pytest modules/ml/models/naive-bayes-models/python -q
```
