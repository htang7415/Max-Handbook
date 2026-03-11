# Agent Tracing Basics

> Track: `ai-agents` | Topic: `observability`

## Concept

Agent tracing basics record the important steps of one run so you can see what happened, how long it took, and which steps failed.

## Key Points

- A trace should be cheap to record and easy to inspect.
- Step-level latency is often enough to find the bottleneck.
- Failed spans are the fastest way to separate model, tool, and workflow issues.

## Core Math

- Total trace latency:
  $$
  \sum_i \text{span latency}_i
  $$
- Failure rate:
  $$
  \frac{\text{failed spans}}{\text{all spans}}
  $$

## Minimal Code Mental Model

```python
trace = start_trace("run_7", "prepare report")
trace = add_span(trace, "tool_call", 180.0, "ok")
summary = summarize_trace(trace)
```

## Function

```python
def start_trace(run_id: str, goal: str) -> dict[str, object]:
def add_span(trace: dict[str, object], name: str, latency_ms: float, status: str) -> dict[str, object]:
def summarize_trace(trace: dict[str, object]) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/ai-agents/observability/agent-tracing-basics/python -q
```
