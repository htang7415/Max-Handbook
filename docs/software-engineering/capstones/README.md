# Capstones

This section is for end-to-end synthesis work after the main software-engineering foundations are in place.

## Purpose

Use this page to combine:
- contract design
- verification strategy
- observability signals
- rollout and rollback decisions
- delivery discipline under operational risk

## First Principles

- Capstones should exercise multiple engineering responsibilities at once.
- The goal is not more code volume; the goal is better judgment across boundaries.
- A capstone is complete only when it includes verification and operating behavior, not just implementation logic.
- AI-assisted code generation should make the capstone stricter about specs and review, not looser.

## Canonical Modules

- `contract-to-production-api-service`
- `ai-assisted-feature-delivery`
- `incident-recovery-drill`

## Math And Code

- Math level: `medium`
- Main quantitative objects: success rates, latency thresholds, error budgets, blast radius, and rollback readiness.
- Code shape: end-to-end flows that stitch together validation, retries, observability, release gates, incident mitigation, and follow-up actions.

## When To Use What

- Start capstones only after the core modules in tooling, APIs, testing, security, reliability, and observability feel comfortable.
- Use the first capstone to practice safe API delivery from spec to canary decision.
- Use the second capstone to practice AI-assisted change control from spec through review and rollout.
- Use the third capstone to practice SLO breach handling, mitigation choice, and postmortem follow-up under production pressure.
