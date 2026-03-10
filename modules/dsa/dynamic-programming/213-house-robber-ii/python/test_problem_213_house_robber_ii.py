from problem_213_house_robber_ii import Solution


def test_house_robber_ii_example():
    assert Solution().rob([2, 3, 2]) == 3


def test_house_robber_ii_edge_single_house():
    assert Solution().rob([5]) == 5


def test_house_robber_ii_tricky_circle_choice():
    assert Solution().rob([1, 2, 3, 1]) == 4


def test_house_robber_ii_tricky_two_houses():
    assert Solution().rob([2, 7]) == 7
