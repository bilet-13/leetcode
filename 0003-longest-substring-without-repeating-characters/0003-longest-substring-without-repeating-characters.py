from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
     # sliding window
     # extend to right
     # shrink the window until there is no duplicate characters and update result
     # time o(n)

       # substring without duplicate -> limiti length sequence -> sliding window

        left = 0
        longest_length = 0
        chars_in_window = defaultdict(int)

        for right in range(len(s)):
            chars_in_window[s[right]] += 1

            while chars_in_window[s[right]] > 1 and left <= right:
                chars_in_window[s[left]] -= 1
                left += 1
            
            longest_length = max(longest_length, right - left + 1)


        return longest_length

            

        