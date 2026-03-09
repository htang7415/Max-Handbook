from problem_714_best_time_to_buy_and_sell_stock_with_transaction_fee import Solution


def test_stock_fee_example():
    assert Solution().maxProfit([1, 3, 2, 8, 4, 9], 2) == 8


def test_stock_fee_edge_single_day():
    assert Solution().maxProfit([1], 2) == 0


def test_stock_fee_tricky_multiple_trades():
    assert Solution().maxProfit([1, 3, 7, 5, 10, 3], 3) == 6
