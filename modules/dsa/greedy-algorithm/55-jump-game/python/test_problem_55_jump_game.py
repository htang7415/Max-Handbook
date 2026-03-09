from problem_55_jump_game import Solution


def test_jump_game_example():
    assert Solution().canJump([2, 3, 1, 1, 4]) is True


def test_jump_game_edge_single():
    assert Solution().canJump([0]) is True


def test_jump_game_tricky_zero_trap():
    assert Solution().canJump([3, 2, 1, 0, 4]) is False
