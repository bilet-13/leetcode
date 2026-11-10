class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        max_sum = cur_sum

        for i in range(k, len(nums)):
            cur_sum -= nums[i - k]
            cur_sum += nums[i]

            max_sum = max(max_sum, cur_sum)

        return max_sum / k

        