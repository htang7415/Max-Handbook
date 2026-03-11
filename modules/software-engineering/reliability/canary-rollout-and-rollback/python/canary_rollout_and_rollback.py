from __future__ import annotations


CANARY_STEPS = [1, 5, 10, 25, 50, 100]


def canary_healthy(baseline_error_rate: float, canary_error_rate: float, max_increase: float) -> bool:
    if baseline_error_rate < 0 or canary_error_rate < 0 or max_increase < 0:
        raise ValueError("rates must be non-negative")
    return canary_error_rate <= baseline_error_rate + max_increase


def next_canary_percentage(current_percentage: int, healthy: bool) -> int:
    if current_percentage not in CANARY_STEPS:
        raise ValueError("current_percentage must be one of the canary steps")
    if not healthy:
        return 0
    current_index = CANARY_STEPS.index(current_percentage)
    return CANARY_STEPS[min(current_index + 1, len(CANARY_STEPS) - 1)]


def rollout_decision(current_percentage: int, healthy: bool) -> str:
    next_percentage = next_canary_percentage(current_percentage, healthy)
    if next_percentage == 0:
        return "rollback"
    if next_percentage == 100 and healthy:
        return "complete"
    return "expand"
