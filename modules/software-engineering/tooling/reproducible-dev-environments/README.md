# Reproducible Dev Environments

> Track: `software-engineering` | Topic: `tooling`

## Concept

A development environment is reproducible when another machine can rebuild the same runtime and dependency set without relying on local accident.

## Key Points

- Reproducibility needs both a pinned runtime and pinned dependencies.
- A lockfile reduces ambiguity, but it does not fix unpinned dependency intent by itself.
- Version drift should be reported explicitly instead of being discovered by failed builds later.

## Minimal Code Mental Model

```python
unpinned = find_unpinned_dependencies({"fastapi": "^0.116.0", "pydantic": "2.11.0"})
drift = environment_drift({"python": "3.12.2"}, {"python": "3.11.9"})
missing = missing_reproducibility_controls(
    runtime_version="3.12.2",
    lockfile_present=True,
    dependencies={"fastapi": "0.116.0", "pydantic": "2.11.0"},
)
```

## Function

```python
def find_unpinned_dependencies(dependencies: dict[str, str]) -> list[str]:
def environment_drift(required: dict[str, str], actual: dict[str, str]) -> dict[str, list[str]]:
def missing_reproducibility_controls(
    runtime_version: str | None,
    lockfile_present: bool,
    dependencies: dict[str, str],
) -> list[str]:
```

## Run tests

```bash
pytest modules/software-engineering/tooling/reproducible-dev-environments/python -q
```
