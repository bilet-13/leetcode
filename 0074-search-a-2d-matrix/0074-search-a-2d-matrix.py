class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            middle = (left + right) // 2

            element = matrix[middle // len(matrix[0])][middle % len(matrix[0])]
            if target == element:
                return True
            elif target > element:
                left = middle + 1
            else :
                right = middle - 1

        return False