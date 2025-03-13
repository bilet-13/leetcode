class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0      

        while zero < len(nums) - 1:
            while nums[zero] != 0 and zero < len(nums) - 1:
                zero += 1

            if zero == len(nums) - 1:
                return

            first_non_zero_num = zero

            while nums[first_non_zero_num] == 0 and first_non_zero_num < len(nums) - 1:
                first_non_zero_num += 1
            
            if first_non_zero_num == len(nums) - 1 and nums[first_non_zero_num] == 0:
                return

            nums[first_non_zero_num], nums[zero] = nums[zero], nums[first_non_zero_num]
            zero += 1

            