from problem_63_unique_paths_ii import Solution


def test_unique_paths_with_obstacles_example():
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert Solution().uniquePathsWithObstacles(grid) == 2


def test_unique_paths_with_obstacles_edge_start_blocked():
    grid = [[1, 0], [0, 0]]
    assert Solution().uniquePathsWithObstacles(grid) == 0


def test_unique_paths_with_obstacles_tricky_single_route():
    grid = [[0, 1], [0, 0]]
    assert Solution().uniquePathsWithObstacles(grid) == 1
