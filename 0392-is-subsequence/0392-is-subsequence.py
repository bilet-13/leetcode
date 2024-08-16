class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        elif not t:
            return False
 
        cur_s = 0
        cur_t = 0

        while cur_s < len(s) and cur_t < len(t):
            while s[cur_s] != t[cur_t]:
                cur_t += 1
                if cur_t >= len(t):
                    return False
            
            cur_s += 1
            cur_t += 1

        return cur_s == len(s) 