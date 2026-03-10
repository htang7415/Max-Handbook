from gaussian_process_regression import gp_posterior_predict, gp_posterior_weights, kernel_matrix, rbf_kernel


def test_rbf_kernel():
    assert abs(rbf_kernel([0.0], [0.0], 1.0) - 1.0) < 1e-6


def test_kernel_matrix_symmetry():
    xs = [[0.0], [1.0]]
    k = kernel_matrix(xs, xs, 1.0)
    assert abs(k[0][1] - k[1][0]) < 1e-12


def test_gp_posterior_predict_hits_training_points():
    x_train = [[0.0], [1.0]]
    y_train = [1.0, 3.0]
    mean, var = gp_posterior_predict(
        x_train, y_train, x_train, length_scale=1.0, noise=1e-6
    )
    assert abs(mean[0] - 1.0) < 1e-5
    assert abs(mean[1] - 3.0) < 1e-5
    assert var[0] < 1e-6
    assert var[1] < 1e-6


def test_gp_posterior_weights_have_one_weight_per_training_point() -> None:
    alpha = gp_posterior_weights([[0.0], [1.0]], [1.0, 3.0], length_scale=1.0, noise=1e-6)
    assert len(alpha) == 2
