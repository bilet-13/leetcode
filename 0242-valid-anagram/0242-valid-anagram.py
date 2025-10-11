class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = [ 0 for _ in range(26) ]
        tChars = [ 0 for _ in range(26) ]

        for c in s:
            sChars[ord(c) - ord('a')] += 1
        for c in t:
            tChars[ord(c) - ord('a')] += 1
        
        for i in range(len(sChars)):
            if sChars[i] != tChars[i]:
                return False

        return True