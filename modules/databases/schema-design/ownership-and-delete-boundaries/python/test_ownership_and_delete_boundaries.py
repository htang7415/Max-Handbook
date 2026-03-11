import pytest

from ownership_and_delete_boundaries import can_delete, delete_plan, relation


def test_owned_children_can_cascade_while_shared_refs_block_delete() -> None:
    plan = delete_plan(
        "workspace",
        [
            relation("documents", "cascade"),
            relation("chunks", "cascade"),
            relation("billing-account", "block"),
        ],
    )

    assert plan == {
        "parent": "workspace",
        "cascade": ["chunks", "documents"],
        "block": ["billing-account"],
        "detach": [],
    }
    assert can_delete(plan) is False


def test_detach_policy_allows_delete_without_cascading_shared_rows() -> None:
    plan = delete_plan(
        "user",
        [relation("sessions", "cascade"), relation("api-keys", "detach")],
    )

    assert can_delete(plan) is True


def test_invalid_policy_is_rejected() -> None:
    with pytest.raises(ValueError, match="unsupported delete policy"):
        relation("mystery", "maybe")
