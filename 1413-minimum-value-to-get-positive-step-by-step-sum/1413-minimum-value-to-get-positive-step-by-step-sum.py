class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        smallest_sum = 0
        cur_sum = 0

        for num in nums:
            cur_sum += num
            
            smallest_sum = min(smallest_sum, cur_sum)

        return max(1, 1 - smallest_sum)
        