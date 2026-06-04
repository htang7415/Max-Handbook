# Requirements And Failure Models

> Track: `software-engineering` | Topic: `system-design`

## Concept

System design starts by making quality requirements and expected failure modes explicit before choosing components.

## Use When

| Design Question | Decide First |
| --- | --- |
| What should the architecture optimize? | Quality attributes |
| What can go wrong? | Failure model |
| Which component pattern fits? | Dominant requirement and failure |

## First Principles

- Latency, availability, and correctness trade off against each other.
- A design should be shaped by likely failures, not by ideal-path diagrams.
- Overload, dependency failure, and state corruption lead to different architectural priorities.

## Workflow

1. State latency, availability, correctness, and scale requirements.
2. List the most likely failure modes.
3. Pick the dominant failure to design around first.
4. Choose architecture patterns that protect the required quality attribute.

## Minimal Code Mental Model

```python
attributes = required_quality_attributes(user_facing=True, high_scale=True, strict_correctness=False)
failure = dominant_failure_model(external_dependencies=4, stateful_components=1, overload_risk=True)
focus = architecture_focus(attributes, failure)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Starting from components | Design optimizes a diagram instead of requirements |
| No failure model | Reliability work is reactive |
| Conflicting quality goals | Trade-offs stay hidden until implementation |

## Function

```python
def required_quality_attributes(user_facing: bool, high_scale: bool, strict_correctness: bool) -> list[str]:
def dominant_failure_model(external_dependencies: int, stateful_components: int, overload_risk: bool) -> str:
def architecture_focus(requirements: list[str], failure_model: str) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/system-design/requirements-and-failure-models/python -q
```
