class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
          #backtrack knappack
        sum_sides = sum(matchsticks)
        if sum_sides % 4 != 0:
            return False

        matchsticks.sort(reverse=True)

        side_len = sum_sides // 4
        sides = [0, 0, 0, 0]

        def backtrack(start):
            if start == len(matchsticks):
                return True

            for i in range(4):
                if sides[i] + matchsticks[start] <= side_len:
                    sides[i] += matchsticks[start]

                    if backtrack(start + 1):
                        return True
                
                    sides[i] -= matchsticks[start]
            
            return False

        return backtrack(0)
        
        