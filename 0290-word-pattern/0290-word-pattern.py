class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_s = {}
        s_pattern = {}
        words = s.strip().split()

        if len(pattern) != len(words):
            return False

        for char, word in zip(pattern, words):
            if char not in pattern_s and word not in s_pattern:
                pattern_s[char] = word
                s_pattern[word] = char
            elif char in pattern_s and word in s_pattern:
                if pattern_s[char] == word and s_pattern[word] == char:
                    continue
                else:
                    return False
            else:
                return False
        return True