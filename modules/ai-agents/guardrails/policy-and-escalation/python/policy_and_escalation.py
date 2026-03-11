from __future__ import annotations


def _contains_any(text: str, terms: list[str]) -> bool:
    lowered = text.lower()
    return any(term.strip().lower() in lowered for term in terms if term.strip())


def policy_decision(text: str, blocked_terms: list[str], review_terms: list[str]) -> str:
    if _contains_any(text, blocked_terms):
        return "block"
    if _contains_any(text, review_terms):
        return "review"
    return "allow"


def escalation_reason(decision: str, model_confidence: float, threshold: float) -> str | None:
    if not 0.0 <= model_confidence <= 1.0:
        raise ValueError("model_confidence must satisfy 0 <= value <= 1")
    if not 0.0 <= threshold <= 1.0:
        raise ValueError("threshold must satisfy 0 <= value <= 1")
    if decision == "block":
        return "policy_block"
    if decision == "review":
        return "policy_review"
    if model_confidence < threshold:
        return "low_confidence"
    return None


def action_message(decision: str) -> str:
    if decision == "allow":
        return "Proceed."
    if decision == "review":
        return "Escalate for review."
    if decision == "block":
        return "Do not answer. Block the request."
    raise ValueError("decision must be allow, review, or block")
