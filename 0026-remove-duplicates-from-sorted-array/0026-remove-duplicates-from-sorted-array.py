class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return len(nums)

        unique_element_index = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[unique_element_index] = nums[i]
                unique_element_index += 1

        return unique_element_index
        