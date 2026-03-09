from problem_70_climbing_stairs import Solution


def test_climb_stairs_example():
    assert Solution().climbStairs(2) == 2


def test_climb_stairs_edge_one():
    assert Solution().climbStairs(1) == 1


def test_climb_stairs_tricky_five():
    assert Solution().climbStairs(5) == 8
