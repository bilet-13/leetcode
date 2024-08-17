class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        lowest_price = prices[0]
        for i in range(0, len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]

            elif prices[i] > lowest_price:
                total_profit += prices[i] - lowest_price
                lowest_price = prices[i]
            else:
                continue
        return total_profit