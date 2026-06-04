# {{SLUG}}

> Track: `{{TRACK}}` | Topic: `{{TOPIC}}`

## Concept

<!-- One sentence: what problem this solves and what mechanism it uses. -->

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| <!-- case --> | <!-- signal or constraint --> | <!-- failure or simpler option --> |

## First Principles

<!--
- What invariant, boundary, or trade-off matters?
- What assumption must be true for the idea to work?
-->

## Workflow

1. <!-- Frame the input contract. -->
2. <!-- Apply the mechanism. -->
3. <!-- Check the output or state transition. -->
4. <!-- Decide whether to accept, retry, or escalate. -->

## Minimal Code Mental Model

```python
# Show the smallest executable shape of the idea.
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| <!-- failure --> | <!-- observable signal --> | <!-- focused check --> |

## Function

```python
# Replace with the public function signatures exercised by tests.
```

## Run tests

```bash
pytest modules/{{TRACK}}/{{TOPIC}}/{{SLUG}}/python -q
```
