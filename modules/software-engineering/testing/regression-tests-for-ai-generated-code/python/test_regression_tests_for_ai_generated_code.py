from __future__ import annotations

from regression_tests_for_ai_generated_code import (
    missing_regression_cases,
    release_ready,
    select_regression_cases,
)


def test_select_regression_cases_uses_change_scope_bugfix_history_and_generated_code_flag() -> None:
    required = select_regression_cases(
        ["services/auth/policy.py", "src/generated/client.ts"],
        {
            "auth": ["auth-deny-default"],
            "generated": ["client-contract-drift"],
            "billing": ["billing-retry"],
        },
        recent_bugfix_case_ids=["incident-1427"],
        touches_generated_code=True,
    )

    assert required == [
        "auth-deny-default",
        "client-contract-drift",
        "generated-output-drift",
        "incident-1427",
        "smoke",
    ]


def test_missing_regression_cases_reports_unexecuted_required_cases() -> None:
    assert missing_regression_cases(
        ["smoke", "auth-deny-default", "incident-1427"],
        ["smoke", "incident-1427"],
    ) == ["auth-deny-default"]


def test_release_ready_requires_all_required_cases_to_pass() -> None:
    required = ["smoke", "auth-deny-default"]

    assert release_ready(required, ["smoke", "auth-deny-default"]) is True
    assert release_ready(required, ["smoke"]) is False
