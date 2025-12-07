class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # time complexity o(n)
        prefix_count = {0: 1}
        count = 0
        cur_sum = 0

        for num in nums:
            cur_sum += num

            target_prefix_sum = cur_sum - k

            count += prefix_count.get(target_prefix_sum, 0)

            prefix_count[cur_sum] = prefix_count.get(cur_sum, 0) + 1

        return count
