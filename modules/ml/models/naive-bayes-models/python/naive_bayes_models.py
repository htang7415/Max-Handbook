from __future__ import annotations

import math


def gaussian_log_likelihood(x: list[float], mean: list[float], var: list[float]) -> float:
    if len(x) != len(mean) or len(mean) != len(var):
        raise ValueError("x, mean, and var must have the same length")

    total = 0.0
    for xi, mu, variance in zip(x, mean, var):
        if variance <= 0:
            raise ValueError("variances must be positive")
        total += -0.5 * (math.log(2 * math.pi * variance) + ((xi - mu) ** 2) / variance)
    return total


def bernoulli_log_likelihood(x: list[int], prob: list[float]) -> float:
    if len(x) != len(prob):
        raise ValueError("x and prob must have the same length")

    total = 0.0
    for xi, p in zip(x, prob):
        if xi not in (0, 1):
            raise ValueError("x must contain only binary values")
        if not 0.0 < p < 1.0:
            raise ValueError("probabilities must be strictly between 0 and 1")
        total += xi * math.log(p) + (1 - xi) * math.log(1 - p)
    return total
