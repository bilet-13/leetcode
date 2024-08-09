class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        
        in_word = False
        length = 0

        for i in range( len(s)-1, -1, -1):
            if s[i] != ' ':
                in_word = True
                length += 1
                
            elif in_word:
                break

        return length
