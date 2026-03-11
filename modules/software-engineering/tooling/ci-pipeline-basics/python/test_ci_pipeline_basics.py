from __future__ import annotations

from ci_pipeline_basics import mergeable, pipeline_blockers, required_ci_stages


def test_required_ci_stages_expand_with_change_risk() -> None:
    assert required_ci_stages(["api", "bugfix"]) == ["lint", "unit", "contract", "regression"]
    assert required_ci_stages(["database", "release"]) == ["lint", "unit", "integration", "build"]


def test_pipeline_blockers_report_missing_or_failed_required_stages() -> None:
    stages = required_ci_stages(["api", "bugfix"])
    statuses = {
        "lint": "passed",
        "unit": "passed",
        "contract": "failed",
        "regression": "passed",
    }

    assert pipeline_blockers(statuses, stages) == ["contract"]


def test_mergeable_requires_all_required_stages_to_pass() -> None:
    stages = required_ci_stages(["api"])

    assert mergeable({"lint": "passed", "unit": "passed", "contract": "passed"}, stages) is True
    assert mergeable({"lint": "passed", "unit": "passed"}, stages) is False
