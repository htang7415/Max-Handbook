# Guardrails

Guardrails are the checks around an agent loop that prevent unsafe, malformed, or low-confidence actions.

## Purpose

Use this page to understand:
- how to block obviously unsafe inputs
- how to validate structured outputs
- when to escalate instead of answering

## First Principles

- Guardrails should check simple conditions before expensive reasoning or tool use.
- Output validation is easier when the expected shape is explicit.
- Escalation is often better than pretending uncertain output is safe.

## Minimal Code Mental Model

```python
blocked = blocked_by_terms(user_text, ["password", "private key"])
valid = required_fields_present(record, ["answer", "confidence"])
escalate = should_escalate(model_confidence=0.42, threshold=0.6, blocked=blocked)
```

## Canonical Modules

- Main validation pattern: `input-output-guardrails`

## Supporting Modules

- Policy decisions and escalation paths: `policy-and-escalation`
- Review queue packets and human handoff: `review-queue-handoff`

## When To Use What

- Start with `input-output-guardrails` when the main need is lightweight safety and validation.
- Use `policy-and-escalation` when the system needs a clear allow / review / block decision.
- Use `review-queue-handoff` when risky requests need a structured packet for human review instead of a direct answer.
- Add stronger policy logic only after the simple checks are in place.
