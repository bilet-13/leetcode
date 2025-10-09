class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        existed_nums = set()

        for num in nums:
            if num in existed_nums:
                return True
            existed_nums.add(num)
        return False 