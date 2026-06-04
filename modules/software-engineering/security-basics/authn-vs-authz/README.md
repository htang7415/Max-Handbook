# Authn vs Authz

> Track: `software-engineering` | Topic: `security-basics`

## Concept

Authentication answers who the caller is. Authorization answers what that caller is allowed to do.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Access check | A credential maps to a principal and an action needs permission | The operation is public and has no identity dependency |
| Security review | A route has both login and permission logic | You only need to validate input shape |
| Scope design | Actions can be represented as explicit capabilities | Role names are the only available policy input |

## First Principles

- A valid identity does not imply permission.
- Authorization should check an explicit scope or capability, not just role names in comments.
- Mixing authn and authz makes access bugs harder to reason about and test.

## Workflow

1. Authenticate the credential into a principal.
2. Treat missing principals as unauthenticated.
3. Look up the principal's scopes.
4. Authorize the required action against those scopes.
5. Return separate decisions for unauthenticated and unauthorized calls.

## Minimal Code Mental Model

```python
principal = authenticate_credential("token_admin", {"token_admin": "alice"})
allowed = authorize_action(["docs:read", "docs:write"], "docs:write")
decision = access_decision(
    "token_admin",
    {"token_admin": "alice"},
    {"alice": ["docs:read", "docs:write"]},
    "docs:write",
)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Identity treated as permission | Any logged-in user can perform protected actions | `access_decision` runs authn and authz separately |
| Unknown credential | Caller has no principal | Returns `deny:unauthenticated` |
| Missing required scope | Principal exists but cannot perform action | Returns `deny:unauthorized` |

## Function

```python
def authenticate_credential(credential: str, token_directory: dict[str, str]) -> str | None:
def authorize_action(scopes: list[str], required_scope: str) -> bool:
def access_decision(
    credential: str,
    token_directory: dict[str, str],
    scope_directory: dict[str, list[str]],
    required_scope: str,
) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/security-basics/authn-vs-authz/python -q
```
