import pytest

from kernel_pca import center_kernel_matrix, centered_rbf_kernel, rbf_kernel_matrix


def test_centered_rbf_kernel_symmetric_and_centered():
    kernel = centered_rbf_kernel([[0.0], [1.0]], gamma=1.0)
    assert kernel[0][1] == pytest.approx(kernel[1][0])
    assert sum(kernel[0]) == pytest.approx(0.0)
    assert sum(kernel[1]) == pytest.approx(0.0)


def test_centered_rbf_kernel_single_point_is_zero():
    assert centered_rbf_kernel([[2.0, 3.0]], gamma=0.5) == [[0.0]]


def test_rbf_kernel_matrix_has_unit_diagonal() -> None:
    kernel = rbf_kernel_matrix([[0.0], [1.0]], gamma=1.0)
    assert kernel[0][0] == pytest.approx(1.0)
    assert kernel[1][1] == pytest.approx(1.0)


def test_center_kernel_matrix_requires_square_input() -> None:
    with pytest.raises(ValueError, match="square"):
        center_kernel_matrix([[1.0, 0.0]])
