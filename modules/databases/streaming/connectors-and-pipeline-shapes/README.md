# Connectors And Pipeline Shapes

> Track: `databases` | Topic: `streaming`

## Concept

Connectors move data between systems, and the shape of the pipeline determines how sources, transforms, and sinks are allowed to connect.

## Key Points

- Sources should not have inbound edges.
- Sinks should not have outbound edges.
- A simple pipeline can be source-to-sink, source-transform-sink, fan-in, or fan-out.
- Validating connector shape early prevents messy pipelines that are hard to operate.

## Minimal Code Mental Model

```python
stages = {"db": "source", "clean": "transform", "warehouse": "sink"}
edges = [("db", "clean"), ("clean", "warehouse")]
valid = validate_pipeline(stages, edges)
shape = classify_pipeline_shape(stages, edges)
```

## Function

```python
def validate_pipeline(
    stages: dict[str, str],
    edges: list[tuple[str, str]],
) -> bool:
def classify_pipeline_shape(
    stages: dict[str, str],
    edges: list[tuple[str, str]],
) -> str:
def reachable_sinks(
    stages: dict[str, str],
    edges: list[tuple[str, str]],
    source_name: str,
) -> list[str]:
```

## Run tests

```bash
pytest modules/databases/streaming/connectors-and-pipeline-shapes/python -q
```
