# Plan-Act Loop

> Track: `ai-agents` | Topic: `planning`

## Concept

A plan-act loop turns a goal into explicit steps, tracks what is still open, and updates the plan after each completed step.

## Key Points

- Planning is most useful when a task has more than one dependent action.
- The next action should come from plan state, not from free-form guessing.
- A simple linear plan is a good baseline before branching strategies.

## Core Math

- Completion fraction:
  $$
  \frac{\text{completed steps}}{\text{total steps}}
  $$
- Next-step rule:
  $$
  \text{next} = \min\{i : \text{step}_i \text{ not done}\}
  $$

## Minimal Code Mental Model

```python
plan = make_plan("Prepare launch report", ["collect metrics", "write summary", "send report"])
next_step = next_pending_step(plan)
updated = mark_step_done(plan, 0)
```

## Function

```python
def make_plan(goal: str, steps: list[str]) -> list[dict[str, object]]:
def next_pending_step(plan: list[dict[str, object]]) -> int | None:
def mark_step_done(plan: list[dict[str, object]], step_index: int) -> list[dict[str, object]]:
```

## Run tests

```bash
pytest modules/ai-agents/planning/plan-act-loop/python -q
```
