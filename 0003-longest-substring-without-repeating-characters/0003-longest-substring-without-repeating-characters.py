class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
     # sliding window
     # extend to right
     # shrink the window until there is no duplicate characters and update result
     # time o(n)

        left = 0
        result_len = 0
        chars_in_window = defaultdict(int)
    
        for right in range(len(s)):
            chars_in_window[s[right]] += 1
    
            while left <= right and chars_in_window[s[right]] > 1:
                chars_in_window[s[left]] -= 1
                left += 1
    
            if right - left + 1 > result_len:
                result_len = right - left + 1
    
        return result_len
    
