# Observability

This section is about how to trace an agent run, inspect the steps it took, and measure where failures or latency come from.

## Purpose

Use this page to understand:
- trace structure
- step-level latency
- failed span counts

## First Principles

- Observability is how you debug the agent loop after the prompt leaves the editor.
- A useful trace records steps, status, and latency with as little extra structure as possible.
- The first goal is to separate model, tool, and workflow problems.

## Core Math

- Run success rate:
  $$
  \frac{\text{successful runs}}{\text{runs observed}}
  $$
- Total run latency:
  $$
  \sum_i \text{span latency}_i
  $$
- Failure share by source:
  $$
  \frac{\text{failures from one source}}{\text{all failures}}
  $$

## Minimal Code Mental Model

```python
trace = start_trace("run_7", "prepare report")
trace = add_span(trace, "tool_call", 180.0, "ok")
summary = summarize_trace(trace)
```

## Canonical Modules

- Trace basics: `agent-tracing-basics`

## Supporting Modules

- Aggregate trace summaries across runs: `run-analysis-metrics`
- Threshold-based alerts over run metrics: `alerting-thresholds`
- Attributing failures to model, tool, or workflow sources: `root-cause-attribution`
- A simple vocabulary for trace span types: `span-taxonomy`
- Deterministic retention of only some runs: `run-sampling`

## When To Use What

- Start with `agent-tracing-basics` as soon as the agent has more than one meaningful step.
- Use `run-analysis-metrics` when you need one dashboard-like summary over many runs.
- Use `alerting-thresholds` when the system needs a simple rule for raising alerts from latency or failure metrics.
- Use `root-cause-attribution` when the main debugging question is which layer is actually causing most failures.
- Use `span-taxonomy` when traces need a consistent naming scheme across model, tool, and workflow steps.
- Use `run-sampling` when full tracing is too expensive and you need a stable subset of runs to inspect.
- Add richer dashboards later; first get the basic run trace right.
