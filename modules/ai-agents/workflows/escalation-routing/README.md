# Escalation Routing

> Track: `ai-agents` | Topic: `workflows`

## Concept

Escalation routing decides where a failed, risky, or low-confidence step should go next instead of blindly retrying.

## Key Points

- Escalation should happen for the right reason: policy review, repeated failure, or low confidence.
- The route should be explicit so humans or fallback workers know why they were chosen.
- A small escalation policy is easier to audit than retry logic mixed into every step.

## Minimal Code Mental Model

```python
reason = escalation_reason(blocked=False, confidence=0.4, threshold=0.7, attempt=2, max_attempts=2)
route = escalation_target(reason, routing_table)
packet = escalation_packet("task_9", reason, route)
```

## Function

```python
def escalation_reason(blocked: bool, confidence: float, threshold: float, attempt: int, max_attempts: int) -> str | None:
def escalation_target(reason: str | None, routing_table: dict[str, str]) -> str | None:
def escalation_packet(task_id: str, reason: str, route: str) -> dict[str, str]:
```

## Run tests

```bash
pytest modules/ai-agents/workflows/escalation-routing/python -q
```
