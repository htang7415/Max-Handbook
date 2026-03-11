from __future__ import annotations

import math


def svd_2x2_singular_values(A: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation on B = A^T A.

    Returns (U, S, Vt) such that A ~= U @ diag(S) @ Vt
    """
    import torch

    if not isinstance(A, torch.Tensor):
        raise TypeError("A must be a torch.Tensor")
    if A.ndim != 2 or A.shape != (2, 2):
        raise ValueError(f"A must be shape (2,2), got {tuple(A.shape)}")
    if not A.dtype.is_floating_point:
        A = A.float()

    dtype, device = A.dtype, A.device
    eps = torch.finfo(dtype).eps

    # B = A^T A is symmetric 2x2
    B = A.T @ A
    a = B[0, 0]
    b = B[0, 1]
    d = B[1, 1]

    # Jacobi rotation to diagonalize B
    if torch.abs(b) <= eps:
        c = torch.ones((), dtype=dtype, device=device)
        s = torch.zeros((), dtype=dtype, device=device)
    else:
        tau = (d - a) / (2 * b)
        # Critical: if tau == 0 => 45 degree rotation
        t = torch.where(
            tau == 0,
            torch.ones((), dtype=dtype, device=device),
            torch.sign(tau) / (torch.abs(tau) + torch.sqrt(1 + tau * tau)),
        )
        c = 1 / torch.sqrt(1 + t * t)
        s = t * c

    V = torch.stack([torch.stack([c, -s]), torch.stack([s, c])], dim=0)

    # Eigenvalues (diagonal entries of V^T B V)
    cs, c2, s2 = c * s, c * c, s * s
    lam1 = c2 * a - 2 * cs * b + s2 * d
    lam2 = s2 * a + 2 * cs * b + c2 * d

    lam1 = torch.clamp(lam1, min=0)
    lam2 = torch.clamp(lam2, min=0)
    s1 = torch.sqrt(lam1)
    s2v = torch.sqrt(lam2)

    # Sort descending singular values; swap V columns accordingly
    if (s2v > s1).item():
        S = torch.stack([s2v, s1])
        V = V[:, [1, 0]]
    else:
        S = torch.stack([s1, s2v])

    Vt = V.T

    # Build U = A V Sigma^{-1}
    # Handle rank-deficient cases carefully.
    if (S[0] <= eps).item():
        U = torch.eye(2, dtype=dtype, device=device)
        Vt = torch.eye(2, dtype=dtype, device=device)
        S = torch.zeros((2,), dtype=dtype, device=device)
        return U, S, Vt

    AV = A @ V
    U = torch.empty((2, 2), dtype=dtype, device=device)

    U[:, 0] = AV[:, 0] / S[0]

    if (S[1] > eps).item():
        U[:, 1] = AV[:, 1] / S[1]
    else:
        # Any unit vector orthogonal to U[:,0]
        u0 = U[:, 0]
        U[:, 1] = torch.stack([-u0[1], u0[0]])

    return U, S, Vt


def svd_2x2(a: list[list[float]]) -> tuple[list[list[float]], list[float], list[list[float]]]:
    if len(a) != 2 or any(len(row) != 2 for row in a):
        raise ValueError("a must be a 2x2 matrix")
    a00, a01 = a[0]
    a10, a11 = a[1]

    # B = A^T A (symmetric 2x2)
    b00 = a00 * a00 + a10 * a10
    b01 = a00 * a01 + a10 * a11
    b11 = a01 * a01 + a11 * a11
    eps = 1e-12

    # Jacobi rotation to diagonalize B
    if abs(b01) <= eps:
        c, s = 1.0, 0.0
    else:
        tau = (b11 - b00) / (2.0 * b01)
        if tau == 0.0:
            t = 1.0
        else:
            t = math.copysign(1.0, tau) / (abs(tau) + math.sqrt(1.0 + tau * tau))
        c = 1.0 / math.sqrt(1.0 + t * t)
        s = t * c

    v00, v01 = c, -s
    v10, v11 = s, c

    # Eigenvalues (diagonal entries of V^T B V)
    cs = c * s
    c2 = c * c
    s2 = s * s
    lam1 = c2 * b00 - 2.0 * cs * b01 + s2 * b11
    lam2 = s2 * b00 + 2.0 * cs * b01 + c2 * b11
    lam1 = max(0.0, lam1)
    lam2 = max(0.0, lam2)

    s1 = math.sqrt(lam1)
    s2v = math.sqrt(lam2)

    # Sort singular values descending; swap V columns if needed.
    if s2v > s1:
        s1, s2v = s2v, s1
        v00, v01 = v01, v00
        v10, v11 = v11, v10

    svals = [s1, s2v]
    if svals[0] <= eps:
        return [[1.0, 0.0], [0.0, 1.0]], [0.0, 0.0], [[1.0, 0.0], [0.0, 1.0]]

    # U = A V Sigma^{-1}
    av00 = a00 * v00 + a01 * v10
    av10 = a10 * v00 + a11 * v10
    av01 = a00 * v01 + a01 * v11
    av11 = a10 * v01 + a11 * v11

    u00 = av00 / svals[0]
    u10 = av10 / svals[0]
    if svals[1] > eps:
        u01 = av01 / svals[1]
        u11 = av11 / svals[1]
    else:
        u01 = -u10
        u11 = u00

    u = [[u00, u01], [u10, u11]]
    vt = [[v00, v10], [v01, v11]]
    return u, svals, vt


def singular_values_2x2(a: list[list[float]]) -> list[float]:
    _, svals, _ = svd_2x2(a)
    return svals
