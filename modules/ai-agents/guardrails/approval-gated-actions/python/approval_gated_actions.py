from __future__ import annotations

_SIDE_EFFECT_ACTIONS = {
    "send_email",
    "purchase",
    "delete_file",
    "publish",
    "change_permissions",
    "submit_form",
}

_RISK_LEVELS = {"low", "medium", "high"}
_DECISION_ROUTES = {
    "approve": "execute",
    "deny": "cancel",
    "edit": "revise",
}


def approval_required(action_type: str, risk_level: str, external_side_effect: bool) -> bool:
    cleaned_action = action_type.strip()
    cleaned_risk = risk_level.strip().lower()
    if not cleaned_action:
        raise ValueError("action_type must be non-empty")
    if cleaned_risk not in _RISK_LEVELS:
        raise ValueError("risk_level must be low, medium, or high")

    return (
        external_side_effect
        and (cleaned_risk in {"medium", "high"} or cleaned_action in _SIDE_EFFECT_ACTIONS)
    )


def approval_packet(
    action_id: str,
    action_type: str,
    summary: str,
    risk_level: str,
) -> dict[str, str]:
    cleaned_action_id = action_id.strip()
    cleaned_action_type = action_type.strip()
    cleaned_summary = summary.strip()
    cleaned_risk = risk_level.strip().lower()

    if not cleaned_action_id:
        raise ValueError("action_id must be non-empty")
    if not cleaned_action_type:
        raise ValueError("action_type must be non-empty")
    if not cleaned_summary:
        raise ValueError("summary must be non-empty")
    if cleaned_risk not in _RISK_LEVELS:
        raise ValueError("risk_level must be low, medium, or high")

    return {
        "action_id": cleaned_action_id,
        "action_type": cleaned_action_type,
        "summary": cleaned_summary,
        "risk_level": cleaned_risk,
    }


def post_approval_route(decision: str) -> str:
    cleaned_decision = decision.strip().lower()
    if cleaned_decision not in _DECISION_ROUTES:
        raise ValueError("decision must be approve, deny, or edit")
    return _DECISION_ROUTES[cleaned_decision]
