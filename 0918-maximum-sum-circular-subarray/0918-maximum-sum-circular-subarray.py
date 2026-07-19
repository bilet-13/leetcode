class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #brute force n ^ 2
        total = sum(nums)
        cur_min = 0
        found_min = float("inf")
        
        cur_max = 0
        found_max = -float("inf")

        for num in nums:
            if cur_max < 0:
                cur_max = 0
            cur_max += num
            found_max = max(found_max, cur_max)

            if cur_min > 0:
                cur_min = 0
            cur_min += num
            found_min = min(found_min, cur_min)

        return found_max if found_max > (total - found_min) or found_max < 0 else total - found_min