import math

import pytest

from transformer import attention_weights, transformer_block


def test_transformer_block_shape():
    x = [[0.1, 0.2], [0.0, 0.3]]
    w1 = [[0.5, 0.0], [0.0, 0.5]]
    w2 = [[1.0, 0.0], [0.0, 1.0]]
    out = transformer_block(x, w1, w2)
    assert len(out) == 2
    assert len(out[0]) == 2


def test_attention_weights_are_row_normalized() -> None:
    weights = attention_weights([[1.0, 0.0], [0.0, 1.0]])
    assert sum(weights[0]) == pytest.approx(1.0)
    assert sum(weights[1]) == pytest.approx(1.0)


def test_transformer_block_zero_ffn_keeps_attention_residual():
    x = [[1.0, 0.0], [0.0, 1.0]]
    w1 = [[0.0, 0.0], [0.0, 0.0]]
    w2 = [[0.0, 0.0], [0.0, 0.0]]

    out = transformer_block(x, w1, w2)

    sharp = math.exp(1 / math.sqrt(2))
    stay = sharp / (sharp + 1.0)
    mix = 1.0 / (sharp + 1.0)
    expected = [[1.0 + stay, mix], [mix, 1.0 + stay]]
    for out_row, exp_row in zip(out, expected):
        for actual, target in zip(out_row, exp_row):
            assert actual == pytest.approx(target, abs=1e-6)


def test_transformer_block_requires_residual_output_dimension():
    x = [[1.0, 0.0], [0.0, 1.0]]
    w1 = [[1.0, 0.0], [0.0, 1.0]]
    w2 = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]

    with pytest.raises(ValueError, match="w2 output dimension"):
        transformer_block(x, w1, w2)
