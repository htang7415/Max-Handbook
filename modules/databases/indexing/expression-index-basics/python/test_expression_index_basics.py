from expression_index_basics import (
    add_lower_email_index,
    create_connection,
    create_users_table,
    explain_lookup_by_lower_email,
    matching_names,
    plan_flags,
    seed_users,
)


def test_without_expression_index_case_insensitive_lookup_scans() -> None:
    conn = create_connection()
    create_users_table(conn)
    seed_users(
        conn,
        [
            ("Ada", "Ada@Example.com"),
            ("Linus", "linus@example.com"),
            ("Grace", "grace@example.com"),
        ],
    )

    flags = plan_flags(explain_lookup_by_lower_email(conn, "ada@example.com"))

    assert flags["full_scan"] is True
    assert flags["uses_expression_index"] is False


def test_expression_index_supports_lowercase_lookup() -> None:
    conn = create_connection()
    create_users_table(conn)
    seed_users(
        conn,
        [
            ("Ada", "Ada@Example.com"),
            ("Linus", "linus@example.com"),
            ("Grace", "grace@example.com"),
        ],
    )
    add_lower_email_index(conn)

    flags = plan_flags(explain_lookup_by_lower_email(conn, "ada@example.com"))

    assert flags["uses_expression_index"] is True
    assert matching_names(conn, "ada@example.com") == ["Ada"]
