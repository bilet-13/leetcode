class Solution:
    def countArrangement(self, n: int) -> int:
        # backtracking do permutaion and check rules in each level
        # input argument: index to track
        # if index == n: add the permuationt
        # else 
        # check [index] is true and do backtrack(idx + 1)
        nums = [i for i in range(1, n + 1)]
        mask = 0
        result = 0

        def backtrack(idx):
            nonlocal result
            nonlocal mask
            if idx == 0:
                result += 1
                return

            for num in range(1, n + 1):
                if mask & (1 << num) == 0 and (num % idx == 0 or idx % num == 0):

                    mask |= 1 << num

                    backtrack(idx - 1)

                    mask ^= 1 << num

        backtrack(n)
        return result
                

        