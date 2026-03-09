from __future__ import annotations


def next_canary_share(current_share: float, step: float, error_rate: float, threshold: float) -> float:
    if not 0.0 <= current_share <= 1.0:
        raise ValueError("current_share must satisfy 0 <= current_share <= 1")
    if not 0.0 < step <= 1.0:
        raise ValueError("step must satisfy 0 < step <= 1")
    if not 0.0 <= error_rate <= 1.0:
        raise ValueError("error_rate must satisfy 0 <= error_rate <= 1")
    if not 0.0 <= threshold <= 1.0:
        raise ValueError("threshold must satisfy 0 <= threshold <= 1")

    if error_rate <= threshold:
        return min(1.0, current_share + step)
    return max(0.0, current_share - step)
