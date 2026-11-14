class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        #  5 7 7 8 8 
        #  x x x o o  
        #      r l
        #  5 7 7 8 8 
        # x  x x x x o     
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]

        result.append(left)

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        result.append(right)

        return result



