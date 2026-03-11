"""index_write_amplification - model how indexes add maintenance work to writes."""

from __future__ import annotations


def insert_work(insert_rows: int, index_count: int) -> int:
    rows = max(insert_rows, 0)
    indexes = max(index_count, 0)
    return rows * (1 + indexes)


def update_work(update_rows: int, index_count: int, indexed_updates: bool) -> int:
    rows = max(update_rows, 0)
    indexes = max(index_count, 0)
    if not indexed_updates:
        return rows
    return rows * (1 + indexes)


def write_summary(
    insert_rows: int,
    update_rows: int,
    index_count: int,
    indexed_updates: bool,
) -> dict[str, int | float]:
    inserts = insert_work(insert_rows, index_count)
    updates = update_work(update_rows, index_count, indexed_updates)
    base_work = max(insert_rows, 0) + max(update_rows, 0)
    total = inserts + updates
    amplification = 0.0 if base_work == 0 else total / base_work
    return {
        "insert_work": inserts,
        "update_work": updates,
        "total_work": total,
        "amplification_ratio": round(amplification, 2),
    }
