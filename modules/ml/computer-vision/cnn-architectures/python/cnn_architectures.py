from __future__ import annotations


def lenet5_layers() -> list[str]:
    return [
        "conv5x5",
        "tanh",
        "avg-pool",
        "conv5x5",
        "tanh",
        "avg-pool",
        "fc",
        "tanh",
        "fc",
        "tanh",
        "fc",
    ]


def alexnet_layers() -> list[str]:
    return [
        "conv11x11",
        "relu",
        "max-pool",
        "conv5x5",
        "relu",
        "max-pool",
        "conv3x3",
        "relu",
        "conv3x3",
        "relu",
        "conv3x3",
        "relu",
        "max-pool",
        "fc",
        "relu",
        "dropout",
        "fc",
        "relu",
        "dropout",
        "fc",
    ]


def vgg_layers() -> list[str]:
    return [
        "conv3x3",
        "relu",
        "conv3x3",
        "relu",
        "max-pool",
        "conv3x3",
        "relu",
        "conv3x3",
        "relu",
        "max-pool",
        "fc",
        "fc",
        "fc",
    ]


def resnet_layers() -> list[str]:
    return [
        "stem",
        "residual-stage-1",
        "residual-stage-2",
        "residual-stage-3",
        "residual-stage-4",
        "global-average-pool",
        "fully-connected",
    ]
