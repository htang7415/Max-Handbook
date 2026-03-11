"""sparse_index_selectivity - an index on a sparse column can stay small and highly selective."""

from __future__ import annotations


def sparse_index_entries(total_rows: int, populated_fraction: float) -> int:
    if total_rows < 0:
        raise ValueError("total_rows must be non-negative")
    if not 0.0 <= populated_fraction <= 1.0:
        raise ValueError("populated_fraction must be between 0 and 1")
    return round(total_rows * populated_fraction)


def full_index_entries(total_rows: int) -> int:
    if total_rows < 0:
        raise ValueError("total_rows must be non-negative")
    return total_rows


def selectivity_summary(
    total_rows: int,
    populated_fraction: float,
    matching_rows: int,
) -> dict[str, int | float]:
    sparse_entries = sparse_index_entries(total_rows, populated_fraction)
    return {
        "full_index_entries": full_index_entries(total_rows),
        "sparse_index_entries": sparse_entries,
        "entries_saved": full_index_entries(total_rows) - sparse_entries,
        "match_fraction_within_sparse_index": 0.0 if sparse_entries == 0 else matching_rows / sparse_entries,
    }
