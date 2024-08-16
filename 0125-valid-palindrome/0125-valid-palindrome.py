class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        cur = 0
        alphanumeric_char = []
        while cur < len(s):
            if( ord('0') <= ord(s[cur])  and ord(s[cur]) <= ord('9') )or (ord('a') <= ord(s[cur]) and ord(s[cur]) <= ord('z')):
                alphanumeric_char += s[cur]
            cur += 1
            
        alphanumeric_s = "".join(alphanumeric_char)
        start = 0
        end = len(alphanumeric_s) - 1
        print(alphanumeric_s)
        while start < end:
            if alphanumeric_s[start] != alphanumeric_s[end]:
                return False
            end -= 1
            start += 1
        return True


       
        