# Tool Failure Handling

> Track: `ai-agents` | Topic: `tool-use`

## Concept

Tool failure handling decides whether a failed tool call should be retried, replaced with a fallback tool, or escalated out of the loop.

## Key Points

- Not every tool failure should be retried.
- Retry is best for transient errors like timeouts or rate limits.
- Fallback and escalation should be explicit so the next step is easy to inspect.

## Minimal Code Mental Model

```python
kind = failure_kind({"status": "error", "message": "timeout"})
action = next_action(kind, retryable_errors={"timeout"}, fallback_map={"search": "browse_docs"})
route = fallback_tool("search", {"search": "browse_docs"})
```

## Function

```python
def failure_kind(result: dict[str, object]) -> str:
def next_action(failure: str, retryable_errors: set[str], fallback_map: dict[str, str] | None = None) -> str:
def fallback_tool(tool_name: str, fallback_map: dict[str, str]) -> str | None:
```

## Run tests

```bash
pytest modules/ai-agents/tool-use/tool-failure-handling/python -q
```
