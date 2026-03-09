from __future__ import annotations


def judge_agreement_matrix(judge_decisions: list[list[int]]) -> list[list[float]]:
    if not judge_decisions:
        return []

    num_items = len(judge_decisions[0])
    if any(len(decisions) != num_items for decisions in judge_decisions):
        raise ValueError("all judges must score the same number of items")
    if any(decision not in {-1, 0, 1} for decisions in judge_decisions for decision in decisions):
        raise ValueError("judge decisions must contain only -1, 0, or 1")
    if num_items == 0:
        return [[0.0 for _ in judge_decisions] for _ in judge_decisions]

    matrix: list[list[float]] = []
    for left in judge_decisions:
        row: list[float] = []
        for right in judge_decisions:
            matches = sum(left_decision == right_decision for left_decision, right_decision in zip(left, right))
            row.append(matches / num_items)
        matrix.append(row)
    return matrix
