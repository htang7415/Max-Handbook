import math

from svd import singular_values_2x2, svd_2x2


def matmul_2x2(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
    ]


def diag_2x2(s: list[float]) -> list[list[float]]:
    return [[s[0], 0.0], [0.0, s[1]]]


def assert_mat_close(a: list[list[float]], b: list[list[float]], tol: float = 1e-9) -> None:
    for i in range(2):
        for j in range(2):
            assert math.isclose(a[i][j], b[i][j], rel_tol=tol, abs_tol=tol)


def test_singular_values():
    vals = singular_values_2x2([[1.0, 0.0], [0.0, 2.0]])
    assert sorted(vals) == [1.0, 2.0]


def test_svd_reconstruction():
    a = [[3.0, 1.0], [0.0, 2.0]]
    u, svals, vt = svd_2x2(a)
    us = matmul_2x2(u, diag_2x2(svals))
    a_hat = matmul_2x2(us, vt)
    assert_mat_close(a_hat, a, tol=1e-8)


def test_svd_requires_2x2_input():
    import pytest

    with pytest.raises(ValueError, match="2x2"):
        svd_2x2([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
