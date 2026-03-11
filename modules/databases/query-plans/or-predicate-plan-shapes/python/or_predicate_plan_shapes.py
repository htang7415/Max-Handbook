"""or_predicate_plan_shapes - compare full scans to multi-branch index union work."""

from __future__ import annotations


def matching_rows(total_rows: int, selectivity: float) -> int:
    if total_rows < 0:
        raise ValueError("total_rows must be non-negative")
    if not 0.0 <= selectivity <= 1.0:
        raise ValueError("selectivity must be between 0 and 1")
    return round(total_rows * selectivity)


def union_rows(
    total_rows: int,
    left_selectivity: float,
    right_selectivity: float,
    overlap_selectivity: float,
) -> int:
    left_rows = matching_rows(total_rows, left_selectivity)
    right_rows = matching_rows(total_rows, right_selectivity)
    overlap_rows = matching_rows(total_rows, overlap_selectivity)
    return max(left_rows + right_rows - overlap_rows, 0)


def index_union_cost(
    total_rows: int,
    left_selectivity: float,
    right_selectivity: float,
    overlap_selectivity: float,
    probe_overhead: int = 8,
    row_fetch_cost: int = 2,
) -> int:
    return (2 * max(probe_overhead, 0)) + union_rows(
        total_rows,
        left_selectivity,
        right_selectivity,
        overlap_selectivity,
    ) * max(row_fetch_cost, 0)


def recommended_path(
    total_rows: int,
    left_selectivity: float,
    right_selectivity: float,
    overlap_selectivity: float,
) -> str:
    index_cost = index_union_cost(
        total_rows,
        left_selectivity,
        right_selectivity,
        overlap_selectivity,
    )
    return "index-union" if index_cost < total_rows else "seq-scan"


def or_plan_summary(
    total_rows: int,
    left_selectivity: float,
    right_selectivity: float,
    overlap_selectivity: float,
) -> dict[str, int | float | str]:
    total_match_rows = union_rows(
        total_rows,
        left_selectivity,
        right_selectivity,
        overlap_selectivity,
    )
    index_cost = index_union_cost(
        total_rows,
        left_selectivity,
        right_selectivity,
        overlap_selectivity,
    )
    return {
        "union_rows": total_match_rows,
        "seq_scan_cost": total_rows,
        "index_union_cost": index_cost,
        "recommended_path": "index-union" if index_cost < total_rows else "seq-scan",
    }
