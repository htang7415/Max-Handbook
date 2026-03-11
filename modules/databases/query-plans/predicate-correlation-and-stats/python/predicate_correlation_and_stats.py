"""predicate_correlation_and_stats - independent estimates break on correlated filters."""

from __future__ import annotations

from math import prod


def independent_estimate(table_rows: int, selectivities: list[float]) -> int:
    if table_rows < 0:
        raise ValueError("table_rows must be non-negative")
    if any(not 0.0 <= value <= 1.0 for value in selectivities):
        raise ValueError("selectivities must be between 0 and 1")
    return round(table_rows * prod(selectivities or [1.0]))


def correlated_estimate(table_rows: int, selectivities: list[float]) -> int:
    if table_rows < 0:
        raise ValueError("table_rows must be non-negative")
    if any(not 0.0 <= value <= 1.0 for value in selectivities):
        raise ValueError("selectivities must be between 0 and 1")
    if not selectivities:
        return table_rows
    return round(table_rows * min(selectivities))


def q_error(estimated_rows: int, actual_rows: int) -> float:
    if estimated_rows <= 0 or actual_rows <= 0:
        raise ValueError("estimated_rows and actual_rows must be positive")
    larger = max(estimated_rows, actual_rows)
    smaller = min(estimated_rows, actual_rows)
    return larger / smaller


def needs_extended_stats(
    estimated_rows: int,
    actual_rows: int,
    q_error_threshold: float = 4.0,
) -> bool:
    return q_error(estimated_rows, actual_rows) >= q_error_threshold


def correlation_summary(table_rows: int, selectivities: list[float]) -> dict[str, int | float | bool]:
    independent = independent_estimate(table_rows, selectivities)
    correlated = correlated_estimate(table_rows, selectivities)
    return {
        "independent_estimate": independent,
        "correlated_actual_rows": correlated,
        "q_error": q_error(independent, correlated),
        "needs_extended_stats": needs_extended_stats(independent, correlated),
    }
