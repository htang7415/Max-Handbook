from __future__ import annotations


def claim_coverage(required_claims: list[str], supported_claims: list[str]) -> float:
    required = [claim.strip() for claim in required_claims if claim.strip()]
    supported = {claim.strip() for claim in supported_claims if claim.strip()}
    if not required:
        raise ValueError("required_claims must contain at least one non-empty claim")
    covered = sum(1 for claim in required if claim in supported)
    return covered / len(required)


def unsupported_claims(required_claims: list[str], supported_claims: list[str]) -> list[str]:
    required = [claim.strip() for claim in required_claims if claim.strip()]
    supported = {claim.strip() for claim in supported_claims if claim.strip()}
    if not required:
        raise ValueError("required_claims must contain at least one non-empty claim")
    return [claim for claim in required if claim not in supported]


def rag_abstention_route(
    coverage: float,
    support_count: int,
    min_coverage: float,
    min_support_count: int,
) -> str:
    if not 0.0 <= coverage <= 1.0:
        raise ValueError("coverage must satisfy 0 <= value <= 1")
    if support_count < 0:
        raise ValueError("support_count must be non-negative")
    if not 0.0 <= min_coverage <= 1.0:
        raise ValueError("min_coverage must satisfy 0 <= value <= 1")
    if min_support_count <= 0:
        raise ValueError("min_support_count must be positive")

    if coverage >= min_coverage and support_count >= min_support_count:
        return "answer"
    if coverage == 0.0 or support_count == 0:
        return "abstain"
    return "retrieve-more"
