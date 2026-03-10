from __future__ import annotations

import math


def gaussian_pdf_1d(x: float, mean: float, variance: float) -> float:
    variance = max(variance, 1e-9)
    scale = math.sqrt(2.0 * math.pi * variance)
    exponent = -((x - mean) ** 2) / (2.0 * variance)
    return math.exp(exponent) / scale


def responsibilities_1d(
    data: list[float],
    weights: list[float],
    means: list[float],
    variances: list[float],
) -> list[list[float]]:
    if not data:
        raise ValueError("data must be non-empty")
    if len(weights) != len(means) or len(means) != len(variances):
        raise ValueError("weights, means, and variances must have the same length")
    if any(weight < 0.0 for weight in weights):
        raise ValueError("weights must be non-negative")
    if any(variance <= 0.0 for variance in variances):
        raise ValueError("variances must be positive")

    k = len(weights)
    responsibilities: list[list[float]] = []
    for x in data:
        unnormalized = [
            weights[j] * gaussian_pdf_1d(x, means[j], variances[j]) for j in range(k)
        ]
        total = sum(unnormalized)
        if total == 0.0:
            raise ValueError("component probabilities must sum to a positive value")
        responsibilities.append([value / total for value in unnormalized])
    return responsibilities


def em_step_1d(
    data: list[float],
    weights: list[float],
    means: list[float],
    variances: list[float],
) -> tuple[list[float], list[float], list[float]]:
    responsibilities = responsibilities_1d(data, weights, means, variances)
    k = len(weights)

    n = len(data)
    new_weights: list[float] = []
    new_means: list[float] = []
    new_variances: list[float] = []

    for j in range(k):
        effective_count = sum(row[j] for row in responsibilities)
        if effective_count == 0.0:
            new_weights.append(0.0)
            new_means.append(means[j])
            new_variances.append(variances[j])
            continue

        mean = sum(row[j] * x for row, x in zip(responsibilities, data)) / effective_count
        variance = (
            sum(row[j] * ((x - mean) ** 2) for row, x in zip(responsibilities, data))
            / effective_count
        )

        new_weights.append(effective_count / n)
        new_means.append(mean)
        new_variances.append(max(variance, 1e-9))

    return new_weights, new_means, new_variances
