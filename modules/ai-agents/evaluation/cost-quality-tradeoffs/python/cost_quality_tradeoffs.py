from __future__ import annotations


def _validate_pairs(left: list[object], right: list[object]) -> None:
    if not left or not right:
        raise ValueError("inputs must be non-empty")
    if len(left) != len(right):
        raise ValueError("inputs must have the same length")


def quality_per_cost(qualities: list[float], costs: list[float]) -> float:
    _validate_pairs(qualities, costs)
    if any(cost <= 0 for cost in costs):
        raise ValueError("costs must be positive")
    return sum(qualities) / sum(costs)


def cost_per_success(successes: list[bool], costs: list[float]) -> float:
    _validate_pairs(successes, costs)
    if any(cost < 0 for cost in costs):
        raise ValueError("costs must be non-negative")
    success_count = sum(1 for success in successes if success)
    if success_count == 0:
        raise ValueError("at least one success is required")
    return sum(costs) / success_count


def best_tradeoff_index(qualities: list[float], costs: list[float]) -> int:
    _validate_pairs(qualities, costs)
    if any(cost <= 0 for cost in costs):
        raise ValueError("costs must be positive")
    scores = [quality / cost for quality, cost in zip(qualities, costs)]
    return max(range(len(scores)), key=lambda index: scores[index])
