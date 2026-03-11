from null_semantics_in_joins import (
    create_connection,
    create_demo_tables,
    inner_join_ticket_assignees,
    left_join_ticket_assignees,
    seed_tickets,
    seed_users,
    unassigned_tickets,
)


def test_inner_join_drops_rows_with_null_join_keys() -> None:
    conn = create_connection()
    create_demo_tables(conn)
    seed_users(conn, [(1, "Ada")])
    seed_tickets(conn, [("bug", 1), ("ops follow-up", None)])

    assert inner_join_ticket_assignees(conn) == [("bug", "Ada")]


def test_left_join_and_is_null_filter_preserve_unassigned_rows() -> None:
    conn = create_connection()
    create_demo_tables(conn)
    seed_users(conn, [(1, "Ada")])
    seed_tickets(conn, [("bug", 1), ("ops follow-up", None)])

    assert left_join_ticket_assignees(conn) == [
        ("bug", "Ada"),
        ("ops follow-up", None),
    ]
    assert unassigned_tickets(conn) == ["ops follow-up"]
