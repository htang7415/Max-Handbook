# Packaging And Project Layout

> Track: `software-engineering` | Topic: `python`

## Concept

A Python project stays maintainable when the package root, test layout, and packaging metadata make import boundaries and build behavior explicit.

## Use When

| Project Signal | Layout Choice |
| --- | --- |
| Package will be installed or reused | Add packaging metadata |
| Imports should reflect installed behavior | Prefer `src/` layout |
| Tests need clear package boundaries | Keep tests outside the package root |

## First Principles

- A `src/` layout reduces accidental imports from the repo root.
- Packaging metadata should exist before the project grows into scripts and services.
- Tests and package entry points should be easy to locate from the directory tree.

## Workflow

1. Choose the import root and package name.
2. Put package code under `src/` when installed behavior matters.
3. Add `pyproject.toml` before scripts and services multiply.
4. Keep tests discoverable and separate from runtime package code.

## Minimal Code Mental Model

```python
paths = recommended_paths("billing_service", uses_src_layout=True)
root = import_root("billing_service", uses_src_layout=True)
ready = packaging_ready(pyproject_present=True, package_init_present=True, tests_present=True)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Importing from repo root accidentally | Tests pass while installed package fails |
| Missing packaging metadata | Build and deploy behavior stays implicit |
| Scattered entry points | New engineers cannot find how the project runs |

## Function

```python
def recommended_paths(package_name: str, uses_src_layout: bool) -> dict[str, str]:
def import_root(package_name: str, uses_src_layout: bool) -> str:
def packaging_ready(pyproject_present: bool, package_init_present: bool, tests_present: bool) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/python/packaging-and-project-layout/python -q
```
