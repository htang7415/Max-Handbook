# Memory Compaction Patterns

> Track: `databases` | Topic: `vector-db`

## Concept

Long-running agents need memory compaction so the raw memory store does not grow without bound while still preserving the useful signal.

## Key Points

- Keep recent or high-importance memories raw.
- Collapse older low-value memories into topic summaries.
- Pinned memories should survive compaction even if they are old.
- Compaction should reduce retrieval noise, not just save storage.
- Keep `importance` in the `0..1` range and `keep_raw` non-negative so the ranking stays interpretable.

## Minimal Code Mental Model

```python
kept = raw_memory_ids(memories, now=200, keep_raw=2)
compacted = compact_memories(memories, now=200, keep_raw=2)
```

## Function

```python
def validate_importance(importance: float) -> None:
def validate_recency_window(recency_window: int) -> None:
def validate_keep_raw(keep_raw: int) -> None:
def memory_score(
    memory: dict[str, object],
    now: int,
    recency_window: int = 3600,
) -> float:
def raw_memory_ids(
    memories: list[dict[str, object]],
    now: int,
    keep_raw: int,
) -> list[str]:
def summary_text(memories: list[dict[str, object]]) -> str:
def compact_memories(
    memories: list[dict[str, object]],
    now: int,
    keep_raw: int,
) -> list[dict[str, object]]:
```

## Run tests

```bash
pytest modules/databases/vector-db/memory-compaction-patterns/python -q
```
