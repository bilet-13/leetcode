class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
           #backtrack knappack
        sum_sides = sum(matchsticks)
        if sum_sides % 4 != 0:
            return False
        matchsticks.sort(reverse=True)

        side_len = sum_sides // 4
        n = len(matchsticks)

        @cache
        def dp(mask):
            if mask == (1 << n) - 1:
                return True
            
            used_len = 0
            for i in range(n):
                if (mask & (1 << i)) != 0:
                    used_len += matchsticks[i]

            cur_len = used_len % side_len

            for i in range(n):
                if (mask & (1 << i)) == 0:
                    if cur_len + matchsticks[i] <= side_len:
                        next_mask = mask | (1 << i)

                        if dp(next_mask):
                            return True
            return False


        return dp(0)
        