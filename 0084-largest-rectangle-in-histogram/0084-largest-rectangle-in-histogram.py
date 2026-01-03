class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_smaller_idx = [-1 for _ in range(len(heights))]
        right_smaller_idx = [-1 for _ in range(len(heights))]

        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                left_smaller_idx[i] = stack[-1]
            
            stack.append(i)

        stack = []
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                right_smaller_idx[i] = stack[-1]
            
            stack.append(i)

        max_area = 0
        for i in range(len(heights)):
            left_bound_idx = 0 if left_smaller_idx[i] == -1 else left_smaller_idx[i] + 1
            right_bound_idx = len(heights) - 1 if right_smaller_idx[i] == -1 else right_smaller_idx[i] - 1

            area = heights[i] * (right_bound_idx - left_bound_idx + 1)
            max_area = max(area, max_area)

        return max_area


        