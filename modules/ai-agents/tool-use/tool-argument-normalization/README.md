# Tool Argument Normalization

> Track: `ai-agents` | Topic: `tool-use`

## Concept

Tool argument normalization cleans, renames, and fills simple defaults in tool arguments before execution.

## Key Points

- Normalization should happen before the tool call, not after it fails.
- Simple cleanup avoids many avoidable tool errors.
- A small explicit mapping is easier to audit than hidden magic.

## Minimal Code Mental Model

```python
normalized = normalize_arguments({"city": " Madison ", "units": ""}, {"city": "location"}, {"units": "metric"})
missing = missing_required_arguments(normalized, ["location", "units"])
ready = arguments_ready(normalized, ["location", "units"])
```

## Function

```python
def normalize_arguments(arguments: dict[str, object], aliases: dict[str, str], defaults: dict[str, object]) -> dict[str, object]:
def missing_required_arguments(arguments: dict[str, object], required: list[str]) -> list[str]:
def arguments_ready(arguments: dict[str, object], required: list[str]) -> bool:
```

## Run tests

```bash
pytest modules/ai-agents/tool-use/tool-argument-normalization/python -q
```
