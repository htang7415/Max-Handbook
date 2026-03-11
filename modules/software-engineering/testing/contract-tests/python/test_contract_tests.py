from __future__ import annotations

import pytest

from contract_tests import contract_report, contract_violations, make_contract


def test_contract_allows_extra_fields_but_requires_consumer_fields() -> None:
    contract = make_contract({"id": "string", "amount_cents": "integer"}, {"memo": "string"})
    payload = {"id": "p_1", "amount_cents": 2500, "currency": "USD"}

    assert contract_violations(contract, payload) == []


def test_contract_detects_missing_fields_and_wrong_types() -> None:
    contract = make_contract({"id": "string", "amount_cents": "integer"}, {"memo": "string"})
    payload = {"amount_cents": "2500", "memo": 123}

    assert contract_violations(contract, payload) == [
        "missing required field: id",
        "wrong type for field: amount_cents",
        "wrong type for field: memo",
    ]


def test_contract_report_requires_name() -> None:
    contract = make_contract({"id": "string"})

    assert contract_report("payment-created", contract, {"id": "p_1"}) == {
        "contract": "payment-created",
        "passed": True,
        "violations": [],
    }

    with pytest.raises(ValueError):
        contract_report(" ", contract, {"id": "p_1"})
