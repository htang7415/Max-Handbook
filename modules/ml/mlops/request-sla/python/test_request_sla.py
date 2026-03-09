import pytest

from request_sla import request_sla_compliance


def test_request_sla_compliance_counts_requests_under_threshold() -> None:
    compliant, rate = request_sla_compliance([100.0, 200.0, 350.0], sla_ms=300.0)

    assert compliant == 2
    assert rate == pytest.approx(2.0 / 3.0)


def test_request_sla_compliance_handles_empty_input() -> None:
    assert request_sla_compliance([], sla_ms=100.0) == (0, 0.0)


def test_request_sla_compliance_requires_positive_threshold() -> None:
    with pytest.raises(ValueError, match="positive"):
        request_sla_compliance([10.0], sla_ms=0.0)
