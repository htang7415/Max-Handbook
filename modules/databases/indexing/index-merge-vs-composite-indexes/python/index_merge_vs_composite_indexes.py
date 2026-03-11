"""index_merge_vs_composite_indexes - conjunctions often want one composite index, not two merged probes."""

from __future__ import annotations


def matching_rows(total_rows: int, selectivity: float) -> int:
    if total_rows < 0:
        raise ValueError("total_rows must be non-negative")
    if not 0.0 <= selectivity <= 1.0:
        raise ValueError("selectivity must be between 0 and 1")
    return round(total_rows * selectivity)


def index_merge_cost(
    total_rows: int,
    left_selectivity: float,
    right_selectivity: float,
    overlap_selectivity: float,
    row_fetch_cost: int = 2,
) -> int:
    left_rows = matching_rows(total_rows, left_selectivity)
    right_rows = matching_rows(total_rows, right_selectivity)
    overlap_rows = matching_rows(total_rows, overlap_selectivity)
    return left_rows + right_rows + overlap_rows * max(row_fetch_cost, 0)


def composite_index_cost(
    total_rows: int,
    overlap_selectivity: float,
    probe_overhead: int = 8,
    row_fetch_cost: int = 2,
) -> int:
    overlap_rows = matching_rows(total_rows, overlap_selectivity)
    return max(probe_overhead, 0) + overlap_rows * max(row_fetch_cost, 0)


def recommended_strategy(
    total_rows: int,
    left_selectivity: float,
    right_selectivity: float,
    overlap_selectivity: float,
) -> str:
    seq_cost = total_rows
    merge_cost = index_merge_cost(
        total_rows,
        left_selectivity,
        right_selectivity,
        overlap_selectivity,
    )
    composite_cost = composite_index_cost(total_rows, overlap_selectivity)
    if composite_cost <= merge_cost and composite_cost < seq_cost:
        return "composite-index"
    if merge_cost < seq_cost:
        return "index-merge"
    return "seq-scan"


def strategy_summary(
    total_rows: int,
    left_selectivity: float,
    right_selectivity: float,
    overlap_selectivity: float,
) -> dict[str, int | float | str]:
    return {
        "left_rows": matching_rows(total_rows, left_selectivity),
        "right_rows": matching_rows(total_rows, right_selectivity),
        "overlap_rows": matching_rows(total_rows, overlap_selectivity),
        "seq_scan_cost": total_rows,
        "index_merge_cost": index_merge_cost(
            total_rows,
            left_selectivity,
            right_selectivity,
            overlap_selectivity,
        ),
        "composite_index_cost": composite_index_cost(total_rows, overlap_selectivity),
        "recommended_strategy": recommended_strategy(
            total_rows,
            left_selectivity,
            right_selectivity,
            overlap_selectivity,
        ),
    }
