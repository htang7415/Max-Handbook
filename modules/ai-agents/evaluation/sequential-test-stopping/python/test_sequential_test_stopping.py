from __future__ import annotations

import pytest

from sequential_test_stopping import (
    sprt_boundaries,
    sprt_log_likelihood_ratio,
    sprt_route,
)


def test_sequential_test_stopping_accepts_alternative_when_evidence_is_strong() -> None:
    boundaries = sprt_boundaries(alpha=0.05, beta=0.2)
    log_lr = sprt_log_likelihood_ratio(successes=18, failures=4, null_rate=0.5, alt_rate=0.7)

    assert boundaries == {
        "upper": pytest.approx(2.7725887222),
        "lower": pytest.approx(-1.5581446180),
    }
    assert log_lr == pytest.approx(4.0131977641)
    assert sprt_route(log_lr, boundaries["upper"], boundaries["lower"]) == "accept-alt"


def test_sequential_test_stopping_distinguishes_accept_null_and_continue() -> None:
    boundaries = sprt_boundaries(alpha=0.05, beta=0.2)

    assert (
        sprt_route(
            sprt_log_likelihood_ratio(successes=4, failures=18, null_rate=0.5, alt_rate=0.7),
            boundaries["upper"],
            boundaries["lower"],
        )
        == "accept-null"
    )
    assert (
        sprt_route(
            sprt_log_likelihood_ratio(successes=7, failures=7, null_rate=0.5, alt_rate=0.7),
            boundaries["upper"],
            boundaries["lower"],
        )
        == "continue"
    )


def test_sequential_test_stopping_validation() -> None:
    with pytest.raises(ValueError):
        sprt_log_likelihood_ratio(-1, 2, null_rate=0.5, alt_rate=0.7)
    with pytest.raises(ValueError):
        sprt_log_likelihood_ratio(1, 2, null_rate=0.5, alt_rate=0.5)
    with pytest.raises(ValueError):
        sprt_boundaries(alpha=1.0, beta=0.2)
    with pytest.raises(ValueError):
        sprt_route(0.0, upper_boundary=0.5, lower_boundary=0.5)
