# Dependency And Supply-Chain Risk

> Track: `software-engineering` | Topic: `security-basics`

## Concept

Dependency risk comes from what third-party code can do in your build and runtime, not just from whether the package is convenient to install.

## Key Points

- Known vulnerabilities are a direct risk signal.
- Install-time scripts increase trust requirements because code runs before the app even starts.
- Unpinned or weakly reviewed dependencies need stronger gates on production paths.

## Minimal Code Mental Model

```python
risk = dependency_risk(version_pinned=False, known_vulnerabilities=0, executes_install_script=True)
gate = dependency_gate(risk, in_production_path=True)
portfolio = portfolio_risk(["low", "medium", "high"])
```

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
