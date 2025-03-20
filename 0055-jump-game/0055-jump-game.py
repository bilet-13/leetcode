class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fartest = 0

        for i in range(len(nums)):
            if i <= fartest:
                fartest = max(fartest, nums[i] + i)
            
            if fartest >= len(nums) - 1:
                return True
        
        return False



        

        