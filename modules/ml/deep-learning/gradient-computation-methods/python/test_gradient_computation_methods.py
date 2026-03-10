from __future__ import annotations

import pytest

from gradient_computation_methods import Value, grad_check, linear_backprop, linear_forward, squared_error


def test_linear_forward_and_squared_error() -> None:
    prediction = linear_forward(3.0, 2.0, b=1.0)
    assert prediction == 7.0
    assert squared_error(prediction, target=5.0) == 2.0


def test_linear_backprop() -> None:
    grad_w = linear_backprop(3.0, 2.0, 0.5)
    assert grad_w == 1.5


def test_value_mul_add_relu_backward() -> None:
    a = Value(2.0)
    b = Value(-3.0)
    c = Value(10.0)
    out = (a * b + c).relu()
    out.backward()

    assert out.data == 4.0
    assert a.grad == -3.0
    assert b.grad == 2.0
    assert c.grad == 1.0


def test_value_zero_grad_single_node() -> None:
    x = Value(3.0)
    y = x * 2.0
    y.backward()
    assert x.grad == 2.0
    x.zero_grad()
    assert x.grad == 0.0


def test_grad_check_square() -> None:
    approx = grad_check(lambda x: x * x, 3.0)
    assert abs(approx - 6.0) < 1e-3


def test_grad_check_requires_positive_eps() -> None:
    with pytest.raises(ValueError, match="positive"):
        grad_check(lambda x: x * x, 3.0, eps=0.0)
