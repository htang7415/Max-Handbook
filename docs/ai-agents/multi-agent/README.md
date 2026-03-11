# Multi-Agent

This section is about when more than one worker is useful, how roles should differ, and how results should be merged back into one answer.

## Purpose

Use this page to understand:
- role specialization
- handoffs between workers
- merging worker outputs

## First Principles

- A multi-agent system only helps when tasks naturally split into different roles.
- Workers should differ by responsibility, not just by name.
- Merging should be simple and structured so the coordinator can decide what to trust.

## Minimal Code Mental Model

```python
worker = select_worker("write release notes", worker_keywords)
handoff = worker_handoff(worker, "write summary", {"doc_id": "abc"})
merged = merge_worker_outputs(outputs)
```

## Canonical Modules

- Coordination basics: `worker-coordination`

## Supporting Modules

- Budgeting coordinator resources across workers: `delegation-budgets`
- Coordinator-to-worker delegation with bounded subtasks: `orchestrator-workers`
- Arbitration over multiple worker answers: `debate-and-arbitration`
- Assigning roles before workers start: `role-assignment`

## When To Use What

- Start with `worker-coordination` when one planner or executor is no longer enough.
- Use `delegation-budgets` when the coordinator must bound worker cost or effort instead of delegating without limits.
- Use `orchestrator-workers` when one coordinator should own the global goal and delegate narrow subtasks to workers.
- Use `debate-and-arbitration` when workers can disagree and the coordinator needs a simple merge rule.
- Use `role-assignment` when the main problem is deciding which workers should exist and what each one should own.
- Do not add more workers until the role boundaries are obvious.
