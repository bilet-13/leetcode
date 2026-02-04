class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result_idx = 0

        for num in nums:
            if num != val:
                nums[result_idx] = num
                result_idx += 1

        return result_idx