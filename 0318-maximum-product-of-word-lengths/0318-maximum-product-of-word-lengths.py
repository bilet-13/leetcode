class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # combination
        states = {}
        max_product = 0

        for word in words:
            states[word] = 0

            for char in word:
                states[word] |= (1 << (ord(char) - ord('a')))
        
        for word_a in states:
            for word_b in states:
                if word_a == word_b:
                    continue
                
                if states[word_a] & states[word_b] == 0:
                    max_product = max(max_product, len(word_a) * len(word_b))

        return max_product

        