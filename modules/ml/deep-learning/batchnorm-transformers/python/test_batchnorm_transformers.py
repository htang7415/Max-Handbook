import pytest

from batchnorm_transformers import batch_stats


def test_batch_stats():
    mean, var = batch_stats([[1.0, 2.0], [3.0, 4.0]])
    assert mean == 2.5
    assert var == pytest.approx(1.25, abs=1e-6)


def test_batch_stats_reject_irregular_matrix():
    with pytest.raises(ValueError, match="rectangular"):
        batch_stats([[1.0, 2.0], [3.0]])
