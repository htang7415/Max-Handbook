# Kernel PCA

> Track: `ml` | Topic: `models`

## Purpose

Use this module to learn the two steps that matter most in kernel PCA:
build a nonlinear kernel matrix, then center it before eigendecomposition.

## First Principles

- Kernel PCA replaces raw coordinates with pairwise similarity.
- The kernel matrix acts like an inner-product matrix in an implicit feature space.
- Centering is required because PCA assumes zero-centered features.

## Core Math

$$K_{ij} = \exp(-\gamma \lVert x_i - x_j \rVert^2)$$

$$K_c = K - \mathbf{1}K - K\mathbf{1} + \mathbf{1}K\mathbf{1}$$

- $K$ -- kernel matrix
- $K_c$ -- centered kernel matrix
- $\gamma$ -- RBF bandwidth parameter
- $\mathbf{1}$ -- matrix with entries $\frac{1}{n}$

## From Math To Code

- Compute the raw RBF kernel matrix first.
- Center that matrix row-wise and column-wise.
- Only then is the matrix ready for eigendecomposition.

## Minimal Code Mental Model

```python
kernel = rbf_kernel_matrix(points, gamma=1.0)
centered = center_kernel_matrix(kernel)
ready = centered_rbf_kernel(points, gamma=1.0)
```

## Function

```python
def rbf_kernel_matrix(points: list[list[float]], gamma: float) -> list[list[float]]:
def center_kernel_matrix(kernel: list[list[float]]) -> list[list[float]]:
def centered_rbf_kernel(points: list[list[float]], gamma: float) -> list[list[float]]:
```

## When To Use What

- Use `rbf_kernel_matrix` when you want to inspect the raw nonlinear similarity structure.
- Use `center_kernel_matrix` when you already have a kernel matrix and need the PCA-ready version.
- Use `centered_rbf_kernel` when you want the compact end-to-end helper.

## Run tests

```bash
pytest modules/ml/models/kernel-pca/python -q
```
