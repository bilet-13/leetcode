class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        total_subsets = pow(2, n)
        result = []

        for i in range(total_subsets):
            current_subset = []
            for j in range(n):
                if i  & (1 << j) != 0:
                    current_subset.append(nums[j])

            result.append(current_subset)
        
        return result



        
        return result
        