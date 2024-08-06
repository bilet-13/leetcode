class Solution:

    def binary_search_index(self, nums, left, right, target):

        if 0 <= left and left <= right and right < len(nums):
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif left != right:
                if target > nums[middle]:
                    return self.binary_search_index(nums, middle + 1, right, target)
                else:
                    return self.binary_search_index(nums, left, middle, target)
            
            else:
                if target > nums[middle]:
                    return middle + 1
                else:
                    return middle

        return None

    def searchInsert(self, nums: List[int], target: int) -> int:
        
            return self.binary_search_index(nums, 0, len(nums)-1, target)