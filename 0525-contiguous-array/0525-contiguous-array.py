class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # maximum  lenth, subarray -> prefix sum?
        # turn all 0 to -1 
        # the problem is to find max length subarray that sum == 0
        # subarray: not empty arr

        # 0 = cur_sum - prefix[j] the farthest j
        # hash map: key : sum value the leftmost idx
        new_nums = [1 if nums[i] == 1 else -1 for i in range(len(nums))]
        prefix_sum = {0: 0}
        cur_sum = 0
        max_len = 0

        for i in range(len(nums)):
            cur_sum += new_nums[i]
            if cur_sum in prefix_sum:
                max_len = max(max_len, i - prefix_sum[cur_sum] + 1)
            else:
                prefix_sum[cur_sum] = i + 1
        
        return max_len
            




        