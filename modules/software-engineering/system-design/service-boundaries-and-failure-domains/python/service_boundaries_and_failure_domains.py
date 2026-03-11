from __future__ import annotations


def should_split_service(
    independent_scaling: bool,
    separate_ownership: bool,
    requires_strong_transaction: bool,
) -> bool:
    if requires_strong_transaction:
        return False
    return independent_scaling or separate_ownership


def failure_domain_risk(shared_dependencies: int, critical_paths: int) -> str:
    if shared_dependencies < 0 or critical_paths < 0:
        raise ValueError("counts must be non-negative")
    if shared_dependencies == 0 or critical_paths == 0:
        return "low"
    if shared_dependencies <= 2 and critical_paths <= 1:
        return "medium"
    return "high"


def boundary_decision(
    independent_scaling: bool,
    separate_ownership: bool,
    requires_strong_transaction: bool,
) -> str:
    if should_split_service(independent_scaling, separate_ownership, requires_strong_transaction):
        return "split"
    if requires_strong_transaction and (independent_scaling or separate_ownership):
        return "review-transaction-boundary"
    return "keep-together"
