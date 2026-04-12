class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute force
        # start with a char extend to left and right and find the max possible palindromic string
        # start with a pair of char and extend left and right max possible string
        # time complexity o(2 * n * n) = o(n ^ 2)

        result = ""
        n = len(s)

        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    result = s[left: right + 1] if len(result) < right - left + 1 else result
                    left -= 1
                    right += 1
                else:
                    break
            
        for i in range(len(s) - 1):
            left = i
            right = i + 1

            while left >= 0 and right < n:
                if s[left] == s[right]:
                    result = s[left: right + 1] if len(result) < right - left + 1 else result
                    left -= 1
                    right += 1
                else:
                    break
        
        return result

        