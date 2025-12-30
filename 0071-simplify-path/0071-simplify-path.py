class Solution:
    def simplifyPath(self, path: str) -> str:
        # stack
        # / == // == ///// 
        # . .. deal with there is no .
        path += '/'
        stack = []

        for char in path:
            if char == '/':
                if stack and stack[-1] == '/':
                    continue
                else:
                    if len(stack) >= 2 and stack[-1] == '.' and stack[-2] == '/':
                        stack.pop()

                    elif len(stack) >= 3 and stack[-1] == '.' and stack[-2] == '.' and stack[-3] == '/':
                        stack.pop()
                        stack.pop()
                        if len(stack) > 1:
                            stack.pop()

                        while stack and stack[-1] != '/':
                            stack.pop()
                    else:
                        stack.append(char)
            
            else:
                stack.append(char)
        
        while len(stack) >= 2 and stack[-1] == '/':
            stack.pop()

        return "".join(stack)

        