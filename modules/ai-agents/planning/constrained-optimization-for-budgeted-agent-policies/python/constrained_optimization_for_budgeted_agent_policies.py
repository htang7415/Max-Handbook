from __future__ import annotations


def policy_objective(
    expected_reward: float,
    cost: float,
    latency_ms: float,
    cost_weight: float = 1.0,
    latency_weight: float = 0.0,
) -> float:
    if expected_reward < 0.0:
        raise ValueError("expected_reward must be non-negative")
    if cost < 0.0:
        raise ValueError("cost must be non-negative")
    if latency_ms < 0.0:
        raise ValueError("latency_ms must be non-negative")
    if cost_weight < 0.0 or latency_weight < 0.0:
        raise ValueError("cost_weight and latency_weight must be non-negative")
    return expected_reward - cost_weight * cost - latency_weight * latency_ms


def feasible_policies(
    policy_to_metrics: dict[str, dict[str, float]],
    max_cost: float,
    max_latency_ms: float,
    max_risk: float,
) -> list[str]:
    if not policy_to_metrics:
        raise ValueError("policy_to_metrics must be non-empty")
    if max_cost < 0.0 or max_latency_ms < 0.0 or max_risk < 0.0:
        raise ValueError("budget constraints must be non-negative")

    feasible: list[str] = []
    for policy_name, metrics in policy_to_metrics.items():
        cleaned_name = policy_name.strip()
        if not cleaned_name:
            raise ValueError("policy names must be non-empty")
        cost = float(metrics.get("cost", 0.0))
        latency_ms = float(metrics.get("latency_ms", 0.0))
        risk = float(metrics.get("risk", 0.0))
        if cost < 0.0 or latency_ms < 0.0 or risk < 0.0:
            raise ValueError("policy metrics must be non-negative")
        if cost <= max_cost and latency_ms <= max_latency_ms and risk <= max_risk:
            feasible.append(cleaned_name)
    return sorted(feasible)


def budgeted_policy_choice(
    policy_to_metrics: dict[str, dict[str, float]],
    max_cost: float,
    max_latency_ms: float,
    max_risk: float,
    cost_weight: float = 1.0,
    latency_weight: float = 0.0,
) -> str:
    feasible = feasible_policies(policy_to_metrics, max_cost, max_latency_ms, max_risk)
    if not feasible:
        return "review"

    ranked: list[tuple[float, str]] = []
    for policy_name in feasible:
        metrics = policy_to_metrics[policy_name]
        score = policy_objective(
            expected_reward=float(metrics.get("expected_reward", 0.0)),
            cost=float(metrics.get("cost", 0.0)),
            latency_ms=float(metrics.get("latency_ms", 0.0)),
            cost_weight=cost_weight,
            latency_weight=latency_weight,
        )
        ranked.append((score, policy_name))

    ranked.sort(key=lambda item: (-item[0], item[1]))
    return ranked[0][1]
