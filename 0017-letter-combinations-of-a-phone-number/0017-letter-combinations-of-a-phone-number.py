class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
           # input arguaments: cur: current combination start: index of digit in digits
        # result: gloabl var to store return result
        # base case if start == len(digits) append cur to result
        # recusive start for start loop throught the chars that digits[start] represents
        # add char to cur and do backtack and then pop
        # 

        result = []
        digit_to_chars = {
            2: ["a", "b", "c"], 
            3: ["d", "e", "f"], 
            4: ["g", "h", "i"], 
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }

        def backtrack(cur, start):
            if start == len(digits):
                result.append("".join(cur))
                return
            
            chars = digit_to_chars[int(digits[start])]

            for char in chars:
                cur.append(char)
                backtrack(cur, start + 1)
                cur.pop()
        if not digits:
            return []
            
        backtrack([], 0)
        return result

        