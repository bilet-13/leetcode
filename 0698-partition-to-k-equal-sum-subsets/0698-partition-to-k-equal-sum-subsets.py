class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
         # 1 check the sum(nums) can be divide by k if not return False
        # 2 backtracking input argument : start index
        # input argument 
        # put them into k buckets and check the sums of buckets equal
        #

        if sum(nums) % k != 0:
            return False 

        equal_num = sum(nums) // k
        nums.sort(reverse=True)
        
        subsets = [0 for _ in range(k)]

        def backtrack(start):
            if start == len(nums):
                return True

            for i in range(k):
                if subsets[i] + nums[start] > equal_num:
                    continue

                subsets[i] += nums[start]

                if backtrack(start + 1):
                    return True

                subsets[i] -= nums[start]
                if subsets[i] == 0:
                    break
            
            return False

        return backtrack(0)
            
                
        