# Normalization Methods

> Track: `ml` | Topic: `deep-learning`

## Purpose

Use this module to compare the main normalization families and understand which
axes they normalize over.

## First Principles

- Normalization stabilizes activation scale so optimization is easier.
- The main difference between methods is which statistics are shared.
- BatchNorm depends on batch statistics, which is why it fits CNN-style training
  better than transformer-style sequence models.
- LayerNorm and RMSNorm normalize within each example, which makes them more
  robust to batch variability.

## Core Math

- BatchNorm:
  $$
  \mathrm{BatchNorm}(x)=\frac{x-\mu_B}{\sqrt{\sigma_B^2+\epsilon}}
  $$
- LayerNorm:
  $$
  \mathrm{LayerNorm}(x)=\frac{x-\mu_f}{\sqrt{\sigma_f^2+\epsilon}}
  $$
- RMSNorm:
  $$
  \mathrm{RMSNorm}(x)=\frac{x}{\sqrt{\frac{1}{d}\sum_i x_i^2+\epsilon}}
  $$

## From Math To Code

- Compute the mean and variance for the axes you want to normalize over.
- Reuse those statistics to standardize activations.
- Skip centering only when you explicitly want RMS-only scaling.

## Minimal Code Mental Model

```python
mean, variance = mean_variance(x_token)
y_token = normalize_with_stats(x_token, mean, variance)
y_batch = batchnorm(x_batch)
rms_scaled = rmsnorm(x_token)
```

## Function

```python
def mean_variance(x: list[float]) -> tuple[float, float]:
def normalize_with_stats(x: list[float], mean: float, variance: float, eps: float = 1e-5) -> list[float]:
def batchnorm(x: list[float], eps: float = 1e-5) -> list[float]:
def layernorm(x: list[float], eps: float = 1e-5) -> list[float]:
def rmsnorm(x: list[float], eps: float = 1e-5) -> list[float]:
def groupnorm(x: list[float], groups: int, eps: float = 1e-5) -> list[float]:
def instancenorm(x: list[float], eps: float = 1e-5) -> list[float]:
def batch_stats(matrix: list[list[float]]) -> tuple[float, float]:
```

## When To Use What

- Use BatchNorm as the classic CNN default when batches are stable and reasonably large.
- Use LayerNorm or RMSNorm for transformers and sequence models.
- Use GroupNorm or InstanceNorm when batch statistics are unreliable or unavailable.
- Use RMSNorm when you want scale control with less computation than full centering.

## Run tests

```bash
pytest modules/ml/deep-learning/normalization-methods/python -q
```
