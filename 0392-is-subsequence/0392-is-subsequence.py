class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        t_index = 0

        for s_index in range(len(s)):
            while t_index < len(t) and t[t_index] != s[s_index]:
                t_index += 1
            if t_index == len(t):
                return False

            t_index += 1

        return True
            

            