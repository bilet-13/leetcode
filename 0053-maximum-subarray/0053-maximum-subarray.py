class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kandane algo
        # o(n)
        max_sum = -float("inf")
        cur_sum = 0

        for num in nums:
            cur_sum = max(0, cur_sum)
            cur_sum += num

            max_sum = max(cur_sum, max_sum)
        
        return max_sum
        