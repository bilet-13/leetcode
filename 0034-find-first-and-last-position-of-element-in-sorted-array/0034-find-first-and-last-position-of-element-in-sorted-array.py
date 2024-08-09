class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
	        return [-1, -1]

        left = 0
        right = len(nums) - 1
        first_index_tar = -1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                if mid - 1 >= 0 and nums[mid-1] == target:
                    right = mid
                else:
                    first_index_tar = mid
                    break
        else:
            if nums[left] == target:
                first_index_tar = left

        if first_index_tar == -1:
            return [-1, -1]

        left = first_index_tar
        right = len(nums) - 1
        last_index_tar = -1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                if mid + 1 < len(nums) and nums[mid+1] == target:
                    left = mid + 1
                else:
                    last_index_tar = mid
                    break
        else:
            if nums[left] == target:
                last_index_tar = left

        return [first_index_tar, last_index_tar]

        