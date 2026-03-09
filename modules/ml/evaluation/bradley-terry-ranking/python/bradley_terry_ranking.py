from __future__ import annotations

import math


def bradley_terry_probability(score_a: float, score_b: float) -> float:
    return 1.0 / (1.0 + math.exp(-(score_a - score_b)))
