"""row_level_security_basics - tenant-scoped policies for reads and writes."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_document_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tenant_id INTEGER NOT NULL,
            title TEXT NOT NULL
        )
        """
    )


def insert_document(conn: sqlite3.Connection, tenant_id: int, title: str) -> int:
    cursor = conn.execute(
        """
        INSERT INTO documents (tenant_id, title)
        VALUES (?, ?)
        """,
        (tenant_id, title),
    )
    return int(cursor.lastrowid)


def can_access_tenant_row(
    session_tenant_id: int,
    row_tenant_id: int,
    is_admin: bool = False,
) -> bool:
    return is_admin or session_tenant_id == row_tenant_id


def visible_documents(
    conn: sqlite3.Connection,
    session_tenant_id: int,
    is_admin: bool = False,
) -> list[tuple[int, str]]:
    if is_admin:
        rows = conn.execute(
            """
            SELECT tenant_id, title
            FROM documents
            ORDER BY tenant_id, id
            """
        ).fetchall()
    else:
        rows = conn.execute(
            """
            SELECT tenant_id, title
            FROM documents
            WHERE tenant_id = ?
            ORDER BY id
            """,
            (session_tenant_id,),
        ).fetchall()
    return [(int(tenant_id), title) for tenant_id, title in rows]


def insert_document_as_session(
    conn: sqlite3.Connection,
    session_tenant_id: int,
    row_tenant_id: int,
    title: str,
    is_admin: bool = False,
) -> int:
    if not can_access_tenant_row(session_tenant_id, row_tenant_id, is_admin):
        raise PermissionError("session cannot write rows for another tenant")
    return insert_document(conn, row_tenant_id, title)
