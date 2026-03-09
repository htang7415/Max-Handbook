import pytest

from self_attention import self_attention


def test_self_attention_shape():
    q = [[1.0, 0.0], [0.0, 1.0]]
    k = [[1.0, 0.0], [0.0, 1.0]]
    v = [[1.0, 2.0], [3.0, 4.0]]
    out = self_attention(q, k, v)
    assert len(out) == 2
    assert len(out[0]) == 2


def test_self_attention_uniform_scores_average_values():
    q = [[1.0, 1.0], [1.0, 1.0]]
    k = [[1.0, 1.0], [1.0, 1.0]]
    v = [[1.0, 0.0], [0.0, 2.0]]

    out = self_attention(q, k, v)

    expected = [[0.5, 1.0], [0.5, 1.0]]
    for out_row, exp_row in zip(out, expected):
        assert out_row == pytest.approx(exp_row, abs=1e-6)


def test_self_attention_rejects_mismatched_sequence_lengths():
    with pytest.raises(ValueError, match="same sequence length"):
        self_attention([[1.0, 0.0]], [[1.0, 0.0], [0.0, 1.0]], [[1.0, 0.0]])
