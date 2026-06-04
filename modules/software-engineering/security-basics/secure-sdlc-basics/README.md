# Secure SDLC Basics

> Track: `software-engineering` | Topic: `security-basics`

## Concept

A secure SDLC makes security checks part of normal design, implementation, review, and release rather than treating security as a final separate phase.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Release gate | Security checks should block unsafe changes | The change is not intended to ship |
| Auth or API change | Authorization and input behavior can change | No protected route or boundary is touched |
| Dependency update | Supply-chain risk changes | Dependencies are unchanged |

## First Principles

- Different change types need different security checks.
- Release blockers should be explicit and auditable.
- Secret scanning, dependency scanning, and auth review are cheap checks to require early.

## Workflow

1. Tag the change by security-relevant scope.
2. Require baseline secret scanning.
3. Add auth review, dependency scan, or validation review from tags.
4. Compare completed checks with required checks.
5. Allow release only when no required checks are missing.

## Minimal Code Mental Model

```python
required = required_security_checks(["api", "auth", "dependency-change"])
missing = missing_security_checks(["api", "auth"], ["secret-scan", "authz-review"])
ready = release_allowed(["api", "auth"], ["secret-scan", "authz-review", "dependency-scan"])
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Security as final phase | Cheap checks happen too late | `required_security_checks` makes checks part of change scope |
| Missing auth review | Protected behavior changes without policy review | `missing_security_checks` reports `authz-review` |
| Dependency risk skipped | Package update ships without scan | Dependency tags require `dependency-scan` |

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
