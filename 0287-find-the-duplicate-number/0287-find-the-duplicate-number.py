import collections
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # buld hash map: key = num val: the number of the num in nums

        # iterate the nums with num and check the map[num] > 0 or not if yes return num else insert the num to map
        # time O(n) space O(n)

        for i, num in enumerate(nums):
            if nums[abs(num) - 1] < 0:
                return abs(num)

            nums[abs(num) - 1] *= -1
            
        return 0
