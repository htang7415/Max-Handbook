# Reliability

This section is about keeping systems useful under failure, overload, and risky change.

## Purpose

Use this page to organize reliability into:
- failure containment
- safe retries and fallbacks
- rollout and rollback
- incident response and learning

## First Principles

- Failure is a normal operating condition, not a surprising exception.
- Reliability comes from bounded blast radius, not from assuming components never fail.
- Overload behavior should be designed, not discovered in production.
- A fast rollback path is often more valuable than a perfect fix path.

## Decision Table

| Mechanism | Use when | Guard |
| --- | --- | --- |
| Graceful degradation | Full quality is optional but usefulness must continue | Make degraded behavior explicit to users or operators |
| Circuit breaker | A dependency can fail or overload callers | Bound retries and recovery probes |
| Bulkhead | One path should not consume all capacity | Reserve capacity or isolate pools |
| Retry and fallback | Failure is transient and the operation is safe to repeat | Avoid retry storms and stale fallbacks |
| Canary rollout | A change may fail only under production traffic | Define health gates before rollout |
| Postmortem | The system violated an assumption | Convert learning into a concrete follow-up |

## Workflow

| Step | Action | Output |
| --- | --- | --- |
| 1 | Define the user-visible failure | Reliability risk |
| 2 | Bound blast radius | Isolation, limit, or rollout scope |
| 3 | Pick recovery behavior | Retry, fallback, degrade, rollback, or page |
| 4 | Add health and rollback signals | Release gate |
| 5 | Feed incidents back into design | Follow-up action |

## Canonical Modules

- `graceful-degradation-and-overload`
- `circuit-breakers-and-bulkheads`
- `retries-and-fallbacks`
- `canary-rollout-and-rollback`
- `incidents-and-postmortems`

## Supporting Modules

- `rollback-readiness`

## Math And Code

- Math level: `high`
- Main quantitative objects: success rates, budget burn, retry counts, concurrency limits, and rollout health.
- Code shape: containment and recovery logic such as fallback choice, breaker state, degradation path, and rollback decision.

## When To Use What

- Start with graceful degradation and rollout safety before advanced control patterns.
- Use bulkheads when one failing dependency should not take down unrelated paths.
- Use retries only when the operation and load profile can tolerate them.
- Use postmortems to improve operating assumptions, not to assign blame.
