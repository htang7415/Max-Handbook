from __future__ import annotations


def metric_drop(baseline: float, candidate: float) -> float:
    return baseline - candidate


def regression_failed(baseline: float, candidate: float, max_drop: float) -> bool:
    if max_drop < 0:
        raise ValueError("max_drop must be non-negative")
    return metric_drop(baseline, candidate) > max_drop


def regression_report(
    metric_name: str,
    baseline: float,
    candidate: float,
    max_drop: float,
) -> dict[str, object]:
    if not metric_name.strip():
        raise ValueError("metric_name must be non-empty")
    failed = regression_failed(baseline, candidate, max_drop)
    return {
        "metric": metric_name,
        "baseline": baseline,
        "candidate": candidate,
        "drop": metric_drop(baseline, candidate),
        "failed": failed,
    }
