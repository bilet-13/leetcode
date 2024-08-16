class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0 or len(nums) == 1:
            return None
        if k < len(nums):
            last_k = [nums[i] for i in range(len(nums)-k, len(nums))]
            for i in range(len(nums)-1, k-1, -1):
                nums[i] = nums[i-k]
            
            for i in range(len(last_k)):
                nums[i] = last_k[i]
        else:
            for _ in range(k):
                self._rotate(nums)

    def _rotate(self, nums):
        first = nums[-1]
        for i in range(len(nums)-1, 0, -1):
            nums[i] = nums[i-1]
        nums[0] = first