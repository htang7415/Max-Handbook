from prefix_search_and_like_indexing import (
    add_name_index,
    create_connection,
    create_users_table,
    like_prefix_plan,
    matching_names,
    plan_flags,
    seed_names,
)


def test_without_index_prefix_like_scans_table() -> None:
    conn = create_connection()
    create_users_table(conn)
    seed_names(conn, ["ada", "adaline", "alan", "grace"])

    flags = plan_flags(like_prefix_plan(conn, "ada"))

    assert flags["full_scan"] is True
    assert flags["uses_index"] is False


def test_with_index_prefix_like_uses_btree_range_lookup() -> None:
    conn = create_connection()
    create_users_table(conn)
    seed_names(conn, ["ada", "adaline", "alan", "grace"])
    add_name_index(conn)

    flags = plan_flags(like_prefix_plan(conn, "ada"))

    assert flags["uses_index"] is True
    assert matching_names(conn, "ada") == ["ada", "adaline"]
