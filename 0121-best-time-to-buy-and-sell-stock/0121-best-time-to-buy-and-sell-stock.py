class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # for each value, compute the difference between the value and its right largest neighbor
        # return the max difference == the maximum profit
        # time complexity o(n) 
        # find all right smallest neighbors o(n) one pass
        largest_rights = [p for p in prices]

        for i in range(len(largest_rights) - 2, - 1, -1):
            largest_rights[i] = max(prices[i + 1], largest_rights[i + 1]) 

        result = 0

        for i in range(len(prices)):
            max_profit_i = largest_rights[i] - prices[i]
            result = max(result, max_profit_i)

        return result

        
        