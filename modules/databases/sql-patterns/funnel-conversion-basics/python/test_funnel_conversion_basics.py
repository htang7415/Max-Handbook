from funnel_conversion_basics import (
    conversion_rates,
    create_connection,
    create_funnel_events_table,
    funnel_counts,
    insert_funnel_event,
)


def test_funnel_counts_require_users_to_progress_in_order() -> None:
    conn = create_connection()
    create_funnel_events_table(conn)

    insert_funnel_event(conn, "u1", "visit", "2026-01-01T09:00:00")
    insert_funnel_event(conn, "u1", "signup", "2026-01-01T09:05:00")
    insert_funnel_event(conn, "u1", "activate", "2026-01-01T09:10:00")

    insert_funnel_event(conn, "u2", "visit", "2026-01-01T09:00:00")
    insert_funnel_event(conn, "u2", "signup", "2026-01-01T09:15:00")

    insert_funnel_event(conn, "u3", "visit", "2026-01-01T10:00:00")

    insert_funnel_event(conn, "u4", "signup", "2026-01-01T10:05:00")
    insert_funnel_event(conn, "u4", "activate", "2026-01-01T10:10:00")

    stages = ["visit", "signup", "activate"]
    assert funnel_counts(conn, stages) == [
        ("visit", 3),
        ("signup", 2),
        ("activate", 1),
    ]


def test_conversion_rates_normalize_each_stage_against_the_previous_stage() -> None:
    conn = create_connection()
    create_funnel_events_table(conn)

    insert_funnel_event(conn, "u1", "visit", "2026-01-01T09:00:00")
    insert_funnel_event(conn, "u1", "signup", "2026-01-01T09:05:00")
    insert_funnel_event(conn, "u1", "activate", "2026-01-01T09:10:00")

    insert_funnel_event(conn, "u2", "visit", "2026-01-01T09:00:00")
    insert_funnel_event(conn, "u2", "signup", "2026-01-01T09:15:00")

    insert_funnel_event(conn, "u3", "visit", "2026-01-01T10:00:00")

    stages = ["visit", "signup", "activate"]
    assert conversion_rates(conn, stages) == [
        ("visit", 1.0),
        ("signup", 2 / 3),
        ("activate", 0.5),
    ]
