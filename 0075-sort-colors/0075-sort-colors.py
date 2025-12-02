class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        red_num = 0
        white_num = 0
        blue_num = 0

        for c in nums:
            if c == 0:
                red_num += 1
            elif c == 1:
                white_num += 1
            else:
                blue_num += 1
        
        for i in range(len(nums)):
            if i < red_num:
                nums[i] = 0
            elif white_num + red_num > i >= red_num:
                nums[i] = 1
            else:
                nums[i] = 2
        