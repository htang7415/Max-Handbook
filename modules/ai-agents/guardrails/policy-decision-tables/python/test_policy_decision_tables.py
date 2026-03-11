from __future__ import annotations

import pytest

from policy_decision_tables import (
    decision_table_action,
    ranked_policy_rules,
    rule_specificity,
)


def test_policy_decision_tables_rank_specific_rules_first() -> None:
    rules = [
        {"conditions": {"blocked_term": True}, "action": "block"},
        {"conditions": {"contains_pii": True, "needs_tool": True}, "action": "review"},
    ]

    assert rule_specificity(rules[0]) == 1
    assert rule_specificity(rules[1]) == 2
    assert ranked_policy_rules(rules) == [
        {
            "conditions": {"contains_pii": True, "needs_tool": True},
            "action": "review",
            "specificity": 2,
        },
        {
            "conditions": {"blocked_term": True},
            "action": "block",
            "specificity": 1,
        },
    ]


def test_policy_decision_tables_route_matching_signals_or_default() -> None:
    rules = [
        {"conditions": {"blocked_term": True}, "action": "block"},
        {"conditions": {"contains_pii": True, "needs_tool": True}, "action": "review"},
    ]

    assert (
        decision_table_action(
            {"blocked_term": False, "contains_pii": True, "needs_tool": True},
            rules,
            default_action="allow",
        )
        == "review"
    )
    assert (
        decision_table_action(
            {"blocked_term": False, "contains_pii": False, "needs_tool": False},
            rules,
            default_action="allow",
        )
        == "allow"
    )


def test_policy_decision_tables_validation() -> None:
    with pytest.raises(ValueError):
        rule_specificity({"conditions": {}, "action": "review"})
    with pytest.raises(ValueError):
        ranked_policy_rules([])
    with pytest.raises(ValueError):
        decision_table_action({}, [{"conditions": {"blocked_term": True}, "action": "block"}], "allow")
    with pytest.raises(ValueError):
        decision_table_action({"blocked_term": "yes"}, [{"conditions": {"blocked_term": True}, "action": "block"}], "allow")
