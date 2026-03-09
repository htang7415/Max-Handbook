from __future__ import annotations

import math


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
