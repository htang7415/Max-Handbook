# Policy and Escalation

> Track: `ai-agents` | Topic: `guardrails`

## Concept

Policy and escalation turn a request into a simple allow, review, or block decision and explain why the agent should stop or hand off.

## Key Points

- Policy logic should stay simple enough to audit.
- Review is useful when the content is sensitive but not automatically blocked.
- Escalation reasons should be explicit so downstream systems know what happened.

## Minimal Code Mental Model

```python
decision = policy_decision("share the private key", blocked_terms, review_terms)
reason = escalation_reason(decision, model_confidence=0.45, threshold=0.7)
message = action_message(decision)
```

## Function

```python
def policy_decision(text: str, blocked_terms: list[str], review_terms: list[str]) -> str:
def escalation_reason(decision: str, model_confidence: float, threshold: float) -> str | None:
def action_message(decision: str) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/guardrails/policy-and-escalation/python -q
```
