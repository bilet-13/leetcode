class Solution:
    def maxProfit(self, prices: List[int]) -> int:
          # if you wnat to buy you need to have no share
        # if we paint the price as 2d xy plane graph
        # we can see that the maximum profit is the sum of the diffence between the two element xi, xj where j > i
        # and xj > xi

        max_result = 0

        for i in range(1, len(prices)):
            max_result += max(0, prices[i] - prices[i - 1])
        
        return max_result
            
        




