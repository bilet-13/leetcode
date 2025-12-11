class Solution:
    def validPalindrome(self, s: str) -> bool:

        # double pointer one from left one from right
        # when encounter the first difference check if s is delete one of them is pali or not

        def check_palindrome(s, ignore_idx=-1):
            left = 0
            right = len(s) - 1

            while left < right:
                if left == ignore_idx:
                    left += 1
                    continue
                
                elif right == ignore_idx:
                    right -= 1
                    continue
                
                if s[left] != s[right]:
                    return False
                    
                left += 1
                right -= 1

            return True

        if check_palindrome(s):
            return True
        
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return check_palindrome(s, left) or check_palindrome(s, right)
            
            right -= 1
            left += 1
        
        return True
            
        

        
        