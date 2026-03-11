from rollups_vs_raw_events import (
    create_connection,
    create_rollup_schema,
    insert_event,
    raw_total,
    rebuild_hourly_rollups,
    rollup_total,
    row_counts,
)


def test_rollups_match_raw_totals_after_rebuild() -> None:
    conn = create_connection()
    create_rollup_schema(conn)

    insert_event(conn, 1, "2026-03-01T10:00", 5)
    insert_event(conn, 1, "2026-03-01T10:00", 7)
    insert_event(conn, 1, "2026-03-01T11:00", 3)
    rebuild_hourly_rollups(conn)

    assert raw_total(conn, 1, "2026-03-01T10:00") == 12
    assert rollup_total(conn, 1, "2026-03-01T10:00") == 12
    assert row_counts(conn) == {"raw_events": 3, "hourly_rollups": 2}


def test_rollups_go_stale_until_they_are_rebuilt() -> None:
    conn = create_connection()
    create_rollup_schema(conn)

    insert_event(conn, 1, "2026-03-01T10:00", 5)
    rebuild_hourly_rollups(conn)
    insert_event(conn, 1, "2026-03-01T10:00", 7)

    assert raw_total(conn, 1, "2026-03-01T10:00") == 12
    assert rollup_total(conn, 1, "2026-03-01T10:00") == 5
