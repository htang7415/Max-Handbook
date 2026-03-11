# Retrieval-Backed Memory

> Track: `ai-agents` | Topic: `memory`

## Concept

Retrieval-backed memory stores older notes and pulls back only the ones that overlap with the current task.

## Key Points

- Retrieval-backed memory is useful when recent summaries are no longer enough.
- The memory store should stay small and text-like before moving to a heavier vector system.
- Returning the top few matching notes is usually enough for a first working loop.

## Minimal Code Mental Model

```python
store = index_memories(["User prefers CSV", "Weekly report due Friday"])
hits = retrieve_memory_hits("csv report", store, k=1)
context = memory_context(hits, max_items=1)
```

## Function

```python
def index_memories(items: list[str]) -> list[dict[str, object]]:
def retrieve_memory_hits(query: str, memory_index: list[dict[str, object]], k: int) -> list[str]:
def memory_context(items: list[str], max_items: int) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/memory/retrieval-backed-memory/python -q
```
