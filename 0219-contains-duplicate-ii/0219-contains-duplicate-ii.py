class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        existed_nums = {}

        for i in range(len(nums)):
            num = nums[i]

            if num in existed_nums and abs(existed_nums[num] - i) <= k:
                return True
            
            existed_nums[num] = i
        
        return False
        