# Asset Versioning

> Track: `databases` | Topic: `schema-design`

## Concept

Versioned assets keep immutable historical snapshots while still letting the system ask for the current version.

## Key Points

- Immutable versions make rollback and reproducibility easier.
- Version labels and content hashes usually need uniqueness per asset.
- Current state can be derived from the latest version instead of overwriting old rows.
- Asset versioning matters for datasets, prompts, configs, and model artifacts in AI systems.

## Minimal Code Mental Model

```python
conn = create_connection()
create_asset_versioning_schema(conn)
asset_id = insert_asset(conn, 42, "prompt-template")
publish_asset_version(conn, asset_id, "v1", "hash-a", "2026-03-11T10:00:00Z")
publish_asset_version(conn, asset_id, "v2", "hash-b", "2026-03-11T11:00:00Z")
latest = latest_version(conn, asset_id)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_asset_versioning_schema(conn: sqlite3.Connection) -> None:
def insert_asset(conn: sqlite3.Connection, workspace_id: int, name: str) -> int:
def publish_asset_version(
    conn: sqlite3.Connection,
    asset_id: int,
    version_label: str,
    content_hash: str,
    created_at: str,
) -> int:
def version_history(
    conn: sqlite3.Connection,
    asset_id: int,
) -> list[tuple[str, str, str]]:
def latest_version(
    conn: sqlite3.Connection,
    asset_id: int,
) -> tuple[str, str, str] | None:
```

## Run tests

```bash
pytest modules/databases/schema-design/asset-versioning/python -q
```
