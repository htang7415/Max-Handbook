from sessionization_basics import (
    create_connection,
    create_event_table,
    insert_event,
    session_counts,
    sessionized_events,
)


def test_gap_threshold_starts_new_sessions() -> None:
    conn = create_connection()
    create_event_table(conn)

    for minute in [0, 5, 40]:
        insert_event(conn, "u1", minute)
    for minute in [2, 10, 50]:
        insert_event(conn, "u2", minute)

    assert sessionized_events(conn, gap_minutes=30) == [
        ("u1", 0, 1),
        ("u1", 5, 1),
        ("u1", 40, 2),
        ("u2", 2, 1),
        ("u2", 10, 1),
        ("u2", 50, 2),
    ]


def test_session_counts_roll_up_per_user() -> None:
    conn = create_connection()
    create_event_table(conn)

    for minute in [0, 5, 40]:
        insert_event(conn, "u1", minute)
    for minute in [2, 10, 50]:
        insert_event(conn, "u2", minute)

    assert session_counts(conn, gap_minutes=30) == [
        ("u1", 2),
        ("u2", 2),
    ]
