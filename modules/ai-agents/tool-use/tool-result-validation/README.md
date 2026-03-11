# Tool Result Validation

> Track: `ai-agents` | Topic: `tool-use`

## Concept

Tool result validation checks whether a tool response has the required fields, signals an execution error, or can be safely passed back into the agent loop.

## Key Points

- Tool outputs should be validated before the model reasons over them.
- Missing required fields are often enough to stop a bad tool response early.
- Validation should produce a simple pass/fail decision plus a reason.

## Minimal Code Mental Model

```python
valid = result_has_fields({"temperature_f": 41, "status": "ok"}, ["temperature_f", "status"])
error = result_has_error({"status": "error", "message": "timeout"})
report = validation_report({"status": "ok", "temperature_f": 41}, ["temperature_f", "status"])
```

## Function

```python
def result_has_fields(result: dict[str, object], required_fields: list[str]) -> bool:
def result_has_error(result: dict[str, object]) -> bool:
def validation_report(result: dict[str, object], required_fields: list[str]) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/ai-agents/tool-use/tool-result-validation/python -q
```
