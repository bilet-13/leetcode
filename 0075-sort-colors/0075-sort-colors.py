class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        color_num = defaultdict(int)

        for c in nums:
            color_num[c] += 1
        
        for i in range(len(nums)):
            if i < color_num[0]:
                nums[i] = 0
            elif color_num[1] + color_num[0] > i >= color_num[0]:
                nums[i] = 1
            else:
                nums[i] = 2
        