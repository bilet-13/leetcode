class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # -4 , -1 , 0 , 3, 10
        #0. .               r
        # 0 1,  9 , 16, 100 
        
        result = []
        left = None
        right = None

        # find left and right
        for i in range(len(nums)):
            if nums[i] >= 0:
                right = i
                left = i - 1
                break

        if right is None: # all negative
            left = len(nums) - 1
            right = len(nums)

        while left >= 0 or right < len(nums):
            if left >= 0 and right < len(nums):
                if pow(nums[left], 2) < pow(nums[right], 2):
                    smaller = pow(nums[left], 2)
                    left -= 1
                else:
                    smaller = pow(nums[right], 2)
                    right += 1
                result.append(smaller)
            elif left >= 0:
                result.append(pow(nums[left], 2))
                left -= 1
            else:
                result.append(pow(nums[right], 2))
                right += 1

        return result


