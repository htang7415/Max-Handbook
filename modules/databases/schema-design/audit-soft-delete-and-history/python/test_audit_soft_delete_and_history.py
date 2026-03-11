from audit_soft_delete_and_history import (
    audit_history,
    create_audit_schema,
    create_connection,
    insert_document,
    live_documents,
    restore_document,
    soft_delete_document,
)


def test_soft_delete_hides_row_from_live_reads_but_keeps_audit_record() -> None:
    conn = create_connection()
    create_audit_schema(conn)
    document_id = insert_document(conn, "policy", "2026-03-11T09:00:00Z")

    soft_delete_document(conn, document_id, "2026-03-11T10:00:00Z")

    assert live_documents(conn) == []
    assert audit_history(conn, document_id) == [
        ("created", "2026-03-11T09:00:00Z", None),
        ("soft-deleted", "2026-03-11T10:00:00Z", "2026-03-11T10:00:00Z"),
    ]


def test_restore_returns_row_to_live_view_and_preserves_history() -> None:
    conn = create_connection()
    create_audit_schema(conn)
    document_id = insert_document(conn, "policy", "2026-03-11T09:00:00Z")
    soft_delete_document(conn, document_id, "2026-03-11T10:00:00Z")

    restore_document(conn, document_id, "2026-03-11T11:00:00Z")

    assert live_documents(conn) == [(document_id, "policy")]
    assert audit_history(conn, document_id)[-1] == (
        "restored",
        "2026-03-11T11:00:00Z",
        None,
    )
