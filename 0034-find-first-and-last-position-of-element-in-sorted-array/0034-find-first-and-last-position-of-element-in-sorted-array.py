class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # do binary search twice                               V  
        # first binary search condiciton : num >= target x x x o o o 

       # do binary search twice                               V  
        # second binary search condiciton : num > target, x x x o o o 
        if not nums:
            return [-1, -1]
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        if left >= len(nums) or nums[left] != target:
            return [-1, -1]

        result = [left]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        result.append(right)

        return result
        
