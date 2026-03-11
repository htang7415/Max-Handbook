# Compaction Debt Signals

> Track: `databases` | Topic: `nosql`

## Concept

Compaction debt is the backlog you build when write and delete pressure outpace background merge work. You usually notice it through indirect signals: too many SSTables, too many tombstones, or too much pending compaction work.

## Key Points

- Compaction debt shows up as read cost and space amplification.
- Tombstones are cheap to write but expensive to carry around for too long.
- Pending compaction bytes are a backlog signal, not a correctness signal.
- Good alerts combine several weak signals instead of one metric alone.

## Minimal Code Mental Model

```python
summary = compaction_summary([6, 8, 5], tombstone_ratio=0.22, pending_bytes_mb=900)
```

## Function

```python
def read_amplification(level_sstables: list[int]) -> int:
def debt_signals(
    level_sstables: list[int],
    tombstone_ratio: float,
    pending_bytes_mb: int,
) -> dict[str, bool]:
def recommended_action(
    level_sstables: list[int],
    tombstone_ratio: float,
    pending_bytes_mb: int,
) -> str:
def compaction_summary(
    level_sstables: list[int],
    tombstone_ratio: float,
    pending_bytes_mb: int,
) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/nosql/compaction-debt-signals/python -q
```
