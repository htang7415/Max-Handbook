import sqlite3

import pytest

from asset_versioning import (
    create_asset_versioning_schema,
    create_connection,
    insert_asset,
    latest_version,
    publish_asset_version,
    version_history,
)


def build_connection():
    conn = create_connection()
    create_asset_versioning_schema(conn)
    asset_id = insert_asset(conn, 42, "prompt-template")
    return conn, asset_id


def test_history_keeps_immutable_versions_in_order() -> None:
    conn, asset_id = build_connection()
    publish_asset_version(conn, asset_id, "v1", "hash-a", "2026-03-11T10:00:00Z")
    publish_asset_version(conn, asset_id, "v2", "hash-b", "2026-03-11T11:00:00Z")

    assert version_history(conn, asset_id) == [
        ("v1", "hash-a", "2026-03-11T10:00:00Z"),
        ("v2", "hash-b", "2026-03-11T11:00:00Z"),
    ]


def test_latest_version_returns_the_newest_published_snapshot() -> None:
    conn, asset_id = build_connection()
    publish_asset_version(conn, asset_id, "v1", "hash-a", "2026-03-11T10:00:00Z")
    publish_asset_version(conn, asset_id, "v2", "hash-b", "2026-03-11T11:00:00Z")

    assert latest_version(conn, asset_id) == (
        "v2",
        "hash-b",
        "2026-03-11T11:00:00Z",
    )


def test_same_asset_cannot_publish_duplicate_label_or_duplicate_content_hash() -> None:
    conn, asset_id = build_connection()
    publish_asset_version(conn, asset_id, "v1", "hash-a", "2026-03-11T10:00:00Z")

    with pytest.raises(sqlite3.IntegrityError):
        publish_asset_version(conn, asset_id, "v1", "hash-b", "2026-03-11T11:00:00Z")

    with pytest.raises(sqlite3.IntegrityError):
        publish_asset_version(conn, asset_id, "v2", "hash-a", "2026-03-11T11:00:00Z")
