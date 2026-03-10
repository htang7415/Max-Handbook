# Vision Architectures

CNN architectures mainly differ in how they scale depth, downsampling, and skip connections.

## Purpose

Use this page to compare the small set of vision architectures worth remembering:
- early CNN stacks
- deeper block-based CNNs
- residual connections
- classifier head choices

## First Principles

- Early CNNs show the basic pattern: convolution, nonlinearity, pooling, classifier.
- VGG-style models deepen this pattern by repeating similar blocks.
- ResNets add skip connections so deeper networks train more reliably.
- Global average pooling changes the classifier head from a large dense map to a small summary.

## Core Math

- Residual block shape:
  $$
  y = F(x) + x
  $$
- This helps optimization because the network can learn a small correction to the identity.

## Minimal Code Mental Model

```python
residual = x
x = conv_bn_relu(x)
x = conv_bn(x)
x = relu(x + residual)
```

## Canonical Modules

- Historical progression: `lenet-5`, `alexnet`, `vggnet`, `resnet`
- Downsampling and heads: `pooling`, `global-average-pooling`

## When To Use What

- Use `lenet-5` or `alexnet` for intuition, not as the modern default.
- Use `vggnet` to understand repeated convolutional blocks.
- Use `resnet` as the main modern CNN reference point.
- Use `global-average-pooling` when parameter efficiency matters more than a large dense head.
