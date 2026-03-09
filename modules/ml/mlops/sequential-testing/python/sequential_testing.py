from __future__ import annotations


def sequential_test_decision(
    p_value: float,
    alpha: float,
    look_index: int,
    total_looks: int,
) -> tuple[float, bool]:
    if not 0.0 <= p_value <= 1.0:
        raise ValueError("p_value must satisfy 0 <= p_value <= 1")
    if not 0.0 < alpha <= 1.0:
        raise ValueError("alpha must satisfy 0 < alpha <= 1")
    if total_looks <= 0:
        raise ValueError("total_looks must be positive")
    if not 1 <= look_index <= total_looks:
        raise ValueError("look_index must satisfy 1 <= look_index <= total_looks")

    spent_alpha = alpha * look_index / total_looks
    return spent_alpha, p_value <= spent_alpha
