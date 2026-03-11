# Normalization Vs Denormalization

> Track: `databases` | Topic: `schema-design`

## Concept

Normalization keeps shared facts in one place, while denormalization duplicates some of those facts to speed up specific read paths.

## Key Points

- A normalized design reduces duplicate data and update fanout.
- A denormalized design can answer hot reads without joins.
- Denormalization shifts complexity from reads to writes because copied fields must stay in sync.
- Good systems often normalize the source of truth first, then add targeted denormalized read models later.

## Minimal Code Mental Model

```python
conn = create_connection()
create_normalization_demo_schema(conn)
customer_id = insert_customer(conn, "Acme")
insert_order_rows(conn, customer_id, ["A-1", "A-2"])
rename_customer(conn, customer_id, "Acme Labs")
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_normalization_demo_schema(conn: sqlite3.Connection) -> None:
def insert_customer(conn: sqlite3.Connection, name: str) -> int:
def insert_order_rows(
    conn: sqlite3.Connection,
    customer_id: int,
    order_codes: list[str],
) -> None:
def normalized_order_feed(conn: sqlite3.Connection) -> list[tuple[str, str]]:
def denormalized_order_feed(conn: sqlite3.Connection) -> list[tuple[str, str]]:
def rename_customer(conn: sqlite3.Connection, customer_id: int, new_name: str) -> tuple[int, int]:
```

## Run tests

```bash
pytest modules/databases/schema-design/normalization-vs-denormalization/python -q
```
