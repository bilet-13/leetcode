class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        for i in range(len(str2)):
            for j in range(len(str2), i, -1):
                if self.isDivideBy(str1, str2[i:j]) and self.isDivideBy(str2, str2[i:j]):
                    return str2[i:j]

        return ""
    
    def isDivideBy(self, str1, str2):
        if (len(str1)%len(str2) != 0):
            return False
        
        time = len(str1) // len(str2)
        sameLengthStr = str2 * time
        return str1 == sameLengthStr






