from __future__ import annotations


def _validate_objectives(maximize_metrics: list[str], minimize_metrics: list[str]) -> tuple[list[str], list[str]]:
    maximize = [metric.strip() for metric in maximize_metrics if metric.strip()]
    minimize = [metric.strip() for metric in minimize_metrics if metric.strip()]
    if not maximize and not minimize:
        raise ValueError("at least one objective metric is required")
    overlap = set(maximize) & set(minimize)
    if overlap:
        raise ValueError("metrics cannot appear in both maximize and minimize")
    return maximize, minimize


def dominates(
    left_metrics: dict[str, float],
    right_metrics: dict[str, float],
    maximize_metrics: list[str],
    minimize_metrics: list[str],
) -> bool:
    maximize, minimize = _validate_objectives(maximize_metrics, minimize_metrics)

    strictly_better = False
    for metric in maximize:
        if metric not in left_metrics or metric not in right_metrics:
            raise ValueError(f"missing metric: {metric}")
        left_value = left_metrics[metric]
        right_value = right_metrics[metric]
        if left_value < right_value:
            return False
        if left_value > right_value:
            strictly_better = True

    for metric in minimize:
        if metric not in left_metrics or metric not in right_metrics:
            raise ValueError(f"missing metric: {metric}")
        left_value = left_metrics[metric]
        right_value = right_metrics[metric]
        if left_value > right_value:
            return False
        if left_value < right_value:
            strictly_better = True

    return strictly_better


def pareto_front(
    variants: dict[str, dict[str, float]],
    maximize_metrics: list[str],
    minimize_metrics: list[str],
) -> list[str]:
    if not variants:
        raise ValueError("variants must be non-empty")
    _validate_objectives(maximize_metrics, minimize_metrics)

    frontier: list[str] = []
    for candidate_name, candidate_metrics in variants.items():
        cleaned_name = candidate_name.strip()
        if not cleaned_name:
            raise ValueError("variant names must be non-empty")
        dominated = False
        for other_name, other_metrics in variants.items():
            if cleaned_name == other_name.strip():
                continue
            if dominates(other_metrics, candidate_metrics, maximize_metrics, minimize_metrics):
                dominated = True
                break
        if not dominated:
            frontier.append(cleaned_name)
    return sorted(frontier)


def pareto_route(
    candidate_name: str,
    variants: dict[str, dict[str, float]],
    maximize_metrics: list[str],
    minimize_metrics: list[str],
) -> str:
    cleaned_name = candidate_name.strip()
    if not cleaned_name:
        raise ValueError("candidate_name must be non-empty")
    if cleaned_name not in variants:
        raise ValueError("candidate_name must exist in variants")
    frontier = pareto_front(variants, maximize_metrics, minimize_metrics)
    if cleaned_name in frontier:
        return "frontier"
    return "dominated"
