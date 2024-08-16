class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        start = 0
        end = len(s) - 1

        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1

            if s[start] != s[end]:
                return False
            start += 1
            end -= 1 
        
        return True


       
        