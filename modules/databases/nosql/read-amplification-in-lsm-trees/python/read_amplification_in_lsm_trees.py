"""read_amplification_in_lsm_trees - estimate how many files a point read may touch."""

from __future__ import annotations


def validate_level_sstables(level_sstables: list[int]) -> None:
    if any(count < 0 for count in level_sstables):
        raise ValueError("level_sstables counts must be non-negative")


def tables_checked_without_bloom(level_sstables: list[int]) -> int:
    validate_level_sstables(level_sstables)
    return sum(level_sstables)


def tables_checked_with_bloom(
    level_sstables: list[int],
    false_positive_tables: int = 0,
) -> int:
    validate_level_sstables(level_sstables)
    if false_positive_tables < 0:
        raise ValueError("false_positive_tables must be non-negative")
    non_empty_levels = sum(1 for count in level_sstables if count > 0)
    return non_empty_levels + false_positive_tables


def point_lookup_cost(
    level_sstables: list[int],
    false_positive_tables: int = 0,
    table_read_ms: int = 1,
) -> dict[str, int]:
    if table_read_ms < 0:
        raise ValueError("table_read_ms must be non-negative")
    without_bloom = tables_checked_without_bloom(level_sstables)
    with_bloom = tables_checked_with_bloom(level_sstables, false_positive_tables)
    return {
        "tables_without_bloom": without_bloom,
        "tables_with_bloom": with_bloom,
        "latency_without_bloom_ms": without_bloom * table_read_ms,
        "latency_with_bloom_ms": with_bloom * table_read_ms,
    }
