# Agent Memory Retrieval

> Track: `databases` | Topic: `vector-db`

## Concept

Agent memory retrieval should combine relevance, scope, and recency so the agent sees useful memories without leaking another tenant's context.

## Key Points

- Memory retrieval should filter by workspace before ranking anything.
- Shared memories can be visible to many agents, but private memories should stay scoped to one agent.
- Pure similarity is not enough for memory systems; recent interactions often deserve a boost.
- Retrieval needs a minimum score or the agent fills context with weak, noisy memories.
- Keep `importance` and `min_score` in the `0..1` range so the weighted score stays interpretable.

## Minimal Code Mental Model

```python
memories = [
    {"id": "m1", "workspace_id": 7, "agent_id": None, "text": "Escalate prod errors fast", "created_at": 100},
    {"id": "m2", "workspace_id": 7, "agent_id": "agent-1", "text": "Use hybrid search for support docs", "created_at": 190},
]
top = retrieve_agent_memories(
    "support docs hybrid retrieval",
    memories,
    workspace_id=7,
    agent_id="agent-1",
    now=200,
    top_k=2,
)
```

## Function

```python
def token_overlap_score(query: str, text: str) -> float:
def matches_scope(memory: dict[str, object], workspace_id: int, agent_id: str) -> bool:
def memory_retrieval_score(
    query: str,
    memory: dict[str, object],
    now: int,
    recency_window: int = 3600,
) -> float:
def retrieve_agent_memories(
    query: str,
    memories: list[dict[str, object]],
    workspace_id: int,
    agent_id: str,
    now: int,
    top_k: int,
    min_score: float = 0.2,
    recency_window: int = 3600,
) -> list[tuple[str, float]]:
```

## Run tests

```bash
pytest modules/databases/vector-db/agent-memory-retrieval/python -q
```
