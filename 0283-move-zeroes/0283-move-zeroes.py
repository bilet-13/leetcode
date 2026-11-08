class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
         # 0 1 0 3 12
         # read: 
         # write: the next non zero elemtn index
         # 
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        for idx in range(write, len(nums)):
            nums[idx] = 0