class Solution:
    def trap(self, height: List[int]) -> int:
         # brute force
        # for each bar, its water is determin by the smallest neighbor among right and left tallest neighbor
        #time complexity o(n)
        result = 0

        leftmost = 0
        rightmost = 0

        left = 0
        right = len(height) - 1

        while left <= right:
            if leftmost < rightmost:
                result += max(leftmost - height[left], 0)
                leftmost = max(height[left], leftmost)
                
                left += 1
            
            else:
                result += max(rightmost - height[right], 0)
                rightmost = max(height[right], rightmost)

                right -= 1

        return result

        