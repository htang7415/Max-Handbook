from __future__ import annotations

import pytest

from service_boundaries_and_failure_domains import (
    boundary_decision,
    failure_domain_risk,
    should_split_service,
)


def test_service_split_prefers_scaling_or_ownership_only_when_transactions_allow_it() -> None:
    assert should_split_service(
        independent_scaling=True,
        separate_ownership=False,
        requires_strong_transaction=False,
    ) is True
    assert should_split_service(
        independent_scaling=True,
        separate_ownership=True,
        requires_strong_transaction=True,
    ) is False


def test_failure_domain_risk_reflects_blast_radius() -> None:
    assert failure_domain_risk(shared_dependencies=0, critical_paths=2) == "low"
    assert failure_domain_risk(shared_dependencies=2, critical_paths=1) == "medium"
    assert failure_domain_risk(shared_dependencies=3, critical_paths=2) == "high"


def test_boundary_decision_calls_out_transaction_review_case() -> None:
    assert boundary_decision(
        independent_scaling=True,
        separate_ownership=False,
        requires_strong_transaction=True,
    ) == "review-transaction-boundary"
    assert boundary_decision(
        independent_scaling=False,
        separate_ownership=False,
        requires_strong_transaction=False,
    ) == "keep-together"

    with pytest.raises(ValueError):
        failure_domain_risk(shared_dependencies=-1, critical_paths=0)
