from seq_scan_vs_index_scan import (
    add_workspace_created_index,
    create_connection,
    create_events_table,
    explain_recent_workspace_events,
    plan_flags,
    seed_events,
)


def test_without_index_the_plan_scans_and_sorts() -> None:
    conn = create_connection()
    create_events_table(conn)
    seed_events(
        conn,
        [
            (1, "2026-03-11T09:00:00Z", "sync"),
            (1, "2026-03-11T10:00:00Z", "sync"),
            (2, "2026-03-11T11:00:00Z", "eval"),
            (1, "2026-03-11T12:00:00Z", "sync"),
        ],
    )

    flags = plan_flags(explain_recent_workspace_events(conn, workspace_id=1))

    assert flags["full_scan"] is True
    assert flags["uses_index"] is False
    assert flags["temp_sort"] is True


def test_with_index_the_plan_switches_to_index_lookup() -> None:
    conn = create_connection()
    create_events_table(conn)
    seed_events(
        conn,
        [
            (1, "2026-03-11T09:00:00Z", "sync"),
            (1, "2026-03-11T10:00:00Z", "sync"),
            (2, "2026-03-11T11:00:00Z", "eval"),
            (1, "2026-03-11T12:00:00Z", "sync"),
        ],
    )
    add_workspace_created_index(conn)

    flags = plan_flags(explain_recent_workspace_events(conn, workspace_id=1))

    assert flags["uses_index"] is True
    assert flags["temp_sort"] is False
