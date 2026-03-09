from __future__ import annotations


def error_budget_status(total_requests: int, failed_requests: int, slo_target: float) -> tuple[float, float]:
    if total_requests <= 0:
        raise ValueError("total_requests must be positive")
    if not 0 <= failed_requests <= total_requests:
        raise ValueError("failed_requests must satisfy 0 <= failed_requests <= total_requests")
    if not 0.0 < slo_target < 1.0:
        raise ValueError("slo_target must satisfy 0 < slo_target < 1")

    allowed_error_rate = 1.0 - slo_target
    observed_error_rate = failed_requests / total_requests
    burn_rate = observed_error_rate / allowed_error_rate
    remaining_budget_fraction = max(0.0, 1.0 - burn_rate)
    return remaining_budget_fraction, burn_rate
