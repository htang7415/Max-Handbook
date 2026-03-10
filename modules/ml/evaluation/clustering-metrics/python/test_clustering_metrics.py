from __future__ import annotations

import pytest

from clustering_metrics import (
    calinski_harabasz_score,
    davies_bouldin_score,
    silhouette_score,
)


def test_silhouette_score_compares_cohesion_and_separation() -> None:
    assert silhouette_score(0.2, 0.6) == pytest.approx(2 / 3)


def test_davies_bouldin_score_penalizes_wide_close_clusters() -> None:
    assert davies_bouldin_score(0.5, 0.5, 2.0) == pytest.approx(0.5)


def test_calinski_harabasz_score_returns_variance_ratio() -> None:
    assert calinski_harabasz_score(10.0, 5.0, 2, 10) == pytest.approx(16.0)


def test_calinski_harabasz_score_validates_partition_shape() -> None:
    with pytest.raises(ValueError):
        calinski_harabasz_score(10.0, 5.0, 1, 10)
