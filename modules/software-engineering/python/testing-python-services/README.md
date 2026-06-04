# Testing Python Services

> Track: `software-engineering` | Topic: `python`

## Concept

Python service tests stay useful when external dependencies are isolated, shared state is controlled, and fixtures make the service boundary easy to exercise.

## Use When

| Dependency | Test Control |
| --- | --- |
| Database | Fixture or transaction boundary |
| External API | Fake or stubbed client |
| Clock or randomness | Inject deterministic provider |
| Shared state | Reset per test |

## First Principles

- Database, clock, and external API dependencies should be isolated in tests.
- Service tests should prefer fast fixtures over broad environment coupling.
- A Python service test suite becomes fragile when state leaks across test cases.

## Workflow

1. Split pure logic tests from service-boundary tests.
2. Add fixtures for required database or state setup.
3. Override external APIs and clocks.
4. Ensure each test can run without depending on previous tests.

## Minimal Code Mental Model

```python
layers = service_test_layers(needs_db=True, external_api=True)
overrides = dependency_overrides(external_api=True, clock_dependency=True)
ready = pytest_service_ready(has_fixtures=True, isolates_state=True)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Hidden shared state | Tests pass or fail depending on order |
| Real external API in routine tests | Suite becomes slow and flaky |
| Broad environment fixture | Failures are hard to diagnose |

## Function

```python
def service_test_layers(needs_db: bool, external_api: bool) -> list[str]:
def dependency_overrides(external_api: bool, clock_dependency: bool) -> list[str]:
def pytest_service_ready(has_fixtures: bool, isolates_state: bool) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/python/testing-python-services/python -q
```
