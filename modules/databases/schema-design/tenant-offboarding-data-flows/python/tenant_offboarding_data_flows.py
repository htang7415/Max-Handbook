"""tenant_offboarding_data_flows - stateful tenant deletion with export gating."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_offboarding_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE tenants (
            tenant_id TEXT PRIMARY KEY
        );

        CREATE TABLE tenant_documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tenant_id TEXT NOT NULL,
            document_id TEXT NOT NULL,
            FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id) ON DELETE CASCADE
        );

        CREATE TABLE offboarding_jobs (
            tenant_id TEXT PRIMARY KEY,
            requested_at TEXT NOT NULL,
            exported_at TEXT,
            FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id) ON DELETE CASCADE
        );

        CREATE TABLE tenant_tombstones (
            tenant_id TEXT PRIMARY KEY,
            deleted_at TEXT NOT NULL
        );
        """
    )


def insert_tenant(conn: sqlite3.Connection, tenant_id: str) -> None:
    conn.execute(
        """
        INSERT INTO tenants (tenant_id)
        VALUES (?)
        """,
        (tenant_id,),
    )


def insert_document(conn: sqlite3.Connection, tenant_id: str, document_id: str) -> None:
    conn.execute(
        """
        INSERT INTO tenant_documents (tenant_id, document_id)
        VALUES (?, ?)
        """,
        (tenant_id, document_id),
    )


def request_offboarding(conn: sqlite3.Connection, tenant_id: str, requested_at: str) -> None:
    conn.execute(
        """
        INSERT INTO offboarding_jobs (tenant_id, requested_at)
        VALUES (?, ?)
        """,
        (tenant_id, requested_at),
    )


def mark_export_complete(conn: sqlite3.Connection, tenant_id: str, exported_at: str) -> None:
    conn.execute(
        """
        UPDATE offboarding_jobs
        SET exported_at = ?
        WHERE tenant_id = ?
        """,
        (exported_at, tenant_id),
    )


def finalize_offboarding(conn: sqlite3.Connection, tenant_id: str, deleted_at: str) -> None:
    row = conn.execute(
        """
        SELECT exported_at
        FROM offboarding_jobs
        WHERE tenant_id = ?
        """,
        (tenant_id,),
    ).fetchone()
    if row is None:
        raise ValueError(f"missing offboarding request for {tenant_id}")
    if row[0] is None:
        raise ValueError(f"export not complete for {tenant_id}")

    conn.execute(
        """
        INSERT INTO tenant_tombstones (tenant_id, deleted_at)
        VALUES (?, ?)
        """,
        (tenant_id, deleted_at),
    )
    conn.execute(
        """
        DELETE FROM tenants
        WHERE tenant_id = ?
        """,
        (tenant_id,),
    )


def tenant_row_counts(conn: sqlite3.Connection, tenant_id: str) -> dict[str, int]:
    tables = {
        "tenants": "SELECT COUNT(*) FROM tenants WHERE tenant_id = ?",
        "tenant_documents": "SELECT COUNT(*) FROM tenant_documents WHERE tenant_id = ?",
        "offboarding_jobs": "SELECT COUNT(*) FROM offboarding_jobs WHERE tenant_id = ?",
        "tenant_tombstones": "SELECT COUNT(*) FROM tenant_tombstones WHERE tenant_id = ?",
    }
    counts: dict[str, int] = {}
    for key, query in tables.items():
        row = conn.execute(query, (tenant_id,)).fetchone()
        assert row is not None
        counts[key] = int(row[0])
    return counts
