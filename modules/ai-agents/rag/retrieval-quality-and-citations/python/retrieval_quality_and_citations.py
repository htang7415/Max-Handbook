from __future__ import annotations


def _has_citation(values: list[str] | None) -> bool:
    if values is None:
        return False
    return any(value.strip() for value in values)


def citation_coverage(claim_ids: list[str], citations: dict[str, list[str]]) -> float:
    cleaned_claims = [claim.strip() for claim in claim_ids if claim.strip()]
    if not cleaned_claims:
        raise ValueError("claim_ids must contain at least one non-empty claim id")
    cited = sum(1 for claim in cleaned_claims if _has_citation(citations.get(claim)))
    return cited / len(cleaned_claims)


def uncited_claims(claim_ids: list[str], citations: dict[str, list[str]]) -> list[str]:
    return [
        claim.strip()
        for claim in claim_ids
        if claim.strip() and not _has_citation(citations.get(claim.strip()))
    ]


def cited_source_counts(citations: dict[str, list[str]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for sources in citations.values():
        for source in sources:
            cleaned = source.strip()
            if not cleaned:
                continue
            counts[cleaned] = counts.get(cleaned, 0) + 1
    return counts
