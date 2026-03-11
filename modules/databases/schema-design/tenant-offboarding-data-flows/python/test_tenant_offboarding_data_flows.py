import pytest

from tenant_offboarding_data_flows import (
    create_connection,
    create_offboarding_schema,
    finalize_offboarding,
    insert_document,
    insert_tenant,
    mark_export_complete,
    request_offboarding,
    tenant_row_counts,
)


def test_cannot_finalize_before_export_completes() -> None:
    conn = create_connection()
    create_offboarding_schema(conn)
    insert_tenant(conn, "tenant-a")
    insert_document(conn, "tenant-a", "doc-1")
    request_offboarding(conn, "tenant-a", "2026-03-11T09:00:00Z")

    with pytest.raises(ValueError, match="export not complete"):
        finalize_offboarding(conn, "tenant-a", "2026-03-11T11:00:00Z")

    assert tenant_row_counts(conn, "tenant-a") == {
        "tenants": 1,
        "tenant_documents": 1,
        "offboarding_jobs": 1,
        "tenant_tombstones": 0,
    }


def test_finalize_deletes_tenant_owned_rows_and_leaves_tombstone() -> None:
    conn = create_connection()
    create_offboarding_schema(conn)
    insert_tenant(conn, "tenant-a")
    insert_document(conn, "tenant-a", "doc-1")
    insert_document(conn, "tenant-a", "doc-2")
    request_offboarding(conn, "tenant-a", "2026-03-11T09:00:00Z")
    mark_export_complete(conn, "tenant-a", "2026-03-11T10:00:00Z")

    finalize_offboarding(conn, "tenant-a", "2026-03-11T11:00:00Z")

    assert tenant_row_counts(conn, "tenant-a") == {
        "tenants": 0,
        "tenant_documents": 0,
        "offboarding_jobs": 0,
        "tenant_tombstones": 1,
    }
