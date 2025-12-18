class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
         def reverse_by_left_right(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)

        k = k % n
        if k == 0:
            return

        reverse_by_left_right(0, n - 1)
        reverse_by_left_right(0, k - 1)
        reverse_by_left_right(k, n - 1)
        