"""asset_versioning - immutable version rows for datasets, prompts, and configs."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_asset_versioning_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            UNIQUE (workspace_id, name)
        );

        CREATE TABLE asset_versions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_id INTEGER NOT NULL,
            version_label TEXT NOT NULL,
            content_hash TEXT NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY (asset_id) REFERENCES assets(id) ON DELETE CASCADE,
            UNIQUE (asset_id, version_label),
            UNIQUE (asset_id, content_hash)
        );
        """
    )


def insert_asset(conn: sqlite3.Connection, workspace_id: int, name: str) -> int:
    cursor = conn.execute(
        """
        INSERT INTO assets (workspace_id, name)
        VALUES (?, ?)
        """,
        (workspace_id, name),
    )
    return int(cursor.lastrowid)


def publish_asset_version(
    conn: sqlite3.Connection,
    asset_id: int,
    version_label: str,
    content_hash: str,
    created_at: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO asset_versions (asset_id, version_label, content_hash, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (asset_id, version_label, content_hash, created_at),
    )
    return int(cursor.lastrowid)


def version_history(
    conn: sqlite3.Connection,
    asset_id: int,
) -> list[tuple[str, str, str]]:
    rows = conn.execute(
        """
        SELECT version_label, content_hash, created_at
        FROM asset_versions
        WHERE asset_id = ?
        ORDER BY created_at, id
        """,
        (asset_id,),
    ).fetchall()
    return [(label, content_hash, created_at) for label, content_hash, created_at in rows]


def latest_version(
    conn: sqlite3.Connection,
    asset_id: int,
) -> tuple[str, str, str] | None:
    row = conn.execute(
        """
        SELECT version_label, content_hash, created_at
        FROM asset_versions
        WHERE asset_id = ?
        ORDER BY created_at DESC, id DESC
        LIMIT 1
        """,
        (asset_id,),
    ).fetchone()
    if row is None:
        return None
    return row[0], row[1], row[2]
