class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # read fast pointer
        # write:next unique element index , insert
        # 
        write = 0

        for read in range(1, len(nums)):
            if nums[read] != nums[write]:
                write += 1
                nums[write] = nums[read]

        return write + 1