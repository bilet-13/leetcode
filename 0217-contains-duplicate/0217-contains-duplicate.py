class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        existed_nums = {}

        for num in nums:
            if num in existed_nums:
                return True
            existed_nums[num] = True
        
        return False
        