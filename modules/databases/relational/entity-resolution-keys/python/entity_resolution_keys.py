"""entity_resolution_keys - map many external identifiers onto one canonical entity."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_entity_resolution_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE entities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            canonical_name TEXT NOT NULL
        );

        CREATE TABLE entity_keys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entity_id INTEGER NOT NULL,
            source_system TEXT NOT NULL,
            source_key TEXT NOT NULL,
            key_kind TEXT NOT NULL,
            FOREIGN KEY (entity_id) REFERENCES entities(id) ON DELETE CASCADE,
            UNIQUE (source_system, source_key)
        );
        """
    )


def insert_entity(conn: sqlite3.Connection, canonical_name: str) -> int:
    cursor = conn.execute(
        """
        INSERT INTO entities (canonical_name)
        VALUES (?)
        """,
        (canonical_name,),
    )
    return int(cursor.lastrowid)


def attach_resolution_key(
    conn: sqlite3.Connection,
    entity_id: int,
    source_system: str,
    source_key: str,
    key_kind: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO entity_keys (entity_id, source_system, source_key, key_kind)
        VALUES (?, ?, ?, ?)
        """,
        (entity_id, source_system, source_key, key_kind),
    )
    return int(cursor.lastrowid)


def resolve_entity_id(
    conn: sqlite3.Connection,
    source_system: str,
    source_key: str,
) -> int | None:
    row = conn.execute(
        """
        SELECT entity_id
        FROM entity_keys
        WHERE source_system = ? AND source_key = ?
        """,
        (source_system, source_key),
    ).fetchone()
    if row is None:
        return None
    return int(row[0])


def keys_for_entity(conn: sqlite3.Connection, entity_id: int) -> list[tuple[str, str, str]]:
    rows = conn.execute(
        """
        SELECT source_system, source_key, key_kind
        FROM entity_keys
        WHERE entity_id = ?
        ORDER BY source_system, source_key
        """,
        (entity_id,),
    ).fetchall()
    return [(source_system, source_key, key_kind) for source_system, source_key, key_kind in rows]
