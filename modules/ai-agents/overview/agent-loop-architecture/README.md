# Agent Loop Architecture

> Track: `ai-agents` | Topic: `overview`

## Concept

An agent loop repeatedly turns state into an action, observes the result, records a trace, and stops when the task is done, blocked, or too risky to continue.

## Key Points

- The model is only one part of the loop; state, tools, traces, and stop rules are equally important.
- A useful architecture has explicit routes for answer, tool, review, block, and stop.
- Risk and remaining budget should affect the next action before the loop takes another step.
- Traces make later evaluation and debugging possible.

## Minimal Code Mental Model

```python
action = choose_next_action(
    goal="summarize failed deploys",
    confidence=0.72,
    risk_score=0.2,
    remaining_steps=3,
    tool_scores={"search_logs": 0.8, "send_email": -0.4},
)
state = update_loop_state({}, action["route"], "found 2 failed deploys")
span = trace_step("step-1", action["route"], latency_ms=120, success=True)
```

## Function

```python
def choose_next_action(
    goal: str,
    confidence: float,
    risk_score: float,
    remaining_steps: int,
    tool_scores: dict[str, float] | None = None,
    blocked: bool = False,
    min_confidence: float = 0.7,
    max_risk: float = 0.6,
    min_tool_margin: float = 0.15,
) -> dict[str, object]:
def update_loop_state(state: dict[str, object], route: str, observation: str) -> dict[str, object]:
def trace_step(step_id: str, route: str, latency_ms: int, success: bool) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/ai-agents/overview/agent-loop-architecture/python -q
```
