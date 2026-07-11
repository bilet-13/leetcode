class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #smallest
        #brute force (choose 2 of n) * (choose 2 of n - 1) ..... (choose 2 of 2)
        #dp[i][j] = smallest possible weight of array start from i to j
        #dp[i][i] = stones[i] 
        #dp[i][i + 1] = abs(stones[i] - stones[i + 1])
        #d[i][i + 2] = min(abs(stones[i] - dp[i+1][i+2], abs(stone[i + 1]-abs(dp[i]- dp[i + 2]), abs(stones[i + 2] - dp[i][i + 1]))) 
        #dp[i][i + k] = min(abs(stones[i] - dp[i+1][i+k], stones[i + 1]- abs)
        # can transfer to 0/1 knapspack problem
        n = len(stones)
        cap = sum(stones) // 2
        dp = [[0 for _ in range(n)] for _ in range(cap + 1)]

        for c in range(0, cap + 1):
            for i in range(n):
                if i == 0:
                    dp[c][i] = stones[0] if c >= stones[0] else 0
                else:
                    dp[c][i] = dp[c][i - 1]
                    if c - stones[i] >= 0:
                        dp[c][i] = max(dp[c][i], stones[i] + dp[c - stones[i]][i - 1])                
            
        return sum(stones) - (2 * dp[cap][n - 1])


        