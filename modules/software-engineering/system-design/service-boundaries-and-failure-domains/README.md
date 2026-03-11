# Service Boundaries And Failure Domains

> Track: `software-engineering` | Topic: `system-design`

## Concept

A service boundary is justified when it improves ownership, scaling, or failure isolation without breaking a transaction boundary that must stay together.

## Key Points

- Splitting services too early adds coordination cost.
- Strong transaction requirements are a reason to keep components together.
- Failure-domain design is mostly about reducing blast radius.

## Minimal Code Mental Model

```python
split = should_split_service(
    independent_scaling=True,
    separate_ownership=True,
    requires_strong_transaction=False,
)
risk = failure_domain_risk(shared_dependencies=3, critical_paths=2)
decision = boundary_decision(
    independent_scaling=True,
    separate_ownership=False,
    requires_strong_transaction=True,
)
```

## Function

```python
def should_split_service(
    independent_scaling: bool,
    separate_ownership: bool,
    requires_strong_transaction: bool,
) -> bool:
def failure_domain_risk(shared_dependencies: int, critical_paths: int) -> str:
def boundary_decision(
    independent_scaling: bool,
    separate_ownership: bool,
    requires_strong_transaction: bool,
) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/system-design/service-boundaries-and-failure-domains/python -q
```
