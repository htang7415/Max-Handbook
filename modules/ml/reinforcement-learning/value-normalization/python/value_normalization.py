from __future__ import annotations

import math


def normalize_value_targets(values: list[float], eps: float = 1.0e-8) -> tuple[list[float], float, float]:
    if eps < 0.0:
        raise ValueError("eps must be non-negative")
    if not values:
        return [], 0.0, 0.0

    mean = sum(values) / len(values)
    variance = sum((value - mean) ** 2 for value in values) / len(values)
    std = math.sqrt(variance)
    normalized = [(value - mean) / (std + eps) for value in values]
    return normalized, mean, std
