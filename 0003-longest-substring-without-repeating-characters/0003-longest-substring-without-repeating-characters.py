from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # substring -> sliding window
        # how to check if there is a duplicate char -> dict -> use set to store the element in the current window 
        # shrink left until the set does not contain the rightmost element
        result_len = 0
        chars_in_window = defaultdict(int)
        left = 0

        for right in range(len(s)):
            chars_in_window[s[right]] += 1

            while left < right and chars_in_window[s[right]] > 1:
                chars_in_window[s[left]] -= 1
                left += 1

            result_len = max(result_len, right - left + 1)
        
        return result_len

     