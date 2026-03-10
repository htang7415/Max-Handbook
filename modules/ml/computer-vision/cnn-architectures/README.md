# CNN Architectures

> Track: `ml` | Topic: `computer-vision`

## Purpose

Use this module to compare the small set of CNN architectures that matter for intuition:
LeNet, AlexNet, VGG, and ResNet.

## First Principles

- LeNet shows the original convolution-plus-pooling template.
- AlexNet shows the jump to deeper ReLU-based CNNs with dropout and max-pooling.
- VGG shows the repeated small-convolution block pattern.
- ResNet shows why skip connections changed deep vision training.

## Core Math

The main architecture jump to remember is the residual block:
$$
y = F(x) + x
$$

Everything else is mostly a different way to stack convolution, activation, pooling, and classifier stages.

## Minimal Code Mental Model

```python
stages = resnet_layers()
baseline = lenet5_layers()
```

## Function

```python
def lenet5_layers() -> list[str]:
def alexnet_layers() -> list[str]:
def vgg_layers() -> list[str]:
def resnet_layers() -> list[str]:
```

## When To Use What

- Use LeNet to understand the earliest CNN template.
- Use AlexNet to understand the shift to deeper modern-style CNNs.
- Use VGG to understand repeated convolutional blocks.
- Use ResNet as the main modern reference point for deep CNN design.

## Run tests

```bash
pytest modules/ml/computer-vision/cnn-architectures/python -q
```
