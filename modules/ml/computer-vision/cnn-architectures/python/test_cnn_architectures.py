from __future__ import annotations

from cnn_architectures import alexnet_layers, lenet5_layers, resnet_layers, vgg_layers


def test_lenet5_layers_keep_early_cnn_pattern() -> None:
    plan = lenet5_layers()
    assert plan[0] == "conv5x5"
    assert plan.count("fc") == 3


def test_alexnet_layers_include_dropout_and_large_first_convolution() -> None:
    plan = alexnet_layers()
    assert plan[0] == "conv11x11"
    assert plan.count("dropout") == 2


def test_vgg_and_resnet_capture_deep_block_repetition_and_skip_stage_layout() -> None:
    assert vgg_layers().count("conv3x3") == 4
    assert resnet_layers()[-2:] == ["global-average-pool", "fully-connected"]
