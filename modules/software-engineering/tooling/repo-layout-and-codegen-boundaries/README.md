# Repo Layout And Codegen Boundaries

> Track: `software-engineering` | Topic: `tooling`

## Concept

A repo stays understandable when humans know which files are source of truth, which files are generated outputs, and which files should never be committed.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Repo review | Source, generated, config, tests, and artifacts are mixed | The repo has one tiny source file |
| Codegen workflow | Generated outputs appear in diffs | The generator output is never committed |
| Build hygiene | Artifacts can accidentally enter commits | The artifact is explicitly part of the source release |

## First Principles

- Generated outputs should be easy to distinguish from hand-edited source.
- Review should focus on generator inputs and ownership boundaries, not just on diff size.
- Build artifacts and source files should not share the same commit path semantics.

## Workflow

1. Classify changed paths by repo role.
2. Reject hand edits to generated outputs and build artifacts.
3. Review generator inputs separately from generated diffs.
4. Warn when source-of-truth and generated changes are mixed.
5. Keep build artifacts out unless the repo explicitly requires them.

## Minimal Code Mental Model

```python
kind = classify_repo_path("src/generated/client.ts")
editable = should_edit_by_hand("src/generated/client.ts")
warnings = boundary_warnings(
    ["src/api/spec.yaml", "src/generated/client.ts", "dist/bundle.js"]
)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Hand-edited generated file | Regeneration overwrites the fix | `should_edit_by_hand` rejects generated paths |
| Mixed source and generated diff | Reviewers miss the real source of truth | `boundary_warnings` asks for separate review |
| Build artifact committed | Repo history fills with non-source outputs | `boundary_warnings` warns on artifact paths |

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
