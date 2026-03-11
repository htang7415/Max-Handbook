# Memory Retention Policy

> Track: `ai-agents` | Topic: `memory`

## Concept

Memory retention policy decides which notes stay in memory and which ones get dropped when the store gets too large.

## Key Points

- A retention policy should prefer notes with higher value or more reuse.
- The goal is to keep the memory store small without dropping the most important facts.
- A simple score-and-keep rule is enough for a first version.

## Minimal Code Mental Model

```python
scored = score_memory_items(["User prefers CSV", "Weekly report due Friday"], {"csv": 2, "report": 1})
kept = retain_top_memory_items(scored, max_items=1)
evicted = evicted_memory_items(scored, max_items=1)
```

## Function

```python
def score_memory_items(items: list[str], keyword_weights: dict[str, int]) -> list[tuple[str, int]]:
def retain_top_memory_items(scored_items: list[tuple[str, int]], max_items: int) -> list[str]:
def evicted_memory_items(scored_items: list[tuple[str, int]], max_items: int) -> list[str]:
```

## Run tests

```bash
pytest modules/ai-agents/memory/memory-retention-policy/python -q
```
