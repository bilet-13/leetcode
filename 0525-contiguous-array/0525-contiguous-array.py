class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # maximum  lenth, subarray -> prefix sum?
        # turn all 0 to -1 
        # the problem is to find max length subarray that sum == 0
        # subarray: not empty arr

        # 0 = cur_sum - prefix[j] the farthest j
        # hash map: key : sum value the leftmost idx
        new_nums = [-1 if num == 0 else 1 for num in nums]
        prefix_sum = {0: 0}
        cur_sum = 0
        max_len = 0

        for i in range(len(nums)):
            cur_sum += new_nums[i]
            cur_len = i + 1

            if cur_sum in prefix_sum:
                max_len = max(max_len, cur_len - prefix_sum[cur_sum])
            else:
                prefix_sum[cur_sum] = cur_len 
        
        return max_len
            




        