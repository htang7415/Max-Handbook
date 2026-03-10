from __future__ import annotations

import math


def rbf_kernel_matrix(points: list[list[float]], gamma: float) -> list[list[float]]:
    if gamma <= 0.0:
        raise ValueError("gamma must be positive")
    if not points:
        return []

    n = len(points)
    kernel = [[0.0] * n for _ in range(n)]
    for i, point_i in enumerate(points):
        for j, point_j in enumerate(points):
            squared_distance = sum((a - b) ** 2 for a, b in zip(point_i, point_j))
            kernel[i][j] = math.exp(-gamma * squared_distance)
    return kernel


def center_kernel_matrix(kernel: list[list[float]]) -> list[list[float]]:
    if not kernel:
        return []
    n = len(kernel)
    if any(len(row) != n for row in kernel):
        raise ValueError("kernel matrix must be square")

    row_means = [sum(row) / n for row in kernel]
    col_means = [sum(kernel[i][j] for i in range(n)) / n for j in range(n)]
    total_mean = sum(row_means) / n

    centered = []
    for i in range(n):
        centered.append([
            kernel[i][j] - row_means[i] - col_means[j] + total_mean for j in range(n)
        ])
    return centered


def centered_rbf_kernel(points: list[list[float]], gamma: float) -> list[list[float]]:
    return center_kernel_matrix(rbf_kernel_matrix(points, gamma))
