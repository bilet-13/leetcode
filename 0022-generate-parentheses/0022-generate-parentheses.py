class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # maintain left num and right number

        def backtrack(cur, left, right, result):
            if len(cur) == 2 * n:
                result.append("".join(cur))
                return

            if left < n:
                cur.append("(")
                backtrack(cur, left + 1, right, result)
                cur.pop()

            if left > right:
                cur.append(")")
                backtrack(cur, left , right + 1, result)
                cur.pop()

        result = []
        backtrack([], 0, 0, result)


        return result
            
        
        