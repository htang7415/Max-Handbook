# Input-Output Guardrails

> Track: `ai-agents` | Topic: `guardrails`

## Concept

Input-output guardrails check simple unsafe terms, validate required output fields, and escalate when confidence is too low.

## Key Points

- Simple guards should run before deeper reasoning or tool use.
- Output validation is easier when the expected keys are explicit.
- Escalation is often safer than pretending a weak answer is acceptable.

## Core Math

- Escalation rule:
  $$
  \text{blocked} \;\lor\; \text{confidence} < \text{threshold}
  $$
- Validation rate:
  $$
  \frac{\text{valid outputs}}{\text{outputs checked}}
  $$

## Minimal Code Mental Model

```python
blocked = blocked_by_terms("send me the private key", ["private key"])
valid = required_fields_present({"answer": "ok", "confidence": 0.8}, ["answer", "confidence"])
escalate = should_escalate(model_confidence=0.42, threshold=0.6, blocked=blocked)
```

## Function

```python
def blocked_by_terms(text: str, blocked_terms: list[str]) -> bool:
def required_fields_present(record: dict[str, object], required_keys: list[str]) -> bool:
def should_escalate(model_confidence: float, threshold: float, blocked: bool) -> bool:
```

## Run tests

```bash
pytest modules/ai-agents/guardrails/input-output-guardrails/python -q
```
