from squares_of_a_sorted_array import Solution


def test_sorted_squares_example():
    assert Solution().sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]


def test_sorted_squares_edge_single():
    assert Solution().sortedSquares([0]) == [0]


def test_sorted_squares_tricky_all_negative():
    assert Solution().sortedSquares([-7, -3, -1]) == [1, 9, 49]
