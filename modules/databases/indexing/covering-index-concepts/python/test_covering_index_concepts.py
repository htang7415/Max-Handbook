from covering_index_concepts import (
    add_covering_index,
    add_non_covering_index,
    create_connection,
    create_documents_table,
    plan_summary,
    query_plan,
    query_rows,
    seed_documents,
)


def build_connection():
    conn = create_connection()
    create_documents_table(conn)
    seed_documents(
        conn,
        [
            (7, "spec", "2026-03-11T10:00:00Z"),
            (7, "notes", "2026-03-11T11:00:00Z"),
            (8, "other", "2026-03-11T12:00:00Z"),
        ],
    )
    return conn


def test_non_covering_index_helps_but_is_not_index_only() -> None:
    conn = build_connection()
    add_non_covering_index(conn)

    assert plan_summary(query_plan(conn, 7)) == {
        "uses_index": True,
        "uses_covering_index": False,
        "temp_sort": False,
    }


def test_covering_index_changes_the_plan_to_index_only_access() -> None:
    conn = build_connection()
    add_covering_index(conn)

    assert plan_summary(query_plan(conn, 7)) == {
        "uses_index": True,
        "uses_covering_index": True,
        "temp_sort": False,
    }


def test_covering_index_does_not_change_query_results() -> None:
    conn = build_connection()
    before = query_rows(conn, 7)
    add_covering_index(conn)
    after = query_rows(conn, 7)

    assert before == after == [
        ("notes", "2026-03-11T11:00:00Z"),
        ("spec", "2026-03-11T10:00:00Z"),
    ]
