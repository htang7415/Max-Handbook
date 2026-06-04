# Dependency And Supply-Chain Risk

> Track: `software-engineering` | Topic: `security-basics`

## Concept

Dependency risk comes from what third-party code can do in your build and runtime, not just from whether the package is convenient to install.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| New dependency | Third-party code enters build or runtime | Code is internal and already owned |
| Production path | Dependency behavior affects users or secrets | Dependency is only local tooling with no install scripts |
| Portfolio review | Several dependencies need one risk summary | Each dependency is already individually blocked |

## First Principles

- Known vulnerabilities are a direct risk signal.
- Install-time scripts increase trust requirements because code runs before the app even starts.
- Unpinned or weakly reviewed dependencies need stronger gates on production paths.

## Workflow

1. Check whether the dependency version is pinned.
2. Count known vulnerabilities.
3. Check whether install scripts execute code.
4. Classify risk as low, medium, or high.
5. Block or review production-path risk before release.

## Minimal Code Mental Model

```python
risk = dependency_risk(version_pinned=False, known_vulnerabilities=0, executes_install_script=True)
gate = dependency_gate(risk, in_production_path=True)
portfolio = portfolio_risk(["low", "medium", "high"])
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Known vulnerability ignored | High-risk package ships | `dependency_risk` returns `high` |
| Install script trusted blindly | Code runs before app startup | Install scripts raise risk to `medium` |
| Invalid risk rollup | Portfolio summary hides bad dependency | `portfolio_risk` validates and returns highest risk |

## Function

```python
def dependency_risk(version_pinned: bool, known_vulnerabilities: int, executes_install_script: bool) -> str:
def dependency_gate(risk: str, in_production_path: bool) -> str:
def portfolio_risk(risks: list[str]) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/security-basics/dependency-and-supply-chain-risk/python -q
```
