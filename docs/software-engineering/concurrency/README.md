# Concurrency

This section is about what changes when work happens in parallel, out of order, or under cancellation.

## Purpose

Use this page to understand:
- shared-state hazards
- queues and background workers
- timeouts and cancellation
- duplicate delivery and retries

## First Principles

- Concurrency bugs are usually state bugs with timing attached.
- Retries, duplicate delivery, and cancellation are normal, not exceptional.
- Queues trade immediate coupling for delayed coordination.
- A clear state machine is often easier to reason about than a pile of interleavings.

## Canonical Modules

- `race-conditions-and-shared-state`
- `queues-vs-locks`
- `cancellation-deadlines-and-timeouts`
- `idempotent-consumers`
- `worker-retry-semantics`
- `state-machine-thinking`

## Math And Code

- Math level: `medium`
- Main quantitative objects: in-flight work, queue depth, retry attempts, deadlines, and ordering assumptions.
- Code shape: state machines, duplicate-handling paths, worker policies, and cancellation-aware control flow.

## When To Use What

- Start with races and cancellation before distributed worker systems.
- Use queues when work can be delayed and retried safely.
- Use explicit idempotency when duplicate execution is possible.
- Model long-running workflows as state transitions instead of implicit control flow.
