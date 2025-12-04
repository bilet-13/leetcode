class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # [ 1, 2, 3]
        # [ 4, 5, 6]

        # [1, 3, 6]
        # [5, 12, 21]
        n = len(matrix)
        m = len(matrix[0])
        self.prefix_matrix = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0:
                    self.prefix_matrix[i][j] = matrix[i][j] if j == 0 else self.prefix_matrix[i][j - 1] + matrix[i][j]

                else:
                    left_part = self.prefix_matrix[i][j - 1] if j > 0 else 0
                    upper_part = self.prefix_matrix[i - 1][j] if i > 0 else 0

                    overlap_part = self.prefix_matrix[i - 1][j - 1] if i > 0 and j > 0 else 0

                    self.prefix_matrix[i][j] = matrix[i][j] + left_part + upper_part - overlap_part

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        left_part = self.prefix_matrix[row2][col1 - 1] if col1 - 1 >= 0 else 0
        upper_part = self.prefix_matrix[row1 - 1][col2] if row1 - 1 >= 0 else 0

        overlap_part = self.prefix_matrix[row1 - 1][col1 - 1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0

        return  self.prefix_matrix[row2][col2] - left_part - upper_part + overlap_part
        


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)