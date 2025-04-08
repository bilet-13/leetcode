class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def char_to_idx(char):
            if 'z' >= char >= 'a':
                return ord(char) - ord('a') 
            return ALPHABET_NUM + ord(char) - ord('A')

        def window_contain_target(window_freq, target_freq):
            return all(window_freq[char] >= target_freq[char] for char in target_freq)

        start = 0
        min_window = s + "t"
        target_freq = Counter(t)
        window_freq = Counter()

        for end in range(len(s)):
            window_freq[s[end]] += 1

            while window_contain_target(window_freq, target_freq) and start <= end:
                str_len = end - start + 1
                if str_len < len(min_window):
                    min_window = s[start: end+1]
                    
                window_freq[s[start]] -= 1
                start += 1
        return min_window if len(min_window) <= len(s) else ""
            