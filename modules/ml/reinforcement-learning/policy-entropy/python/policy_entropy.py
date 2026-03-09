from __future__ import annotations

import math


def policy_entropy(probabilities: list[float]) -> float:
    if not probabilities:
        return 0.0
    if any(probability < 0.0 for probability in probabilities):
        raise ValueError("probabilities must be non-negative")

    total_probability = sum(probabilities)
    if not math.isclose(total_probability, 1.0, rel_tol=1.0e-9, abs_tol=1.0e-9):
        raise ValueError("probabilities must sum to 1")

    return -sum(
        probability * math.log(probability)
        for probability in probabilities
        if probability > 0.0
    )
