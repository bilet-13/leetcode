class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        step = 0
        down = True
        rows = ["" for i in range(numRows)]
        for i in range(len(s)):
            rows[step] += s[i]
            if step == 0 :
                down = True
            elif step == numRows - 1:
                down = False
            
            step += 1 if down else -1

        return "".join(rows)

                    


