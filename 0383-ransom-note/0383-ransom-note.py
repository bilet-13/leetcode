class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = [0] * 26
        
        for letter in magazine:
            hashmap[ord(letter) - ord('a')] += 1
        
        for letter in ransomNote:
            if hashmap[ord(letter) - ord('a')] <= 0:
                return False

            hashmap[ord(letter) - ord('a')] -= 1
        
        return True