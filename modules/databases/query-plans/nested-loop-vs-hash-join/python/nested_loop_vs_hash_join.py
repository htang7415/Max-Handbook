"""nested_loop_vs_hash_join - compare indexed nested loops to hash joins."""

from __future__ import annotations

import math


def nested_loop_cost(outer_rows: int, inner_rows: int, indexed_lookup: bool) -> int:
    outer = max(outer_rows, 0)
    inner = max(inner_rows, 0)
    if outer == 0 or inner == 0:
        return 0
    if indexed_lookup:
        probe_cost = max(1, int(math.ceil(math.log2(inner + 1))))
        return outer * probe_cost
    return outer * inner


def hash_join_cost(left_rows: int, right_rows: int) -> int:
    return max(left_rows, 0) + max(right_rows, 0)


def choose_join_strategy(
    outer_rows: int,
    inner_rows: int,
    indexed_lookup: bool,
    equality_join: bool = True,
) -> str:
    nested = nested_loop_cost(outer_rows, inner_rows, indexed_lookup)
    if not equality_join:
        return "nested-loop"
    hashed = hash_join_cost(outer_rows, inner_rows)
    return "nested-loop" if nested <= hashed else "hash-join"


def join_cost_summary(
    outer_rows: int,
    inner_rows: int,
    indexed_lookup: bool,
    equality_join: bool = True,
) -> dict[str, int | str]:
    nested = nested_loop_cost(outer_rows, inner_rows, indexed_lookup)
    hashed = hash_join_cost(outer_rows, inner_rows)
    return {
        "nested_loop_cost": nested,
        "hash_join_cost": hashed,
        "recommended_strategy": choose_join_strategy(
            outer_rows,
            inner_rows,
            indexed_lookup,
            equality_join,
        ),
    }
