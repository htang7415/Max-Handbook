from problem_45_jump_game_ii import Solution


def test_jump_game_ii_example():
    assert Solution().jump([2, 3, 1, 1, 4]) == 2


def test_jump_game_ii_edge_single():
    assert Solution().jump([0]) == 0


def test_jump_game_ii_tricky_window_extension():
    assert Solution().jump([1, 2, 1, 1, 1]) == 3
