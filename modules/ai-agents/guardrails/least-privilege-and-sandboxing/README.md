# Least Privilege and Sandboxing

> Track: `ai-agents` | Topic: `guardrails`

## Concept

Least privilege and sandboxing give an agent only the scopes and execution environment it needs for the current step, not the maximum it could ever use.

## Key Points

- Permission scope should come from the requested tools, not from convenience.
- Sandbox choice depends on whether the step needs writes, network, or secret-bearing data.
- Any scope expansion beyond the current grant should be explicit and reviewable.

## Minimal Code Mental Model

```python
scopes = least_privilege_scopes(["search_docs", "read_repo"], tool_scopes)
profile = sandbox_profile(needs_write=False, needs_network=True, handles_secrets=False)
needs_review = scope_escalation_required(["repo:read"], ["repo:read", "email:send"])
```

## Function

```python
def least_privilege_scopes(
    requested_tools: list[str],
    tool_scopes: dict[str, list[str]],
) -> list[str]:
def sandbox_profile(needs_write: bool, needs_network: bool, handles_secrets: bool) -> str:
def scope_escalation_required(current_scopes: list[str], requested_scopes: list[str]) -> bool:
```

## Run tests

```bash
pytest modules/ai-agents/guardrails/least-privilege-and-sandboxing/python -q
```
