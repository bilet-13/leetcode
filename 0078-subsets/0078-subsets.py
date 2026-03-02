class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        total_subsets = 1 << n
        result = []

        for i in range(total_subsets):
            current_subset = []
            for j in range(n):
                if (i >> j) & 1:
                    current_subset.append(nums[j])

            result.append(current_subset)
        
        return result
        


        
        return result
        