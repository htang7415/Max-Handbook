# Role Assignment

> Track: `ai-agents` | Topic: `multi-agent`

## Concept

Role assignment picks which worker roles should exist for a task and maps each role to the part of the job it should own.

## Key Points

- Roles should be assigned from task needs, not from arbitrary worker names.
- A small number of clear roles is easier to debug than many overlapping ones.
- The assignment should explain why a worker was chosen.

## Minimal Code Mental Model

```python
roles = assign_roles("investigate outage and write summary", role_keywords)
owners = role_owners(roles)
plan = role_assignment_summary(roles)
```

## Function

```python
def assign_roles(task: str, role_keywords: dict[str, list[str]]) -> list[str]:
def role_owners(roles: list[str]) -> dict[str, str]:
def role_assignment_summary(roles: list[str]) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/multi-agent/role-assignment/python -q
```
