from outer_join_filter_traps import (
    create_connection,
    create_demo_tables,
    open_tasks_filter_in_on,
    open_tasks_filter_in_where,
    projects_without_open_tasks,
    seed_projects,
    seed_tasks,
)


def test_where_filter_on_right_table_turns_left_join_into_inner_join() -> None:
    conn = create_connection()
    create_demo_tables(conn)
    seed_projects(conn, [(1, "alpha"), (2, "beta"), (3, "gamma")])
    seed_tasks(conn, [(2, "closed-task", "closed"), (3, "open-task", "open")])

    assert open_tasks_filter_in_where(conn) == ["gamma"]


def test_filter_in_on_preserves_projects_without_open_tasks() -> None:
    conn = create_connection()
    create_demo_tables(conn)
    seed_projects(conn, [(1, "alpha"), (2, "beta"), (3, "gamma")])
    seed_tasks(conn, [(2, "closed-task", "closed"), (3, "open-task", "open")])

    assert open_tasks_filter_in_on(conn) == [
        ("alpha", None),
        ("beta", None),
        ("gamma", "open-task"),
    ]
    assert projects_without_open_tasks(conn) == ["alpha", "beta"]
