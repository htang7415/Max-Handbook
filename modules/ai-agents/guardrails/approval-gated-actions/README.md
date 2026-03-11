# Approval-Gated Actions

> Track: `ai-agents` | Topic: `guardrails`

## Concept

Approval-gated actions stop an agent before a risky external side effect and require an explicit approve, deny, or edit decision.

## Key Points

- Actions that send, buy, delete, publish, or change permissions often need approval even when the plan is otherwise correct.
- Approval packets should summarize the exact action, not the whole transcript.
- `Edit` is different from `approve`: it means revise the action first, then ask again.

## Minimal Code Mental Model

```python
needs_approval = approval_required("send_email", risk_level="medium", external_side_effect=True)
packet = approval_packet("act_7", "send_email", "Email the signed contract to the vendor", "medium")
route = post_approval_route("edit")
```

## Function

```python
def approval_required(action_type: str, risk_level: str, external_side_effect: bool) -> bool:
def approval_packet(action_id: str, action_type: str, summary: str, risk_level: str) -> dict[str, str]:
def post_approval_route(decision: str) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/guardrails/approval-gated-actions/python -q
```
