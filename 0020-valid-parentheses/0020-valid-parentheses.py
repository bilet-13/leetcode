class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def is_valid_pair(char1, char2):
            if char1 == '(':
                return char2 == ')'

            if char1 == '[':
                return char2 == ']'

            if char1 == '{':
                return char2 == '}'

        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)

            else:
                if not stack:
                    return False
                
                left_part = stack.pop()
                if not is_valid_pair(left_part, char):
                    return False
        
        return len(stack) == 0

        