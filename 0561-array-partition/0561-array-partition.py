class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # pigeon principle
        # sort array and 
        # maximum number must not be in the result
        # the maxium numbe rin sum is the sedcond maxmimum value

        nums.sort(reverse=True)
        maximized_sum = 0

        for i in range(1, len(nums), 2):
            maximized_sum += nums[i]
        
        return maximized_sum

        