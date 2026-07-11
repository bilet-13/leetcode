class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        #smallest
        n = len(stones)
        cap = sum(stones) // 2
        dp = [0 for _ in range(cap + 1)]

        for i in range(n):
            for c in range(cap, -1, -1):
                if c - stones[i] >= 0:
                    dp[c] = max(dp[c], dp[c - stones[i]] + stones[i])

        return sum(stones) - (2 * dp[cap]) 



       


        