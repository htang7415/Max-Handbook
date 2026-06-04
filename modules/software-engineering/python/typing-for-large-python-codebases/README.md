# Typing For Large Python Codebases

> Track: `software-engineering` | Topic: `python`

## Concept

Typing helps large Python codebases by making public boundaries explicit and by showing where interface drift would otherwise stay hidden until runtime.

## Use When

| Boundary | Typing Priority |
| --- | --- |
| Public function or service API | Annotate parameters and return type |
| Multiple implementations share behavior | Consider a protocol |
| Internal one-off helper | Keep typing useful but lightweight |

## First Principles

- Missing annotations at public boundaries create ambiguity that spreads through the codebase.
- Return types matter as much as parameter types for readers and checkers.
- Protocol-style interfaces become useful when multiple implementations need one contract.

## Workflow

1. Annotate public boundaries before private helpers.
2. Add return types for anything consumed by another module.
3. Use protocols when callers need one contract across implementations.
4. Tighten internal typing as the code stabilizes.

## Minimal Code Mental Model

```python
missing = missing_annotations({"user_id": "str", "limit": None}, return_type="list[str]")
ready = typed_api_ready({"user_id": "str", "limit": "int"}, return_type="list[str]")
protocol = needs_protocol(interface_methods=4, multiple_implementations=True)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Only annotating parameters | Return shape still drifts |
| Protocol for one implementation | Extra abstraction without payoff |
| Leaving public APIs untyped | Ambiguity spreads to callers |

## Function

```python
def missing_annotations(params: dict[str, str | None], return_type: str | None) -> list[str]:
def typed_api_ready(params: dict[str, str | None], return_type: str | None) -> bool:
def needs_protocol(interface_methods: int, multiple_implementations: bool) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/python/typing-for-large-python-codebases/python -q
```
