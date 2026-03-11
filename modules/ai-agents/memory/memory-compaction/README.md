# Memory Compaction

> Track: `ai-agents` | Topic: `memory`

## Concept

Memory compaction turns many small notes into a shorter working summary so the agent can keep the main facts without replaying the full history.

## Key Points

- Compaction is useful when note count grows faster than the active prompt budget.
- A compact summary should keep only the strongest repeated or recent facts.
- The compacted summary is for working state, not permanent storage.

## Minimal Code Mental Model

```python
summary = compact_memories(
    ["User prefers CSV", "Weekly report due Friday", "Use concise tone"],
    max_items=2,
)
updated = append_compacted_summary("User prefers CSV | Weekly report due Friday", "Use concise tone")
```

## Function

```python
def compact_memories(items: list[str], max_items: int) -> str:
def append_compacted_summary(summary: str, new_item: str) -> str:
def compacted_item_count(summary: str) -> int:
```

## Run tests

```bash
pytest modules/ai-agents/memory/memory-compaction/python -q
```
