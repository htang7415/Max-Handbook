from problem_198_house_robber import Solution


def test_house_robber_example():
    assert Solution().rob([1, 2, 3, 1]) == 4


def test_house_robber_edge_empty():
    assert Solution().rob([]) == 0


def test_house_robber_tricky_later_choice():
    assert Solution().rob([2, 7, 9, 3, 1]) == 12
