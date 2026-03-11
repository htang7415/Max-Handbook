# Planning

Planning is the layer that turns a broad goal into ordered steps the agent can execute and track.

## Purpose

Use this page to understand:
- when a task needs an explicit plan
- how to track unfinished work
- why short plans beat vague reasoning loops

## First Principles

- Planning is most useful when a task has multiple dependent steps.
- A plan should be explicit enough to inspect and update.
- The next action should come from plan state, not just free-form generation.

## Minimal Code Mental Model

```python
plan = make_plan("Prepare launch report", ["collect metrics", "write summary", "send report"])
step = next_pending_step(plan)
plan = mark_step_done(plan, 0)
```

## Canonical Modules

- Main step-tracking pattern: `plan-act-loop`

## Supporting Modules

- Breaking a goal into smaller checkpoints: `task-decomposition`
- Adjusting a plan after new constraints or blocked steps: `replanning`
- Deciding when the plan should stop or hand off: `planning-stop-conditions`

## When To Use What

- Start with `plan-act-loop` when the task needs state and ordering.
- Use `task-decomposition` when the main difficulty is splitting a broad goal into concrete subgoals.
- Use `replanning` when the current plan becomes stale because the task changes or a step gets blocked.
- Use `planning-stop-conditions` when the workflow needs an explicit rule for done, blocked, or escalate.
- Keep plans short and concrete before adding branching or multi-agent coordination.
