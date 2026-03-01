class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # combination
        states = {} # key mask of word. value: the max length of the same mask words
        max_product = 0

        for word in words:
            mask = 0

            for char in word:
                mask |= (1 << (ord(char) - ord('a')))

            if mask not in states:
                states[mask] = len(word)
            else:
                states[mask] = max(states[mask], len(word))
        
        for mask_a in states:
            for mask_b in states:
                if mask_a == mask_b:
                    continue
                
                if mask_a & mask_b == 0:
                    max_product = max(max_product, states[mask_a] * states[mask_b])

        return max_product

        