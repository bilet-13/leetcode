class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for i in range(1, len(prices)):
            total_profit += max(prices[i]-prices[i-1], 0)
        return total_profit