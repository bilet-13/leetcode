class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # [ 1, 2, 3]
        # [ 4, 5, 6]

        # [1, 3, 6]
        # [5, 12, 21]
        n = len(matrix)
        m = len(matrix[0])
        self.prefix_matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                self.prefix_matrix[i + 1][j + 1] = matrix[i][j] + self.prefix_matrix[i + 1][j] + self.prefix_matrix[i][j + 1] - self.prefix_matrix[i][j]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_matrix[row2 + 1][col2 + 1] - self.prefix_matrix[row1][col2 + 1] - self.prefix_matrix[row2 + 1][col1] + self.prefix_matrix[row1][col1]

        


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)