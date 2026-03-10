from __future__ import annotations

import math

import pytest

from naive_bayes_models import bernoulli_log_likelihood, gaussian_log_likelihood


def test_gaussian_log_likelihood_matches_univariate_gaussian_case() -> None:
    value = gaussian_log_likelihood([0.0], [0.0], [1.0])
    assert value == pytest.approx(-0.5 * math.log(2 * math.pi), abs=1e-6)


def test_bernoulli_log_likelihood_matches_binary_presence_case() -> None:
    value = bernoulli_log_likelihood([1, 0], [0.8, 0.2])
    assert value == pytest.approx(math.log(0.8) + math.log(0.8), abs=1e-6)


def test_naive_bayes_variants_validate_inputs() -> None:
    with pytest.raises(ValueError):
        gaussian_log_likelihood([0.0], [0.0], [0.0])
    with pytest.raises(ValueError):
        bernoulli_log_likelihood([1], [1.0])
