from __future__ import annotations

import pytest

from dependency_and_supply_chain_risk import dependency_gate, dependency_risk, portfolio_risk


def test_dependency_risk_rises_for_vulnerabilities_or_install_scripts() -> None:
    assert dependency_risk(version_pinned=True, known_vulnerabilities=0, executes_install_script=False) == "low"
    assert dependency_risk(version_pinned=False, known_vulnerabilities=0, executes_install_script=True) == "medium"
    assert dependency_risk(version_pinned=True, known_vulnerabilities=2, executes_install_script=False) == "high"


def test_dependency_gate_blocks_or_reviews_production_risk() -> None:
    assert dependency_gate("high", in_production_path=True) == "block"
    assert dependency_gate("medium", in_production_path=True) == "review"
    assert dependency_gate("medium", in_production_path=False) == "allow"


def test_portfolio_risk_returns_highest_risk_level() -> None:
    assert portfolio_risk(["low", "medium", "high"]) == "high"

    with pytest.raises(ValueError):
        portfolio_risk([])
