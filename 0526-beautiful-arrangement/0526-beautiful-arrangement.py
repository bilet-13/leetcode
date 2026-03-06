class Solution:
    def countArrangement(self, n: int) -> int:
        # backtracking
        # input argument: index to track
        # if index == n: add the permuationt
        # else 
        # check [index] is true and do backtrack(start + 1)
        nums = [i for i in range(1, n + 1)]
        result = 0

        def backtrack(start):
            nonlocal result
            if start == n:
                result += 1

            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]

                if nums[start] % (start + 1) == 0 or (start + 1) % nums[start] == 0:
                    backtrack(start + 1)

                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result
                

        