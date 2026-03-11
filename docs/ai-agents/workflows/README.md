# Workflows

This section is about how an agent routes tasks, hands state to another step or worker, and decides when to retry.

## Purpose

Use this page to understand:
- routing to the right worker
- structured handoffs
- bounded retries

## First Principles

- Workflows matter when one free-form agent loop is not enough.
- Routing should depend on task type, not on vague prompt wording alone.
- Handoffs should pass compact structured state, not the entire raw transcript.
- Retries should be limited and explicit.

## Minimal Code Mental Model

```python
route = route_task("summarize docs and file a ticket", routes)
handoff = build_handoff("task_7", route, {"doc_id": "abc"})
retry = should_retry(attempt=1, max_attempts=3, retryable=True)
```

## Canonical Modules

- Routing and handoff basics: `handoffs-and-routing`
- Retry and fallback basics: `retries-and-recovery`

## Supporting Modules

- Escalation routing after failed or risky steps: `escalation-routing`
- Explicit state transitions for multi-step runs: `state-machine-basics`
- Parallel branches and join points in a workflow: `workflow-concurrency-basics`

## When To Use What

- Start with `handoffs-and-routing` when the agent needs more than one specialized step.
- Use `retries-and-recovery` when steps can fail transiently and need bounded retries or a safe fallback.
- Use `escalation-routing` when failures need a structured handoff to review instead of another retry.
- Use `state-machine-basics` when the workflow has a small fixed set of stages and transitions.
- Use `workflow-concurrency-basics` when independent steps can run in parallel and later join.
- Add more workflow depth only after the baseline route and handoff state are stable.
