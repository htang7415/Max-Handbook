# Computer Vision

Computer vision is about turning images into features that preserve spatial structure.

## Purpose

Use this page to keep vision study in the right order:
- image preprocessing
- convolution and pooling
- CNN architecture choices
- common vision-specific postprocessing

## First Principles

- Images have local structure, so convolution reuses weights across space.
- Downsampling trades spatial detail for larger receptive fields and lower cost.
- Preprocessing and augmentation matter because image scale, lighting, and crop choices change what the model sees.
- Architecture choices mainly change how efficiently the model builds hierarchical visual features.

## Core Math

- Convolution at location $(i, j)$:
  $$
  y_{i,j} = \sum_{u,v} K_{u,v} x_{i+u,j+v}
  $$
- Pooling keeps a summary over a local region instead of every pixel.

## Minimal Code Mental Model

```python
x = preprocess(image)
features = conv(x)
features = pool(features)
logits = classifier(features)
```

## Canonical Modules

- Vision basics: `cnn-basics`, `convolution-layer`, `pooling`, `global-average-pooling`
- Image preparation: `image-preprocessing`, `rgb-to-grayscale`, `contrast-brightness`, `bilinear-resizing`, `data-augmentation`
- Postprocessing and signals: `non-maximum-suppression`, `sobel-edge-detection`, `optical-flow-epe`
- Architectures: `resnet` with the architecture guide in `docs/ml/computer-vision/architectures`

## When To Use What

- Start with convolution, pooling, and preprocessing before named architectures.
- Use `data-augmentation` when robustness is the bottleneck.
- Use `global-average-pooling` when you want a lighter classifier head than flattening.
- Use `non-maximum-suppression` only when the task produces overlapping detections or proposals.
