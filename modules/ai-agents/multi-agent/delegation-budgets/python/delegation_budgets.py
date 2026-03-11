from __future__ import annotations


def proportional_worker_budgets(
    worker_weights: dict[str, float],
    total_budget: float,
    reserve_budget: float = 0.0,
) -> dict[str, float]:
    if not worker_weights:
        raise ValueError("worker_weights must be non-empty")
    if total_budget <= 0.0:
        raise ValueError("total_budget must be positive")
    if reserve_budget < 0.0:
        raise ValueError("reserve_budget must be non-negative")
    if reserve_budget >= total_budget:
        raise ValueError("reserve_budget must be smaller than total_budget")

    cleaned: dict[str, float] = {}
    total_weight = 0.0
    for worker_name, weight in worker_weights.items():
        cleaned_name = worker_name.strip()
        if not cleaned_name:
            raise ValueError("worker names must be non-empty")
        if weight <= 0.0:
            raise ValueError("worker weights must be positive")
        cleaned[cleaned_name] = weight
        total_weight += weight

    usable_budget = total_budget - reserve_budget
    return {
        worker_name: usable_budget * weight / total_weight
        for worker_name, weight in sorted(cleaned.items())
    }


def over_budget_workers(worker_costs: dict[str, float], worker_budgets: dict[str, float]) -> list[str]:
    if not worker_costs:
        raise ValueError("worker_costs must be non-empty")
    if not worker_budgets:
        raise ValueError("worker_budgets must be non-empty")

    over_budget: list[str] = []
    for worker_name, cost in worker_costs.items():
        cleaned_name = worker_name.strip()
        if not cleaned_name:
            raise ValueError("worker names must be non-empty")
        if cleaned_name not in worker_budgets:
            raise ValueError(f"missing budget for worker: {cleaned_name}")
        if cost < 0.0:
            raise ValueError("worker costs must be non-negative")
        if cost > worker_budgets[cleaned_name]:
            over_budget.append(cleaned_name)
    return sorted(over_budget)


def delegation_budget_route(worker_costs: dict[str, float], worker_budgets: dict[str, float]) -> str:
    over_budget = over_budget_workers(worker_costs, worker_budgets)
    if not over_budget:
        return "execute"
    if len(over_budget) == len(worker_costs):
        return "review"
    return "rebalance"
