class Solution:
    def trap(self, height: List[int]) -> int:

        left_max = [0 for _ in range(len(height))]
        right_max = [0 for _ in range(len(height))]
        max_element = height[0]
        water = 0

        for i in range(len(height)):
            max_element = max(max_element, height[i])
            left_max[i] = max_element

        max_element = height[-1]
        for i in range(len(height)-1, -1, -1):
            max_element = max(max_element, height[i])
            right_max[i] = max_element
        
        for i in range(len(height)):
            water += max(min(left_max[i], right_max[i]) - height[i], 0)
        return water
