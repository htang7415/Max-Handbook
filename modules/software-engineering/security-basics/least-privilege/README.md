# Least Privilege

> Track: `software-engineering` | Topic: `security-basics`

## Concept

Least privilege means granting only the scopes required for the task, then forcing review whenever a change expands access beyond that minimum.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Scope design | Capabilities can be mapped to concrete permissions | The operation has no protected action |
| Access review | A change requests new or broader scopes | Current and requested scopes are identical |
| Agent or service credential | Automation can call external systems | The credential is read-only and already scoped |

## First Principles

- Access should be derived from required actions, not convenience.
- Scope expansion should be explicit and reviewable.
- Privilege models should make unnecessary permissions obvious in code review.

## Workflow

1. Map capabilities to the scopes they require.
2. Derive requested scopes from requested capabilities.
3. Compare requested scopes with current scopes.
4. Flag any extra scope as privilege expansion.
5. Require review before granting expanded access.

## Minimal Code Mental Model

```python
scopes = least_privilege_scopes(["read-docs", "write-docs"], capability_scopes)
extra = extra_scopes(["docs:read"], scopes)
review = privilege_escalation_required(["docs:read"], scopes)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Unknown capability | Policy grants unclear permission | `least_privilege_scopes` rejects unknown capabilities |
| Empty requested scope set | Review cannot tell what is being requested | `privilege_escalation_required` rejects empty requests |
| Silent scope expansion | New access appears without review | `extra_scopes` returns newly requested scopes |

## Function

```python
def least_privilege_scopes(
    requested_capabilities: list[str],
    capability_scopes: dict[str, list[str]],
) -> list[str]:
def extra_scopes(current_scopes: list[str], requested_scopes: list[str]) -> list[str]:
def privilege_escalation_required(current_scopes: list[str], requested_scopes: list[str]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/security-basics/least-privilege/python -q
```
