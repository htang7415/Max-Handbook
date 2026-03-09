from problem_455_assign_cookies import Solution


def test_assign_cookies_example():
    assert Solution().findContentChildren([1, 2, 3], [1, 1]) == 1


def test_assign_cookies_edge_no_cookies():
    assert Solution().findContentChildren([1, 2], []) == 0


def test_assign_cookies_tricky_extra_cookies():
    assert Solution().findContentChildren([1, 2], [1, 2, 3]) == 2
