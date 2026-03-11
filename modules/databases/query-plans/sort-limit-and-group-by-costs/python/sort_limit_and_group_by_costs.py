"""sort_limit_and_group_by_costs - simple work models for sort and aggregation."""

from __future__ import annotations

import math


def full_sort_work_units(row_count: int) -> float:
    if row_count <= 1:
        return 0.0
    return row_count * math.log2(row_count)


def top_n_sort_work_units(row_count: int, limit: int) -> float:
    if row_count <= 0 or limit <= 0:
        return 0.0
    return row_count * math.log2(max(limit, 1))


def hash_group_by_work_units(row_count: int, distinct_groups: int) -> int:
    return row_count + distinct_groups


def choose_order_plan(row_count: int, limit: int, has_covering_index: bool) -> str:
    if has_covering_index:
        return "index-order-scan"
    if limit > 0 and limit < max(row_count // 10, 1):
        return "top-n-sort"
    return "full-sort"


def plan_cost_summary(
    row_count: int,
    limit: int,
    distinct_groups: int,
    has_covering_index: bool,
) -> dict[str, float | int | str]:
    plan = choose_order_plan(row_count, limit, has_covering_index)
    sort_work = 0.0
    if plan == "full-sort":
        sort_work = full_sort_work_units(row_count)
    elif plan == "top-n-sort":
        sort_work = top_n_sort_work_units(row_count, limit)
    return {
        "plan": plan,
        "sort_work": sort_work,
        "group_by_work": hash_group_by_work_units(row_count, distinct_groups),
    }
