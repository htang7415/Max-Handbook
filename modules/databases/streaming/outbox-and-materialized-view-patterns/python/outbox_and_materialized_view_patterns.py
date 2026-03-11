"""outbox_and_materialized_view_patterns - transactional events plus incremental views."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.isolation_level = None
    return conn


def create_pipeline_tables(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE orders (
            order_id TEXT PRIMARY KEY,
            workspace_id INTEGER NOT NULL,
            status TEXT NOT NULL
        );

        CREATE TABLE outbox (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id TEXT NOT NULL,
            workspace_id INTEGER NOT NULL,
            status TEXT NOT NULL,
            projected_at TEXT
        );

        CREATE TABLE projected_orders (
            order_id TEXT PRIMARY KEY,
            workspace_id INTEGER NOT NULL,
            status TEXT NOT NULL
        );

        CREATE TABLE workspace_status_view (
            workspace_id INTEGER NOT NULL,
            status TEXT NOT NULL,
            total INTEGER NOT NULL,
            PRIMARY KEY (workspace_id, status)
        );
        """
    )


def write_order_status(
    conn: sqlite3.Connection,
    order_id: str,
    workspace_id: int,
    status: str,
    fail_before_outbox: bool = False,
) -> None:
    conn.execute("BEGIN")
    try:
        conn.execute(
            """
            INSERT INTO orders (order_id, workspace_id, status)
            VALUES (?, ?, ?)
            ON CONFLICT(order_id) DO UPDATE SET
                workspace_id = excluded.workspace_id,
                status = excluded.status
            """,
            (order_id, workspace_id, status),
        )
        if fail_before_outbox:
            raise RuntimeError("simulated failure before writing outbox")
        conn.execute(
            """
            INSERT INTO outbox (order_id, workspace_id, status, projected_at)
            VALUES (?, ?, ?, NULL)
            """,
            (order_id, workspace_id, status),
        )
        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise


def order_rows(conn: sqlite3.Connection) -> list[tuple[str, int, str]]:
    rows = conn.execute(
        """
        SELECT order_id, workspace_id, status
        FROM orders
        ORDER BY order_id
        """
    ).fetchall()
    return [(str(order_id), int(workspace_id), str(status)) for order_id, workspace_id, status in rows]


def outbox_event_rows(
    conn: sqlite3.Connection,
) -> list[tuple[int, str, int, str, str | None]]:
    rows = conn.execute(
        """
        SELECT id, order_id, workspace_id, status, projected_at
        FROM outbox
        ORDER BY id
        """
    ).fetchall()
    return [
        (int(event_id), str(order_id), int(workspace_id), str(status), None if projected_at is None else str(projected_at))
        for event_id, order_id, workspace_id, status, projected_at in rows
    ]


def next_unprojected_event(
    conn: sqlite3.Connection,
) -> tuple[int, str, int, str] | None:
    row = conn.execute(
        """
        SELECT id, order_id, workspace_id, status
        FROM outbox
        WHERE projected_at IS NULL
        ORDER BY id
        LIMIT 1
        """
    ).fetchone()
    if row is None:
        return None
    event_id, order_id, workspace_id, status = row
    return int(event_id), str(order_id), int(workspace_id), str(status)


def project_next_event(conn: sqlite3.Connection) -> int | None:
    event = next_unprojected_event(conn)
    if event is None:
        return None

    event_id, order_id, workspace_id, status = event
    conn.execute("BEGIN")
    try:
        previous = conn.execute(
            """
            SELECT workspace_id, status
            FROM projected_orders
            WHERE order_id = ?
            """,
            (order_id,),
        ).fetchone()
        if previous is not None:
            old_workspace_id, old_status = previous
            _adjust_count(conn, int(old_workspace_id), str(old_status), -1)

        conn.execute(
            """
            INSERT INTO projected_orders (order_id, workspace_id, status)
            VALUES (?, ?, ?)
            ON CONFLICT(order_id) DO UPDATE SET
                workspace_id = excluded.workspace_id,
                status = excluded.status
            """,
            (order_id, workspace_id, status),
        )
        _adjust_count(conn, workspace_id, status, 1)
        conn.execute(
            """
            UPDATE outbox
            SET projected_at = 'projected'
            WHERE id = ?
            """,
            (event_id,),
        )
        conn.execute("COMMIT")
        return event_id
    except Exception:
        conn.execute("ROLLBACK")
        raise


def workspace_status_totals(
    conn: sqlite3.Connection,
    workspace_id: int,
) -> dict[str, int]:
    rows = conn.execute(
        """
        SELECT status, total
        FROM workspace_status_view
        WHERE workspace_id = ?
        ORDER BY status
        """,
        (workspace_id,),
    ).fetchall()
    return {str(status): int(total) for status, total in rows if int(total) > 0}


def rebuild_workspace_status_view(
    events: list[tuple[str, int, str]],
) -> dict[int, dict[str, int]]:
    latest_by_order: dict[str, tuple[int, str]] = {}
    counts_by_workspace: dict[int, dict[str, int]] = {}

    for order_id, workspace_id, status in events:
        previous = latest_by_order.get(order_id)
        if previous is not None:
            old_workspace_id, old_status = previous
            old_counts = counts_by_workspace.setdefault(old_workspace_id, {})
            old_counts[old_status] = max(old_counts.get(old_status, 0) - 1, 0)

        workspace_counts = counts_by_workspace.setdefault(workspace_id, {})
        workspace_counts[status] = workspace_counts.get(status, 0) + 1
        latest_by_order[order_id] = (workspace_id, status)

    return {
        workspace_id: {status: total for status, total in counts.items() if total > 0}
        for workspace_id, counts in counts_by_workspace.items()
    }


def _adjust_count(
    conn: sqlite3.Connection,
    workspace_id: int,
    status: str,
    delta: int,
) -> None:
    row = conn.execute(
        """
        SELECT total
        FROM workspace_status_view
        WHERE workspace_id = ? AND status = ?
        """,
        (workspace_id, status),
    ).fetchone()
    current = 0 if row is None else int(row[0])
    updated = current + delta
    if updated <= 0:
        conn.execute(
            """
            DELETE FROM workspace_status_view
            WHERE workspace_id = ? AND status = ?
            """,
            (workspace_id, status),
        )
        return
    conn.execute(
        """
        INSERT INTO workspace_status_view (workspace_id, status, total)
        VALUES (?, ?, ?)
        ON CONFLICT(workspace_id, status) DO UPDATE SET total = excluded.total
        """,
        (workspace_id, status, updated),
    )
