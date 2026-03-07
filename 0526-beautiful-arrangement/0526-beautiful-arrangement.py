class Solution:
    def countArrangement(self, n: int) -> int:
        # dping do permutaion and check rules in each level
        # input argument: index to track
        # if index == n: add the permuationt
        # else 
        # check [index] is true and do dp(idx + 1)
        nums = [i for i in range(1, n + 1)]
        memo = {}
        
        def dp(mask, idx):
            if idx == 0:
                return 1
            
            if (mask, idx) in memo:
                return memo[(mask, idx)]

            total_arrangement = 0

            for num in range(1, n + 1):
                if mask & (1 << num) == 0 and (num % idx == 0 or idx % num == 0):
                    total_arrangement += dp(mask | (1 << num), idx - 1)

            memo[(mask, idx)] = total_arrangement
            return total_arrangement

        return dp(0, n)

                

        