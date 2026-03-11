from __future__ import annotations

import pytest

from slis_slos_and_alerting import alert_state, error_budget_remaining, sli_rate


def test_sli_and_error_budget_are_computed_from_good_and_total_events() -> None:
    sli = sli_rate(good_events=995, total_events=1000)

    assert sli == pytest.approx(0.995)
    assert error_budget_remaining(actual_sli=sli, target_slo=0.99) == pytest.approx(0.5)


def test_alert_state_pages_when_slo_is_missed_and_tickets_on_low_budget() -> None:
    assert alert_state(actual_sli=0.989, target_slo=0.99) == "page"
    assert alert_state(actual_sli=0.992, target_slo=0.99, page_when_remaining_below=0.25) == "ticket"
    assert alert_state(actual_sli=0.999, target_slo=0.99, page_when_remaining_below=0.25) == "ok"


def test_validation_rejects_invalid_event_counts_and_thresholds() -> None:
    with pytest.raises(ValueError):
        sli_rate(good_events=11, total_events=10)
    with pytest.raises(ValueError):
        error_budget_remaining(actual_sli=1.1, target_slo=0.99)
    with pytest.raises(ValueError):
        alert_state(actual_sli=0.999, target_slo=0.99, page_when_remaining_below=1.5)
