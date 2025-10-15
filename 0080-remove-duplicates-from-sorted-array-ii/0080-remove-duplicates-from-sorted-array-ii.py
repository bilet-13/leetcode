class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # double pointer, one for the element, one for the element that are at most twice
        # one variable duplicate_num the duplicate_num so far

        unique_idx = 1
        duplicate_num = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_idx] = nums[i]
                unique_idx += 1
                duplicate_num = 1
            
            elif duplicate_num < 2:
                nums[unique_idx] = nums[i]
                unique_idx += 1
                duplicate_num += 1

        return unique_idx # 
        