class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def find_row():
            left = 0
            right = m - 1

            while left <= right:
                mid = (right + left) // 2

                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    return mid
                
                elif target > matrix[mid][-1]:
                    left = mid + 1
                
                else:
                    right = mid - 1

            return -1


        def find_column(row):
            if row < 0 or row >= m:
                return False
            
            left = 0
            right = n - 1

            while left <= right:
                mid = (right + left) // 2

                if matrix[row][mid] == target:
                    return True
                
                elif target > matrix[row][mid]:
                    left = mid + 1
                
                else:
                    right = mid - 1

            return False

        row = find_row()
        return find_column(row)
        
        