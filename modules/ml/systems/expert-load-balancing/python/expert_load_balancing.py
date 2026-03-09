from __future__ import annotations


def expert_load_balance_loss(
    router_probs: list[list[float]],
    assignments: list[int],
) -> float:
    if len(router_probs) != len(assignments):
        raise ValueError("router_probs and assignments must have the same length")
    if not router_probs:
        return 0.0

    num_experts = len(router_probs[0])
    if num_experts == 0:
        raise ValueError("router_probs must include at least one expert")
    if any(len(row) != num_experts for row in router_probs):
        raise ValueError("all router_probs rows must have the same length")
    if any(index < 0 or index >= num_experts for index in assignments):
        raise ValueError("assignments must be valid expert indices")

    token_fractions = [0.0] * num_experts
    prob_fractions = [0.0] * num_experts
    num_tokens = len(assignments)

    for assignment in assignments:
        token_fractions[assignment] += 1.0 / num_tokens
    for row in router_probs:
        for expert, probability in enumerate(row):
            prob_fractions[expert] += probability / num_tokens

    return num_experts * sum(
        token_fraction * prob_fraction
        for token_fraction, prob_fraction in zip(token_fractions, prob_fractions)
    )
