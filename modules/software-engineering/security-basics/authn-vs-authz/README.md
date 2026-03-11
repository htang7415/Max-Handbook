# Authn vs Authz

> Track: `software-engineering` | Topic: `security-basics`

## Concept

Authentication answers who the caller is. Authorization answers what that caller is allowed to do.

## Key Points

- A valid identity does not imply permission.
- Authorization should check an explicit scope or capability, not just role names in comments.
- Mixing authn and authz makes access bugs harder to reason about and test.

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
