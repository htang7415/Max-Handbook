import pytest

from gaussian_mixture_model_em import em_step_1d, responsibilities_1d


def test_em_step_1d_updates_toward_cluster_means():
    weights, means, variances = em_step_1d(
        data=[0.0, 0.2, 10.0, 10.2],
        weights=[0.5, 0.5],
        means=[0.0, 10.0],
        variances=[1.0, 1.0],
    )

    assert weights[0] == pytest.approx(0.5, abs=1e-3)
    assert weights[1] == pytest.approx(0.5, abs=1e-3)
    assert means[0] == pytest.approx(0.1, abs=1e-2)
    assert means[1] == pytest.approx(10.1, abs=1e-2)
    assert variances[0] == pytest.approx(0.01, abs=1e-2)
    assert variances[1] == pytest.approx(0.01, abs=1e-2)


def test_responsibilities_form_rowwise_probabilities() -> None:
    rows = responsibilities_1d(
        data=[0.0, 10.0],
        weights=[0.5, 0.5],
        means=[0.0, 10.0],
        variances=[1.0, 1.0],
    )

    assert len(rows) == 2
    assert rows[0][0] > rows[0][1]
    assert rows[1][1] > rows[1][0]
    assert sum(rows[0]) == pytest.approx(1.0)


def test_responsibilities_validate_variances() -> None:
    with pytest.raises(ValueError, match="positive"):
        responsibilities_1d(
            data=[0.0],
            weights=[1.0],
            means=[0.0],
            variances=[0.0],
        )
