from problem_860_lemonade_change import Solution


def test_lemonade_change_example():
    assert Solution().lemonadeChange([5, 5, 5, 10, 20]) is True


def test_lemonade_change_edge_false():
    assert Solution().lemonadeChange([5, 5, 10, 10, 20]) is False


def test_lemonade_change_tricky_choose_10_and_5():
    assert Solution().lemonadeChange([5, 5, 5, 10, 10, 20]) is True
