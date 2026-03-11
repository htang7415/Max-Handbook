# Memory Conflict Resolution

> Track: `ai-agents` | Topic: `memory`

## Concept

Memory conflict resolution ranks conflicting memories by recency, source trust, and confirming evidence so the agent can choose one or escalate when the conflict remains ambiguous.

## Key Points

- A conflicting memory should not win just because it was seen most recently.
- Recency, source trust, and confirmations should be combined explicitly.
- If the best memory is weak or too close to the next one, review is safer than guessing.

## Minimal Code Mental Model

```python
score = memory_evidence_score(recency_score=0.9, source_trust=0.8, confirmations=2)
ranked = rank_conflicting_memories(memories)
route = memory_conflict_route(memories, min_score=0.6, min_margin=0.1)
```

## Function

```python
def memory_evidence_score(recency_score: float, source_trust: float, confirmations: int) -> float:
def rank_conflicting_memories(memories: list[dict[str, object]]) -> list[dict[str, object]]:
def memory_conflict_route(memories: list[dict[str, object]], min_score: float, min_margin: float = 0.0) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/memory/memory-conflict-resolution/python -q
```
