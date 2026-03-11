"""partition_pruning_basics - monthly partitions plus simple pruning logic."""

from __future__ import annotations

from datetime import date


def month_key(date_text: str) -> str:
    value = date.fromisoformat(date_text)
    return f"{value.year:04d}-{value.month:02d}"


def build_monthly_partitions(
    rows: list[dict[str, object]],
) -> dict[str, list[dict[str, object]]]:
    partitions: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        key = month_key(str(row["event_date"]))
        partitions.setdefault(key, []).append(row)
    return partitions


def pruned_partition_keys(
    partitions: dict[str, list[dict[str, object]]],
    start_date: str,
    end_date: str,
) -> list[str]:
    raw_start = date.fromisoformat(start_date)
    raw_end = date.fromisoformat(end_date)
    if raw_end < raw_start:
        raise ValueError("end_date must be on or after start_date")
    start = raw_start.replace(day=1)
    end = raw_end.replace(day=1)

    keys: list[str] = []
    current = start
    while current <= end:
        key = f"{current.year:04d}-{current.month:02d}"
        if key in partitions:
            keys.append(key)
        if current.month == 12:
            current = date(current.year + 1, 1, 1)
        else:
            current = date(current.year, current.month + 1, 1)
    return keys


def query_partitioned_rows(
    partitions: dict[str, list[dict[str, object]]],
    workspace_id: int,
    start_date: str,
    end_date: str,
) -> tuple[list[str], list[str]]:
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)
    scanned = pruned_partition_keys(partitions, start_date, end_date)
    matches: list[str] = []
    for key in scanned:
        for row in partitions[key]:
            row_date = date.fromisoformat(str(row["event_date"]))
            if int(row["workspace_id"]) != workspace_id:
                continue
            if start <= row_date <= end:
                matches.append(str(row["id"]))
    return scanned, matches
