class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        # len(nums) > 1 and rotate [1,  n-1]
        left = 0 
        right = len(nums) - 1
        rightest = nums[-1]

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > rightest:
                left = mid + 1
            else:
                if nums[mid-1] > rightest:
                    return nums[mid]
                else:
                    right = mid
        return nums[left]

        
        