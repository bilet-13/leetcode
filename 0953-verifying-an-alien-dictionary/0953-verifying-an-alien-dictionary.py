class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # just follow problem
        # time complexity o(len(words) * maximum word length + len(order))
        order_int = {}
        for i in range(len(order)):
            order_int[order[i]] = i 

        prev = words[0]
        for i in range(1, len(words)):
            word = words[i]

            is_correct_order = True
            all_same = True
            for j in range(min(len(word), len(prev))):
                if order_int[word[j]] < order_int[prev[j]]:
                    all_same = False
                    is_correct_order = False
                    break
                
                elif order_int[word[j]] > order_int[prev[j]]:
                    all_same = False
                    is_correct_order = True
                    break

            if all_same and len(word) < len(prev):
                is_correct_order = False

            if not is_correct_order:
                return False

            prev = word

        return True





        
        