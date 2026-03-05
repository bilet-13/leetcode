class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        num_subsets = pow(2, len(nums))

        for mask in range(num_subsets):
            xor_total = 0
            
            for i in range(len(nums)):
                if mask & (1 << i) != 0:
                    xor_total ^= nums[i]

            result += xor_total

        return result



            

            




        