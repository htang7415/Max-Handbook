# Secure SDLC Basics

> Track: `software-engineering` | Topic: `security-basics`

## Concept

A secure SDLC makes security checks part of normal design, implementation, review, and release rather than treating security as a final separate phase.

## Key Points

- Different change types need different security checks.
- Release blockers should be explicit and auditable.
- Secret scanning, dependency scanning, and auth review are cheap checks to require early.

## Minimal Code Mental Model

```python
required = required_security_checks(["api", "auth", "dependency-change"])
missing = missing_security_checks(["api", "auth"], ["secret-scan", "authz-review"])
ready = release_allowed(["api", "auth"], ["secret-scan", "authz-review", "dependency-scan"])
```

## Function

```python
def required_security_checks(change_tags: list[str]) -> list[str]:
def missing_security_checks(change_tags: list[str], completed_checks: list[str]) -> list[str]:
def release_allowed(change_tags: list[str], completed_checks: list[str]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/security-basics/secure-sdlc-basics/python -q
```
