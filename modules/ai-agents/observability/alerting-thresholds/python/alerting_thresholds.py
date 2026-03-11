from __future__ import annotations


def threshold_breached(value: float, threshold: float, direction: str) -> bool:
    if direction == "above":
        return value > threshold
    if direction == "below":
        return value < threshold
    raise ValueError("direction must be above or below")


def alert_message(metric_name: str, value: float, threshold: float, direction: str) -> str:
    if not metric_name.strip():
        raise ValueError("metric_name must be non-empty")
    breached = threshold_breached(value, threshold, direction)
    status = "ALERT" if breached else "OK"
    return f"{status}: {metric_name}={value:.2f} vs {direction} {threshold:.2f}"


def alert_candidates(
    metrics: dict[str, float],
    thresholds: dict[str, tuple[float, str]],
) -> list[str]:
    alerts: list[str] = []
    for metric_name, (threshold, direction) in thresholds.items():
        if metric_name not in metrics:
            continue
        if threshold_breached(metrics[metric_name], threshold, direction):
            alerts.append(metric_name)
    return alerts
