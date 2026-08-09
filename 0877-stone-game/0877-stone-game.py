class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # dp[i][j] = max positive diffrence if i take first of the arr[i:j]
        n = len(piles)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]

        for length in range(1, n):

            for i in range(n - length):
                j = i + length 

                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])

        return dp[0][n - 1] > 0
            









