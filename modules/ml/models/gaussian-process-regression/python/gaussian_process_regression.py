import math


def rbf_kernel(x: list[float], y: list[float], length_scale: float) -> float:
    if length_scale <= 0:
        raise ValueError("length_scale must be positive")
    dist2 = sum((a - b) ** 2 for a, b in zip(x, y))
    return math.exp(-dist2 / (2 * length_scale ** 2))


def kernel_matrix(
    xs: list[list[float]], ys: list[list[float]], length_scale: float
) -> list[list[float]]:
    return [[rbf_kernel(x, y, length_scale) for y in ys] for x in xs]


def _matvec(a: list[list[float]], v: list[float]) -> list[float]:
    return [sum(a[i][k] * v[k] for k in range(len(v))) for i in range(len(a))]


def _invert_matrix(a: list[list[float]]) -> list[list[float]]:
    n = len(a)
    if n == 0 or any(len(row) != n for row in a):
        raise ValueError("matrix must be square")

    # Gauss-Jordan elimination (sufficient for small learning examples)
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(a)]
    for col in range(n):
        pivot_row = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot_row][col]) < 1e-12:
            raise ValueError("matrix is singular")
        if pivot_row != col:
            aug[col], aug[pivot_row] = aug[pivot_row], aug[col]

        pivot = aug[col][col]
        for j in range(2 * n):
            aug[col][j] /= pivot

        for r in range(n):
            if r == col:
                continue
            factor = aug[r][col]
            if factor == 0:
                continue
            for j in range(2 * n):
                aug[r][j] -= factor * aug[col][j]

    return [row[n:] for row in aug]


def gp_posterior_weights(
    x_train: list[list[float]],
    y_train: list[float],
    length_scale: float,
    noise: float,
) -> list[float]:
    if len(x_train) != len(y_train):
        raise ValueError("x_train and y_train must have the same length")
    if noise < 0:
        raise ValueError("noise must be non-negative")

    k_xx = kernel_matrix(x_train, x_train, length_scale)
    for i in range(len(k_xx)):
        k_xx[i][i] += noise ** 2

    k_inv = _invert_matrix(k_xx)
    return _matvec(k_inv, y_train)


def gp_posterior_predict(
    x_train: list[list[float]],
    y_train: list[float],
    x_test: list[list[float]],
    length_scale: float,
    noise: float,
) -> tuple[list[float], list[float]]:
    alpha = gp_posterior_weights(x_train, y_train, length_scale, noise)
    k_xx = kernel_matrix(x_train, x_train, length_scale)
    for i in range(len(k_xx)):
        k_xx[i][i] += noise ** 2
    k_inv = _invert_matrix(k_xx)
    k_xs = kernel_matrix(x_train, x_test, length_scale)
    k_ss = kernel_matrix(x_test, x_test, length_scale)
    mean = [
        sum(k_xs[i][j] * alpha[i] for i in range(len(x_train)))
        for j in range(len(x_test))
    ]

    variance = []
    for j in range(len(x_test)):
        k_col = [k_xs[i][j] for i in range(len(x_train))]
        temp = _matvec(k_inv, k_col)
        v = sum(k_col[i] * temp[i] for i in range(len(k_col)))
        var = k_ss[j][j] - v
        variance.append(var if var > 0.0 else 0.0)

    return mean, variance
