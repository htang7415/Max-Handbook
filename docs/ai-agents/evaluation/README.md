# Evaluation

This section is about how to measure whether an agent succeeds, whether its tool calls work, and where failures happen.

## Purpose

Use this page to understand:
- task success
- tool-call success
- latency and cost baselines
- failure category counts

## First Principles

- Agent evaluation should measure both final outcomes and the steps that produced them.
- Simple metrics are usually enough to find the main bottlenecks.
- A useful evaluation loop separates model failure, tool failure, and workflow failure.

## Minimal Code Mental Model

```python
success = task_success_rate([True, False, True])
tool_success = tool_call_success_rate([True, True, False])
breakdown = failure_breakdown(["tool", "model", "tool"])
```

## Canonical Modules

- Core agent metrics: `agent-evaluation-basics`

## Supporting Modules

- Step-level completion and blockage summaries: `step-level-evaluation`
- Cost-quality summaries across runs: `cost-quality-tradeoffs`
- A/B-style comparison between agent variants: `experiment-comparison`
- Detecting quality drift against a baseline: `regression-checks`
- Grouping failures into stable categories: `failure-taxonomy`

## When To Use What

- Start with `agent-evaluation-basics` before adding judge-based or benchmark-heavy evaluation.
- Use `step-level-evaluation` when whole-run success is too coarse to explain where the agent fails.
- Use `cost-quality-tradeoffs` when comparing variants where quality, cost, and success all matter.
- Use `experiment-comparison` when you need a side-by-side summary of two prompts, tools, or workflows.
- Use `regression-checks` when a new variant should not fall below an existing baseline on key metrics.
- Use `failure-taxonomy` when repeated failures need a stable set of labels for triage and reporting.
- Track latency and failure labels together so you know whether the bottleneck is planning, tool use, or execution.
