from problem_279_perfect_squares import Solution


def test_perfect_squares_example():
    assert Solution().numSquares(12) == 3


def test_perfect_squares_edge_one():
    assert Solution().numSquares(1) == 1


def test_perfect_squares_tricky_composite():
    assert Solution().numSquares(13) == 2
