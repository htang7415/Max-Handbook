import math

import pytest

from bernoulli_naive_bayes import bernoulli_log_likelihood


def test_bernoulli_log_likelihood():
    ll = bernoulli_log_likelihood([1, 0], [0.8, 0.2])
    assert ll == pytest.approx(math.log(0.8) + math.log(0.8), abs=1e-6)


def test_bernoulli_log_likelihood_rejects_invalid_probability():
    with pytest.raises(ValueError, match="strictly between 0 and 1"):
        bernoulli_log_likelihood([1], [1.0])
