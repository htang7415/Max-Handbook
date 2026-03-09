from problem_188_best_time_to_buy_and_sell_stock_iv import Solution


def test_stock_iv_example():
    assert Solution().maxProfit(2, [2, 4, 1]) == 2


def test_stock_iv_edge_zero_transactions():
    assert Solution().maxProfit(0, [3, 2, 6, 5, 0, 3]) == 0


def test_stock_iv_tricky_two_transactions():
    assert Solution().maxProfit(2, [3, 2, 6, 5, 0, 3]) == 7
