import pytest

from multi_head_attention import multi_head_attention


def test_multi_head_attention_shape():
    q = [[1.0, 0.0, 0.0, 1.0]] * 2
    out = multi_head_attention(q, q, q, heads=2)
    assert len(out) == 2
    assert len(out[0]) == 4


def test_multi_head_attention_identical_tokens_preserve_values():
    q = [[1.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 1.0]]
    out = multi_head_attention(q, q, q, heads=2)
    for out_row, exp_row in zip(out, q):
        assert out_row == pytest.approx(exp_row, abs=1e-6)


def test_multi_head_attention_requires_divisible_dimension():
    with pytest.raises(ValueError, match="divisible"):
        multi_head_attention([[1.0, 0.0, 1.0]], [[1.0, 0.0, 1.0]], [[1.0, 0.0, 1.0]], heads=2)
