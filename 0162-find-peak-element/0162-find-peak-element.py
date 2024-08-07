class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while 0 <= left and left <= right and right < len(nums):
            mid = (left + right) // 2   
              
            if self.is_peak(nums, mid):
                return mid
            elif mid - 1 >= 0 and nums[mid-1] > nums[mid]:
                right = mid
            else:
                left = mid+1

        return left

    def is_peak(self, nums, ind):
        if ind == 0:
            if  ind+1 <len(nums) and nums[ind] > nums[ind+1]:
                return True 
            elif len(nums) == 1:
                return True
            return False
        elif ind == len(nums) - 1:
            if  nums[ind] > nums[ind-1]:
                return True
            return False
        else:
            if  nums[ind] > nums[ind+1] and nums[ind] > nums[ind-1]:
                return True
            return False
