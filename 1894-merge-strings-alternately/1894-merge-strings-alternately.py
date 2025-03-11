class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index = 0
        len_word1 = len(word1)
        len_word2 = len(word2)

        merged_word = ""

        while(index < len_word1 or index < len_word2):
            if (index < len_word1):
                merged_word += word1[index]
            if (index < len_word2):
                merged_word += word2[index]
            index += 1

        return merged_word
        