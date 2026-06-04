# Secrets Management

> Track: `software-engineering` | Topic: `security-basics`

## Concept

Secrets management keeps credentials out of logs, source control, and long-lived plaintext storage by forcing them through managed injection and rotation paths.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Credential handling | API keys, tokens, or passwords move through code or config | The value is not secret and can be public |
| Environment setup | Prod and dev need different secret destinations | Secret storage is managed by a platform contract |
| Rotation review | Credentials can expire or leak over time | The credential is short-lived and automatically rotated |

## First Principles

- Secrets should move through managed systems instead of ad hoc files and logs.
- Output paths should distinguish deny, redact, and safe managed storage.
- Rotation rules should be explicit because stale secrets often survive unnoticed.

## Workflow

1. Identify whether the value is a secret.
2. Deny logs, tickets, and source control destinations.
3. Redact unsafe local outputs.
4. Use process environment locally and secret manager in staging or production.
5. Rotate when age reaches the maximum allowed age.

## Minimal Code Mental Model

```python
action = secret_handling_action("OPENAI_API_KEY", "log")
stored = managed_secret_destination("production")
rotate = secret_rotation_required(age_days=95, max_age_days=90)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Secret logged or committed | Credential leaks into durable text | `secret_handling_action` returns `deny` |
| Wrong environment destination | Production secrets live in ad hoc storage | `managed_secret_destination` chooses secret manager for prod and staging |
| Stale credential | Old secret remains active too long | `secret_rotation_required` flags expired secrets |

## Function

```python
def secret_handling_action(secret_name: str, destination: str) -> str:
def managed_secret_destination(environment: str) -> str:
def secret_rotation_required(age_days: int, max_age_days: int) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/security-basics/secrets-management/python -q
```
