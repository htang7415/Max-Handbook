# Initialization Methods

> Track: `ml` | Topic: `deep-learning`

## Purpose

Use this module to compare the two initialization schemes most worth remembering:
Xavier/Glorot and He initialization.

## First Principles

- Initialization exists to keep activations and gradients in a usable range.
- Xavier is designed for roughly symmetric activations like `tanh`.
- He initialization increases variance for ReLU-style networks so signal does not die out too quickly.

## Core Math

$$
W \sim \mathcal{U}\left(-\sqrt{\frac{6}{fan_{in}+fan_{out}}}, \sqrt{\frac{6}{fan_{in}+fan_{out}}}\right)
$$

$$
W \sim \mathcal{N}\left(0, \frac{2}{fan_{in}}\right)
$$

## Minimal Code Mental Model

```python
xavier = xavier_uniform(fan_in=128, fan_out=64, seed=1)
he = he_normal(fan_in=128, fan_out=64, seed=1)
```

## Function

```python
def xavier_uniform(fan_in: int, fan_out: int, seed: int = 0) -> list[float]:
def he_normal(fan_in: int, fan_out: int, seed: int = 0) -> list[float]:
```

## When To Use What

- Use Xavier when activations are roughly symmetric around zero.
- Use He when the network uses ReLU-style activations.
- If training is unstable, treat initialization together with normalization and gradient flow, not as an isolated trick.

## Run tests

```bash
pytest modules/ml/deep-learning/initialization-methods/python -q
```
