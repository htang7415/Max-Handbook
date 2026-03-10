from __future__ import annotations

import math


def sample_mean_and_std(samples: list[float]) -> tuple[float, float]:
    if len(samples) < 2:
        raise ValueError("samples must contain at least two values")
    mean = sum(samples) / len(samples)
    variance = sum((sample - mean) ** 2 for sample in samples) / (len(samples) - 1)
    return mean, math.sqrt(variance)


def standard_error(samples: list[float]) -> float:
    mean, std = sample_mean_and_std(samples)
    del mean
    return std / math.sqrt(len(samples))


def mean_confidence_interval(
    samples: list[float],
    z: float = 1.96,
) -> tuple[float, float]:
    if z <= 0.0:
        raise ValueError("z must be positive")

    mean, _ = sample_mean_and_std(samples)
    margin = z * standard_error(samples)
    return mean - margin, mean + margin


def _quantile(sorted_values: list[float], q: float) -> float:
    position = q * (len(sorted_values) - 1)
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return sorted_values[lower]
    weight = position - lower
    return sorted_values[lower] * (1.0 - weight) + sorted_values[upper] * weight


def bootstrap_percentile_interval(
    bootstrap_statistics: list[float],
    alpha: float = 0.05,
) -> tuple[float, float]:
    if len(bootstrap_statistics) < 2:
        raise ValueError("bootstrap_statistics must contain at least two values")
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must satisfy 0 < alpha < 1")

    sorted_values = sorted(bootstrap_statistics)
    lower = _quantile(sorted_values, alpha / 2.0)
    upper = _quantile(sorted_values, 1.0 - alpha / 2.0)
    return lower, upper


def wilson_interval(successes: int, trials: int, z: float = 1.96) -> tuple[float, float]:
    if trials <= 0:
        raise ValueError("trials must be positive")
    if not 0 <= successes <= trials:
        raise ValueError("successes must satisfy 0 <= successes <= trials")
    if z < 0.0:
        raise ValueError("z must be non-negative")

    proportion = successes / trials
    z_squared = z * z
    denominator = 1.0 + z_squared / trials
    center = (proportion + z_squared / (2.0 * trials)) / denominator
    margin = z * math.sqrt((proportion * (1.0 - proportion) + z_squared / (4.0 * trials)) / trials)
    margin /= denominator

    lower = max(0.0, center - margin)
    upper = min(1.0, center + margin)
    return lower, upper
