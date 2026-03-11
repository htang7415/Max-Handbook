# Read Amplification In LSM Trees

> Track: `databases` | Topic: `nosql`

## Concept

LSM trees make writes cheap by spreading data across memtables and SSTables, but a point read may need to consult many files across levels before it finds the answer.

## Key Points

- More SSTables and more levels can increase point-read work.
- Bloom filters reduce unnecessary file reads, but they do not make read amplification disappear.
- Read amplification is one of the main tradeoffs behind LSM write performance.
- Compaction helps reduce how many files a read has to touch.
- SSTable counts, false-positive estimates, and per-table latency should all stay non-negative.

## Minimal Code Mental Model

```python
summary = point_lookup_cost(
    level_sstables=[3, 5, 10],
    false_positive_tables=1,
    table_read_ms=2,
)
```

## Function

```python
def validate_level_sstables(level_sstables: list[int]) -> None:
def tables_checked_without_bloom(level_sstables: list[int]) -> int:
def tables_checked_with_bloom(
    level_sstables: list[int],
    false_positive_tables: int = 0,
) -> int:
def point_lookup_cost(
    level_sstables: list[int],
    false_positive_tables: int = 0,
    table_read_ms: int = 1,
) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/databases/nosql/read-amplification-in-lsm-trees/python -q
```
