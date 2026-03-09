from __future__ import annotations

import itertools


def _mean(values: list[float]) -> float:
    return sum(values) / len(values)


def permutation_test_p_value(group_a: list[float], group_b: list[float]) -> float:
    if not group_a or not group_b:
        raise ValueError("group_a and group_b must be non-empty")

    pooled = group_a + group_b
    size_a = len(group_a)
    observed = _mean(group_a) - _mean(group_b)

    extreme = 0
    total = 0
    indices = range(len(pooled))
    for chosen in itertools.combinations(indices, size_a):
        chosen_set = set(chosen)
        perm_a = [pooled[index] for index in chosen]
        perm_b = [pooled[index] for index in indices if index not in chosen_set]
        statistic = _mean(perm_a) - _mean(perm_b)
        if abs(statistic) >= abs(observed):
            extreme += 1
        total += 1

    return extreme / total
