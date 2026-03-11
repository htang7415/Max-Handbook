# Agent Evaluation Basics

> Track: `ai-agents` | Topic: `evaluation`

## Concept

Agent evaluation basics measure whether tasks finish successfully, whether tools work reliably, how long runs take, and which failure category dominates.

## Key Points

- Final task success is the main outcome metric.
- Tool-call success tells you whether failures come from execution instead of reasoning.
- A simple failure breakdown is often enough to find the next bottleneck.

## Core Math

- Task success rate:
  $$
  \frac{\text{successful tasks}}{\text{tasks evaluated}}
  $$
- Tool-call success rate:
  $$
  \frac{\text{successful tool calls}}{\text{tool calls}}
  $$
- Mean latency:
  $$
  \frac{1}{N}\sum_i \text{latency}_i
  $$

## Minimal Code Mental Model

```python
success = task_success_rate([True, False, True])
tool_success = tool_call_success_rate([True, True, False])
latency = mean_latency_ms([100.0, 140.0, 160.0])
breakdown = failure_breakdown(["tool", "model", "tool"])
```

## Function

```python
def task_success_rate(outcomes: list[bool]) -> float:
def tool_call_success_rate(outcomes: list[bool]) -> float:
def mean_latency_ms(latencies_ms: list[float]) -> float:
def failure_breakdown(labels: list[str]) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/ai-agents/evaluation/agent-evaluation-basics/python -q
```
