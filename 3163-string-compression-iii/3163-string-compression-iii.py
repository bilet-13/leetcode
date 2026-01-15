class Solution:
    def compressedString(self, word: str) -> str:
        read = 0
        n = len(word)
        comp = ""

        while read < n:
            char = word[read]
            count = 0

            while read < n and word[read] == char and count < 9:
                read += 1
                count += 1
            
            comp += str(count) + char
        
        return comp



        