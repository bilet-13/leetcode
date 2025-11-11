class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #tupel: read only
        candidate, count = nums[0], 1

        for i in range(1, len(nums)):
            if nums[i] != candidate:
                count -= 1
                
                if count == 0:
                    candidate, count = nums[i], 1
            else:
                count += 1

        return candidate

        