# Memory Patterns

> Track: `ai-agents` | Topic: `memory`

## Concept

Memory patterns let an agent keep a small amount of useful state, summarize recent context, and retrieve the most relevant past facts.

## Key Points

- Working memory should stay short and task-relevant.
- Summaries compress recent state so later steps do not need the entire transcript.
- Retrieval is better than replaying every past message when memory grows.

## Core Math

- Retrieval score:
  $$
  \text{relevance} + \text{recency}
  $$
- Memory cap:
  $$
  \text{stored items} \le \text{max items}
  $$

## Minimal Code Mental Model

```python
memory = append_memory([], "User prefers CSV output", max_items=3)
summary = summarize_recent_memory(memory + ["Need weekly totals"], max_items=2)
hits = retrieve_relevant_memories("csv totals", memory, k=1)
```

## Function

```python
def append_memory(memory: list[str], item: str, max_items: int | None = None) -> list[str]:
def summarize_recent_memory(memory: list[str], max_items: int) -> str:
def retrieve_relevant_memories(query: str, memory: list[str], k: int) -> list[str]:
```

## Run tests

```bash
pytest modules/ai-agents/memory/memory-patterns/python -q
```
