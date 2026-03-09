from problem_309_best_time_to_buy_and_sell_stock_with_cooldown import Solution


def test_stock_cooldown_example():
    assert Solution().maxProfit([1, 2, 3, 0, 2]) == 3


def test_stock_cooldown_edge_single():
    assert Solution().maxProfit([1]) == 0


def test_stock_cooldown_tricky_extra_trade():
    assert Solution().maxProfit([1, 2, 3, 0, 2, 4]) == 5
