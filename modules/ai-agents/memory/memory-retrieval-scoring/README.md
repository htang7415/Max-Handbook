# Memory Retrieval Scoring

> Track: `ai-agents` | Topic: `memory`

## Concept

Memory retrieval scoring ranks stored notes by how useful they are for the current query before the agent builds context.

## Key Points

- Ranking is useful when many notes match a query.
- A simple score can combine token overlap and note priority.
- Better ordering often matters more than adding more notes.

## Minimal Code Mental Model

```python
scored = score_memory_for_query("csv report", memories)
top = top_scored_memories(scored, k=2)
best = best_memory_match("csv report", memories)
```

## Function

```python
def score_memory_for_query(query: str, memories: list[dict[str, object]]) -> list[tuple[str, int]]:
def top_scored_memories(scored_items: list[tuple[str, int]], k: int) -> list[str]:
def best_memory_match(query: str, memories: list[dict[str, object]]) -> str | None:
```

## Run tests

```bash
pytest modules/ai-agents/memory/memory-retrieval-scoring/python -q
```
