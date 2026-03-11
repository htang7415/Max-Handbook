# Self-Check Patterns

> Track: `ai-agents` | Topic: `prompting`

## Concept

Self-check patterns ask the model to verify a small checklist before it returns the final answer.

## Key Points

- A self-check is most useful for explicit constraints, not for deep hidden correctness.
- The checklist should be short and easy to inspect.
- The final answer should stay separate from the self-check notes.

## Minimal Code Mental Model

```python
checklist = self_check_checklist(["answer in bullets", "cite sources"])
notes = self_check_notes({"bullets": True, "citations": False})
ready = self_check_pass({"bullets": True, "citations": True})
```

## Function

```python
def self_check_checklist(items: list[str]) -> list[str]:
def self_check_notes(results: dict[str, bool]) -> list[str]:
def self_check_pass(results: dict[str, bool]) -> bool:
```

## Run tests

```bash
pytest modules/ai-agents/prompting/self-check-patterns/python -q
```
