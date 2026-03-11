from __future__ import annotations


def sli_rate(good_events: int, total_events: int) -> float:
    if total_events <= 0:
        raise ValueError("total_events must be positive")
    if good_events < 0 or good_events > total_events:
        raise ValueError("good_events must be between 0 and total_events")
    return good_events / total_events


def error_budget_remaining(actual_sli: float, target_slo: float) -> float:
    if not 0 <= actual_sli <= 1:
        raise ValueError("actual_sli must be between 0 and 1")
    if not 0 < target_slo < 1:
        raise ValueError("target_slo must be between 0 and 1")

    allowed_failure_rate = 1 - target_slo
    actual_failure_rate = 1 - actual_sli
    remaining = (allowed_failure_rate - actual_failure_rate) / allowed_failure_rate
    return max(0.0, min(1.0, remaining))


def alert_state(actual_sli: float, target_slo: float, page_when_remaining_below: float = 0.25) -> str:
    if not 0 <= page_when_remaining_below <= 1:
        raise ValueError("page_when_remaining_below must be between 0 and 1")

    remaining = error_budget_remaining(actual_sli, target_slo)
    if actual_sli < target_slo:
        return "page"
    if remaining <= page_when_remaining_below:
        return "ticket"
    return "ok"
