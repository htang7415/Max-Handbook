from __future__ import annotations


def _tokens(text: str) -> set[str]:
    return {token for token in text.lower().split() if token}


def claim_support_map(claims: list[str], evidence: list[str]) -> dict[str, bool]:
    evidence_tokens = [_tokens(item) for item in evidence if item.strip()]
    support: dict[str, bool] = {}
    for claim in claims:
        cleaned = claim.strip()
        if not cleaned:
            continue
        claim_tokens = _tokens(cleaned)
        support[cleaned] = any(claim_tokens <= evidence_set for evidence_set in evidence_tokens)
    return support


def grounded_claim_rate(support_map: dict[str, bool]) -> float:
    if not support_map:
        raise ValueError("support_map must be non-empty")
    return sum(1 for value in support_map.values() if value) / len(support_map)


def unsupported_claims(support_map: dict[str, bool]) -> list[str]:
    return [claim for claim, supported in support_map.items() if not supported]
