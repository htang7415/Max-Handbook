from __future__ import annotations

import pytest

from linear_models import (
    elastic_net_penalty,
    linear_predict,
    logistic_predict_proba,
    softmax_probabilities,
)


def test_linear_predict_and_logistic_predict_proba_share_affine_core() -> None:
    assert linear_predict([1.0, 2.0], [0.5, 1.0], 0.0) == pytest.approx(2.5)
    assert logistic_predict_proba([0.0], [1.0], 0.0) == pytest.approx(0.5)


def test_softmax_probabilities_sum_to_one() -> None:
    assert sum(softmax_probabilities([1.0, 1.0])) == pytest.approx(1.0)


def test_elastic_net_penalty_combines_l1_and_l2_terms() -> None:
    assert elastic_net_penalty([1.0, -2.0], 0.1, 0.1) == pytest.approx(0.8)
