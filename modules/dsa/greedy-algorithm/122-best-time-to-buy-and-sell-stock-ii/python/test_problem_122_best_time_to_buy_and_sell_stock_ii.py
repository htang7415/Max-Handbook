from problem_122_best_time_to_buy_and_sell_stock_ii import Solution


def test_stock_profit_example():
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7


def test_stock_profit_edge_none():
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0


def test_stock_profit_tricky_all_rising():
    assert Solution().maxProfit([1, 2, 3, 4, 5]) == 4
