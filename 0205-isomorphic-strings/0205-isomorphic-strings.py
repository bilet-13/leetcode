class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t_map = {}
        t_s_map = {}
        for i in range(len(s)):
            if s[i] not in s_t_map and t[i] not in t_s_map:
                s_t_map[s[i]] = t[i]
                t_s_map[t[i]] = s[i]
            elif s[i] not in s_t_map or t[i] not in t_s_map:
                return False
            elif s_t_map[s[i]] == t[i] and t_s_map[t[i]] == s[i]:
                continue
            else:
                return False
        return True