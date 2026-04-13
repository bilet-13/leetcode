class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # need to consider target not exist or the nums is empty arr
        # do binary search twice                               V  
        # first binary search condiciton : num >= target x x x o o o 

       # do binary search twice                               V  
        # second binary search condiciton : num > target, x x x o o o 
      
        
        def search(condiction, return_left=True):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
    
                if condiction(nums[mid]):
                    right = mid - 1
                else:
                    left = mid + 1
            
            return left if return_left else right

        left = search(lambda x: x >= target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]

        result = [left]

        right = search(lambda x: x > target, False)
        result.append(right)

        return result
        
