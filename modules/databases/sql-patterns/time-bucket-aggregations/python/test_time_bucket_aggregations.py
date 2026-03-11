from time_bucket_aggregations import (
    create_connection,
    create_metric_table,
    insert_metric,
    totals_by_hour,
    workspace_hour_totals,
)


def test_events_in_the_same_hour_share_one_bucket() -> None:
    conn = create_connection()
    create_metric_table(conn)

    insert_metric(conn, 1, "2026-03-01T10:05:00", 5)
    insert_metric(conn, 1, "2026-03-01T10:45:00", 7)
    insert_metric(conn, 1, "2026-03-01T11:15:00", 3)

    assert totals_by_hour(conn) == [
        ("2026-03-01T10:00", 12),
        ("2026-03-01T11:00", 3),
    ]


def test_workspace_hour_buckets_stay_separate() -> None:
    conn = create_connection()
    create_metric_table(conn)

    insert_metric(conn, 1, "2026-03-01T10:05:00", 5)
    insert_metric(conn, 2, "2026-03-01T10:15:00", 8)
    insert_metric(conn, 1, "2026-03-01T10:45:00", 7)

    assert workspace_hour_totals(conn) == [
        (1, "2026-03-01T10:00", 12),
        (2, "2026-03-01T10:00", 8),
    ]
