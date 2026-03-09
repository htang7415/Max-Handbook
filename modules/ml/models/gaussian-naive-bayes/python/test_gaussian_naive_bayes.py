import math

import pytest

from gaussian_naive_bayes import gaussian_log_likelihood


def test_gaussian_log_likelihood():
    ll = gaussian_log_likelihood([0.0], [0.0], [1.0])
    assert ll == pytest.approx(-0.5 * math.log(2 * math.pi), abs=1e-6)


def test_gaussian_log_likelihood_rejects_nonpositive_variance():
    with pytest.raises(ValueError, match="positive"):
        gaussian_log_likelihood([0.0], [0.0], [0.0])
