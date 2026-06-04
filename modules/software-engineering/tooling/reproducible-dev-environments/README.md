# Reproducible Dev Environments

> Track: `software-engineering` | Topic: `tooling`

## Concept

A development environment is reproducible when another machine can rebuild the same runtime and dependency set without relying on local accident.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Onboarding | A new machine should match the project runtime | The project is a throwaway local script |
| CI drift | Builds differ between local and CI | The runtime is managed outside the repo by policy |
| Dependency review | Version ranges or wildcards can change behavior | All dependencies are pinned and locked |

## First Principles

- Reproducibility needs both a pinned runtime and pinned dependencies.
- A lockfile reduces ambiguity, but it does not fix unpinned dependency intent by itself.
- Version drift should be reported explicitly instead of being discovered by failed builds later.

## Workflow

1. Pin the runtime version.
2. Commit a lockfile for resolved dependencies.
3. Detect unpinned dependency specs.
4. Compare required and actual tool versions.
5. Report missing controls before the build fails later.

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

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Floating dependency | Same install produces different code later | `find_unpinned_dependencies` flags ranges and wildcards |
| Runtime drift | Local and CI disagree about versions | `environment_drift` reports missing and mismatched tools |
| Missing lockfile | Dependency resolution is not reproducible | `missing_reproducibility_controls` reports `commit lockfile` |

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
