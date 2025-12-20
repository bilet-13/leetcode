class Solution:
    def trap(self, height: List[int]) -> int:
         # brute force
        # for each bar, its water is determin by the smallest neighbor among right and left tallest neighbor
        #time complexity o(n)
        result = 0
        leftmost = [0 for _ in range(len(height))]
        rightmost = [0 for _ in range(len(height))]

        for i in range(1, len(height)):
            cur_left_most = max(height[i - 1], leftmost[i - 1])
            leftmost[i] = cur_left_most

        for i in range(len(height) - 2, -1, -1):
            cur_right_most = max(height[i + 1], rightmost[i + 1])
            rightmost[i] = cur_right_most
        
        trap_water = 0
        for i in range(len(height)):
            trap_water += max(min(rightmost[i], leftmost[i]) - height[i], 0)

        return trap_water

        
        