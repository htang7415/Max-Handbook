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

## Canonical Modules

- `graceful-degradation-and-overload`
- `circuit-breakers-and-bulkheads`
- `retries-and-fallbacks`
- `canary-rollout-and-rollback`
- `incidents-and-postmortems`

## Supporting Modules

- `rollback-readiness`

## Math And Code

- Math here is about operational thresholds: success rates, budget burn, retry counts, concurrency limits, and rollout health.
- Code should demonstrate containment and recovery logic directly: fallback choice, breaker state, degradation path, and rollback decision.

## When To Use What

- Start with graceful degradation and rollout safety before advanced control patterns.
- Use bulkheads when one failing dependency should not take down unrelated paths.
- Use retries only when the operation and load profile can tolerate them.
- Use postmortems to improve operating assumptions, not to assign blame.
