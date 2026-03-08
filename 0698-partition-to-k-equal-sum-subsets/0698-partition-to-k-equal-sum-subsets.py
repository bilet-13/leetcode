class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
         # 1 check the sum(nums) can be divide by k if not return False
        # 2 backtracking input argument : start index
        # input argument 
        # put them into k buckets and check the sums of buckets equal
        #

        sum_nums = sum(nums)

        if sum_nums % k != 0:
            return False

        target_sum = sum_nums // k
        nums.sort(reverse=True)

        @cache
        def dp(mask, cur_sum):
            if mask.bit_count() == len(nums):
                return True

            for i in range(len(nums)):
                if mask & (1 << i) == 0 and cur_sum + nums[i] <= target_sum:
                    subset_sum = 0 if cur_sum + nums[i] == target_sum else cur_sum + nums[i]

                    if dp(mask | (1 << i), subset_sum):
                        return True

            return False

        return dp(0, 0)