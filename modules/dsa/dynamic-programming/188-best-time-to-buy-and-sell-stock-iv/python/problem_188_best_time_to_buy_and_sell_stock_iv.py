from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
        n = len(prices)
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        buy = [float("-inf")] * (k + 1)
        sell = [0] * (k + 1)
        for price in prices:
            for transaction in range(1, k + 1):
                buy[transaction] = max(buy[transaction], sell[transaction - 1] - price)
                sell[transaction] = max(sell[transaction], buy[transaction] + price)

        return sell[k]
