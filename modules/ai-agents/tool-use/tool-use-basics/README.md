# Tool Use Basics

> Track: `ai-agents` | Topic: `tool-use`

## Concept

Basic tool use turns a user request into a structured tool call and then feeds the tool result back into the agent loop.

## Key Points

- Tool use is only helpful when the task needs fresh data or an external action.
- The core loop is select tool -> call tool -> read result.
- Structured calls reduce parsing errors and make retries safer.

## Core Math

- Expected tool value:
  $$
  p(\text{success}) \cdot \text{success value} - \text{tool cost}
  $$
- Validation rate:
  $$
  \frac{\text{valid results}}{\text{tool calls}}
  $$

## Minimal Code Mental Model

```python
tool = select_tool("check the weather in Madison", tool_keywords)
call = tool_call(tool, {"location": "Madison, WI"})
result = tool_result(call["id"], {"temperature_f": 41})
```

## Function

```python
def select_tool(intent: str, tool_keywords: dict[str, list[str]]) -> str | None:
def tool_call(name: str, arguments: dict[str, object], call_id: str = "call_1") -> dict[str, object]:
def tool_result(call_id: str, output: object, is_error: bool = False) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/ai-agents/tool-use/tool-use-basics/python -q
```
