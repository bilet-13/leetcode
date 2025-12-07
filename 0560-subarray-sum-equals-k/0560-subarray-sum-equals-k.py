class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # time complexity o(n)
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        count = 0
        cur_sum = 0

        for num in nums:
            cur_sum += num

            target_prefix_sum = cur_sum - k

            count += prefix_count[target_prefix_sum]

            prefix_count[cur_sum] += 1

        return count
