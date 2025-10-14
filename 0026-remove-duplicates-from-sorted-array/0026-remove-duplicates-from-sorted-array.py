class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_element_idx = 1
        prev = nums[0]
        # double pointer one for each element , another one for unique element

        for i in range(1, len(nums)):
            if nums[i] != prev:
                nums[unique_element_idx] = nums[i]
                unique_element_idx += 1

            prev = nums[i]
        return unique_element_idx

        