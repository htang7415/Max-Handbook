from __future__ import annotations

import math


def pairwise_logistic_loss(preferred_score: float, rejected_score: float) -> float:
    margin = preferred_score - rejected_score
    if margin >= 0.0:
        return math.log1p(math.exp(-margin))
    return -margin + math.log1p(math.exp(margin))
