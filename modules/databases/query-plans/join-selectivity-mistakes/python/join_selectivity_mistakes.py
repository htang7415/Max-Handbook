"""join_selectivity_mistakes - bad selectivity estimates can pick the wrong join algorithm."""

from __future__ import annotations


def filtered_rows(base_rows: int, selectivity: float) -> int:
    if base_rows < 0:
        raise ValueError("base_rows must be non-negative")
    if not 0.0 <= selectivity <= 1.0:
        raise ValueError("selectivity must be between 0 and 1")
    return round(base_rows * selectivity)


def join_work(strategy: str, outer_rows: int, inner_rows: int) -> int:
    outer = max(outer_rows, 0)
    inner = max(inner_rows, 0)
    if strategy == "nested-loop":
        return outer * inner
    if strategy == "hash-join":
        return outer + inner
    raise ValueError(f"unsupported strategy: {strategy}")


def choose_join_strategy(
    estimated_outer_rows: int,
    nested_loop_outer_threshold: int = 10,
) -> str:
    if estimated_outer_rows <= nested_loop_outer_threshold:
        return "nested-loop"
    return "hash-join"


def plan_outcome(
    base_outer_rows: int,
    estimated_selectivity: float,
    actual_selectivity: float,
    inner_rows: int,
    nested_loop_outer_threshold: int = 10,
) -> dict[str, int | str]:
    estimated_outer = filtered_rows(base_outer_rows, estimated_selectivity)
    actual_outer = filtered_rows(base_outer_rows, actual_selectivity)
    chosen = choose_join_strategy(estimated_outer, nested_loop_outer_threshold)

    nested_actual = join_work("nested-loop", actual_outer, inner_rows)
    hash_actual = join_work("hash-join", actual_outer, inner_rows)

    return {
        "estimated_outer_rows": estimated_outer,
        "actual_outer_rows": actual_outer,
        "chosen_strategy": chosen,
        "estimated_work": join_work(chosen, estimated_outer, inner_rows),
        "actual_work": join_work(chosen, actual_outer, inner_rows),
        "better_actual_strategy": "nested-loop" if nested_actual <= hash_actual else "hash-join",
    }
