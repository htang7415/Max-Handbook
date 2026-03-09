import math

import pytest

from pairwise_ranking_loss import pairwise_logistic_loss


def test_pairwise_ranking_loss_is_small_when_preferred_item_scores_higher() -> None:
    loss = pairwise_logistic_loss(preferred_score=2.0, rejected_score=1.0)

    assert loss == pytest.approx(0.3132616875)


def test_pairwise_ranking_loss_is_log_two_when_scores_tie() -> None:
    loss = pairwise_logistic_loss(preferred_score=1.0, rejected_score=1.0)

    assert loss == pytest.approx(math.log(2.0))


def test_pairwise_ranking_loss_grows_when_preferred_item_scores_lower() -> None:
    loss = pairwise_logistic_loss(preferred_score=0.0, rejected_score=1.0)

    assert loss > math.log(2.0)
