from problem_20_valid_parentheses import Solution


def test_valid_parentheses_example():
    assert Solution().isValid("{[]}") is True


def test_valid_parentheses_edge_empty():
    assert Solution().isValid("") is True


def test_valid_parentheses_tricky_crossed_pairs():
    assert Solution().isValid("([)]") is False
