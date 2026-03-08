class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 7 1 2 6 so the max profit is 6 - 1 = 5
       # sliding window?
        max_profit = 0
        l = 0
        
        for r in range(len(prices)):
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            
            else:
                l = r
        
        return max_profit