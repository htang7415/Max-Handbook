# Internal Platforms

> Track: `software-engineering` | Topic: `platform-and-delivery`

## Concept

An internal platform is justified when many teams repeat the same infrastructure or delivery work and a shared abstraction can remove that toil without hiding essential choices.

## Use When

| Signal | Platform Decision |
| --- | --- |
| Many teams repeat the same work | Consider a shared platform |
| Exceptions are rare and understood | Abstraction may be stable enough |
| Teams need very different workflows | Keep the platform narrower |

## First Principles

- A platform should solve repeated pain, not invent new surfaces to maintain.
- Too many exceptions are a sign the abstraction is premature or too broad.
- Platform value depends on adoption and reduced repeated work.

## Workflow

1. Quantify repeated work per team.
2. Count teams that would actually adopt the abstraction.
3. List exceptions before designing the platform surface.
4. Start narrow and expand only when the pattern repeats.

## Minimal Code Mental Model

```python
worth_it = platform_candidate(teams=6, repeated_work_hours_per_team=5, custom_exceptions=1)
risk = abstraction_risk(custom_exceptions=5)
value = platform_value(teams=6, repeated_work_hours_per_team=5)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Platform before repeated pain | New maintenance burden |
| Ignoring exceptions | Teams bypass the platform |
| Measuring build effort only | Value is unclear after launch |

## Function

```python
def platform_candidate(teams: int, repeated_work_hours_per_team: int, custom_exceptions: int) -> bool:
def abstraction_risk(custom_exceptions: int) -> str:
def platform_value(teams: int, repeated_work_hours_per_team: int) -> int:
```

## Run tests

```bash
pytest modules/software-engineering/platform-and-delivery/internal-platforms/python -q
```
