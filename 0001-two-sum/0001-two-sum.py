class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        existed_nums = {}

        for i in range(len(nums)):
            target_num = target - nums[i] 
            
            if target_num in existed_nums:
                return [existed_nums[target_num], i]

            existed_nums[nums[i]] = i

        return [-1, -1]
        
        