from foreign_key_cascades import (
    create_cascade_schema,
    create_connection,
    delete_document,
    delete_workspace,
    insert_chunk,
    insert_document,
    insert_workspace,
    row_counts,
)


def test_deleting_document_cascades_to_chunks_only() -> None:
    conn = create_connection()
    create_cascade_schema(conn)
    workspace_id = insert_workspace(conn, "alpha")
    document_id = insert_document(conn, workspace_id, "doc-1")
    insert_chunk(conn, document_id, "a")
    insert_chunk(conn, document_id, "b")

    delete_document(conn, document_id)

    assert row_counts(conn) == {
        "workspaces": 1,
        "documents": 0,
        "chunks": 0,
    }


def test_deleting_workspace_cascades_through_documents_and_chunks() -> None:
    conn = create_connection()
    create_cascade_schema(conn)
    workspace_id = insert_workspace(conn, "alpha")
    document_id = insert_document(conn, workspace_id, "doc-1")
    insert_chunk(conn, document_id, "a")

    delete_workspace(conn, workspace_id)

    assert row_counts(conn) == {
        "workspaces": 0,
        "documents": 0,
        "chunks": 0,
    }
