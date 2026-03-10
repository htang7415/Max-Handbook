from __future__ import annotations


def linear_forward(x: float, w: float, b: float = 0.0) -> float:
    return w * x + b


def squared_error(prediction: float, target: float) -> float:
    return 0.5 * (prediction - target) ** 2


def linear_backprop(x: float, w: float, grad_out: float) -> float:
    return grad_out * x


class Value:
    """A tiny scalar autodiff value with reverse-mode backprop."""

    def __init__(self, data: float, _children=(), _op: str = ""):
        self.data = float(data)
        self.grad = 0.0
        self._backward = lambda: None
        self._prev = tuple(_children)
        self._op = _op

    def _wrap(self, other):
        return other if isinstance(other, Value) else Value(other)

    def __add__(self, other):
        other = self._wrap(other)
        out = Value(self.data + other.data, (self, other), "+")

        def _backward() -> None:
            self.grad += out.grad
            other.grad += out.grad

        out._backward = _backward
        return out

    __radd__ = __add__

    def __mul__(self, other):
        other = self._wrap(other)
        out = Value(self.data * other.data, (self, other), "*")

        def _backward() -> None:
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad

        out._backward = _backward
        return out

    __rmul__ = __mul__

    def relu(self):
        out = Value(self.data if self.data > 0 else 0.0, (self,), "relu")

        def _backward() -> None:
            self.grad += (1.0 if out.data > 0 else 0.0) * out.grad

        out._backward = _backward
        return out

    def zero_grad(self) -> None:
        self.grad = 0.0

    def backward(self, retain_graph: bool = False) -> None:
        del retain_graph

        topo: list[Value] = []
        visited: set[int] = set()

        def build(node: Value) -> None:
            node_id = id(node)
            if node_id in visited:
                return
            visited.add(node_id)
            for child in node._prev:
                build(child)
            topo.append(node)

        build(self)
        self.grad = 1.0
        for node in reversed(topo):
            node._backward()


def grad_check(f, x: float, eps: float = 1e-5) -> float:
    if eps <= 0.0:
        raise ValueError("eps must be positive")
    return (f(x + eps) - f(x - eps)) / (2 * eps)
