class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fartest = 0 + nums[0]
        
        for i in range(len(nums)):
            if i + nums[i] > fartest and i <= fartest:
                fartest = i + nums[i]
        
        return fartest >= len(nums) - 1
            


