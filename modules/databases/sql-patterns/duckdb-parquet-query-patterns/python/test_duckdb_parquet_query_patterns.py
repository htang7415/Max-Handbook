from duckdb_parquet_query_patterns import (
    projected_columns,
    prune_partitions,
    query_plan_summary,
)


FILES = [
    {"path": "runs/day=2026-03-10/part-0.parquet", "partitions": {"day": "2026-03-10"}},
    {"path": "runs/day=2026-03-11/part-0.parquet", "partitions": {"day": "2026-03-11"}},
    {"path": "runs/day=2026-03-11/part-1.parquet", "partitions": {"day": "2026-03-11"}},
]


def test_partition_pruning_keeps_only_matching_parquet_fragments() -> None:
    assert prune_partitions(FILES, {"day": "2026-03-11"}) == [
        "runs/day=2026-03-11/part-0.parquet",
        "runs/day=2026-03-11/part-1.parquet",
    ]


def test_projection_keeps_only_requested_available_columns() -> None:
    assert projected_columns(
        ["workspace_id", "score", "missing"],
        ["day", "workspace_id", "score"],
    ) == ["workspace_id", "score"]


def test_plan_summary_reflects_file_and_column_pruning() -> None:
    summary = query_plan_summary(
        ["runs/day=2026-03-11/part-0.parquet"],
        ["workspace_id", "score"],
    )

    assert summary == {
        "file_count": 1,
        "columns": ["workspace_id", "score"],
        "can_prune_files": True,
        "can_project_columns": True,
    }
