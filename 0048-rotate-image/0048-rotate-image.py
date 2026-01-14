class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # swap along x asix and y asix
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            left = 0
            right = n - 1

            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1



        