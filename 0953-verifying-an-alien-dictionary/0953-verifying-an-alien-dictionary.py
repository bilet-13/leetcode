class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # idea for each element, 
        #    compare it to the next eleemnt if all comparsion is true return true
        # else return false
        # use hash map: key : the char value: idx of the char in the order
        # time complexity O(n * length of word) n: len of words list

        order_map = {}
        for i in range(len(order)):
            order_map[order[i]] = i

        for i in range(0, len(words) - 1):
            word_a = words[i]
            word_b = words[i + 1]
            valid_pair = False

            for j in range(min(len(word_a), len(word_b))):
                if order_map[word_a[j]] > order_map[word_b[j]]:
                    return False
                elif order_map[word_a[j]] < order_map[word_b[j]]:
                    valid_pair = True
                    break
                    

            if not valid_pair and len(word_a) > len(word_b):
                return False
        
        return True