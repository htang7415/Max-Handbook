"""duckdb_parquet_query_patterns - partition pruning and column projection mental model."""

from __future__ import annotations


def prune_partitions(
    files: list[dict[str, object]],
    filters: dict[str, object],
) -> list[str]:
    selected: list[str] = []
    for file in files:
        partitions = file.get("partitions", {})
        assert isinstance(partitions, dict)
        if all(partitions.get(key) == value for key, value in filters.items()):
            selected.append(str(file["path"]))
    return selected


def projected_columns(select_columns: list[str], available_columns: list[str]) -> list[str]:
    available = set(available_columns)
    return [column for column in select_columns if column in available]


def query_plan_summary(
    selected_files: list[str],
    selected_columns: list[str],
) -> dict[str, object]:
    return {
        "file_count": len(selected_files),
        "columns": list(selected_columns),
        "can_prune_files": len(selected_files) > 0,
        "can_project_columns": len(selected_columns) > 0,
    }
