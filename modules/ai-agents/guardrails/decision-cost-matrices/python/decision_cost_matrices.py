from __future__ import annotations


def _validate_outcome_probabilities(outcome_probabilities: dict[str, float]) -> dict[str, float]:
    if not outcome_probabilities:
        raise ValueError("outcome_probabilities must be non-empty")

    normalized: dict[str, float] = {}
    total = 0.0
    for outcome_name, probability in outcome_probabilities.items():
        cleaned_name = outcome_name.strip()
        if not cleaned_name:
            raise ValueError("outcome names must be non-empty")
        if not 0.0 <= probability <= 1.0:
            raise ValueError("probabilities must satisfy 0 <= value <= 1")
        normalized[cleaned_name] = probability
        total += probability

    if abs(total - 1.0) > 1e-9:
        raise ValueError("outcome probabilities must sum to 1")
    return normalized


def expected_action_cost(
    outcome_probabilities: dict[str, float],
    action_costs: dict[str, float],
) -> float:
    normalized_probs = _validate_outcome_probabilities(outcome_probabilities)
    if not action_costs:
        raise ValueError("action_costs must be non-empty")

    expected_cost = 0.0
    for outcome_name, probability in normalized_probs.items():
        if outcome_name not in action_costs:
            raise ValueError(f"missing cost for outcome: {outcome_name}")
        cost = action_costs[outcome_name]
        if cost < 0.0:
            raise ValueError("costs must be non-negative")
        expected_cost += probability * cost
    return expected_cost


def ranked_actions_by_cost(
    action_cost_matrix: dict[str, dict[str, float]],
    outcome_probabilities: dict[str, float],
) -> list[dict[str, object]]:
    if not action_cost_matrix:
        raise ValueError("action_cost_matrix must be non-empty")

    ranked: list[dict[str, object]] = []
    for action_name, action_costs in action_cost_matrix.items():
        cleaned_action = action_name.strip()
        if not cleaned_action:
            raise ValueError("action names must be non-empty")
        ranked.append(
            {
                "action": cleaned_action,
                "expected_cost": expected_action_cost(outcome_probabilities, action_costs),
            }
        )

    return sorted(
        ranked,
        key=lambda item: (float(item["expected_cost"]), str(item["action"])),
    )


def cost_matrix_decision(
    action_cost_matrix: dict[str, dict[str, float]],
    outcome_probabilities: dict[str, float],
) -> str:
    ranked = ranked_actions_by_cost(action_cost_matrix, outcome_probabilities)
    return str(ranked[0]["action"])
