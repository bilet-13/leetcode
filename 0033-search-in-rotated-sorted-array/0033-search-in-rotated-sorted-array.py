class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
	        return 0 if nums[0] == target else -1

        end= nums[-1] #valuue
        left = 0
        right = len(nums) - 1
        pivot = -1

        while left < right:
            mid = (left + right) // 2
            if  nums[mid] > end:
                left = mid + 1
            else:
                right = mid

        original_start_index =  left 

        if target > end:
            left = 0
            right = original_start_index - 1
        else:
            left = original_start_index
            right = len(nums) - 1 

        while left < right:
            mid = (left + right) // 2
            if  nums[mid] <  target:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1

      

