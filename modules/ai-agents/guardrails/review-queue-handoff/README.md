# Review Queue Handoff

> Track: `ai-agents` | Topic: `guardrails`

## Concept

Review queue handoff turns a risky or blocked request into a structured packet that a reviewer can inspect and resolve.

## Key Points

- Human review is easier when the reason and requested action are explicit.
- A review packet should be small, structured, and auditable.
- Queue priority should depend on risk level, not just arrival order.

## Minimal Code Mental Model

```python
priority = review_priority(reason="policy_review", confidence=0.42)
packet = review_packet("task_17", "policy_review", "human_review", priority)
needs_review = send_to_review_queue(packet)
```

## Function

```python
def review_priority(reason: str, confidence: float) -> str:
def review_packet(task_id: str, reason: str, route: str, priority: str) -> dict[str, str]:
def send_to_review_queue(packet: dict[str, str]) -> bool:
```

## Run tests

```bash
pytest modules/ai-agents/guardrails/review-queue-handoff/python -q
```
