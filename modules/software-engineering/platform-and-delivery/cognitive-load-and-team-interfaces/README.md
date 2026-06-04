# Cognitive Load And Team Interfaces

> Track: `software-engineering` | Topic: `platform-and-delivery`

## Concept

Team boundaries work best when a team can understand its own systems without constant coordination across blurry ownership lines.

## Use When

| Signal | Boundary Action |
| --- | --- |
| Too many services, workflows, or pager domains | Reduce team load |
| Shared components create ambiguity | Clarify ownership |
| Escalation paths are unclear | Define team interfaces |

## First Principles

- Cognitive load is a real limit, not a soft preference.
- Shared ownership often looks flexible at first and expensive later.
- Team interfaces should make dependencies and escalation paths obvious.

## Workflow

1. Count systems, workflows, and pager domains the team must understand.
2. Identify shared components with unclear decision rights.
3. Move ownership or define the interface explicitly.
4. Re-check whether the team can operate the system without constant coordination.

## Minimal Code Mental Model

```python
load = team_cognitive_load(services=5, workflows=4, pager_domains=3)
clarity = interface_clarity(owned_components=4, shared_components=1)
assert boundary_rework_needed(load, clarity) is True
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Treating load as personal weakness | System design ignores human limits |
| Everyone owns it | No one can make timely decisions |
| Hidden escalation path | Incidents and changes stall across teams |

## Function

```python
def team_cognitive_load(services: int, workflows: int, pager_domains: int) -> str:
def interface_clarity(owned_components: int, shared_components: int) -> str:
def boundary_rework_needed(load: str, clarity: str) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/platform-and-delivery/cognitive-load-and-team-interfaces/python -q
```
