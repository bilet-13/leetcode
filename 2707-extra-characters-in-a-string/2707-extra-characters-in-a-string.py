from functools import cache
class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert_word(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = Node()

            node = node.children[char]
        
        node.end_of_word = True

    def startWith(self, sub_str):
        node = self.root

        for char in sub_str:
            if char not in node.children:
                return False
            
            node = node.children[char]
        
        return True
    
    def has_word(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]
        
        return node.end_of_word


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        #dfs -> memo dp?
        # input argument: cur_idx
        # how to make extra char?
        n = len(s)
        words = set(dictionary)
        trie = Trie()

        for word in dictionary:
            trie.insert_word(word)

        @cache
        def dp(cur_idx):
            if cur_idx == n:
                return 0

            # skip the current char
            min_extra_char_result = 1 + dp(cur_idx + 1) 

            node = trie.root
            for i in range(cur_idx, n):
                if s[i] not in node.children:
                    break

                node = node.children[s[i]]
                
                if node.end_of_word:
                    min_extra_char_result = min(min_extra_char_result, dp(i + 1))


            return min_extra_char_result

        return dp(0)

        
        