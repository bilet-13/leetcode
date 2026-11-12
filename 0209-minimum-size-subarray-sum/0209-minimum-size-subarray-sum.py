class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len = float("inf")
        left = 0
        cur_sum = 0

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target and left <= right:
                min_len = min(min_len, right - left + 1)

                cur_sum -= nums[left]
                left += 1

        return min_len if min_len != float("inf") else 0


        