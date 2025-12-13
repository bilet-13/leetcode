class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # brute force double loop
        # for calsue the difrence betwen result[i] to other elemnt result[j]
        # time complexity o(n^2)
        # how to make it faster
        # prefix sum

        prefix_sum = [0 for _ in range(len(nums) + 1)]

        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        result = []

        n = len(nums)
        for i in range(len(nums)):
            left_sum = prefix_sum[i] - prefix_sum[0]
            left_count = i
            left_part = left_count * nums[i] - left_sum

            right_count = n - i - 1
            right_sum = prefix_sum[n] - prefix_sum[i + 1]
            right_part = right_sum - right_count * nums[i]

            result.append(left_part + right_part) 
           
        return result

