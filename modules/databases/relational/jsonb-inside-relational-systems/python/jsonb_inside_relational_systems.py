"""jsonb_inside_relational_systems - relational rows with indexed JSON-like metadata."""

from __future__ import annotations

import json
import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_ticket_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER NOT NULL,
            status TEXT NOT NULL,
            title TEXT NOT NULL,
            metadata_json TEXT NOT NULL
        );

        CREATE TABLE ticket_metadata_terms (
            ticket_id INTEGER NOT NULL,
            term TEXT NOT NULL,
            PRIMARY KEY (ticket_id, term),
            FOREIGN KEY (ticket_id) REFERENCES tickets (id) ON DELETE CASCADE
        );

        CREATE INDEX idx_ticket_metadata_terms_term
        ON ticket_metadata_terms (term);
        """
    )


def metadata_terms(metadata: dict[str, object]) -> set[str]:
    terms: set[str] = set()
    for key, value in metadata.items():
        if isinstance(value, list):
            singular = key[:-1] if key.endswith("s") else key
            for item in value:
                terms.add(f"{singular}={item}")
        else:
            terms.add(f"{key}={value}")
    return terms


def insert_ticket(
    conn: sqlite3.Connection,
    workspace_id: int,
    status: str,
    title: str,
    metadata: dict[str, object],
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO tickets (workspace_id, status, title, metadata_json)
        VALUES (?, ?, ?, ?)
        """,
        (workspace_id, status, title, json.dumps(metadata, sort_keys=True)),
    )
    ticket_id = int(cursor.lastrowid)
    _replace_metadata_terms(conn, ticket_id, metadata)
    return ticket_id


def update_ticket_metadata(
    conn: sqlite3.Connection,
    ticket_id: int,
    metadata: dict[str, object],
) -> None:
    conn.execute(
        """
        UPDATE tickets
        SET metadata_json = ?
        WHERE id = ?
        """,
        (json.dumps(metadata, sort_keys=True), ticket_id),
    )
    _replace_metadata_terms(conn, ticket_id, metadata)


def filter_ticket_ids(
    conn: sqlite3.Connection,
    workspace_id: int,
    status: str | None = None,
    required_terms: list[str] | None = None,
) -> list[int]:
    terms = required_terms or []
    if not terms:
        if status is None:
            rows = conn.execute(
                """
                SELECT id
                FROM tickets
                WHERE workspace_id = ?
                ORDER BY id
                """,
                (workspace_id,),
            ).fetchall()
        else:
            rows = conn.execute(
                """
                SELECT id
                FROM tickets
                WHERE workspace_id = ? AND status = ?
                ORDER BY id
                """,
                (workspace_id, status),
            ).fetchall()
        return [int(ticket_id) for (ticket_id,) in rows]

    placeholders = ", ".join("?" for _ in terms)
    params: list[object] = [workspace_id]
    query = [
        """
        SELECT t.id
        FROM tickets AS t
        JOIN ticket_metadata_terms AS m
          ON m.ticket_id = t.id
        WHERE t.workspace_id = ?
        """.strip()
    ]
    if status is not None:
        query.append("AND t.status = ?")
        params.append(status)
    query.append(f"AND m.term IN ({placeholders})")
    params.extend(terms)
    query.append("GROUP BY t.id")
    query.append("HAVING COUNT(DISTINCT m.term) = ?")
    query.append("ORDER BY t.id")
    params.append(len(set(terms)))
    rows = conn.execute("\n".join(query), params).fetchall()
    return [int(ticket_id) for (ticket_id,) in rows]


def ticket_metadata(conn: sqlite3.Connection, ticket_id: int) -> dict[str, object]:
    row = conn.execute(
        """
        SELECT metadata_json
        FROM tickets
        WHERE id = ?
        """,
        (ticket_id,),
    ).fetchone()
    if row is None:
        raise KeyError(ticket_id)
    return json.loads(str(row[0]))


def _replace_metadata_terms(
    conn: sqlite3.Connection,
    ticket_id: int,
    metadata: dict[str, object],
) -> None:
    conn.execute(
        """
        DELETE FROM ticket_metadata_terms
        WHERE ticket_id = ?
        """,
        (ticket_id,),
    )
    conn.executemany(
        """
        INSERT INTO ticket_metadata_terms (ticket_id, term)
        VALUES (?, ?)
        """,
        [(ticket_id, term) for term in sorted(metadata_terms(metadata))],
    )
