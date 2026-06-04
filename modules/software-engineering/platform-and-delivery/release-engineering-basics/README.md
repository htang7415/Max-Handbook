# Release Engineering Basics

> Track: `software-engineering` | Topic: `platform-and-delivery`

## Concept

Release engineering turns a code change into a repeatable, auditable production release with explicit gates and rollback readiness.

## Use When

| Change Type | Gate |
| --- | --- |
| Any production release | Build and test status |
| Database or API change | Migration or compatibility review |
| Risky rollout | Rollback plan and release owner |

## First Principles

- A release gate should be tied to a real risk, not just tradition.
- Build, test, and migration checks should be visible before shipping.
- A release is not ready if rollback or recovery is unclear.

## Workflow

1. Tag the change by risk type.
2. Derive required gates from those tags.
3. Check each gate before promotion.
4. Block release when rollback or recovery is unclear.

## Minimal Code Mental Model

```python
gates = required_release_gates(["database", "api"])
blockers = release_blockers(gates, {"build": "passed", "tests": "passed", "migration-review": "failed"})
ready = releasable(gates, {"build": "passed", "tests": "passed", "migration-review": "passed", "rollback-plan": "passed"})
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Gate exists by tradition only | Process slows releases without reducing risk |
| Hidden gate status | Teams ship with unknown blockers |
| No rollback plan | Failed release becomes an incident response problem |

## Function

```python
def required_release_gates(change_tags: list[str]) -> list[str]:
def release_blockers(required_gates: list[str], gate_statuses: dict[str, str]) -> list[str]:
def releasable(required_gates: list[str], gate_statuses: dict[str, str]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/platform-and-delivery/release-engineering-basics/python -q
```
