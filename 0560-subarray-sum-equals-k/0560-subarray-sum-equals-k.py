class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # integer, negative , positive
        # prefix sum
        # k = prefix[i] - prefix[j] i > j
        # prefix[j] = prefix[i] - k
        # record the number of prefix[j]
        #time comolexity o(n)
        #space comolexity o(n)

        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        cur_sum = 0
        result = 0

        for num in nums:
            cur_sum += num
            target = cur_sum - k

            result += prefix_sum.get(target, 0)
            prefix_sum[cur_sum] += 1

        return result


