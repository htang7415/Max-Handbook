"""phantom_reads_basics - a changing range query can see new matching rows."""

from __future__ import annotations


def task_row(task_id: int, priority: int) -> dict[str, int]:
    return {
        "task_id": task_id,
        "priority": priority,
    }


def matching_task_ids(rows: list[dict[str, int]], min_priority: int) -> list[int]:
    return sorted(
        int(row["task_id"])
        for row in rows
        if int(row["priority"]) >= min_priority
    )


def read_committed_counts(
    initial_rows: list[dict[str, int]],
    inserted_row: dict[str, int],
    min_priority: int,
) -> tuple[int, int]:
    first = len(matching_task_ids(initial_rows, min_priority))
    second = len(matching_task_ids(initial_rows + [inserted_row], min_priority))
    return first, second


def repeatable_read_counts(
    initial_rows: list[dict[str, int]],
    inserted_row: dict[str, int],
    min_priority: int,
) -> tuple[int, int]:
    del inserted_row
    snapshot = [dict(row) for row in initial_rows]
    first = len(matching_task_ids(snapshot, min_priority))
    second = len(matching_task_ids(snapshot, min_priority))
    return first, second


def phantom_summary(
    initial_rows: list[dict[str, int]],
    inserted_row: dict[str, int],
    min_priority: int,
) -> dict[str, object]:
    committed = read_committed_counts(initial_rows, inserted_row, min_priority)
    repeatable = repeatable_read_counts(initial_rows, inserted_row, min_priority)
    return {
        "read_committed": committed,
        "repeatable_read": repeatable,
        "phantom_under_read_committed": committed[1] > committed[0],
        "phantom_under_repeatable_read": repeatable[1] > repeatable[0],
    }
