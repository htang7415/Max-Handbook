# Repo Layout And Codegen Boundaries

> Track: `software-engineering` | Topic: `tooling`

## Concept

A repo stays understandable when humans know which files are source of truth, which files are generated outputs, and which files should never be committed.

## Key Points

- Generated outputs should be easy to distinguish from hand-edited source.
- Review should focus on generator inputs and ownership boundaries, not just on diff size.
- Build artifacts and source files should not share the same commit path semantics.

## Minimal Code Mental Model

```python
kind = classify_repo_path("src/generated/client.ts")
editable = should_edit_by_hand("src/generated/client.ts")
warnings = boundary_warnings(
    ["src/api/spec.yaml", "src/generated/client.ts", "dist/bundle.js"]
)
```

## Function

```python
def classify_repo_path(path: str) -> str:
def should_edit_by_hand(path: str) -> bool:
def boundary_warnings(changed_paths: list[str]) -> list[str]:
```

## Run tests

```bash
pytest modules/software-engineering/tooling/repo-layout-and-codegen-boundaries/python -q
```
