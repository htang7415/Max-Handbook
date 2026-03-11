# Expected-Value Tool Selection

> Track: `ai-agents` | Topic: `tool-use`

## Concept

Expected-value tool selection compares candidate tools by balancing likely success value against execution cost and failure penalty before the agent commits to a call.

## Key Points

- The best tool is not always the one with the highest success probability.
- Expected value should include both tool cost and the downside of failure.
- A weak top tool should be skipped, and a close race should go to review.

## Minimal Code Mental Model

```python
ranking = rank_tools_by_expected_value(tool_profiles)
tool = tool_selection_route(tool_profiles, min_expected_value=4.0, min_margin=1.0)
```

## Function

```python
def expected_tool_value(
    success_probability: float,
    success_value: float,
    tool_cost: float,
    failure_penalty: float = 0.0,
) -> float:
def rank_tools_by_expected_value(tool_to_profile: dict[str, dict[str, float]]) -> list[dict[str, object]]:
def tool_selection_route(
    tool_to_profile: dict[str, dict[str, float]],
    min_expected_value: float,
    min_margin: float = 0.0,
) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/tool-use/expected-value-tool-selection/python -q
```
