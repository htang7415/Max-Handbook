"""low_cardinality_index_tradeoffs - an index loses value when too much of the table matches."""

from __future__ import annotations


def matching_rows(total_rows: int, match_fraction: float) -> int:
    if total_rows < 0:
        raise ValueError("total_rows must be non-negative")
    if not 0.0 <= match_fraction <= 1.0:
        raise ValueError("match_fraction must be between 0 and 1")
    return round(total_rows * match_fraction)


def seq_scan_cost(total_rows: int) -> int:
    if total_rows < 0:
        raise ValueError("total_rows must be non-negative")
    return total_rows


def index_scan_cost(
    total_rows: int,
    match_fraction: float,
    probe_overhead: int = 8,
    heap_fetch_cost: int = 2,
) -> int:
    matches = matching_rows(total_rows, match_fraction)
    return max(probe_overhead, 0) + matches * (1 + max(heap_fetch_cost, 0))


def recommended_path(
    total_rows: int,
    match_fraction: float,
    probe_overhead: int = 8,
    heap_fetch_cost: int = 2,
) -> str:
    index_cost = index_scan_cost(total_rows, match_fraction, probe_overhead, heap_fetch_cost)
    return "index-scan" if index_cost < seq_scan_cost(total_rows) else "seq-scan"


def tradeoff_summary(
    total_rows: int,
    match_fraction: float,
    probe_overhead: int = 8,
    heap_fetch_cost: int = 2,
) -> dict[str, int | float | str]:
    rows = matching_rows(total_rows, match_fraction)
    index_cost = index_scan_cost(total_rows, match_fraction, probe_overhead, heap_fetch_cost)
    seq_cost = seq_scan_cost(total_rows)
    return {
        "matching_rows": rows,
        "match_fraction": match_fraction,
        "seq_scan_cost": seq_cost,
        "index_scan_cost": index_cost,
        "recommended_path": "index-scan" if index_cost < seq_cost else "seq-scan",
    }
