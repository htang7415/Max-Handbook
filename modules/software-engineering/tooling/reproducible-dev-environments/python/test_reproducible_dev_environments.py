from __future__ import annotations

from reproducible_dev_environments import (
    environment_drift,
    find_unpinned_dependencies,
    missing_reproducibility_controls,
)


def test_find_unpinned_dependencies_flags_ranges_and_wildcards() -> None:
    dependencies = {
        "fastapi": "^0.116.0",
        "httpx": ">=0.28.0",
        "pydantic": "2.11.0",
        "pytest": "*",
    }

    assert find_unpinned_dependencies(dependencies) == ["fastapi", "httpx", "pytest"]


def test_environment_drift_reports_missing_mismatched_and_unexpected_entries() -> None:
    required = {"python": "3.12.2", "node": "22.14.0"}
    actual = {"python": "3.11.9", "pnpm": "10.8.0"}

    assert environment_drift(required, actual) == {
        "missing": ["node"],
        "mismatched": ["python"],
        "unexpected": ["pnpm"],
    }


def test_missing_reproducibility_controls_combines_runtime_lockfile_and_pin_checks() -> None:
    missing = missing_reproducibility_controls(
        runtime_version="",
        lockfile_present=False,
        dependencies={"fastapi": "^0.116.0", "pydantic": "2.11.0"},
    )

    assert missing == [
        "pin runtime version",
        "commit lockfile",
        "pin dependency versions: fastapi",
    ]
