class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
         # backtrack

        def backtrack(cur, start, result):
            if len(cur) == k:
                result.append(cur[:])
                return

            for i in range(start, n + 1):
                cur.append(i)

                backtrack(cur, i + 1, result)

                cur.pop()


        result = []
        backtrack([], 1, result)

        return result
        