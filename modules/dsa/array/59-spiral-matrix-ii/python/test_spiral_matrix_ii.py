from spiral_matrix_ii import Solution


def test_spiral_matrix_ii_example():
    assert Solution().generateMatrix(3) == [
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5],
    ]


def test_spiral_matrix_ii_edge_one():
    assert Solution().generateMatrix(1) == [[1]]


def test_spiral_matrix_ii_tricky_even_size():
    assert Solution().generateMatrix(2) == [[1, 2], [4, 3]]
