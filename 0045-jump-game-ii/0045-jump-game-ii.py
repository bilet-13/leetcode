class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        pos = 0

        while pos < len(nums)-1:
            if pos + nums[pos] >= len(nums) - 1:
                return jump + 1

            start = pos
            for i in range(1, nums[start]+1):
                if nums[start + i] + start + i > nums[pos] + pos:
                    pos = start + i
            jump += 1
        
        return jump






        