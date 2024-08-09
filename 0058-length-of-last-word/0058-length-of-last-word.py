class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        
        word_right_index = None
        length = 0

        for i in range( len(s)-1, -1, -1):
            if not word_right_index and s[i] != ' ':
                word_right_index = i

            if word_right_index and s[i] == ' ':
                length = word_right_index - i
                break
            elif i == 0:
                length = len([char for char in s if char != ' '])

        return length
