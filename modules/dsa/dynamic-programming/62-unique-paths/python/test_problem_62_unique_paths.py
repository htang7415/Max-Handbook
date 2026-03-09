from problem_62_unique_paths import Solution


def test_unique_paths_example():
    assert Solution().uniquePaths(3, 7) == 28


def test_unique_paths_edge_single_row():
    assert Solution().uniquePaths(1, 5) == 1


def test_unique_paths_tricky_square_grid():
    assert Solution().uniquePaths(3, 3) == 6
