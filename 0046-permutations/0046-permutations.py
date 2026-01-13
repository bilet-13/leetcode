class Solution:
    def _find_permute(self, nums, start, result):
        if start == len(nums):
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]

            self._find_permute(nums, start+1, result)

            nums[start], nums[i] = nums[i], nums[start]

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        self._find_permute(nums, 0, result)

        return result

    
