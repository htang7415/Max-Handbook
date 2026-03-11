from soft_delete_and_tombstone_patterns import (
    all_document_rows,
    create_connection,
    create_delete_demo_schema,
    hard_delete_with_tombstone,
    insert_document,
    live_documents,
    soft_delete_document,
    tombstone_rows,
)


def test_soft_delete_hides_row_but_keeps_it_in_the_base_table() -> None:
    conn = create_connection()
    create_delete_demo_schema(conn)

    first = insert_document(conn, "Guide")
    second = insert_document(conn, "Playbook")
    soft_delete_document(conn, first, "2026-03-01T10:00:00")

    assert live_documents(conn) == [(second, "Playbook")]
    assert all_document_rows(conn) == [
        (first, "Guide", "2026-03-01T10:00:00"),
        (second, "Playbook", None),
    ]


def test_tombstone_keeps_delete_metadata_after_the_row_is_removed() -> None:
    conn = create_connection()
    create_delete_demo_schema(conn)

    document_id = insert_document(conn, "Spec")
    hard_delete_with_tombstone(conn, document_id, "2026-03-01T11:00:00", "privacy-request")

    assert all_document_rows(conn) == []
    assert tombstone_rows(conn) == [
        (document_id, "2026-03-01T11:00:00", "privacy-request"),
    ]
