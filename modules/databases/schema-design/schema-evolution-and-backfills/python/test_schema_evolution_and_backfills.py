from schema_evolution_and_backfills import (
    backfill_priority,
    create_connection,
    create_job_table_v1,
    evolve_to_v2_add_priority,
    insert_job_v1,
    insert_job_v2,
    job_rows,
    null_priority_count,
)


def test_additive_column_allows_old_rows_before_backfill() -> None:
    conn = create_connection()
    create_job_table_v1(conn)
    insert_job_v1(conn, "ingest", "batch")
    evolve_to_v2_add_priority(conn)
    insert_job_v2(conn, "alert", "incident", "urgent")

    assert null_priority_count(conn) == 1


def test_backfill_fills_missing_priority_without_overwriting_new_rows() -> None:
    conn = create_connection()
    create_job_table_v1(conn)
    insert_job_v1(conn, "ingest", "batch")
    insert_job_v1(conn, "page", "incident")
    evolve_to_v2_add_priority(conn)
    insert_job_v2(conn, "notify", "incident", "urgent")

    backfill_priority(conn)

    assert job_rows(conn) == [
        ("ingest", "batch", "normal"),
        ("page", "incident", "high"),
        ("notify", "incident", "urgent"),
    ]
