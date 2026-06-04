# Service Boundaries And Failure Domains

> Track: `software-engineering` | Topic: `system-design`

## Concept

A service boundary is justified when it improves ownership, scaling, or failure isolation without breaking a transaction boundary that must stay together.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Boundary review | Teams propose splitting a service | The split is only for code organization |
| Scaling or ownership pressure | One part needs independent capacity or ownership | Strong transaction rules require one boundary |
| Failure-domain design | Shared dependencies can widen blast radius | Failure impact is already isolated |

## First Principles

- Splitting services too early adds coordination cost.
- Strong transaction requirements are a reason to keep components together.
- Failure-domain design is mostly about reducing blast radius.

## Workflow

1. Check whether strong transactions must stay together.
2. Look for independent scaling pressure.
3. Look for separate ownership pressure.
4. Estimate blast radius from shared dependencies and critical paths.
5. Decide `split`, `keep-together`, or `review-transaction-boundary`.

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

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Splitting across strong transaction boundary | Distributed coordination becomes the new bug source | `should_split_service` rejects splits that require strong transactions |
| Shared dependency blast radius | One dependency failure harms multiple critical paths | `failure_domain_risk` classifies shared-dependency risk |
| Ambiguous decision | Review hides the real trade-off | `boundary_decision` calls out transaction-boundary review |

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
