from __future__ import annotations

from failure_taxonomy import categorize_failure, failure_category_counts, top_failure_category


def test_failure_taxonomy_groups_common_failures() -> None:
    assert categorize_failure("tool timeout") == "tool"
    assert categorize_failure("policy block") == "policy"
    assert categorize_failure("workflow handoff missing state") == "workflow"
    assert categorize_failure("model hallucination") == "model"
    counts = failure_category_counts(["tool timeout", "policy block", "tool timeout"])
    assert counts == {"tool": 2, "policy": 1}
    assert top_failure_category(["tool timeout", "policy block", "tool timeout"]) == "tool"


def test_failure_taxonomy_handles_unknown() -> None:
    assert categorize_failure("") == "unknown"
    assert top_failure_category([]) is None
