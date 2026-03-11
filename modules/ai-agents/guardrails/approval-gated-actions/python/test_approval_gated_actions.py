from __future__ import annotations

import pytest

from approval_gated_actions import (
    approval_packet,
    approval_required,
    post_approval_route,
)


def test_approval_gate_detects_risky_or_sensitive_actions() -> None:
    assert approval_required("send_email", risk_level="medium", external_side_effect=True) is True
    assert approval_required("purchase", risk_level="low", external_side_effect=True) is True
    assert approval_required("summarize_notes", risk_level="low", external_side_effect=False) is False


def test_approval_packet_and_routes_cover_approve_deny_edit() -> None:
    packet = approval_packet(
        "act_7",
        "send_email",
        "Email the signed contract to the vendor",
        "medium",
    )

    assert packet == {
        "action_id": "act_7",
        "action_type": "send_email",
        "summary": "Email the signed contract to the vendor",
        "risk_level": "medium",
    }
    assert post_approval_route("approve") == "execute"
    assert post_approval_route("deny") == "cancel"
    assert post_approval_route("edit") == "revise"


def test_approval_gated_actions_validation() -> None:
    with pytest.raises(ValueError):
        approval_required("", risk_level="medium", external_side_effect=True)
    with pytest.raises(ValueError):
        approval_required("send_email", risk_level="urgent", external_side_effect=True)
    with pytest.raises(ValueError):
        approval_packet("act_7", "send_email", "", "medium")
    with pytest.raises(ValueError):
        post_approval_route("retry")
