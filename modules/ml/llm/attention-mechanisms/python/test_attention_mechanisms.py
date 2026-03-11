from __future__ import annotations

import numpy as np
import pytest

from attention_mechanisms import (
    attention_weights,
    causal_mask,
    causal_self_attention,
    multi_head_attention,
    scaled_dot_product_scores,
    self_attention,
    softmax,
    window_mask,
)


def test_self_attention_shape() -> None:
    q = [[1.0, 0.0], [0.0, 1.0]]
    out = self_attention(q, q, [[1.0, 2.0], [3.0, 4.0]])
    assert len(out) == 2
    assert len(out[0]) == 2


def test_self_attention_uniform_scores_average_values() -> None:
    q = [[1.0, 1.0], [1.0, 1.0]]
    v = [[1.0, 0.0], [0.0, 2.0]]
    out = self_attention(q, q, v)
    expected = [[0.5, 1.0], [0.5, 1.0]]
    for out_row, exp_row in zip(out, expected):
        assert out_row == pytest.approx(exp_row, abs=1e-6)


def test_attention_weights_are_row_normalized() -> None:
    weights = attention_weights([[1.0, 0.0], [0.0, 1.0]], [[1.0, 0.0], [0.0, 1.0]])
    assert sum(weights[0]) == pytest.approx(1.0)
    assert sum(weights[1]) == pytest.approx(1.0)


def test_scaled_dot_product_scores_are_symmetric_when_q_equals_k() -> None:
    scores = scaled_dot_product_scores([[1.0, 0.0], [0.0, 1.0]], [[1.0, 0.0], [0.0, 1.0]])
    assert scores[0][1] == pytest.approx(scores[1][0])


def test_multi_head_attention_requires_divisible_dimension() -> None:
    with pytest.raises(ValueError, match="divisible"):
        multi_head_attention([[1.0, 0.0, 1.0]], [[1.0, 0.0, 1.0]], [[1.0, 0.0, 1.0]], heads=2)


def test_softmax_sums_to_one() -> None:
    x = np.array([[1.0, 2.0, 3.0]])
    assert softmax(x).sum(axis=-1) == pytest.approx([1.0])


def test_causal_mask_lower_triangular_behavior() -> None:
    mask = causal_mask(3)
    assert mask[0, 0] == 0.0
    assert mask[1, 0] == 0.0
    assert mask[1, 1] == 0.0
    assert mask[0, 1] == -np.inf
    assert mask[1, 2] == -np.inf


def test_causal_attention_no_future_leakage() -> None:
    seq_len, d = 4, 2
    Q = np.ones((seq_len, d))
    K = np.ones((seq_len, d))
    V = np.eye(seq_len, d)
    out = causal_self_attention(Q, K, V)
    np.testing.assert_allclose(out[0], V[0], atol=1e-6)


def test_window_mask_marks_local_neighbors() -> None:
    assert window_mask(4, 1)[0] == [1, 1, 0, 0]


def test_attention_validation_rejects_invalid_shapes() -> None:
    with pytest.raises(ValueError, match="positive"):
        causal_mask(0)
    with pytest.raises(ValueError, match="same shape"):
        causal_self_attention(np.ones((2, 2)), np.ones((3, 2)), np.ones((2, 2)))
    with pytest.raises(ValueError, match="non-negative"):
        window_mask(4, -1)
