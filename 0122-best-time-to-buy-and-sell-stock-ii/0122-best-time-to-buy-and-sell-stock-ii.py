class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # the quesiont == find the sum of all positive differce for prices[i + 1] - prices[i - 1]

        max_sum = 0

        for i in range(1, len(prices)):
            max_sum += max(0, prices[i] - prices[i - 1])
        
        return max_sum
        