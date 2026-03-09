from __future__ import annotations

import math


def normalize_advantages(advantages: list[float], eps: float = 1.0e-8) -> list[float]:
    if eps < 0.0:
        raise ValueError("eps must be non-negative")
    if not advantages:
        return []

    mean = sum(advantages) / len(advantages)
    variance = sum((advantage - mean) ** 2 for advantage in advantages) / len(advantages)
    std = math.sqrt(variance)
    return [(advantage - mean) / (std + eps) for advantage in advantages]
