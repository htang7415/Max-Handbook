from __future__ import annotations


def _normalized_statuses(statuses: list[str]) -> list[str]:
    cleaned = [status.strip().lower() for status in statuses if status.strip()]
    if not cleaned:
        raise ValueError("statuses must contain at least one non-empty status")
    return cleaned


def step_completion_rate(statuses: list[str]) -> float:
    cleaned = _normalized_statuses(statuses)
    return sum(1 for status in cleaned if status == "done") / len(cleaned)


def blocked_step_rate(statuses: list[str]) -> float:
    cleaned = _normalized_statuses(statuses)
    return sum(1 for status in cleaned if status == "blocked") / len(cleaned)


def step_status_counts(statuses: list[str]) -> dict[str, int]:
    cleaned = _normalized_statuses(statuses)
    counts: dict[str, int] = {}
    for status in cleaned:
        counts[status] = counts.get(status, 0) + 1
    return counts
