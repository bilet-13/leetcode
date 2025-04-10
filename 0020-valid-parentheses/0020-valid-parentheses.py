class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket_stack = deque()
        close_to_open_bracket = {')': '(', ']': '[', '}': '{'}
        open_bracket_set = set(['(', '[', '{'])
        
        for bracket in s:
            if bracket in open_bracket_set:
                open_bracket_stack.append(bracket)
                continue
            
            if not open_bracket_stack or close_to_open_bracket[bracket] != open_bracket_stack[-1]:
                return False
            
            open_bracket_stack.pop()

        return not open_bracket_stack
