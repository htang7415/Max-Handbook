from problem_746_min_cost_climbing_stairs import Solution


def test_min_cost_example():
    assert Solution().minCostClimbingStairs([10, 15, 20]) == 15


def test_min_cost_edge_short():
    assert Solution().minCostClimbingStairs([1, 2]) == 1


def test_min_cost_tricky_skip_expensive_steps():
    assert Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
