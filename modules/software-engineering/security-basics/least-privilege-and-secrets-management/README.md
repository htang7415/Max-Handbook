# Least Privilege And Secrets Management

> Track: `software-engineering` | Topic: `security-basics`

## Concept

Least privilege reduces granted access to the minimum needed, and secret management keeps credentials out of logs, source control, and long-lived plaintext storage.

## Key Points

- Access scopes should come from required actions, not from convenience.
- Secrets should move through managed injection paths, not through logs or committed files.
- Any privilege expansion touching secrets should be explicit and reviewable.

## Minimal Code Mental Model

```python
scopes = least_privilege_scopes(["read-docs", "write-docs"], capability_scopes)
action = secret_handling_action("OPENAI_API_KEY", "log")
review = privilege_escalation_required(["docs:read"], ["docs:read", "docs:write"], secret_access=True)
```

## Function

```python
def least_privilege_scopes(
    requested_capabilities: list[str],
    capability_scopes: dict[str, list[str]],
) -> list[str]:
def secret_handling_action(secret_name: str, destination: str) -> str:
def privilege_escalation_required(
    current_scopes: list[str],
    requested_scopes: list[str],
    secret_access: bool = False,
) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/security-basics/least-privilege-and-secrets-management/python -q
```
