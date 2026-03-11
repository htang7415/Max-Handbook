import pytest

from row_level_security_basics import (
    create_connection,
    create_document_table,
    insert_document,
    insert_document_as_session,
    visible_documents,
)


def test_non_admin_sessions_only_see_their_own_tenant_rows() -> None:
    conn = create_connection()
    create_document_table(conn)

    insert_document(conn, 1, "Tenant 1 Guide")
    insert_document(conn, 2, "Tenant 2 Guide")

    assert visible_documents(conn, session_tenant_id=1) == [(1, "Tenant 1 Guide")]
    assert visible_documents(conn, session_tenant_id=2) == [(2, "Tenant 2 Guide")]


def test_admin_can_see_all_rows() -> None:
    conn = create_connection()
    create_document_table(conn)

    insert_document(conn, 1, "Tenant 1 Guide")
    insert_document(conn, 2, "Tenant 2 Guide")

    assert visible_documents(conn, session_tenant_id=1, is_admin=True) == [
        (1, "Tenant 1 Guide"),
        (2, "Tenant 2 Guide"),
    ]


def test_write_policy_blocks_cross_tenant_inserts() -> None:
    conn = create_connection()
    create_document_table(conn)

    insert_document_as_session(conn, session_tenant_id=1, row_tenant_id=1, title="Safe")
    with pytest.raises(PermissionError):
        insert_document_as_session(conn, session_tenant_id=1, row_tenant_id=2, title="Unsafe")
