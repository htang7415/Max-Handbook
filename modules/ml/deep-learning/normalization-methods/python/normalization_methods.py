from __future__ import annotations

import math


def _validate_vector(x: list[float]) -> None:
    if not x:
        raise ValueError("x must be non-empty")


def _mean_variance(x: list[float]) -> tuple[float, float]:
    mean = sum(x) / len(x)
    variance = sum((value - mean) ** 2 for value in x) / len(x)
    return mean, variance


def mean_variance(x: list[float]) -> tuple[float, float]:
    _validate_vector(x)
    return _mean_variance(x)


def normalize_with_stats(x: list[float], mean: float, variance: float, eps: float = 1e-5) -> list[float]:
    if eps <= 0.0:
        raise ValueError("eps must be positive")
    return [(value - mean) / math.sqrt(variance + eps) for value in x]


def batchnorm(x: list[float], eps: float = 1e-5) -> list[float]:
    mean, variance = mean_variance(x)
    return normalize_with_stats(x, mean, variance, eps=eps)


def layernorm(x: list[float], eps: float = 1e-5) -> list[float]:
    mean, variance = mean_variance(x)
    return normalize_with_stats(x, mean, variance, eps=eps)


def rmsnorm(x: list[float], eps: float = 1e-5) -> list[float]:
    _validate_vector(x)
    rms = math.sqrt(sum(value * value for value in x) / len(x) + eps)
    return [value / rms for value in x]


def groupnorm(x: list[float], groups: int, eps: float = 1e-5) -> list[float]:
    _validate_vector(x)
    if groups <= 0:
        raise ValueError("groups must be positive")
    if len(x) % groups != 0:
        raise ValueError("len(x) must be divisible by groups")

    group_size = len(x) // groups
    out: list[float] = []
    for group_index in range(groups):
        chunk = x[group_index * group_size : (group_index + 1) * group_size]
        mean, variance = mean_variance(chunk)
        out.extend(normalize_with_stats(chunk, mean, variance, eps=eps))
    return out


def instancenorm(x: list[float], eps: float = 1e-5) -> list[float]:
    mean, variance = mean_variance(x)
    return normalize_with_stats(x, mean, variance, eps=eps)


def batch_stats(matrix: list[list[float]]) -> tuple[float, float]:
    if not matrix or not matrix[0]:
        raise ValueError("matrix must be non-empty")
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("matrix must be rectangular")

    values = [value for row in matrix for value in row]
    mean = sum(values) / len(values)
    variance = sum((value - mean) ** 2 for value in values) / len(values)
    return mean, variance
