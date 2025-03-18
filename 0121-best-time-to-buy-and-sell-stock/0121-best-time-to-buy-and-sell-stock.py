class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price_before = prices[0]
        max_profit = 0

        for price in prices:
            if (price - min_price_before > max_profit):
                max_profit = price - min_price_before

            min_price_before = price if price < min_price_before else min_price_before

        return max_profit
        