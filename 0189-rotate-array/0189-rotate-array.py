class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0 or len(nums) == 1:
            return None
        k = k % len(nums)
        self._reverse(nums, 0, len(nums)-1)
        self._reverse(nums, 0, k-1)
        self._reverse(nums, k, len(nums)-1)


    def _reverse(self, nums, start, end):
        while start < end:
            tmp_num = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp_num
            start += 1
            end -= 1