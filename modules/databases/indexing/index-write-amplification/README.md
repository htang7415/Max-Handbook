# Index Write Amplification

> Track: `databases` | Topic: `indexing`

## Concept

Every extra index speeds up some reads, but inserts and key-changing updates must maintain that index too. Write amplification is the reason “just add another index” becomes expensive on hot OLTP tables.

## Key Points

- Inserts usually touch every secondary index.
- Updates only pay index maintenance when indexed columns change.
- Read-optimized schemas can become write bottlenecks.
- Index count should follow actual query value, not wishful future queries.

## Minimal Code Mental Model

```python
summary = write_summary(insert_rows=1000, update_rows=200, index_count=4, indexed_updates=True)
```

## Function

```python
def insert_work(insert_rows: int, index_count: int) -> int:
def update_work(update_rows: int, index_count: int, indexed_updates: bool) -> int:
def write_summary(
    insert_rows: int,
    update_rows: int,
    index_count: int,
    indexed_updates: bool,
) -> dict[str, int | float]:
```

## Run tests

```bash
pytest modules/databases/indexing/index-write-amplification/python -q
```
