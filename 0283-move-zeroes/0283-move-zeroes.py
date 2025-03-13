class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        first_non_zero_num = 0      

        while first_non_zero_num < len(nums) - 1 and left < len(nums) - 1:
            while nums[first_non_zero_num] == 0 and first_non_zero_num < len(nums) - 1:
                first_non_zero_num += 1

            if nums[first_non_zero_num] == 0:
                return

            nums[first_non_zero_num], nums[left] = nums[left], nums[first_non_zero_num]
            
            left += 1
            first_non_zero_num = left

            