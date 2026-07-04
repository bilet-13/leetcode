class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                up = dp[i - 1][j] if (i - 1) >= 0 else float("inf")
                left = dp[i][j - 1] if (j - 1) >= 0 else float("inf")
                dp[i][j] = min(up, left) + grid[i][j]
        
        return dp[m - 1][n - 1]


        
        