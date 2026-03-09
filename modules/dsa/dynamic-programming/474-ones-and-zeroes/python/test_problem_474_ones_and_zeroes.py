from problem_474_ones_and_zeroes import Solution


def test_ones_and_zeroes_example():
    assert Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) == 4


def test_ones_and_zeroes_edge_zero_capacity():
    assert Solution().findMaxForm(["10", "0", "1"], 0, 0) == 0


def test_ones_and_zeroes_tricky_small_capacity():
    assert Solution().findMaxForm(["10", "0", "1"], 1, 1) == 2
