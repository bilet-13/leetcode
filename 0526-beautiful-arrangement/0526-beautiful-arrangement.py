class Solution:
    def countArrangement(self, n: int) -> int:
        # backtracking do permutaion and check rules in each level
        # input argument: index to track
        # if index == n: add the permuationt
        # else 
        # check [index] is true and do backtrack(idx + 1)
        nums = [i for i in range(1, n + 1)]
        used = [False for _ in range(n + 1)]
        result = 0

        def backtrack(idx):
            nonlocal result
            if idx == 0:
                result += 1
                return

            for num in range(1, n + 1):
                if not used[num] and (num % idx == 0 or idx % num == 0):

                    used[num] = True

                    backtrack(idx - 1)

                    used[num] = False

        backtrack(n)
        return result
                

        