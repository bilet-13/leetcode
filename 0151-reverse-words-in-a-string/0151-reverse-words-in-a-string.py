class Solution:
    def reverse(self, s):
        r_s = ""
        for i in range(len(s)-1, -1, -1):
            r_s += s[i]
        return r_s
    def reverseWords(self, s: str) -> str:
        
        words = []
        in_word = False
        word_start = 0

        for i in range(len(s)):
            if s[i] == ' ':
                if in_word:
                    word = s[word_start:i]
                    words.append(word)
                    in_word = False
                continue
            else:
                if not in_word:
                    in_word = True
                    word_start = i
                if i == len(s) -  1:
                    word = s[word_start:]
                    words.append(word)
                continue
        
        result = ""
        print(words)
        for i in range(len(words)-1, -1, -1):
            result += words[i]
            if i != 0:
                result += " "
        return result
