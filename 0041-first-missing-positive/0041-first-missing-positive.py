class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        idx = 0

        while idx < n:
            num = nums[idx]

            if n >= num >= 1 and nums[idx] != nums[num - 1]:
                nums[idx], nums[num - 1] = nums[num - 1], nums[idx]
            else:
                idx += 1
        
        for idx in range(n):
            if nums[idx] != idx + 1:
                return idx + 1

        return n + 1
        